import zimp_clf_client
import mlflow
import pandas as pd
import os
import time
import logging

from zimp_clf_client.rest import ApiException

from experiment.config import Config
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, precision_score, recall_score


def get_or_create_mlflow_experiment(experiment_name):
    existing_exp = mlflow.get_experiment_by_name(experiment_name)
    if existing_exp is not None:
        return existing_exp

    exp_id = mlflow.create_experiment(experiment_name)
    return mlflow.get_experiment(exp_id)


class Experiment:

    def __init__(self, config: Config):
        self.config = config

        # init classification API
        configuration = zimp_clf_client.Configuration()
        configuration.host = config.classification_service_url
        api_client = zimp_clf_client.ApiClient(configuration=configuration)
        api_client.rest_client.pool_manager.connection_pool_kw['retries'] = 10  # in case api is unstable
        self.train_api = zimp_clf_client.TrainingApi(api_client)
        self.predict_api = zimp_clf_client.PredictionApi(api_client)
        self.download_api = zimp_clf_client.DownloadApi(api_client)

        # init mlflow API
        mlflow.set_tracking_uri(config.mlflow_url)
        self.mlflow_experiment = get_or_create_mlflow_experiment(config.experiment_name)

        # resource paths
        self.train_path = os.path.join('resources', config.dataset, 'train.csv')
        self.test_path = os.path.join('resources', config.dataset, 'test.csv')

    def run(self):
        with mlflow.start_run(experiment_id=self.mlflow_experiment.experiment_id,
                              run_name=self.config.run_name) as mlflow_run:
            mlflow.log_param('model_type', self.config.model_type)
            mlflow.log_param('zimp_mechanism', 'None')
            mlflow.log_param('random_seed', self.config.random_seed)
            mlflow.log_param('dataset', self.config.dataset)

            # TRAIN
            ref_time = time.time()
            self.safe_train(ignore_errors=False)
            self.wait_for_train_completion()  # poll api until training is completed
            mlflow.log_metric('train_time_sec', time.time() - ref_time)

            # EVAL TRAIN
            ref_time = time.time()
            self.predict_file_async(self.train_path, metric_prefix='train_')
            mlflow.log_metric('train_predict_time_sec', time.time() - ref_time)

            # EVAL TEST
            ref_time = time.time()
            self.predict_file_async(self.test_path, metric_prefix='test_')
            mlflow.log_metric('test_predict_time_sec', time.time() - ref_time)

            self.store_model()

        logging.debug(self.train_api.clf_training_status_get())

    def exists_in_mlflow(self) -> bool:
        """

        :return: True if a successful experiment exists in mlflow which has the same run name
        """
        run_cnt = mlflow.search_runs(
            experiment_ids=[self.mlflow_experiment.experiment_id],
            filter_string=f'tags."mlflow.runName"="{self.config.run_name}" attributes.status="FINISHED"').shape[0]

        return run_cnt > 0

    def store_model(self):
        """
        retrieves trained model from clf-api and stores it in mlflow
        :return:
        """
        model_path = 'resources/model'
        binary_file = self.download_api.clf_download_get(_preload_content=False).data
        with open(model_path, 'wb') as f:
            f.write(binary_file)

        mlflow.log_artifact(model_path)

    def predict_file_async(self, file_path, metric_prefix=""):
        """
        sends complete file for prediction and polls for completion
        :param file_path: path to the file which should be predicted ('text', 'target')
        :return:
        """
        tmp_file = 'prediction_input.csv'
        df_pred = pd.read_csv(file_path)
        df_pred['text'].to_csv(tmp_file, index=False)
        result_id = self.predict_api.clf_file_predict_proba_post(file=tmp_file)['resultId']
        self.wait_for_predict_completion(file_path, result_id, metric_prefix)

    def get_predictions_for_file(self, file_path):
        """
        retrieves predictions and related certainty for all texts in the supplied file
        :param file_path: path to the file which should be predicted ('text', 'target')
        :return: pandas df which contains loaded data plus prediction and certainty cols
        """
        batch_size = 6 if self.config.model_type == 'BERT' else 128  # OOM-exception for BERT
        df_pred = pd.read_csv(file_path)
        df_pred['prediction'] = ''
        df_pred['certainty'] = 0
        df_pred['target'] = df_pred['target'].astype(str)
        for idx in range(0, df_pred.shape[0], batch_size):
            clf_response = self.get_api_prediction({'n': 1, 'texts': df_pred.loc[idx:idx+batch_size-1, 'text'].tolist()})
            df_pred.loc[idx:idx+batch_size-1, 'prediction'] = [res['labels'][0]['label'] for res in clf_response]
            df_pred.loc[idx:idx+batch_size-1, 'certainty'] = [res['labels'][0]['probability'] for res in clf_response]

        return df_pred

    def get_api_prediction(self, request_body):
        """
        wrapper for predict_proba API call which adds a retry in case of gateway errors (may happen with slow bert model)
        :param request_body:
        :return:
        """
        attempt_count = 0

        while attempt_count < 10:
            if attempt_count > 0:
                logging.info("Retry API CALL")

            try:
                clf_response = self.predict_api.clf_m_predict_proba_post(body=request_body)
            except ApiException as e:
                logging.warning("Predict Call failed", e)
                attempt_count += 1
            else:
                return clf_response

        raise ApiException(0, 'API-Call fails consistently. Pleas check logs')

    def safe_get_status(self):
        try:
            train_state = self.train_api.clf_training_status_get()
            return train_state['isTrained']
        except ApiException as e:
            logging.warning("Status Call failed", e)
            return False

    def safe_train(self, ignore_errors=False):
        try:
            self.train_api.clf_train_post(file=self.train_path, model_type=self.config.model_type,
                                          seed=self.config.random_seed, asynchronous='true')
        except ApiException as e:
            logging.warning("Training might have failed - check backend server", e)
            if not ignore_errors:
                raise e
            else:
                # wait for train process to start
                time.sleep(180)

    def wait_for_train_completion(self):
        wait_time = 1
        while True:
            if self.safe_get_status() :
                logging.info('Training completed.')
                break
            logging.info(f'Training not completed. Waiting for {int(wait_time)} seconds..')
            time.sleep(int(wait_time))
            wait_time += 0.1

    def safe_get_predictions(self, result_id, prediction_path):
        try:
            csv_file = self.download_api.clf_file_predictions_id_get(id=result_id, _preload_content=False).data
            with open(prediction_path, 'wb') as f:
                f.write(csv_file)
        except ApiException as e:
            logging.warning("Prediction Poll Call failed", e)

        if not os.path.exists(prediction_path):
            return pd.DataFrame()

        return pd.read_csv(prediction_path)

    def wait_for_predict_completion(self, input_path, result_id, metric_prefix=""):
        wait_time = 10
        prediction_path = f'predictions_{result_id}.csv'
        df_input = pd.read_csv(input_path)
        cnt_records = df_input.shape[0]

        while True:
            df_pred = self.safe_get_predictions(result_id, prediction_path)
            cnt_pred = df_pred.shape[0]
            if cnt_pred < 1:
                continue

            df_pred['target'] = df_input.loc[:cnt_pred, ['target']].astype(str)
            df_pred['prediction'] = df_pred['prediction'].astype(str)
            self.report_metrics(df_pred, metric_prefix=metric_prefix)

            if cnt_pred == cnt_records:
                logging.info('Prediction complete')
                mlflow.log_artifact(prediction_path)
                os.remove(prediction_path)
                break

            logging.info(f'Prediction not completed. Waiting for {int(wait_time)} seconds..')
            time.sleep(int(wait_time))
            wait_time += 1

    def report_metrics(self, df_pred, metric_prefix=""):
        """
        calculates several metrics and reports them to mlflow
        :param metric_prefix: prefix for reported mlflow metric name
        :param df_pred: pandas dataframe with cols ['text', 'prediction', 'target', 'certainty']
        :return: nothing
        """
        metrics = {}
        for metric_name, fun_score in [('accuracy', accuracy_score), ('balanced_accuracy', balanced_accuracy_score)]:
            metrics[metric_prefix + metric_name] = fun_score(df_pred['target'], df_pred['prediction'])

        for avg in ['micro', 'macro', 'weighted']:
            for metric_name, fun_score in [('f1', f1_score), ('precision', precision_score), ('recall', recall_score)]:
                metrics[metric_prefix + metric_name + '_' + avg] = fun_score(df_pred['target'], df_pred['prediction'],
                                                                             average=avg)

        metrics[metric_prefix + 'certainty_pos'] = df_pred[df_pred['target'] == df_pred['prediction']][
            'certainty'].mean()
        metrics[metric_prefix + 'certainty_neg'] = df_pred[df_pred['target'] != df_pred['prediction']][
            'certainty'].mean()
        metrics[metric_prefix + 'count_observations'] = df_pred.shape[0]

        mlflow.log_metrics(metrics)

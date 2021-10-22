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
        self.clf_api = zimp_clf_client.DefaultApi(api_client)

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
            self.clf_api.clf_train_post(file=self.train_path, model_type=self.config.model_type,
                                        seed=self.config.random_seed, asynchronous='true')
            self.wait_for_completion()  # poll api until training is completed
            mlflow.log_metric('train_time_sec', time.time() - ref_time)

            # EVAL TRAIN
            ref_time = time.time()
            df_pred_train = self.get_predictions_for_file(self.train_path)
            mlflow.log_metric('train_predict_time_sec', time.time() - ref_time)
            self.report_metrics(df_pred_train, metric_prefix='train_')

            # EVAL TEST
            ref_time = time.time()
            df_pred_test = self.get_predictions_for_file(self.test_path)
            mlflow.log_metric('test_predict_time_sec', time.time() - ref_time)
            self.report_metrics(df_pred_test, metric_prefix='test_')

            self.store_model()

        logging.debug(self.clf_api.clf_training_status_get())

    def store_model(self):
        """
        retrieves trained model from clf-api and stores it in mlflow
        :return:
        """
        model_path = 'resources/model'
        binary_file = self.clf_api.clf_download_get(_preload_content=False).data
        with open(model_path, 'wb') as f:
            f.write(binary_file)

        mlflow.log_artifact(model_path)

    def get_predictions_for_file(self, file_path):
        """
        retrieves predictions and related certainty for all texts in the supplied file
        :param file_path: path to the file which should be predicted (columns text must be present, target can be present)
        :return: pandas df which contains loaded data plus prediction and certainty cols
        """
        BATCH_SIZE = 128
        df_pred = pd.read_csv(file_path)
        df_pred['prediction'] = ''
        df_pred['certainty'] = 0
        for idx in range(0, df_pred.shape[0], BATCH_SIZE):
            clf_response = self.get_api_prediction({'n': 1, 'texts': df_pred.loc[idx:idx+BATCH_SIZE-1, 'text'].tolist()})
            df_pred.loc[idx:idx+BATCH_SIZE-1, 'prediction'] = [res['labels'][0]['label'] for res in clf_response]
            df_pred.loc[idx:idx+BATCH_SIZE-1, 'certainty'] = [res['labels'][0]['probability'] for res in clf_response]

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
                clf_response = self.clf_api.clf_m_predict_proba_post(body=request_body)
            except ApiException as e:
                logging.warning("Predict Call failed", e)
                attempt_count += 1
            else:
                return clf_response

        raise ApiException(0, 'API-Call fails consistently. Pleas check logs')

    def wait_for_completion(self):
        wait_time = 1
        while True:
            train_state = self.clf_api.clf_training_status_get()
            if train_state['isTrained']:
                break
            logging.info(f'Training not completed. Waiting for {int(wait_time)} seconds..')
            time.sleep(int(wait_time))
            wait_time += 0.1

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

        mlflow.log_metrics(metrics)

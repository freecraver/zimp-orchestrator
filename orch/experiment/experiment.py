import time

from experiment.config import Config

import zimp_clf_client
import mlflow


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
        self.clf_api = zimp_clf_client.DefaultApi(zimp_clf_client.ApiClient(configuration=configuration))

        # init mlflow API
        mlflow.set_tracking_uri(config.mlflow_url)
        self.mlflow_experiment = get_or_create_mlflow_experiment(config.experiment_name)

    def run(self, train_path: str, test_path: str):
        with mlflow.start_run(experiment_id=self.mlflow_experiment.experiment_id,
                              run_name=self.config.run_name) as mlflow_run:
            mlflow.log_param('model_type', self.config.model_type)
            mlflow.log_param('zimp_mechanism', 'None')
            mlflow.log_param('random_seed', self.config.random_seed)

            pre_train_time = time.time()
            self.clf_api.clf_train_post(file=train_path, model_type=self.config.model_type,
                                        seed=self.config.random_seed, asynchronous='false')
            mlflow.log_metric('train_time_sec', time.time()-pre_train_time)


        print(self.clf_api.clf_training_status_get())

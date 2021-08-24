from experiment.config import Config

import zimp_clf_client


class Experiment:

    def __init__(self, config: Config):
        self.config = config
        configuration = zimp_clf_client.Configuration()
        configuration.host = config.classification_service_url
        self.clf_api = zimp_clf_client.DefaultApi(zimp_clf_client.ApiClient(configuration=configuration))

    def run(self, train_path: str, test_path: str):
        print(self.clf_api.clf_training_status_get())


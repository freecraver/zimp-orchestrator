import yaml


class Config:
    model_type: str
    classification_service_url: str
    mlflow_url: str
    experiment_name: str
    run_name: str
    random_seed: str
    dataset: str

    def __init__(self, **entries):
        self.__dict__.update(entries)

    @staticmethod
    def from_yaml(file_path):
        with open(file_path) as f:
            data_map = yaml.safe_load(f)
        return Config(**data_map)

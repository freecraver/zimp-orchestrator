import os

from experiment.config import Config

experiment_name = 'Baseline'

run_directory = 'runs/' + experiment_name + '/'

random_seeds = [13146, 36755, 47120, 45710, 270817, 139949, 214282, 16940, 28328, 214463]
model_types = ['BERT', 'FASTTEXT', 'SVM']

en_datasets = ['DBP-14', 'TREC-6', 'YELP-5']

run_idx = 101

if __name__ == '__main__':

    if not os.path.exists(run_directory):
        os.makedirs(run_directory)

    for seed in random_seeds:
        for dataset in en_datasets:
            for model in model_types:
                cfg = Config()
                cfg.model_type = model
                cfg.classification_service_url = "http://localhost/"
                cfg.mlflow_url = 'http://localhost/'
                cfg.experiment_name = experiment_name
                cfg.run_name = model + '-' + str(run_idx)
                cfg.random_seed = seed
                cfg.dataset = dataset
                cfg.to_yaml(run_directory + cfg.run_name + '.yaml')

            run_idx += 1

import os

from experiment.config import Config

experiment_name = 'Baseline-async'

run_directory = 'runs/' + experiment_name + '/'

random_seeds = [13146, 36755, 47120, 45710, 270817, 139949, 214282, 16940, 28328, 214463]
model_types = ['BERT', 'GERMAN_BERT', 'FASTTEXT']
deterministic_model_types = ['SVM']

en_datasets = ['DBP-14', 'TREC-6', 'YELP-5']
de_datasets = ['10K-GNAD', 'GERMEVAL-2018', 'GERMEVAL-2020']


def build_config(model, seed, dataset, idx):
    cfg = Config()
    cfg.model_type = model
    cfg.classification_service_url = "http://localhost/"
    cfg.mlflow_url = 'http://localhost/'
    cfg.experiment_name = experiment_name
    cfg.run_name = model + '-' + str(idx)
    cfg.random_seed = seed
    cfg.dataset = dataset

    cfg.to_yaml(run_directory + cfg.run_name + '.yaml')


def get_models(lang):
    if lang == 'en':
        return [m for m in model_types if m != 'GERMAN_BERT']
    if lang == 'de':
        return [m for m in model_types if m != 'BERT']

    return []


if __name__ == '__main__':

    run_idx = 101

    if not os.path.exists(run_directory):
        os.makedirs(run_directory)

    for s in random_seeds:
        for d in en_datasets:
            for m in get_models('en'):
                build_config(m, s, d, run_idx)
            run_idx += 1

    run_idx = 201
    for s in random_seeds:
        for d in de_datasets:
            for m in get_models('de'):
                build_config(m, s, d, run_idx)
            run_idx += 1

    # build deterministic runs (no seed impact)
    for m in deterministic_model_types:
        run_idx = 101
        for d in en_datasets:
            build_config(m, 0, d, run_idx)
            run_idx += 1

        run_idx = 201
        for d in de_datasets:
            build_config(m, 0, d, run_idx)
            run_idx += 1

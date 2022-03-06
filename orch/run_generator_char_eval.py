import os

from zimp.simplification.builder import SimplificationStrategy

from experiment.config import Config

experiment_name = 'character'

run_directory = 'runs/' + experiment_name + '/'

random_seeds = [13146, 36755, 47120]
model_types = ['DECISION_TREE', 'RANDOM_FOREST', 'FASTTEXT']
deterministic_model_types = ['SVM']

en_datasets = ['DBP-14', 'TREC-6', 'YELP-5']
de_datasets = ['10K-GNAD', 'GERMEVAL-2018', 'GERMEVAL-2020']

zimp_scenarios = [
    (SimplificationStrategy.SYMBOL_SIMPLE, {}),
    (SimplificationStrategy.SYMBOL_SIMPLE_ALPHA_NOCASING, {})
] + [
    (SimplificationStrategy.SYMBOL_VOCAB_NOCASING, {'min_document_frequency': df})
    for df in [0.001, 0.01, 0.1]
] + [
    (SimplificationStrategy.SYMBOL_VOCAB, {'min_document_frequency': df})
    for df in [0.001, 0.01, 0.1]
] + [
    (SimplificationStrategy.SYMBOL_VOCAB_NOCASING, {'min_term_frequency': tf})
    for tf in [0.001, 0.01, 0.05]
]


def build_config(model, seed, dataset, idx, zimp_mechanism, zimp_config):
    cfg = Config()
    cfg.model_type = model
    cfg.classification_service_url = "http://localhost/"
    cfg.mlflow_url = 'http://localhost/'
    cfg.experiment_name = experiment_name
    cfg.run_name = model + '-' + str(idx)
    cfg.random_seed = seed
    cfg.dataset = dataset
    cfg.zimp_mechanism = zimp_mechanism.name
    cfg.zimp_config = zimp_config
    cfg.store_artifacts = False

    cfg.to_yaml(run_directory + cfg.run_name + '.yaml')


if __name__ == '__main__':

    run_idx = 301

    if not os.path.exists(run_directory):
        os.makedirs(run_directory)

    for s in random_seeds:
        for d in en_datasets:
            for zs in zimp_scenarios:
                for m in model_types:
                    build_config(m, s, d, run_idx, zs[0], zs[1])
                run_idx += 1

    run_idx = 401
    for s in random_seeds:
        for d in de_datasets:
            for zs in zimp_scenarios:
                for m in model_types:
                    build_config(m, s, d, run_idx, zs[0], zs[1])
                run_idx += 1

    run_idx = 301
    for d in en_datasets:
        for zs in zimp_scenarios:
            for m in deterministic_model_types:
                build_config(m, 0, d, run_idx, zs[0], zs[1])
            run_idx += 1

    run_idx = 401
    for d in de_datasets:
        for zs in zimp_scenarios:
            for m in deterministic_model_types:
                build_config(m, 0, d, run_idx, zs[0], zs[1])
            run_idx += 1

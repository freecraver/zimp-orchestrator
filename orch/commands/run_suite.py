from cleo import Command

import logging
import glob

from experiment.config import Config
from experiment.experiment import Experiment


class RunSuite(Command):
    """
    runs a whole experiment suite

    suite
        {config_folder=runs : Folder containing experiment config files}
    """

    def handle(self):
        config_folder = self.argument('config_folder')

        logging.basicConfig(level=logging.INFO)

        config_files = glob.glob(config_folder + '*.yaml')
        logging.info(f'Found {len(config_files)} experiments')

        for idx, experiment_config in enumerate(config_files):
            logging.info(f'Starting with experiment {idx} - {experiment_config}')
            Experiment(Config.from_yaml(experiment_config)).run()

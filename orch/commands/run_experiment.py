from cleo import Command

from experiment.config import Config
from experiment.experiment import Experiment

import logging


class RunExperiment(Command):
    """
    runs a single experiment with specified settings

    experiment
        {config_file=config.yaml : Configuration for experiment and environment}
    """

    def handle(self):
        config_file = self.argument('config_file')
        logging.basicConfig(level=logging.INFO)

        Experiment(Config.from_yaml(config_file)).run()

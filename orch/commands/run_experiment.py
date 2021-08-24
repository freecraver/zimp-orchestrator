from cleo import Command

from experiment.config import Config
from experiment.experiment import Experiment


class RunExperiment(Command):
    """
    runs a single experiment with specified settings

    experiment
        {train_file : Path to file containing training set instances}
        {test_file : Path to file containing test set instances}
        {config_file=config.yaml : Configuration for experiment and environment}
    """

    def handle(self):
        train_file = self.argument('train_file')
        test_file = self.argument('test_file')
        config_file = self.argument('config_file')

        Experiment(Config.from_yaml(config_file)).run(train_file, test_file)

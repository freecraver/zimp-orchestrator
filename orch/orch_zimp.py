from cleo import Application

from commands.run_experiment import RunExperiment
from commands.run_suite import RunSuite

application = Application()
application.add(RunExperiment())
application.add(RunSuite())

if __name__ == '__main__':
    application.run()

from cleo import Application

from commands.run_experiment import RunExperiment

application = Application()
application.add(RunExperiment())

if __name__ == '__main__':
    application.run()

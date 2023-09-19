import os

class Job:
    def __init__(self, command: str) -> None:
        self.command = command

class Cron:
    def __init__(self) -> None:
        self.jobs: list[Job] = []

    def commit_cron(self):
        command = ''
        for job in self.jobs:
            command += job.command + '\n'
        command += '\n'
        with open(f'/tmp/cron_job', 'w+') as f:
            f.write(command)

        os.system(f'crontab /tmp/cron_job')

    def remove_job(self, removed_job: Job):
        self.jobs = [job for job in self.jobs if job != removed_job]

    def add_job(self, new_job: Job):
        print('new_job')
        print(new_job)
        self.jobs = self.jobs + [new_job]

cron = Cron()


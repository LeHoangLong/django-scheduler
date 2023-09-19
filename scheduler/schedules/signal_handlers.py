from django.dispatch import receiver
from django.db.models import signals as db_signals
from schedules import signals
from schedules import cron
from schedules import models

jobs: dict[str, dict[str, cron.Job]] = {}

@receiver(db_signals.post_save, sender=models.Schedule)
def on_schedule_save(sender, **kwargs):
    instance : models.Schedule = kwargs['instance']
    tenant = instance.tenant
    tenant_jobs : dict[str, cron.Job] = getattr(jobs, tenant, {})
    job = tenant_jobs.get(instance.id)
    if job is not None:
        cron.cron.remove_job(job)
        tenant_jobs.pop(instance.id)
    start_cron(instance)

@receiver(signals.app_init)
def on_app_init(sender, **kwargs):
    schedules = models.Schedule.objects.filter(is_enabled=True)
    for schedule in schedules:
        start_cron(schedule)

def start_cron(schedule: models.Schedule):
    print('starting cron')
    print(schedule.cron)
    command = f'{schedule.cron.strip()} echo "hello" && curl http://localhost:8080/cron/{schedule.id} --header "x-country:{schedule.tenant}"'
    job = cron.Job(command)
    cron.cron.add_job(job)
    if not schedule.tenant in jobs:
        jobs[schedule.tenant] = {}
    cron.cron.commit_cron()
    jobs[schedule.tenant][schedule.id] = job

from celery import shared_task

@shared_task
def add_schedule():
    print('adding schedule')
    pass
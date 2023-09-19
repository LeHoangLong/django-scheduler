from django.apps import AppConfig
from . import signals

class SchedulesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedules'

    def ready(self):
        import schedules.signal_handlers
        signals.app_init.send(sender=self)
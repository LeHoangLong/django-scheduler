from django.db import models
from django.db.models import signals
from django import dispatch
from schedules import middlewares

# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    transport = models.TextField()
    transport_params = models.JSONField(blank=True, null=True)
    cron = models.TextField()
    params = models.JSONField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)
    tenant = models.TextField()
    
@dispatch.receiver(signal=signals.pre_save, sender=Schedule)
def pre_model_save(sender, **kwargs):
    try:
        tenant = middlewares.get_tenant()
        instance : Schedule = kwargs['instance']
        instance.tenant = tenant
    except:
        pass
from rest_framework import serializers
from schedules import models 

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = ['id', 'transport', 'transport_params', 'cron', 'params', 'created_at', 'updated_at']
        
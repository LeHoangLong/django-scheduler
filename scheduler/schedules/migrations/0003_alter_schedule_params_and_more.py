# Generated by Django 4.2.5 on 2023-09-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_schedule_is_enabled_schedule_tenant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='params',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='transport_params',
            field=models.JSONField(blank=True, null=True),
        ),
    ]

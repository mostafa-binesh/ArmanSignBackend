# Generated by Django 4.2.7 on 2023-12-17 09:16

import datetime
from django.db import migrations, models, transaction
# from ..models import Report

def updateData(apps, schema_editor):
    Report = apps.get_model('reports', 'Report')
    new_date = datetime.date(2023,1,1)
    with transaction.atomic():
        Report.objects.all().update(started_at=new_date, ended_at=new_date)
    

class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0022_alter_report_started_at'),
    ]

    operations = [
        migrations.RunPython(updateData)
    ]

# Generated by Django 4.2.7 on 2023-12-17 09:29

from django.db import migrations

def updateStandardTimeFieldToInteger(apps, schema_editor):
    Report = apps.get_model('reports', 'Report')
    new_standard_time = 1  # example date, change accordingly
    Report.objects.all().update(standard_time = new_standard_time)


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0023_auto_20231217_1252'),
    ]

    operations = [
        migrations.RunPython(updateStandardTimeFieldToInteger)
    ]

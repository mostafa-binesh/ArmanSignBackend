# Generated by Django 4.2.7 on 2023-12-11 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_remove_report_client_alter_report_ended_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='creator',
            new_name='operator',
        ),
        migrations.RemoveField(
            model_name='report',
            name='stop_time',
        ),
        migrations.RemoveField(
            model_name='report',
            name='title',
        ),
    ]

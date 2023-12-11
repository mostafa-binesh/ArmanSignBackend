# Generated by Django 4.2.7 on 2023-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0016_report_created_at_report_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='client',
        ),
        migrations.AlterField(
            model_name='report',
            name='ended_at',
            field=models.DateTimeField(null=True, verbose_name='Ended At'),
        ),
    ]

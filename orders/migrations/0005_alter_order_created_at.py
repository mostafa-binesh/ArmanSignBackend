# Generated by Django 4.2.7 on 2023-11-17 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 12, 24, 20, 879007, tzinfo=datetime.timezone.utc), verbose_name='Created At'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-17 09:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parts', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 17, 12, 56, 35, 767949))),
                ('order_number', models.CharField(max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('parts', models.ManyToManyField(to='parts.part')),
            ],
        ),
    ]

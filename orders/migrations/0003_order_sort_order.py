# Generated by Django 4.2.7 on 2024-04-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_category_order_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sort_order',
            field=models.PositiveIntegerField(default=1, verbose_name='Sort Order'),
        ),
    ]

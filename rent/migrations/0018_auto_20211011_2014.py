# Generated by Django 3.2 on 2021-10-11 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0017_auto_20211011_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_order',
            name='new_from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 14, 51, 12730)),
        ),
        migrations.AlterField(
            model_name='extended_order',
            name='new_to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 14, 51, 12730)),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 14, 51, 11702)),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 14, 51, 11702)),
        ),
    ]

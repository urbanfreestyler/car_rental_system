# Generated by Django 3.2 on 2021-10-11 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0015_auto_20211011_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_order',
            name='new_from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 10, 55, 359690)),
        ),
        migrations.AlterField(
            model_name='extended_order',
            name='new_to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 10, 55, 359690)),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 10, 55, 358693)),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 10, 55, 358693)),
        ),
    ]
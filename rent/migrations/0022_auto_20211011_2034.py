# Generated by Django 3.2 on 2021-10-11 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0021_auto_20211011_2019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Num_of_orders',
        ),
        migrations.AlterField(
            model_name='extended_order',
            name='new_from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 34, 43, 390196)),
        ),
        migrations.AlterField(
            model_name='extended_order',
            name='new_to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 34, 43, 390196)),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 34, 43, 389199)),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 34, 43, 389199)),
        ),
    ]
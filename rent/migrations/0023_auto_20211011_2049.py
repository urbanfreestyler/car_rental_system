# Generated by Django 3.2 on 2021-10-11 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0022_auto_20211011_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extended_order',
            name='new_from_date',
        ),
        migrations.AlterField(
            model_name='extended_order',
            name='new_to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 49, 26, 4634)),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 49, 26, 3631)),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 20, 49, 26, 3631)),
        ),
    ]
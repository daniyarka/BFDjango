# Generated by Django 2.1.2 on 2018-10-09 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181009_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 0, 11, 12, 433356)),
        ),
        migrations.AlterField(
            model_name='post',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 0, 11, 12, 433035)),
        ),
    ]
# Generated by Django 2.1.2 on 2018-10-09 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181010_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 1, 33, 12, 402344)),
        ),
        migrations.AlterField(
            model_name='post',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 1, 33, 12, 402014)),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField()),
                ('author', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('cr_date', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]

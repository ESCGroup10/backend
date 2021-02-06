# Generated by Django 3.1.5 on 2021-02-04 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditor_id', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=30)),
                ('report_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
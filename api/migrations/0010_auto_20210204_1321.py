# Generated by Django 3.1.5 on 2021-02-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210204_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='foodhygiene_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='healthierchoice_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='housekeeping_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='safety_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='staffhygiene_score',
            field=models.IntegerField(default=0),
        ),
    ]
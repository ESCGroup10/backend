# Generated by Django 3.1.5 on 2021-02-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210204_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_image',
            field=models.CharField(default='', max_length=200),
        ),
    ]
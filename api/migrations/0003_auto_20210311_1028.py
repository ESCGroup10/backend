# Generated by Django 3.1.5 on 2021-03-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_report_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='company',
            field=models.CharField(max_length=30),
        ),
    ]
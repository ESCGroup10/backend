# Generated by Django 3.1.5 on 2021-02-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_report_report_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='resolution_image',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_image',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_notes',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]

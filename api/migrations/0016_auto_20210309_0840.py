# Generated by Django 3.1.5 on 2021-03-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210226_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(blank='True', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='institution',
            field=models.CharField(blank='True', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank='True', max_length=200),
        ),
    ]
# Generated by Django 3.1.5 on 2021-03-09 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210309_0840'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auth',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]

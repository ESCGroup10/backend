# Generated by Django 3.1.5 on 2021-02-04 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='report_date',
            new_name='news_date',
        ),
    ]
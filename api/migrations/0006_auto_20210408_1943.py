# Generated by Django 3.1.5 on 2021-04-08 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210408_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportedcase',
            old_name='tenant_id',
            new_name='report_id',
        ),
        migrations.RenameField(
            model_name='resolvedcase',
            old_name='tenant_id',
            new_name='report_id',
        ),
    ]

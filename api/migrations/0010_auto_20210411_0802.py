# Generated by Django 3.1.5 on 2021-04-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_resolvedcase_tenant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='rejected_comments',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='institution',
            field=models.CharField(default='', max_length=30),
        ),
    ]

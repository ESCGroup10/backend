# Generated by Django 3.1.5 on 2021-03-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210323_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='unresolved_date',
            field=models.DateTimeField(blank=True),
        ),
    ]

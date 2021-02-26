# Generated by Django 3.1.5 on 2021-02-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
# Generated by Django 3.2.13 on 2022-12-02 00:38

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('walkings', '0003_dogroup_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogroup',
            name='date',
        ),
        migrations.AddField(
            model_name='dogroup',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dogroup',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 3.0 on 2020-01-25 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_gym', '0004_session_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 25, 17, 35, 10, 101879)),
        ),
    ]

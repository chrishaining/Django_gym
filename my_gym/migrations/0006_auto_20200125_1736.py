# Generated by Django 3.0 on 2020-01-25 17:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_gym', '0005_session_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 25, 17, 36, 35, 188952, tzinfo=utc)),
        ),
    ]

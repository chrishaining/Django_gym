# Generated by Django 3.0 on 2020-01-25 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_gym', '0006_auto_20200125_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
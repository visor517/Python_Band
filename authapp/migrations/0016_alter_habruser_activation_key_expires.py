# Generated by Django 3.2.12 on 2022-04-16 06:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_auto_20220415_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 6, 37, 44, 973834, tzinfo=utc)),
        ),
    ]
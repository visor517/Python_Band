# Generated by Django 3.2.12 on 2022-04-06 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20220406_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habrprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('W', 'Ж')], max_length=1, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='habruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 14, 8, 19, 828361, tzinfo=utc)),
        ),
    ]
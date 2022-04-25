# Generated by Django 3.2.12 on 2022-04-24 23:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
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
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 23, 0, 16, 326745, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='habruser',
            name='role',
            field=models.CharField(choices=[('U', 'Зарегистрированный пользователь'), ('M', 'Модератор'), ('A', 'Администратор')], default='U', max_length=1, verbose_name='роль'),
        ),
    ]

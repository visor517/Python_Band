# Generated by Django 3.2.12 on 2022-05-07 19:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 19, 10, 10, 958525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='habruser',
            name='role',
            field=models.CharField(choices=[('U', 'Зарегистрированный пользователь'), ('M', 'Модератор'), ('A', 'Администратор')], default='U', max_length=1, verbose_name='роль'),
        ),
    ]
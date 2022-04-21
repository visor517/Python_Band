# Generated by Django 3.2.12 on 2022-04-18 12:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0017_auto_20220418_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 20, 12, 49, 20, 177257, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='habruser',
            name='role',
            field=models.CharField(choices=[('A', 'Администратор'), ('U', 'Зарегистрированный пользователь'), ('M', 'Модератор')], default='U', max_length=1, verbose_name='роль'),
        ),
    ]
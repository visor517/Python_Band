# Generated by Django 3.2.12 on 2022-04-24 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
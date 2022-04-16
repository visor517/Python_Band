# Generated by Django 3.2.12 on 2022-04-16 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0019_auto_20220416_2155'),
        ('commentapp', '0008_remove_comments_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.habrprofile', to_field='user', verbose_name='Автор комментария'),
        ),
    ]

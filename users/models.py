from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_TYPES = (
        (1, 'Администратор'),
        (2, 'Модератор'),
        (3, 'Пользователь'),
    )
    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    avatar = models.ImageField(upload_to='users_images', blank=True)
    email = models.EmailField(blank=True, unique=True)
    role = models.IntegerField(verbose_name='Роль', choices=ROLE_TYPES, null=True)

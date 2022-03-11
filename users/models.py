from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 1
    MODERATOR = 2
    CLIENT = 3
    ROLE_TYPES = (
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (CLIENT, 'Пользователь'),
    )
    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    avatar = models.ImageField(upload_to='users_images', blank=True)
    email = models.EmailField(unique=True)
    role = models.IntegerField(verbose_name='Роль', choices=ROLE_TYPES, default=CLIENT)

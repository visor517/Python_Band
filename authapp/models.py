from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.timezone import now

from django.db.models.signals import post_save
from django.dispatch import receiver


class HabrUser(AbstractUser):

    USER = 'U'
    MODERATOR = 'M'
    ADMINISTRATOR = "A"

    ROLE_CHOICES = {
        (USER, 'Зарегистрированный пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMINISTRATOR, 'Администратор'),
    }

    activation_key = models.CharField(max_length=128, blank=True, null=True)
    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=48)))
    role = models.CharField(verbose_name='роль', max_length=1, choices=ROLE_CHOICES, default=USER)

    def is_activation_key_expired(self):
        if now() < self.activation_key_expires:
            return False
        return True

    def __str__(self):
        return f'{self.first_name if self.first_name else ""}{ ", "+ self.last_name if self.last_name else ""} ' \
               f'({self.username})'

    def delete(self, using=None, keep_parents=False):
        """ Переопределение метода delete"""
        self.is_active = False

class HabrProfile(models.Model):

    class Meta:
        verbose_name = "профиль пользователя"
        verbose_name_plural = "профили пользователей"

    MALE = 'M'
    FEMALE = "W"

    GENDER_CHOICES = {
        (MALE, 'M'),
        (FEMALE, 'Ж')
    }

    user = models.OneToOneField(
        HabrUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    nik = models.CharField(blank=True, max_length=50, verbose_name='ник')
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    birthday = models.DateField(verbose_name='дата рождения', null=True)
    gender = models.CharField(blank=True, max_length=1,
                              choices=GENDER_CHOICES, verbose_name='пол')
    tagline = models.CharField(blank=True, max_length=255, verbose_name='тэги')
    zone = models.IntegerField(verbose_name='часовая зона', default=0)
    is_active = models.BooleanField(verbose_name='Статус активности', default=True)


    def __str__(self):
        return f'{self.user.username}{" - " if self.user.first_name or self.user.last_name else ""} {self.user.first_name} {self.user.last_name}'

    @receiver(post_save, sender=HabrUser)
    def create_user_profile(sender, instance, created, **kwards):
        if created:
            HabrProfile.objects.create(user=instance)
            # Выше тоже самое, что и
            # shop_user_profile = ShopUserProfile(user=instance)
            # shop_user_profile.save()

    # @receiver(post_save, sender=HabrUser)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.user.profile.save()

    def delete(self, using=None, keep_parents=False):
        """ Переопределение метода delete"""
        self.is_active = False
        self.user.is_active = False


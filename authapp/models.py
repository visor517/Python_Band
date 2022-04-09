from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.utils.timezone import now

from django.db.models.signals import post_save
from django.dispatch import receiver


class HabrUser(AbstractUser):

    activation_key = models.CharField(max_length=128, blank=True, null=True)
    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):

        if now() < self.activation_key_expires:
            return False
        return True


class HabrProfile(models.Model):

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

"""
Django settings for habrband project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from config.config import settings
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = settings.DEBUG

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Application definition

INSTALLED_APPS = settings.INSTALLED_APPS

MIDDLEWARE = settings.MIDDLEWARE

ROOT_URLCONF = 'habrband.urls'

TEMPLATES = settings.TEMPLATES

WSGI_APPLICATION = 'habrband.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = settings.LANGUAGE_CODE

TIME_ZONE = settings.TIME_ZONE

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_USER_MODEL = 'users.User'

AUTH_USER_MODEL = settings.AUTH_USER_MODEL

"""
Локальная отправка почты
"""
DOMAIN_NAME = 'http://localhost:8000'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '2525'
EMAIL_HOST_USER = 'django@geekshop.local'
EMAIL_HOST_PASSWORD = 'geekshop'
EMAIL_USE_SSL = False

# EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = None, None //Отправка через тестовый сервере
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

LOGIN_ERROR_URL = '/'

AUTHENTICATION_BACKENDS = settings.AUTHENTICATION_BACKENDS
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CKEDITOR_CONFIGS = settings.CKEDITOR_CONFIGS
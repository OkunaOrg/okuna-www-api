"""
Django settings for openbook_org project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sentry_sdk
sentry_sdk.init("https://b4e45e84fa73420d91989e9122d08e4d@sentry.io/1212322")

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Environment flags
ENVIRONMENT = os.environ.get('ENVIRONMENT')

IS_PRODUCTION_ENVIRONMENT = True if ENVIRONMENT == 'production' else False

DEBUG = not IS_PRODUCTION_ENVIRONMENT

# Django secrets

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Hosts

ALLOWED_HOSTS = [] if not IS_PRODUCTION_ENVIRONMENT else [os.environ.get('DJANGO_ALLOWED_HOSTNAME')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'rest_framework',
    'openbook_org_contact',
    'mailchimp3'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'openbook_org.urls'

TEMPLATES = []

WSGI_APPLICATION = 'openbook_org.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Mail config 

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')

# Google re-captcha config

GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY')

# Django rest framework config

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# App config

OPENBOOK_CONTACT_FORM_MAIL = os.environ.get('OPENBOOK_CONTACT_FORM_MAIL')

USE_X_FORWARDED_HOST = IS_PRODUCTION_ENVIRONMENT

if IS_PRODUCTION_ENVIRONMENT:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
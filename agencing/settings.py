from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zh^_^6*^gk#1$i=b-s5nm!f1^dmaea=#u+)^n3-0q%%rd28!0t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'mainapp',

    'django_celery_beat',
    'django_celery_results',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agencing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'agencing.wsgi.application'


import os
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
TIME_ZONE = 'Etc/GMT-3'

LANGUAGE_CODE = 'en'
from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = True


#    Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []


# FTP_service
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CELERY SETTINGS
CELERY_BROKER_URL = "redis://localhost:6379" #install: redis -v 5.0.10 linux github
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SEREALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE #"UTC"
CELERY_RESULTBACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


#SMTP_SERVICE
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ranjalahyandrytahianasylvain@gmail.com'
EMAIL_HOST_PASSWORD = "dhsbbrbcinkfeuxp " # receive from "App password from gmail"
DEFAULT_FROM_EMAIL = 'Celery <ranjalahyandrytahianasylvain@gmail.com>'

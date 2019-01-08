"""
Django settings for estz project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, djcelery

djcelery.setup_loader()
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
REDIS_ADDR = os.environ.get('REDIS_1_PORT_6379_TCP_ADDR', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_1_PORT_6379_TCP_PORT', '6379')
REDIS_PWD = os.environ.get('REDIS_1_PORT_6379_TCP_PWD', '')
BROKER_URL = 'redis://:{}@{}:{}/0'.format(REDIS_PWD, REDIS_ADDR, REDIS_PORT)
CELERY_RESULT_BACKEND = BROKER_URL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.environ.get('DJANGO_DEVELOPMENT'):
    DEBUG = True
    SITE_URL = "http://estz.su:8000/, "
    CLAMD_ENABLED = False
else:
    # log to mod wsgi
    import logging
    import sys
    logging.basicConfig(stream=sys.stderr)
    DEBUG = True
    SITE_URL = "http://estz.su/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't#!40b5d9cjt&$084(rj&mk!8^+#pf5s)z3i=i_14#^n&-06cx'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ['estz.su', '*', 'localhost:8000']

# AUTH_USER_MODEL = 'users.User'

# -*- coding: utf-8 -*-

# Application definition

INSTALLED_APPS = [
    # 'users',  # must be on top!
    # 'localflavor',
    # 'smart_selects',
    'contact',
    'cms', 
    'treebeard', 
    'menus', 
    'sekizai', 
    'djangocms_admin_style',
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.admin', 
    'django.contrib.sites', 
    'django.contrib.sitemaps', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'djcelery',
	'django_crontab',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'blabla',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',

    'djangocms_text_ckeditor',
    'aldryn_style',
    'easy_thumbnails',
    'filer',
    'djangocms_picture',

    'plugin',
    'widget_tweaks',
    'phonenumber_field',
    'rest_framework',
    'snowpenguin.django.recaptcha2',
    'api',
    'captcha',
    'admin_area',
    'crispy_forms',
    # virus scan
    'django_clamd'
]

CLAMD_SOCKET = '/var/run/clamav/clamd.ctl'
CLAMD_USE_TCP = False


CRISPY_TEMPLATE_PACK = "bootstrap3"

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_LETTER_ROTATION = None
CAPTCHA_IMAGE_SIZE = (130, 50)
CAPTCHA_FONT_SIZE = 36
CAPTCHA_TIMEOUT = 25

# RECAPTCHA_PRIVATE_KEY = '6Le6KFUUAAAAAGriNHuzbLfA6gH02ckRnkZR2Hx-'
# RECAPTCHA_PUBLIC_KEY = '6Le6KFUUAAAAAJkV0p6EuhoM9igSZ1YpMjo0W57i'

PHONENUMBER_DEFAULT_REGION = 'ru'

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'estz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'estz/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

CMS_TEMPLATES = (
    ('home.html','Home Template'),
    ('page.html', 'Page Template'),
    ('about.html', 'About Template'),
    ('calculator.html', 'Calculator Template'),
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

WSGI_APPLICATION = 'estz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    'PAGINATE_BY': 10,  # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100  # Maximum limit allowed when using `?page_size=xxx`.
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'magic',
        'USER': 'root',
        'PASSWORD': '123456789@X',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

ADMINS = [('Admin', 'alpvira@yandex.ru'), ('admin estz.su', 'sasha1975@bk.ru')]

# -*- coding: utf-8 -*-
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/\
# EMAIL_FROM = 'administrator@estz.su'
# EMAIL_FROM = 'noreply@estz.su'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.estz.su'
# EMAIL_HOST = '127.0.0.1'
# EMAIL_PORT = 25
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'noreply@estz.su'
# EMAIL_HOST_PASSWORD = 'dfe23847ft34blo3u'
# EMAIL_USE_TLS = True

EMAIL_FROM = 'estz.su@simlit.com'
EMAIL_HOST_USER = 'estz.su@simlit.com'
EMAIL_HOST_PASSWORD = '5guhR9G789'
EMAIL_HOST = '194.182.68.217'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LANGUAGE_CODE = 'ru'
LANGUAGES = [('ru', 'Russian'), ]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# SITE_URL = "http://estz.su/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'estz/static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = SITE_URL+"static/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = SITE_URL+"media/"


LOGGING = {
    'version': 1,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CRONJOBS = [
    ('30 6 * * *', 'api.tasks.send_newsletters')
]


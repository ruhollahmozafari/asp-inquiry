"""
Django settings for Integrated_inquiry_system project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0#cm^rx9vu3nx$%v6^pigbbb%bo6#%7tr_zhk#=ve-a$vz6_#u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# CORS_ALLOWED_ORIGINS = [
#     # 'http://localhost:8000',
    
# ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'azbankgateways',
    
    'corsheaders',

    'django_filters',
    'rest_framework_swagger',

    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',

    'property',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Integrated_inquiry_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            }
        },
    },
]

WSGI_APPLICATION = 'Integrated_inquiry_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles'),)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
ELASTICSEARCH_DSL = {
    "default": {
        "hosts": "http://192.168.100.31:9200/",
        "timeout": 60, # Custom timeout
        },
}
CORS_ALLOW_ALL_ORIGINS=True


AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        # 'BMI': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        #     'SECRET_KEY': '<YOUR SECRET CODE>',
        # },
        # 'SEP': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        # },
        # 'ZARINPAL': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        # },
        'IDPAY': {
            # 'MERCHANT_CODE': '6a7f99eb-7c20-4412-a972-6dfb7cd253a4',
            'MERCHANT_CODE': '6a7t95eb-7e20-4412-a972-6dfb7cd253a4',
            'METHOD': 'POST',  # GET or POST
            'X_SANDBOX': 1,  # 0 disable, 1 active
        },
        # 'ZIBAL': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        # },
        # 'BAHAMTA': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        # },
        # 'MELLAT': {
        #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        #     'USERNAME': '<YOUR USERNAME>',
        #     'PASSWORD': '<YOUR PASSWORD>',
        # },
    },
    'IS_SAMPLE_FORM_ENABLE': True,  # اختیاری و پیش فرض غیر فعال است
    'DEFAULT': 'IDPAY',
    'CURRENCY': 'IRR',  # اختیاری
    'TRACKING_CODE_QUERY_PARAM': 'tc',  # اختیاری
    'TRACKING_CODE_LENGTH': 16,  # اختیاری
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',  # اختیاری
    'BANK_PRIORITIES': [
        # 'BMI',
        # 'SEP',
        # and so on ...
    ],  # اختیاری
}

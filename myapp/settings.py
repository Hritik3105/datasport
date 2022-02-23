"""
Django settings for myapp project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)

pymysql.install_as_MySQLdb()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@l_4z$myv1l378++o3p*zdv#(d#i=pl6wo1m6$u$=4$vxoa^l3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
   
import os
from django.contrib.messages import constants as messages


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }


ALLOWED_HOSTS = ['3.92.217.18']
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]


AUTH_USER_MODEL = 'app.user'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myapp.urls'

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

WSGI_APPLICATION = 'myapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql', 
       'NAME': 'datasport',
       'HOST': 'localhost',
       'PORT': '3306',
       'USER': 'admin',
       'PASSWORD': 'AdMiN@12345',
       'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
                     
        }
    }
}






# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.mysql',   
#        'NAME': 'myapp',
#        'HOST': 'localhost',
#        'PORT': '3306',
#        'USER': 'root',
#        'PASSWORD': '',
#        'OPTIONS': {
#             'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            
             
#         }
#     }
# }

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

PUBLISH_KEY = 'pk_test_51KR8onSF4o4pBHwpQer2dr9JWzMioxPtk60gknl4gmuwjIuMlhco11muEyApTshOM6WF9VVEi6gPwLX38bCwk4ZO00m2As3twU'
SECTRET_KEY = 'sk_test_51KR8onSF4o4pBHwpEbvzOhoSepVcczo3y7voulkh2OQwzt2PovTdTFAPKga4XKJjCrpn2JEB1sYRaWu5a9courlW00O0nRY5IT'
STRIPE_SIGNING_SECRET='whsec_41b779a2f382cc951f9705c8ca00a473f31201319eab5416d1ae614fe63007eb'



BASIC_PRICE_ID = 'price_1KTJNlSF4o4pBHwpoV9oCZ3J'
PROF_PRICE_ID = 'price_1KTJMvSF4o4pBHwpvI4g7UJP'
DAILY_PRICE_ID="price_1KTJMGSF4o4pBHwpBywN1s7q"
MONTHLY_PRICE_ID="price_1KTP23SF4o4pBHwpzwN3GQrE"
PROFE_PRICE_ID = 'price_1KTP23SF4o4pBHwpzwN3GQrE'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testsood981@gmail.com'
EMAIL_HOST_PASSWORD = 'mongodb31'
EMAIL_PORT = 587

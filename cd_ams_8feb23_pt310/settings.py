"""
Django settings for cd_ams_8feb23_pt310 project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ayou0coekw11p$l4(icxiwo=%3md=zl&0d4rd*h$m@a-^h73_v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [

    'users.apps.UsersConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'my_app',

    'django.contrib.humanize',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cd_ams_8feb23_pt310.urls'

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
        },
    },
]

WSGI_APPLICATION = 'cd_ams_8feb23_pt310.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cd8feb23pt310_db',
        'USER': 'root',
        'PASSWORD': 'mysqlpb',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ***********************************************************************
AUTH_USER_MODEL = 'users.CustomUser'

TIME_ZONE = 'Asia/Bangkok'
USE_TZ = False  # TO USE LOCALTIME NOT TIME AWARE
#
# LOGIN_REDIRECT_URL = 'gateway'  # if not defined will go to: acounts/profiles !!(default path)
# LOGOUT_REDIRECT_URL = 'logout'
# LOGIN_URL = 'login'  # if not defined, will go to http://127.0.0.1:8000/accounts/login/?next=/account/
# LOGOUT_URL = 'logout'


LOGIN_REDIRECT_URL = 'gateway'  # if not defined will go to: acounts/profiles !!(default path)
LOGOUT_REDIRECT_URL = 'Chollada_Apartment'
LOGIN_URL = 'login'  # if not defined, will go to http://127.0.0.1:8000/accounts/login/?next=/account/
LOGOUT_URL = 'admin_page'

# Tell Django to write email to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # OK

# Email server configuration
# ---------------------------

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp-relay.sendinblue.com'
# EMAIL_HOST_USER = 'pbootwicha@gmail.com'
# EMAIL_HOST_PASSWORD = '***********W8G2L3'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # static folder/directory
STATIC_ROOT = BASE_DIR / "staticfiles"  # all static files from collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

"""
Django settings for expertmind_service project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3695=15m))r7#ba2m(sys_4cp+hs6#_cp%#*cin+bue#9m2d#='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_stormpath',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # ...
    'django_stormpath.backends.StormpathBackend',
    'django_stormpath.backends.StormpathIdSiteBackend',
)


STORMPATH_ID = 'JSIDH4RGPFWXN6OKHPU30FC2X'
STORMPATH_SECRET = '/BGmEiZX0o5KFBJ3plIrN0MKTlD2vkBjYMkd4Fg5PGU'
STORMPATH_APPLICATION = 'https://api.stormpath.com/v1/applications/3pXFDJUov6hjrk2PTZg4tf'

AUTH_USER_MODEL = 'django_stormpath.StormpathUser'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LOGIN_REDIRECT_URL = '/'

# This should be set to the same URI you've specified in your Stormpath ID
# Site dashboard.  NOTE: This URL must be *exactly* the same as the one in
# your Stormpath ID Site dashboard.
STORMPATH_ID_SITE_CALLBACK_URI = 'http://aws.kelvmiao.info/stormpath-id-site-callback/'

# The URL you'd like to redirect users to after they've successfully logged
# into their account.
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web/templates')]
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

WSGI_APPLICATION = 'service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "web/static"),
)


REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES' : (
        'rest_framework.parsers.JSONParser',
    )
}
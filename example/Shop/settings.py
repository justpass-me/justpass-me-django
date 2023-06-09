"""
Django settings for theshop_demo_app project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!e+)(v@t9+!xxcaa^!aw*(hq_!v=sy%g)ys7l#qjo@1twg54iu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Shop',
    'justpass'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Shop.urls'

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

WSGI_APPLICATION = 'Shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('django_db_backend', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('django_db_name', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('django_db_username', 'postgres'),
        'PASSWORD': os.getenv('django_db_password', 'postgresPass'),
        'HOST': os.getenv('django_db_host', 'db'),
        'PORT': os.getenv('django_db_port', '5432'),
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = BASE_DIR/ 'staticfiles/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR/ 'static/']

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'Shop.User'

AUTHENTICATION_BACKENDS = (
    'justpass.OIDC_CLIENT.OIDCUserFinder',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_URL = "https://shop.amwal.co/"
LOGIN_URL = "/accounts/login/"
OIDC_RP_CLIENT_ID = "341992"
OIDC_RP_CLIENT_SECRET="250f218c9c1135ec962b07d0c876e0cf20b56612e68e70efa3456706"
OIDC_OP_URL= "https://mkalioby2.accounts.justpass.me/openid/"

# OIDC_RP_CLIENT_ID = "401818"
# OIDC_RP_CLIENT_SECRET="2c1e709fc7cb4b53ae168096608da4e63db36b0ff81506da243df61f"
# OIDC_OP_URL= "https://theshop.id.amwal.co/openid/"

#OIDC_CALLBACK_CLASS= "justpass.OIDC_CLIENT.Callback"
OIDC_USERNAME_FIELD = 'phone_number'

OIDC_RP_SCOPES= "openid token profile"
OIDC_RP_SIGN_ALGO = 'HS256'
OIDC_STORE_ID_TOKEN = True
OIDC_OP_JWKS_ENDPOINT=OIDC_OP_URL  +"jwks"
OIDC_OP_AUTHORIZATION_ENDPOINT=OIDC_OP_URL + "authorize/"
OIDC_OP_TOKEN_ENDPOINT = OIDC_OP_URL +"token/"
OIDC_OP_USER_ENDPOINT = OIDC_OP_URL + "userinfo/"
LOGIN_REDIRECT_URL_FAILURE="/justpass/failure/"
LOGIN_REDIRECT_URL = "/justpass/success/"

REGISTRATION_SUCCESS = "Shop.justpass.reg_success"
REGISTRATION_FAILURE = "Shop.justpass.reg_failure"
AUTHENTICATION_SUCCESS = "Shop.justpass.auth_success"
AUTHENTICATION_FAILURE = "Shop.justpass.auth_failure"



OIDC_AUTHENTICATE_CLASS = "justpass.OIDC_CLIENT.Authenticate"
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Customize these paths to match your project

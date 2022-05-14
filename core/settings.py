from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!c$^-qh^@l#58_(kz4s^gu_4*8d6d9m3ksf564agta5q2cpw)o'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True

ALLOWED_HOSTS = ['book-webite-read.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'searchfunc',
    "crispy_forms",
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        
        # Postgresql database
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbqajhj3bi0i7i',
        'USER': 'jeoltiyzuntqmz',
        'PASSWORD': '3534fa57e2b2f762d66ea54c129b218a09bb80e41c562421f177e3b1c42b5c62',
        'HOST': 'ec2-107-22-238-112.compute-1.amazonaws.com',
        'PORT': '5432'
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

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATIC_ROOT = 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'searchfunc.User'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'AKIA6DK2Y5GRJ5UZ6ZYK'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'booksitepictures'
AWS_QUERYSTRING_AUTH = False

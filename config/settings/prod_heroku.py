import dj_database_url

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600),
}

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = BASE_DIR / 'staticfiles'

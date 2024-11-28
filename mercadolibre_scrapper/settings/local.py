from .base import *
import os

SECRET_KEY = 'django-insecure-f-h*8&x9b%dayt#yuyua!=i*s4)v9p5)p_uu0bq_9(@po4^-lb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de archivos estáticos
STATIC_URL = '/static/'

# Directorio para archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
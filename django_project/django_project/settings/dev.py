from .base import *


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '120.76.41.122'
]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
import os
load_dotenv(os.path.join(BASE_DIR.parent, '.env'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_DEFAULT_NAME'),
        'USER': os.getenv('DB_DEFAULT_USER'),
        'PASSWORD': os.getenv('DB_DEFAULT_PASSWORD'),
        'HOST': os.getenv('DB_DEFAULT_HOST'),
        'PORT': os.getenv('DB_DEFAULT_PORT'),
    },
    'ocr_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_OCR_NAME'),
        'USER': os.getenv('DB_OCR_USER'),
        'PASSWORD': os.getenv('DB_OCR_PASSWORD'),
        'HOST': os.getenv('DB_OCR_HOST'),
        'PORT': os.getenv('DB_OCR_PORT'),
    }
}

# cors header setting
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",      # 开发时本地前端
    "http://127.0.0.1:5173",
]


# celery config https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
CELERY_BROKER_URL = 'amqp://jeremy:123456@127.0.0.1:5672//'
# CELERY_RESULT_BACKEND = 'django-db'


CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
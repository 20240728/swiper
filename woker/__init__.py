import os

from celery import Celery

from woker import config

os.environ.setdefault('DJANGO_SETTING_MODULE', 'swiper.settings')

celery_app = Celery('swiper')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()
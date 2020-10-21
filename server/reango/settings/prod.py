from .base import *

DEBUG = False
ALLOWED_HOST = os.environ.get('ALLOWED_HOSTS', ['*'])
SECRET_KEY = os.environ.get('SECRET_KEY', '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

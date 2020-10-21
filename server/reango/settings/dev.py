from .base import *

DEBUG = True
ALLOWED_HOST = ['*']
SECRET_KEY = 't_ujm45p)xy$d4co0gz+w)7uxe02av$vkjn^2)gs6kd@(vrhf+'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

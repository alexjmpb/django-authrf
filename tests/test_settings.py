"""Settings module for django tests."""
import os

SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = [
    'authrf',
    'tests',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
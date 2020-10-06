from .base import *
import os
from datetime import date
import logging
import requests


DEBUG = True

ALLOWED_HOSTS = ['*']

secret_file = os.path.join(BASE_DIR, 'secrets-dev.json')
secrets = Secrets(secret_file)

DATABASES = secrets.get_secret('DATABASES')

class MattermostRequestsHandler(logging.Handler):
        
    def emit(self, record):
        log_entry = self.format(record)
        return requests.post(
            url=secrets.get_secret('MATTERMOST_URL'),
            data=log_entry.encode('utf-8'),
            headers={'Content-type': 'application/json'}
        )

log_file_path = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'django-dev-log')
log_file_name = f'django-dev.log.{date.today().isoformat()}'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
        'json': {
            'format': '{"text": "#### %(asctime)s %(name)s %(levelname)s \n##### %(message)s"}'
        }
    },
    'handlers': {
        'file': {  
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(log_file_path, log_file_name),
            'when': 'midnight',
            'backupCount': 100,
            'formatter': 'standard',
        },
        'http': {
            'class': 'spc_pjt.settings.development.MattermostRequestsHandler',
            'formatter': 'json'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'http'],  
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
            'propagate': False
        },
    },
}
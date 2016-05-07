============
django-logit
============

Django Decorator of Logging Request Params

Installation
============

::

    pip install django-logit


Usage
=====

::

    from logit import logit

    @logit
    def xxx(request):
        xxx


Settings.py
===========

::

    # logger setting
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'logit': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/tmp/logit.log',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'logit': {
                'handlers': ['logit'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

    Use RotatingFileHandler to support rotation of disk log files.

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'logit': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/tmp/logit.log',
                'maxBytes': 15728640,  # 1024 * 1024 * 15B = 15MB
                'backupCount': 10,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'logit': {
                'handlers': ['logit'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

    Use TimedRotatingFileHandler to support rotation of disk log files at certain timed intervals.

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'logit': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '/tmp/logit.log',
                'when': 'midnight',
                'backupCount': 10,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'logit': {
                'handlers': ['logit'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }



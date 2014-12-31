#########################################################
# This is an example ``settings.py`` DO NOT use this    #
# in production, it is for demonstration purposes only. #
#########################################################

## First, we begin with the minimum required settings that
## django will need in order to run the demonstration.

import sys

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ldap_groups_test_db'
    }
}

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'ldap_groups',                  ## The django-ldap-group-mapper ...
    'myapp')                        ## ... and our "demo" app

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)


ROOT_URLCONF = 'myapp.urls'

STATIC_URL='/static/'
STATIC_ROOT='staticfiles'

SECRET_KEY = 'XXXxxxXXXxxxXXXxxxXXXxxxXXXxxx'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'standard'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_ldap.backend.LDAPBackend'
)

## Next, import the configuration options common to most (all?)
## LDAP implementations:

from Example_LDAP_Configs.common_config import *

## Finally, uncomment the line(s) that correspond to the LDAP
## implementation that you are running.

## OpenLDAP:

from Example_LDAP_Configs.openldap_config import *

## Microsoft Active Directory:

#from Example_LDAP_Configs.msad_config import *

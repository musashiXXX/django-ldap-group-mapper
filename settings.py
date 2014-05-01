import sys

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ldap_groups_test_db'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'ldap_groups',
    'tests')

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

# Bare minimum LDAP non-configuration
AUTH_LDAP_SERVER_URI = 'ldap://nonexistentserver'
AUTH_LDAP_BIND_DN = 'CN=Nonexistent,OU=Users,DC=example,DC=local'
AUTH_LDAP_BIND_PASSWORD = 'password'
LDAP_GROUPS_BASE_DN = 'OU=Groups,DC=example,DC=local'
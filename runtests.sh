#!/bin/sh
export PYTHONPATH='./'
if [ `which django-admin.py` ] ; then
    export DJANGO_ADMIN=django-admin.py
else
    export DJANGO_ADMIN=django-admin
fi

export args="$@"
if [ -z "$args" ] ; then
    # avoid running the tests for django.contrib.* (they're in INSTALLED_APPS)
    export args=ldap_groups
fi

$DJANGO_ADMIN test --traceback \
				   --settings=settings \
				   --verbosity 2 \
				   --pythonpath="../" "$args"

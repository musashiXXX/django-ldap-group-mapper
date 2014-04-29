#!/bin/sh
if [ `which django-admin.py` ] ; then
    export DJANGO_ADMIN=django-admin.py
else
    export DJANGO_ADMIN=django-admin
fi
$DJANGO_ADMIN test --traceback \
				   --settings=settings \
				   --verbosity 2 \
				   --pythonpath="./" "tests"

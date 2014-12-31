#!/bin/sh
export PYTHONPATH="./:../"
export DJANGO_SETTINGS_MODULE='settings'
FIXTURES="`pwd`/myapp/fixtures"
# Only load django groups and ldap_groups
# users fixture is not necessary if LDAP
# authentication is working.
GROUP_FIXTURES="$FIXTURES/groups.json"
LDAP_GROUP_FIXTURES="$FIXTURES/ldap_groups.json"

if [ `which django-admin.py` ] ; then
    export DJANGO_ADMIN=django-admin.py
else
    export DJANGO_ADMIN=django-admin
fi

export args="$@"

if [ -z "$args" ]; then
    export args='localhost:8000'
fi

$DJANGO_ADMIN syncdb --settings="$DJANGO_SETTINGS_MODULE" \
                     --pythonpath="$PYTHONPATH"

$DJANGO_ADMIN loaddata --settings="$DJANGO_SETTINGS_MODULE" \
                       --pythonpath="$PYTHONPATH" \
                       "$GROUP_FIXTURES" "$LDAP_GROUP_FIXTURES"

$DJANGO_ADMIN runserver --traceback \
				        --settings="$DJANGO_SETTINGS_MODULE" \
                        --pythonpath="$PYTHONPATH" \
				        --verbosity 1 "$args"

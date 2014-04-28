LDAP Group mapper for Django
============================

A simple LDAP group -> Django group mapper
------------------------------------------

The purpose of this Django app is to assist with mapping Django groups to LDAP
groups. This assumes that your Django project uses LDAP, via django-auth-ldap
for authentication and that you would like to use group membership to control
access to the application from an LDAP directory.

This app creates a 1:1 mapping between an LDAP group and a Django group so that
you can add users to the LDAP group and they will gain access to the application
according to their Django group counterpart.


Disclaimer: This isn't as polished (yet) as it needs to be for use in production. YMMV


Prerequisites
=============

You will need to ensure the following items are installed on your system:

* libldap2-dev
* python-dev
* libssl-dev
* libsasl2-dev

The following items can be installed in a virtualenv via pip or easy_install:

* python-ldap
* django-auth-ldap


Settings
========

Here is an example of the required settings you'll need to put into settings.py:
(...assuming that you are authenticating with Microsoft Active Directory)


    import os, ldap
    from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType

    AUTH_LDAP_START_TLS = True
    AUTH_LDAP_SERVER_URI = "ldap://ldapserver.example.local"
    AUTH_LDAP_BIND_DN = 'CN=LDAP Bind,CN=Users,DC=example,DC=local'
    AUTH_LDAP_BIND_PASSWORD = 'mysupersecretpassword'

    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        'OU=App Users,DC=example,DC=local',
        ldap.SCOPE_SUBTREE,
        '(sAMAccountName=%(user)s)') 

    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        'OU=App Users,DC=example,DC=local',
        ldap.SCOPE_SUBTREE,
        '(objectClass=group)')

    AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()
    AUTH_LDAP_REQUIRE_GROUP = 'CN=Permitted Users,OU=App Users,DC=example,DC=local'
    AUTH_LDAP_MIRROR_GROUPS = False
    AUTH_LDAP_ALWAYS_UPDATE_USER = True
    AUTH_LDAP_USER_FLAGS_BY_GROUP = { 
        'is_staff': 'CN=Staff,OU=App Users,DC=example,DC=local',
        'is_active': 'CN=Active,OU=App Users,DC=example,DC=local',
    }
    AUTH_LDAP_USER_ATTR_MAP = { 
        'first_name': 'givenName',
        'last_name': 'sn',
        'email': 'mail'
    }
    AUTH_LDAP_GLOBAL_OPTIONS = { 
        ldap.OPT_X_TLS_REQUIRE_CERT: False,
        ldap.OPT_REFERRALS: False,
    }
    LDAP_GROUPS_BASE_DN = 'OU=Users,DC=example,DC=local'

    try:
        AUTHENTICATION_BACKENDS += ( 
            'django_auth_ldap.backend.LDAPBackend',
            'django.contrib.auth.backends.ModelBackend',
        )
    except NameError:
        AUTHENTICATION_BACKENDS = ( 
            'django_auth_ldap.backend.LDAPBackend',
            'django.contrib.auth.backends.ModelBackend',
        )
    INSTALLED_APPS += ('ldap_groups',)


At a bare minimum, you need to configure these options:

* AUTH_LDAP_SERVER_URI
* AUTH_LDAP_BIND_DN
* AUTH_LDAP_BIND_PASSWORD
* LDAP_GROUPS_BASE_DN

Or else you run the risk of breaking your application.


Once everything has been configured, you simply need to login to Django's admin
interface, click on _Ldap group maps_, _Add ldap group map_, and then select
an LDAP group from the dropbox labeled _LDAP OU_, and select a Django group from
the multiple select box labeled _Django group_. Save. Now, any LDAP user that you
add to the LDAP group you selected, will gain access to the Django application
according to the rights of the Django group that it was mapped to.



_See Also:_

[http://pythonhosted.org/django-auth-ldap/index.html#](http://pythonhosted.org/django-auth-ldap/index.html#)
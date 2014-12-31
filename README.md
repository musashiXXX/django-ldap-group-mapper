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


Prerequisites
-------------

You will need to ensure the following items are installed on your system
(package names vary between distributions; these are the names of the 
required packages on debian variants):

* libldap2-dev
* python-dev
* libssl-dev
* libsasl2-dev

The following items can be installed in a virtualenv via pip or easy_install:

* python-ldap
* django-auth-ldap


HOW-TO & Demonstration
----------------------

It is recommended that you try running the included demo configuration first.
See ``tests/README.md`` for more details.



_See Also:_

[http://pythonhosted.org/django-auth-ldap/index.html#](http://pythonhosted.org/django-auth-ldap/index.html#)

LDAP Group mapper for Django
============================


A simple LDAP group -> Django group mapper
------------------------------------------

The purpose of this Django app is to assist with mapping Django groups to LDAP groups. This assumes that your Django
project uses LDAP, via django-auth-ldap for authentication and that you would like to use group membership to control
access to the application from an LDAP directory.

This app creates a 1:1 mapping between an LDAP group and a Django group so that you can add users to the LDAP group and
they will gain access to the application according to their Django group counterpart.


Prerequisites
-------------

You will need to ensure the following items are installed on your system (package names vary between distributions; these
are the names of the required packages on debian variants):

* libldap2-dev
* python-dev
* libssl-dev
* libsasl2-dev

The following items can be installed in a virtualenv via pip or easy_install:

* python-ldap
* django-auth-ldap


HOW-TO & Demonstration
----------------------

It is recommended that you try running the included demo configuration first. See [tests/README.md](tests/README.md) for
more details.

The basic steps are as follows:

1.  Setup a functional instance of Django and the admin interface.

2.  Install ``django-ldap-group-mapper`` and it's requirements. Alternatively, ensure that the path to the ``ldap_groups``
    directory exists in your pythonpath.

3.  Configure the appropriate options in ``settings.py`` see the following files for more details:

    *   [tests/settings.py](tests/settings.py)
    *   [tests/Example\_LDAP_Configs/common\_config.py](tests/Example_LDAP_Configs/common_config.py)
    *   [tests/Example\_LDAP_Configs/openldap\_config.py](tests/Example_LDAP_Configs/openldap_config.py)
    *   [tests/Example\_LDAP_Configs/msad\_config.py](tests/Example_LDAP_Configs/msad_config.py)

    The latter two in the list are separate examples for OpenLDAP and Microsoft Active Directory, respectively.

4.  If you use one of the included configs (at this time, there are only two; ``openldap_config.py`` and
    ``msad_config.py``) then make sure that the search scopes are appropriate for the structure of your LDAP directory. By
    default, the searches will only search the immediate container (i.e., SCOPE_ONELEVEL) and not subcontainers (i.e.,
    SCOPE_SUBTREE.) See the links below for more information about this.


Further reading
---------------

*   [django-auth-ldap.config.LDAPGroupType](https://pythonhosted.org/django-auth-ldap/reference.html?highlight=grouptype#django_auth_ldap.config.LDAPGroupType)

*   [django-auth-ldap.config.LDAPSearch](https://pythonhosted.org/django-auth-ldap/reference.html?highlight=ldapsearch#django_auth_ldap.config.LDAPSearch)

*   __Search filters in [python-ldap](http://www.python-ldap.org):__ ``django-auth-ldap.config.LDAPSearch`` relies on
    [LDAPObject.search*](http://www.python-ldap.org/doc/html/ldap.html?highlight=search#ldap.LDAPObject.search) from
    [python-ldap](http://www.python-ldap.org). Take a moment to familarize yourself with it.

*   [LDAP String Representation of Search Filters (RFC)](http://tools.ietf.org/html/rfc4515.html)
   
*   [Active Directory Search Filter Syntax](http://msdn.microsoft.com/en-us/library/aa746475%28v=vs.85%29.aspx)

*   [All Active Directory Object Attributes](http://msdn.microsoft.com/en-us/library/ms675090%28v=vs.85%29.aspx)

*   [How to Query Individual Properties of the "userAccountControl" Active Directory User property using LDAP](http://blogs.msdn.com/b/muaddib/archive/2008/10/08/query-individual-properties-of-the-useraccountcontrol-active-directory-user-property.aspx)

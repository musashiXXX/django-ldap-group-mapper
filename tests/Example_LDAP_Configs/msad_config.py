import ldap
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType
from common_config import users_ou, groups_ou

# See the following url for more information about AUTH_LDAP_GROUP_TYPE:
# https://pythonhosted.org/django-auth-ldap/reference.html?highlight=grouptype#django_auth_ldap.config.LDAPGroupType

AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# In the example below, the user search will only match users with accounts that are _not_ disabled. Refer to the section
# titled "Further Reading" in this package's README.md for more information about search scopes.

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    users_ou, ldap.SCOPE_ONELEVEL, '(&(sAMAccountName=%(user)s)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))')

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    groups_ou, ldap.SCOPE_ONELEVEL, '(objectClass=group)')

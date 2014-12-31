import ldap
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType
from common_config import users_ou, groups_ou

AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# See http://www.python-ldap.org/doc/html/ldap.html
# for more information about configuring search scopes

# In the example below, the user search will only match users
# with accounts that are _not_ disabled.

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    users_ou, ldap.SCOPE_ONELEVEL, '(&(sAMAccountName=%(user)s)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))')

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    groups_ou, ldap.SCOPE_ONELEVEL, '(objectClass=group)')

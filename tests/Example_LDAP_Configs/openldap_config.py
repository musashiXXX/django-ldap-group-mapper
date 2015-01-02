import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
from common_config import users_ou, groups_ou

# See the following url for more information about AUTH_LDAP_GROUP_TYPE:
# https://pythonhosted.org/django-auth-ldap/reference.html?highlight=grouptype#django_auth_ldap.config.LDAPGroupType

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

#Refer to the section titled "Further Reading" in this package's README.md for more information about search scopes.

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    users_ou, ldap.SCOPE_ONELEVEL, '(uid=%(user)s)')

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    groups_ou, ldap.SCOPE_ONELEVEL, '(objectClass=groupOfNames)')

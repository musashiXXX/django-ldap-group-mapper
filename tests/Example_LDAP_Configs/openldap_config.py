import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
from common_config import users_ou, groups_ou

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# See http://www.python-ldap.org/doc/html/ldap.html
# for more information about configuring search scopes

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    users_ou, ldap.SCOPE_ONELEVEL, '(uid=%(user)s)')

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    groups_ou, ldap.SCOPE_ONELEVEL, '(objectClass=groupOfNames)')

ldap_domain = 'dc=example,dc=local'
groups_ou = 'ou=Groups,dc=example,dc=local'
users_ou = 'ou=Users,dc=example,dc=local'

AUTH_LDAP_SERVER_URI = 'ldap://localhost'
AUTH_LDAP_BIND_DN = 'uid=lbind,%s' % users_ou
AUTH_LDAP_BIND_PASSWORD = 'password'
AUTH_LDAP_REQUIRE_GROUP = 'cn=All Users,%s' % groups_ou
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_MIRROR_GROUPS = False
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_staff': 'cn=App Admins,%s' % groups_ou,
    'is_active': 'cn=All Users,%s' % groups_ou,
    'is_superuser': 'cn=App Admins,%s' % groups_ou
}
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
}

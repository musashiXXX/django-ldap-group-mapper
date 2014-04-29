from django.db.models import Q
from django.test import TestCase
#from ldap_groups.models import LDAPGroupMap
from django_auth_ldap.backend import LDAPBackend, populate_user
from django.contrib.auth.models import User, Group

class LDAPGroupMapTestCase(TestCase):
    fixtures = ['users',
                'groups',
                'ldap_groups']

    def setUp(self):
        self.admin_user_group_dns = set([
            u'cn=app admins,ou=groups,dc=example,dc=local',
            u'cn=app users,ou=groups,dc=example,dc=local'])
        self.non_admin_user_group_dns = set([
            u'cn=app users,ou=groups,dc=example,dc=local'])
        self.admin_user = User.objects.get(username = 'admin')
        self.nonadmin_user = User.objects.get(username = 'user')
        # Our users have not been assigned to any django groups yet, if this
        # raises an exception, there is something wrong with our fixtures
        self.assertEquals(self.admin_user.groups.count(), 0)
        self.assertEquals(self.nonadmin_user.groups.count(), 0)


    def test_admin_user_group_mapping(self):
        # Test the group map for the 'admin' user
        ldap_user = User()
        ldap_user.group_dns = self.admin_user_group_dns
        populate_user.send(
            LDAPBackend, user = self.admin_user, ldap_user = ldap_user)

        # According to our group mapping, the 'admin' user should be populated
        # to both the 'Admins' and the 'Users' Django groups.
        self.assertTrue(self.admin_user.groups.filter(name = 'Admins'))
        self.assertTrue(self.admin_user.groups.filter(name = 'Users'))

        self.assertEquals(Group.objects.filter(
            user__username = 'admin').count(), 2)

        self.assertFalse(self.admin_user.groups.filter(
            name = 'nonexistentgroup'))

        # Ensure Django groups are updated when LDAP group membership changes.
        ldap_user.group_dns = set([
            u'cn=app users,ou=groups,dc=example,dc=local'])
        populate_user.send(
            LDAPBackend, user = self.admin_user, ldap_user = ldap_user)
        self.assertFalse(self.nonadmin_user.groups.filter(
            name = 'Admins'))
        self.assertEquals(Group.objects.filter(
            user__username = 'admin').count(), 1)

        
    def test_nonadmin_user_group_mapping(self):
        # Test the mapping for the non-admin user, 'user'.
        ldap_user = User()
        ldap_user.group_dns = self.non_admin_user_group_dns
        populate_user.send(
            LDAPBackend, user = self.nonadmin_user, ldap_user = ldap_user)

        # According to our group mapping, the 'user' user should be populated
        # to only the 'Users' Django group.
        self.assertFalse(self.nonadmin_user.groups.filter(
            name = 'Admins'))
        self.assertTrue(self.nonadmin_user.groups.filter(
            name = 'Users'))

        self.assertEquals(Group.objects.filter(
            user__username = 'user').count(), 1)

        self.assertFalse(self.nonadmin_user.groups.filter(
            name = 'nonexistentgroup'))

        # Ensure Django groups are updated when LDAP group membership changes.
        ldap_user.group_dns = set([])
        populate_user.send(
            LDAPBackend, user = self.nonadmin_user, ldap_user = ldap_user)
        self.assertFalse(self.nonadmin_user.groups.filter(
            name = 'Users'))
        self.assertEquals(Group.objects.filter(
            user__username = 'user').count(), 0)

import ldap, logging
from ldap import SERVER_DOWN
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django_auth_ldap.backend import LDAPBackend, populate_user
logger = logging.getLogger(__name__)

server_uri = settings.AUTH_LDAP_SERVER_URI
bind_dn = settings.AUTH_LDAP_BIND_DN
bind_password = settings.AUTH_LDAP_BIND_PASSWORD
ldap_groups_search = settings.AUTH_LDAP_GROUP_SEARCH

def get_ldap_groups():
    dn_choices = []
    l = ldap.initialize(server_uri)
    try:
        l.simple_bind_s(bind_dn, bind_password)
    except SERVER_DOWN, e:
        logger.warning('%s: %s' % (e.message.get('desc'), server_uri))
        return dn_choices
    for dn, entry in ldap_groups_search.execute(l):
        dn_choices += [(dn, entry['cn'][0])]
    return dn_choices

class LDAPGroupMap(models.Model):
    ldap_group = models.CharField(
        unique = True,
        verbose_name = 'LDAP Group',
        choices = get_ldap_groups(),
        max_length = 255)

    django_group = models.ManyToManyField(Group)
    
    def __unicode__(self):
        django_groups = ', '.join(i.name for i in self.django_group.all())
        return '%s -> %s' % (self.ldap_group, django_groups)
    
    class Meta:
        ordering = ('ldap_group',)


@receiver(populate_user, sender = LDAPBackend)
def set_group_perms(sender, **kwargs):
    '''
    Make sure that the user's group membership is always up to date.
    Note: Updates only occur when a user authenticates.
    '''
    user = kwargs['user']
    ldap_user = kwargs['ldap_user']
    user.groups.clear()
    for group_map in LDAPGroupMap.objects.all():
        dn = group_map.ldap_group.lower()
        if dn in ldap_user.group_dns:
            user.groups.add(*group_map.django_group.filter(
                ldapgroupmap__ldap_group__iexact = dn))
            user.save()

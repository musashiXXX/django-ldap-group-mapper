from django.contrib import admin
from models import LDAPGroupMap

class LDAPGroupMapAdmin(admin.ModelAdmin):
    filter_horizontal = ('django_group',)
    search_fields = ['ldap_group',
                    'django_group__name']

admin.site.register(LDAPGroupMap, LDAPGroupMapAdmin)
from django.contrib.admin.sites import AlreadyRegistered
from tf.restricted.sites import site
from django.contrib import admin


from models import Shell, PyShell, DBShell, Site

class NoAddDel( admin.ModelAdmin):
     def has_add_permission(self, request):
        return False
     def has_delete_permission(self, request):
        return False

try:
    site.register( Shell, NoAddDel)
    site.register( PyShell, NoAddDel)
    site.register( DBShell, NoAddDel)
    site.register( Site)
except AlreadyRegistered:
    pass

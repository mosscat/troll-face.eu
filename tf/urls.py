from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from tf import restricted
restricted.autodiscover()

urlpatterns = patterns('',
    url(r'^', include( restricted.site.urls)),
    url(r'^ascii/', include( 'tf.asciiart.urls')),
	url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^process/', include( 'tf.process.urls')),
	
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import *

urlpatterns = patterns( 'tf.manager.views',
	url(r'^shell/$', 'shell'),
	url(r'^pyshell/$', 'pyshell'),
	url(r'^dbshell/$', 'dbshell'),

	url(r'^site/$', 'site'),
	url(r'^site/add/$', 'site_add'),
	url(r'^site/\d+/delete/$', 'site_del'),
)

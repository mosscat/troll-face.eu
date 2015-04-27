from django.conf.urls import *

urlpatterns = patterns( 'tf.process.views',
	url(r'^(?P<shell_id>\w+)/$', 'process'),
)

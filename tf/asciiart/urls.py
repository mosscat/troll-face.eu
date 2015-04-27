from django.conf.urls import *

urlpatterns = patterns( 'tf.asciiart.views',
	url(r'^$', 'getASCII'),
	url(r'^(?P<art_id>\d+)/$', 'getASCII'),
)

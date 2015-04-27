# -*- coding:utf-8 -*-
import tf.imaginator.render

from functools import update_wrapper
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.sites import site as default_site
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.contenttypes import views as contenttype_views
import json
from django.views.decorators.csrf import csrf_protect
from django.http import Http404

from random import randint

import tf.index.views
from tf.restricted.decorators import xhr_required
from tf.restricted.auth import auth
from tf import settings, imaginator
from tf.restricted.models import origin

from django.conf import settings
import datetime

from django.conf.urls import *
	
def set_cookie(response, key, value, expire=None):
	if expire is None:
		max_age = 365*24*60*60  #one year
	else:
		max_age = expire
	expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
	response.set_cookie(key, value, max_age=max_age, expires=expires, 
		domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)

class AdminSiteRegistryFix( object ):
	'''
	This fix links the '_registry' property to the orginal AdminSites
	'_registry' property. This is necessary, because of the character of
	the admins 'autodiscover' function. Otherwise the admin site will say,
	that you havn't permission to edit anything.
	'''

	def _registry_getter(self):
		return default_site._registry

	def _registry_setter(self,value):
		default_site._registry = value

	_registry = property(_registry_getter, _registry_setter)

class MyAdminSite( AdminSite, AdminSiteRegistryFix ):
	#index_template = 'restricted/index.html'

	# return 404 if user has no permission to view
	def admin_view(self, view, cacheable=False):
		def inner(request, *args, **kwargs):
			if not self.has_permission(request):
				raise Http404
			return view(request, *args, **kwargs)
		if not cacheable:
			inner = never_cache(inner)
		if not getattr(view, 'csrf_exempt', False):
			inner = csrf_protect(inner)
			
		return update_wrapper(inner, view)

	def get_urls(self):
		if settings.DEBUG:
			self.check_dependencies()

		def wrap(view, cacheable=False):
			def wrapper(*args, **kwargs):
				return self.admin_view(view, cacheable)(*args, **kwargs)
			return update_wrapper(wrapper, view)

		# Admin-site-wide views.
		urlpatterns = patterns('',
			url( r'^$',					self.index, name='index'),
			url( r'^login/$',			self.login,	name='login'),
			url( r'^logout/$',			self.logout, name='logout'),

			# get origin image
			url( r'^origin/$',			self.getorigin, name='origin'),

			# manager
			url( r'^manager/',			include( 'tf.manager.urls')),
			
			# parent routes
			url( r'^change/$',
				wrap( self.password_change, cacheable=True),
				name='password_change'),
			url( r'^change/done/$',
				wrap( self.password_change_done, cacheable=True),
				name='password_change_done'),
			url( r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$',
				wrap( contenttype_views.shortcut))
		)

		for model, model_admin in self._registry.iteritems():
			urlpatterns += patterns('',
				url( r'^(?P<app_label>%s)/$' % (model._meta.app_label ), wrap( self.app_index), name='app_list')
#				url( r'^%s/%s/' % (model._meta.app_label, model._meta.module_name), include(model_admin.urls))
			)

		return urlpatterns

	@never_cache
	def index(self, request, extra_context=None):
		if not request.user.is_authenticated():
			return tf.index.views.main( request)
		else:
			return super( MyAdminSite, self).index( request, extra_context)

	@never_cache
	def logout(self, request, extra_context=None):
		result = auth.logout( request)
		if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			return HttpResponse(
					simplejson.dumps( { 'result' : result } ),
					mimetype='application/json'
				)
		else:
			return HttpResponseRedirect( '/');

	@never_cache
	@xhr_required
	def login( self, request, extra_context=None):
		request.session.set_expiry( 900)			# 15 min
		return HttpResponse(
					simplejson.dumps( { 'result' : auth.login( request)} ),
					mimetype='application/json'
				)

	@never_cache
	def getorigin(self, request, extra_context=None):
		def text():
			while True:
				try: return u'%s' % origin.objects.get(  id = randint(1, origin.objects.count()))
				except: return 'error..'
		return imaginator.render.text(
			text()
		)

site = MyAdminSite()

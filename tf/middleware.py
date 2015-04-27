from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response
from django.template import RequestContext

TEMPLATE_PATH = '401.html'

class PermissionDeniedTo404(object):
	def process_exception(self, request, exception):
		if type(exception) == PermissionDenied:
			return render_to_response(TEMPLATE_PATH, { 'exception': exception },
				context_instance = RequestContext(request))
		return None
#		raise Exception('test, %s, %s' % ( type(exception), PermissionDenied))
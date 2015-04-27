from django.template.response import TemplateResponse
from django.http import HttpResponse, Http404

from tf.restricted.decorators import permission_required
from tf import settings

import httplib, urllib

@permission_required('process.change_shellinabox')
def process( request, shell_id = 'bash'):
	if request.method == 'GET':
		return TemplateResponse(
					request,
					'shell.html'
				)

	conn = httplib.HTTPSConnection(settings.SHELL_HOSTNAME)
	headers = {"Content-type": "application/x-www-form-urlencoded",
		"Accept": "text/plain"}
	try:
		conn.request("POST", "/" + shell_id + '/', urllib.urlencode( request.POST), headers)
		conn.sock.settimeout(settings.SHELL_TIMEOUT)

		response = conn.getresponse()
	
		if response.status != 200:
			raise Http404

		return HttpResponse( content = "%s" % response.read())
	except Http404:
		raise Http404
	except:
		return TemplateResponse(
					request,
					'shell_response.html',
					{ 'response': 'OK'}
				)

	

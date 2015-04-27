from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.http import Http404

from tf.restricted.decorators import permission_required

@permission_required('manager.change_shell')
def shell( request):
	return TemplateResponse(
				request,
				'newWindow.html',
				{ 'url' : '/process/bash/' }
			)

@permission_required('manager.change_pyshell')
def pyshell( request):
	return TemplateResponse(
				request,
				'newWindow.html',
				{ 'url' : '/process/main/' }
			)

@permission_required('manager.change_dbshell')
def dbshell( request):
	return TemplateResponse(
				request,
				'newWindow.html',
				{ 'url' : '/process/db_main/' }
			)

@permission_required('manager.change_site')
def site( request):
	return TemplateResponse(
				request,
				'manager.html'
			)

@permission_required('manager.add_site')
def site_add( request):
	return TemplateResponse(
				request,
				'manager.html'
			)

@permission_required('manager.delete_site')
def site_del( request):
	return TemplateResponse(
				request,
				'manager.html'
			)

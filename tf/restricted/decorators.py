from django.http import HttpResponseRedirect
from functools import wraps
from django.http import Http404

def _login_required( f):
	def decorated(request, *args, **kwargs):
		#this check the session if userid key exist, if not it will redirect to login page
		if not request.user.is_authenticated():
			raise Http404
		return f(request, *args, **kwargs)

	decorated.__doc__ = f.__doc__
	decorated.__name__ = f.__name__
	decorated.__dict__.update( f.__dict__)
	return decorated

def login_required( f):
	def decorated(self, request, *args, **kwargs):
		#this check the session if userid key exist, if not it will redirect to login page
		if not request.user.is_authenticated():
			raise Http404
		return f(self, request, *args, **kwargs)

	decorated.__doc__ = f.__doc__
	decorated.__name__ = f.__name__
	decorated.__dict__.update( f.__dict__)
	return decorated

param_decorator = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)

@param_decorator
def permission_required( function, perm):
	def _function( request, *args, **kwargs):
		if request.user.has_perm( perm):
			return function( request, *args, **kwargs)
		else:
			raise Http404
	return _function

def xhr_required( f):
	def decorated(self, request, *args, **kwargs):
		if request.META.get('HTTP_X_REQUESTED_WITH') != 'XMLHttpRequest':
			raise Http404
		return f( self, request, *args, **kwargs)

	decorated.__doc__ = f.__doc__
	decorated.__name__ = f.__name__
	decorated.__dict__.update( f.__dict__)
	return decorated

# todo:
# def permission_required(p):

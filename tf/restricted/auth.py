from django.contrib.auth import authenticate, login, logout

class Authenticate(object):
	def login(self, request):
		username = request.REQUEST['name']
		password = request.REQUEST['pass']

		user = authenticate( username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return 'OK'
			else:
				return 'DISABLED'
		else:
			return 'INVALID'

	def logout(self, request):
		logout(request);
		return 'OK'

auth = Authenticate()
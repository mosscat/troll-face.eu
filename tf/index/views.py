from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect

from tf.asciiart.selector import Picture

@csrf_protect
def main( request):
	pic = Picture()
	return TemplateResponse( 
				request,
				'index.html',
				{ 'ascii' : pic.getArtwork() }
			)

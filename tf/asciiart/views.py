from django.template.response import TemplateResponse

from selector import Picture
#from tf.restricted.decorators import xhr_required

def getASCII( request, art_id = -1):
	pic = Picture()
	return TemplateResponse(
				request,
				'asciiart.html',
				{ 'ascii' : pic.getArtwork( art_id) }
			)

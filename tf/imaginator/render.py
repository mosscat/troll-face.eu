# -*- coding: utf-8 -*-

from django.http import HttpResponse
from cStringIO import StringIO
import random

try:
    import Image, ImageDraw, ImageFont, ImageChops
except ImportError:
    from PIL import Image, ImageDraw, ImageFont, ImageChops

from tf.imaginator.conf import settings

class text( HttpResponse):

	def __init__(self, message):
		if settings.TEXT_FONT_PATH.lower().strip().endswith('ttf'):
			font = ImageFont.truetype( settings.TEXT_FONT_PATH, settings.TEXT_FONT_SIZE, encoding = "unic")
		else:
			font = ImageFont.load( settings.TEXT_FONT_PATH, encoding = "unic")

		size = font.getsize( message)
		size = ( size[0]*2, int(size[1] * 1.2))
		image = Image.new( 'RGBA', size , settings.TEXT_BACKGROUND_COLOR)

		try:
			PIL_VERSION = int(NON_DIGITS_RX.sub('',Image.VERSION))
		except:
			PIL_VERSION = 116

		xpos = 2
		for char in message:
			if( char!=' '):
				fgimage = Image.new( 'RGB', size, settings.TEXT_FOREGROUND_COLOR)
				charimage = Image.new( 'RGB', font.getsize(' %s '%char), '#000000')
				chardraw = ImageDraw.Draw( charimage)
				chardraw.text( ( 0,0), '%s' % char, font=font, fill='#ffffff')

				if settings.TEXT_LETTER_ROTATION:
					if PIL_VERSION >= 116:
						charimage = charimage.rotate( random.randrange( *settings.TEXT_LETTER_ROTATION ), expand=0, resample=Image.BICUBIC)
					else:
						charimage = charimage.rotate( random.randrange( *settings.TEXT_LETTER_ROTATION ), resample=Image.BICUBIC)

				charimage = charimage.crop( charimage.getbbox())
				maskimage = Image.new( 'L', size)

				maskimage.paste( charimage, (xpos, 4 + ( 12 - charimage.size[1]), xpos+charimage.size[0], 4 + ( 12 - charimage.size[1]) + charimage.size[1]))
				size = maskimage.size
				image = Image.composite( fgimage, image, maskimage)
				xpos = xpos + 2 + charimage.size[0]
			else:
				xpos = xpos + 8

		image = image.crop((0,0,xpos+1,size[1]))

		self.out = StringIO()
		image.save( self.out, "PNG")
		self.out.seek( 0)

		super( text, self).__init__(
			content_type = 'image/png',
			status = 200,
			content = self.out.read(),
		)

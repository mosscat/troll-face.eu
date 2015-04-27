import os
from django.conf import settings

TEXT_FONT_PATH = getattr(settings,'TEXT_FONT_PATH', os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'fonts/DejaVuSansMono-Bold.ttf')))
TEXT_FONT_SIZE = getattr(settings,'TEXT_FONT_SIZE', 12)
TEXT_LETTER_ROTATION = getattr(settings, 'TEXT_LETTER_ROTATION', (-15,15))
TEXT_BACKGROUND_COLOR = getattr(settings,'TEXT_BACKGROUND_COLOR', ( 51, 51, 51, 0))
TEXT_FOREGROUND_COLOR= getattr(settings,'TEXT_FOREGROUND_COLOR', '#ffffcc')
#TEXT_CHALLENGE_FUNCT = getattr(settings,'TEXT_CHALLENGE_FUNCT','captcha.helpers.random_char_challenge')
#TEXT_NOISE_FUNCTIONS = getattr(settings,'TEXT_NOISE_FUNCTIONS', ('captcha.helpers.noise_arcs','captcha.helpers.noise_dots',))
#TEXT_FILTER_FUNCTIONS = getattr(settings,'TEXT_FILTER_FUNCTIONS',('captcha.helpers.post_smooth',))
#TEXT_WORDS_DICTIONARY = getattr(settings,'TEXT_WORDS_DICTIONARY', '/usr/share/dict/words')
#TEXT_PUNCTUATION = getattr(settings, 'TEXT_PUNCTUATION', '''_"',.;:-''')
#TEXT_FLITE_PATH = getattr(settings,'TEXT_FLITE_PATH',None)
#TEXT_TIMEOUT = getattr(settings, 'TEXT_TIMEOUT', 5) # Minutes
#TEXT_LENGTH = int(getattr(settings, 'TEXT_LENGTH', 4)) # Chars
TEXT_IMAGE_BEFORE_FIELD = getattr(settings,'TEXT_IMAGE_BEFORE_FIELD', True)
#TEXT_DICTIONARY_MIN_LENGTH = getattr(settings,'TEXT_DICTIONARY_MIN_LENGTH', 0)
#TEXT_DICTIONARY_MAX_LENGTH = getattr(settings,'TEXT_DICTIONARY_MAX_LENGTH', 99)

if TEXT_IMAGE_BEFORE_FIELD:
	TEXT_OUTPUT_FORMAT = getattr(settings,'TEXT_OUTPUT_FORMAT', u'%(image)s %(hidden_field)s %(text_field)s')
else:
	TEXT_OUTPUT_FORMAT = getattr(settings,'TEXT_OUTPUT_FORMAT', u'%(hidden_field)s %(text_field)s %(image)s')

# Failsafe
#if TEXT_DICTIONARY_MIN_LENGTH > TEXT_DICTIONARY_MAX_LENGTH:
#	TEXT_DICTIONARY_MIN_LENGTH, TEXT_DICTIONARY_MAX_LENGTH = TEXT_DICTIONARY_MAX_LENGTH, TEXT_DICTIONARY_MIN_LENGTH
#
#
#def _callable_from_string(string_or_callable):
#	if callable(string_or_callable):
#		return string_or_callable
#	else:
#		return getattr(__import__( '.'.join(string_or_callable.split('.')[:-1]), {}, {}, ['']), string_or_callable.split('.')[-1])
#
#def get_challenge():
#	return _callable_from_string(TEXT_CHALLENGE_FUNCT)
#
#
#def noise_functions():
#	if TEXT_NOISE_FUNCTIONS:
#		return map(_callable_from_string, TEXT_NOISE_FUNCTIONS)
#	return list()
#
#def filter_functions():
#	if TEXT_FILTER_FUNCTIONS:
#		return map(_callable_from_string, TEXT_FILTER_FUNCTIONS)
#	return list()

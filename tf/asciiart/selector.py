from django.http import Http404
from numpy import append, array
from random import randint
from tf.settings import ASCII_ART_FOLDER

import os

class Picture( object):
	path = ASCII_ART_FOLDER;
	picCount = 0

	items = array( [])

	def __init__(self):
		dirList=os.listdir(self.path)

		for fname in dirList:
			self.picCount += 1
			self.items = append( self.items, [fname])

	def getFileContents(self, filename):
		try:
			return open( self.path + filename).read()
		except:
			raise Http404

	def getArtwork(self, id = -1):
		try:
			return self.getFileContents( self.items[ [int( id), (int(randint( 1, self.picCount))-1)][id<0]])
		except:
			raise Http404

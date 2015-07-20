from __future__ import unicode_literals
from nltk.stem.api import StemmerI

class Stemmer(StemmerI):
	def __init__(self):
		self.ends = ['ên', 'an', 'yan', 'mend', 'em', 'êmin', 'in', 'tir']
	def stem(self, word):


		for end in self.ends:
			if word.endswith(end):
				word = word[:-len(end)]
		return word

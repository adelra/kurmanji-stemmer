from __future__ import unicode_literals
from nltk.stem.api import StemmerI

class Stemmer(StemmerI):
	def __init__(self):
		self.ends = ['é','í', 'a', 'ek', 'van', 'dar', 'kar', 'xane', 'stan', 'geh', 'én', 'an', 'yan', 'mend', 'em', 'émin', 'in', 'tir']
	def stem(self, word):


		for end in self.ends:
			if word.endswith(end):
				word = word[:-len(end)]
		return word

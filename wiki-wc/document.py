import re

class Document:
	def __init__(self, text):
		self.text = text
		self.words = list(re.split(r'\s', re.sub(r'[^A-Za-z ]', '', text)))
		self.bag = { }
		for word in self.words:
			if word not in self.bag:
				self.bag[word] = 0
			self.bag[word] += 1

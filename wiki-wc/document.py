class Document:
	def __init__(self, text):
		self.text = text
		self.words = text.split(' ')
		self.bag = { }
		for word in self.words:
			if word not in self.bag:
				self.bag[word] = 0
			self.bag[word] += 1
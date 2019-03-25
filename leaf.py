class Decision_tree_leaf (object):
	def __init__(self, data, classification):
		self.data = data
		self.classification = classification

	def print(self, level):
		print('-'*level + str(self.data) + ' ' + str(self.classification))

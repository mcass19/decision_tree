class Decision_tree_leaf (object):
	def __init__(self, classification):
		self.classification = classification

	def print(self, level):
		print(str(self.classification))

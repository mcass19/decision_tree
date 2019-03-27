class Decision_tree_leaf (object):
	def __init__(self,val):
		self.value = val
		self.label = None

	def set_label(self, lab):
		self.label = lab

	def print(self, level):
		print('-'*(level + 1) + str(self.value) + ' -> ' + str(self.label))

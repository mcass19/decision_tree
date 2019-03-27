#from leaf import Decision_tree_leaf

class Decision_tree_node (object):
	def __init__ (self, attr):
		self.attribute = attr
		self._branches = []

	# def add_children_node(self, children_attribute, children_data):
	# 	children_node = Decision_tree_node(children_attribute)
	# 	self._children.append((children_node, children_data))
	# 	return children_node

	# def add_children_leaf(self, children_data, children_classification):
	# 	children_leaf = Decision_tree_leaf(children_classification) 
	# 	self._children.append((children_leaf, children_data))

	def add_branch(self, branch):
		self._branches.append(branch)

	def set_attribute(self, att):
		self.attribute = att

	def print(self, level):
		print(str(self.attribute))
		for branch in self._branches:
			branch.print(level + 1)

class Decision_tree_leaf (object):
	def __init__ (self, lab):
		self.label = lab

	def set_label(self, lab):
		self.label = lab

	def print(self, level):
		print(self.label)

class Decision_tree_branch (object):
	def __init__(self, val):
		self.value = val
		self.child = None

	def add_child(self, node):
		self.child = node

	def print(self, level):
		print("-"*level + str(self.value) + ' -> ',end='')
		self.child.print(level + 1)
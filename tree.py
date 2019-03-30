class DecisionTreeNode(object):
	
	def __init__ (self, attr):
		self.attribute = attr
		self._branches = []

	def add_branch(self, branch):
		self._branches.append(branch)

	def set_attribute(self, att):
		self.attribute = att

	def print(self, level):
		print(str(self.attribute))
		for branch in self._branches:
			branch.print(level + 1)

# ---------------------------------------------------------------------------

class DecisionTreeLeaf(object):
	
	def __init__ (self, lab):
		self.label = lab

	def set_label(self, lab):
		self.label = lab

	def print(self, level):
		print(self.label)

# ---------------------------------------------------------------------------

class DecisionTreeBranch(object):
	
	def __init__(self, val):
		self.value = val
		self.child = None

	def add_child(self, node):
		self.child = node

	def print(self, level):
		print("-"*level + str(self.value) + ' -> ',end='')
		self.child.print(level + 1)
		
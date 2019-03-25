from leaf import Decision_tree_leaf

class Decision_tree_node (object):
	def __init__ (self, att, data):
		self.attribute = att
		self.data = data
		self._children = []

	def add_children_node(self, children_attribute, children_data):
		children_node = Decision_tree_node(children_attribute, children_data)
		self._children.append(children_node)
		return children_node

	def add_children_leaf(self, children_data, children_classification):
		children_leaf = Decision_tree_leaf(children_data, children_classification) 
		self._children.append(children_leaf)

	def childrens(self):
		return _children

	def search_by_attribute(self, att):
		print(self.attribute)
		if self.attribute is att:
			return self
		else:
			aux = None
			i = 0
			while aux == None and i < len(self._children):
				if not type(self._children[i]) is Decision_tree_leaf:
					aux = self._children[i].search_by_attribute(att)
				i += 1
			return aux

	def print(self, level):
		print('-'*level + str(self.attribute) + ' / ' + str(self.data))
		for child in self._children:
			child.print(level + 1)
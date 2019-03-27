from leaf import Decision_tree_leaf

class Decision_tree_node (object):
	def __init__ (self, att):
		self.attribute = att
		self._children = []

	def add_children_node(self, children_attribute, children_data):
		children_node = Decision_tree_node(children_attribute)
		self._children.append((children_node, children_data))
		return children_node

	def add_children_leaf(self, children_data, children_classification):
		children_leaf = Decision_tree_leaf(children_classification) 
		self._children.append((children_leaf, children_data))

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
		print(str(self.attribute))
		for child in self._children:
			print('-'*(level + 1) + str(child[1]) + ' / ', end='')
			child[0].print(level + 1)
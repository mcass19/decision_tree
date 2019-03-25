from tree import Decision_tree_node

class id3(object):
	def __init__(self):

	def create_tree(self, dataset, attributes):
		index_attribute = gain.calculate_max_gain()

		root = Decision_tree_node(index_attribute, None)

		self.create_tree_recursive(root, dataset)




	def create_tree_recursive(self, root, dataset, attributes):
		if dataset.target_values.len() == 1:
			for a in attributes[root.attribute]:
				root.add_children_leaf(a, dataset.target_values[0])

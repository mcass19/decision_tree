from tree import Decision_tree_node, Decision_tree_leaf, Decision_tree_branch

class Id3(object):
	
	def __init__(self):
		pass

	def generate_tree(self, data_set, attributes):
		attr = data_set.max_gain_attribute(attributes)
		root = Decision_tree_node(attr)

		for vi in attributes[attr]:
			child_branch = Decision_tree_branch(vi)
			root.add_branch(child_branch)

			if (attr in data_set.continue_attributes):
				if (vi == attributes[attr][0]):
					data_set_vi = data_set.subset_of_value(attr, float('-inf'), vi)
				elif(vi == attributes[attr][-1]):
					data_set_vi = data_set.subset_of_value(attr, vi, float('inf'))
				else:
					data_set_vi = data_set.subset_of_value(attr, vi , attributes[attr][attributes[attr].index(vi) + 1])
			else:
				data_set_vi = data_set.subset_of_value(attr, vi, -1)

			available_labels = data_set_vi.target_values()

			if len(data_set_vi.data) == 0:
				available_labels = data_set.target_values()
				aux_leaf = Decision_tree_leaf(data_set.most_common_target_value(available_labels))
				child_branch.add_child(aux_leaf)
			elif len(available_labels) == 1:
				aux_leaf = Decision_tree_leaf(available_labels[0])
				child_branch.add_child(aux_leaf)
			elif len(attributes) == 0:
				aux_leaf = Decision_tree_leaf(data_set_vi.most_common_target_value(available_labels))
				child_branch.add_child(aux_leaf)
			else:
				child_branch.add_child(self.generate_tree(data_set_vi, attributes.remove(attr)))

		return root
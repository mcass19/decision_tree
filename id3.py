from tree import Decision_tree_node, Decision_tree_leaf, Decision_tree_branch

class Id3(object):
	
	def __init__(self):
		pass

	def generate_tree(self, data_set, attributes, attributes_aux):
		attr = data_set.max_gain_attribute(attributes, attributes_aux)
		root = Decision_tree_node(attributes.index(attributes_aux[attr]))

		for vi in attributes_aux[attr]:
			child_branch = Decision_tree_branch(vi)
			root.add_branch(child_branch)

			data_set_vi = data_set.subset_of_value(attributes.index(attributes_aux[attr]), vi)

			available_labels = data_set_vi.target_values()

			if len(data_set_vi.data) == 0:
				available_labels = data_set.target_values()
				aux_leaf = Decision_tree_leaf(data_set.most_common_target_value(available_labels))
				child_branch.add_child(aux_leaf)
			elif len(available_labels) == 1:
				aux_leaf = Decision_tree_leaf(available_labels[0])
				child_branch.add_child(aux_leaf)
			elif len(attributes_aux) == 0:
				aux_leaf = Decision_tree_leaf(data_set_vi.most_common_target_value(available_labels))
				child_branch.add_child(aux_leaf)
			else:
				attributes_aux.pop(attr)
				child_branch.add_child(self.generate_tree(data_set_vi, attributes, attributes_aux))

		return root
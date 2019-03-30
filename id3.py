from tree import DecisionTreeNode, DecisionTreeLeaf, DecisionTreeBranch

class Id3(object):
	
	def __init__(self):
		pass

	def generate_tree(self, data_set, attributes, attributes_aux):
		attr = data_set.max_gain_attribute(attributes, attributes_aux)

		root = DecisionTreeNode(attributes.index(attributes_aux[attr]))

		values_list = attributes_aux[attr].copy()
		attributes_aux.pop(attr)

		for value in values_list:
			branch = DecisionTreeBranch(value)
			root.add_branch(branch)

			data_set_value = data_set.subset_of_value(attributes.index(values_list), value)

			available_labels = data_set_value.target_values()

			if len(data_set_value.data) == 0:
				available_labels = data_set.target_values()
				leaf = DecisionTreeLeaf(data_set.most_common_target_value(available_labels))
				branch.add_child(leaf)
			elif len(available_labels) == 1:
				leaf = DecisionTreeLeaf(available_labels[0])
				branch.add_child(leaf)
			elif len(attributes_aux) == 0:
				leaf = DecisionTreeLeaf(data_set_value.most_common_target_value(available_labels))
				branch.add_child(leaf)
			else:
				branch.add_child(self.generate_tree(data_set_value, attributes, attributes_aux))

		return root
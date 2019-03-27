from tree import Decision_tree_node, Decision_tree_leaf, Decision_tree_branch

class Id3 (object):
	def __init__(self):
		self.gain = Gain()		

	def ID3_recursive(self, data_set,  _attributes):
		a = data_set.max_gain_attribute(_attributes)
		root = Decision_tree_node(a)

		for vi in _attributes[a]:
			child_branch = Decision_tree_branch(vi)
			root.add_branch(child_branch)

			if(a in data_set.continue_attributes):
				if(vi == _attributes[a][0]):
					data_set_vi = data_set.subset_of_value(a, float('-inf'), vi)
				elif(vi == _attributes[a][-2]):
					data_set_vi = data_set.subset_of_value(a, vi, float('inf'))
				else:
					data_set_vi = data_set.subset_of_value(a, vi , _attributes[a][_attributes[a].index(vi) + 1])
			else:
				data_set_vi = data_set.subset_of_value(a, vi, -1)

			available_labels = data_set_vi.target_values()

			if data_set_vi.len() == 0:
				aux_leaf = Decision_tree_leaf()
				aux_leaf.set_label( data_set.most_common_target_value(available_labels))
				child_branch.add_leaf(aux_leaf)
			elif available_labels.len() == 1:
				aux_leaf = Decision_tree_leaf()
				aux_leaf.set_label(available_labels[0])
				child_branch.add_leaf(aux_leaf)
			elif _attributes.len() == 0:
				aux_leaf = Decision_tree_leaf()
				aux_leaf.set_label( data_set_vi.most_common_target_value(available_labels) )
				child_branch.add_leaf(aux_leaf)
			else:
				child_branch.add_node(ID3_recursive(data_set_vi, _attributes.remove(A)))

		return root
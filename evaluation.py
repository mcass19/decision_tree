from tree import DecisionTreeLeaf
class Evaluation(object):

	def __init__(self):
		pass

	def evaluate_tree(self, tree, data_set):
		cant_classified = 0
		cant_not_classified = 0

		for instance in data_set.data:
			_ = self.recursive_evaluate_tree(tree, instance, data_set)
			if _:	
				cant_classified += 1
			else:
				cant_not_classified += 1

		return cant_classified, cant_not_classified

	def recursive_evaluate_tree(self, node, instance, data_set):
		if(type(node) is DecisionTreeLeaf):
			return node.label == instance[-1]
		else:
			for branch in node._branches:
				if ((node.attribute in data_set.continue_attributes) and
					(instance[node.attribute] > branch.value[0]) and
					(instance[node.attribute] <= branch.value[1])):
					return self.recursive_evaluate_tree(branch.child, instance, data_set)	
					
				elif branch.value == instance[node.attribute]:
					return self.recursive_evaluate_tree(branch.child, instance, data_set)


	def confusion_matrix(self, data_set, classes_trees):
		target_values = data_set.target_values()
		evaluations = []
		for instance in data_set.data:
			best_evaluation = (-1,float('inf'))
			for tree in classes_trees:
				aux = self.evaluate_tree_class(tree[1], instance, data_set)
				if (aux[0] and  best_evaluation[1] > aux[1]):
					best_evaluation = (classes_trees.index(tree), aux[1])
			evaluations.append((instance, classes_trees[best_evaluation[0]][0]))

		confusion_matrix = []
		cant_labels = len(target_values)
		for label in target_values:
			row = [0]*cant_labels
			for e in evaluations:
				if e[0][-1] == label:
					row[target_values.index(e[1])] += 1
			confusion_matrix.append(row)
		return confusion_matrix


	#devuelvo true o false y la cantidad de pasos
	# El tree tiene en sus hojas verdadero o falso
	def evaluate_tree_class(self, tree_class, instance, data_set):
		if type(tree_class) is DecisionTreeLeaf:
			return (tree_class.label, 1)
		else:
			for branch in tree_class._branches:
				if ((tree_class.attribute in data_set.continue_attributes) and
					(instance[tree_class.attribute] > branch.value[0]) and
					(instance[tree_class.attribute] <= branch.value[1])):
					_ = self.evaluate_tree_class(branch.child, instance, data_set)
					return 	(_[0], _[1] + 1)
					
				elif branch.value == instance[tree_class.attribute]:
					_ = self.evaluate_tree_class(branch.child, instance, data_set)
					return (_[0], _[1] + 1)
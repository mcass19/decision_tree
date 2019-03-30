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
			print('node.label ' + str(node.label) + ' instance[-1] ' +str(instance[-1]))
			print('return ' + str(node.label == instance[-1]))
			return node.label == instance[-1]
		else:
			for branch in node._branches:
				if ((node.attribute in data_set.continue_attributes) and
					(instance[node.attribute] > branch.value[0]) and
					(instance[node.attribute] <= branch.value[1])):
					return self.recursive_evaluate_tree(branch.child, instance, data_set)	
					
				elif branch.value == instance[node.attribute]:
					return self.recursive_evaluate_tree(branch.child, instance, data_set)	
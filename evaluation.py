from tree import DecisionTreeLeaf

class Evaluation(object):

	def __init__(self):
		pass

	# cant_classified es la cantidad de instancias del data_set (test) que clasificaron 
	# cant_not_classified las que no
	def evaluate_tree(self, tree, data_set):
		cant_classified = 0
		cant_not_classified = 0

		for instance in data_set.data:
			classify = self.recursive_evaluate_tree(tree, instance, data_set)
			if classify:	
				cant_classified += 1
			else:
				cant_not_classified += 1

		return cant_classified, cant_not_classified

	# Recorre el arbol recursivamente, eligiendo las ramas que clasifican el valor
	# del atributo nodo en instance. Si al llegar a una hoja la etiqueta 
	# es la misma verdadero, si no falso
	def recursive_evaluate_tree(self, node, instance, data_set):
		if (type(node) is DecisionTreeLeaf):
			return node.label == instance[-1]
		else:
			for branch in node._branches:
				if ((node.attribute in data_set.continue_attributes) and
					(instance[node.attribute] > branch.value[0]) and
					(instance[node.attribute] <= branch.value[1])):
					return self.recursive_evaluate_tree(branch.child, instance, data_set)		
				elif branch.value == instance[node.attribute]:
					return self.recursive_evaluate_tree(branch.child, instance, data_set)


	# Devuelve una matriz (lista de listas) de confusion para data_set (test) 
	# y la lista de arboles de clase classes_trees
	def confusion_matrix(self, data_set, classes_trees):
		target_values = data_set.target_values()

		# evaluations es una lista donde cada elemento es una tupla
		# (instancia, etiqueta), donde instancia es la instancia que se evaluó
		# y etiqueta la clase del arbol que mejor clasificó a dicha instancia
		evaluations = []
		for instance in data_set.data:
			best_evaluation = (-1, float('inf'))
			for tree in classes_trees:
				aux = self.evaluate_tree_class(tree[1], instance, data_set)

				# Se selecciona el árbol que menos ramas precisó para llegar a True
				if (aux[0] and  best_evaluation[1] > aux[1]):
					best_evaluation = (classes_trees.index(tree), aux[1])
			
			# Agrega la instancia y la etiqueta del árbol que mejor clasificó
			evaluations.append((instance, classes_trees[best_evaluation[0]][0]))

		confusion_matrix = []
		for label in target_values:
			row = [0] * len(target_values)
			for e in evaluations:
				if e[0][-1] == label:
					row[target_values.index(e[1])] += 1
			confusion_matrix.append(row)
			row.insert(0, label)

		return confusion_matrix


	# Devuelve la tupla (clasificaciíon, pasos) donde clasificación es el valor con el
	# que clasificó a la instancia el árbol tree_class (True o False) y pasos la cantidad de
	# nodos que recorrio para llegar a la hoja
	def evaluate_tree_class(self, tree_class, instance, data_set):
		if (type(tree_class) is DecisionTreeLeaf):
			return (tree_class.label, 1)
		else:
			for branch in tree_class._branches:
				if ((tree_class.attribute in data_set.continue_attributes) and
					(instance[tree_class.attribute] > branch.value[0]) and
					(instance[tree_class.attribute] <= branch.value[1])):
					classify = self.evaluate_tree_class(branch.child, instance, data_set)
					return 	(classify[0], classify[1] + 1)
				elif branch.value == instance[tree_class.attribute]:
					classify = self.evaluate_tree_class(branch.child, instance, data_set)
					return (classify[0], classify[1] + 1)
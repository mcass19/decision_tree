from data_set import DataSet
from generate_attributes import Generator
from id3 import Id3
from evaluation import Evaluation

print('*****************************')
print('ARBOLES DE DECISION - ALGORITMO ID3')
print('*****************************')

option_data_set = input('Ingrese 1 para generar un árbol a partir del data set Iris \no 2 para generar un árbol a partir del data set Covtype: ')
option_cant = input('Ingrese la cantidad de puntos de corte para los atributos continuos: ')

data_set = DataSet()
data_set_test = data_set.load_data_set(float(option_data_set))

print('Generó dataset')

generator = Generator()
attributes = generator.generate_attributes(data_set, int(option_cant), data_set.continue_attributes)

print('Generó atributos')

id3 = Id3()
attributes_aux = attributes.copy()
tree = id3.generate_tree(data_set, attributes, attributes_aux)

print('Generó árbol')

print('\n')

print('Árbol ID3 generado:')
tree.print(0)

print('\n')

evaluation = Evaluation()
cant_classified, cant_not_classified = evaluation.evaluate_tree(tree, data_set_test)
print('De las {} instancias tomadas para evaluar:'.format(cant_classified + cant_not_classified))
print('\t -> {} instancias clasificaron correctamente'.format(cant_classified))
print('\t -> {} instancias clasificaron incorrectamente'.format(cant_not_classified))

print('\n')

print('Árboles de clases generados: ')

classes_trees = []

for label in data_set.target_values():
    data_set_class = data_set.data_set_class(label)
    attributes_aux = attributes.copy()
    tree = id3.generate_class_tree(data_set_class, label, attributes, attributes_aux)
    classes_trees.append((label ,tree))
    print('Clase: ' + str(label))
    tree.print(0)
    print('\n')

confusion_matrix = evaluation.confusion_matrix(data_set_test, classes_trees)

for i in confusion_matrix:
	print(str(i))


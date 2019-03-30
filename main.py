from data_set import DataSet
from generate_attributes import Generator
from id3 import Id3

print('*****************************')
print('ARBOLES DE DECISION - ALGORITMO ID3')
print('*****************************')

option_data_set = input('Ingrese 1 para generar un árbol a partir del data set Iris \no 2 para generar un árbol a partir del data set Covtype: ')

option_continue_attributes = input('Ingrese los índices (comienzan en 0) de los atributos continuos (si tiene), separados por coma: ')
continue_attributes = []
option_cant = 0
if (option_continue_attributes):
    aux = option_continue_attributes.split(',')
    for a in aux:
        continue_attributes.append(int(a))
    option_cant = input('Ingrese la cantidad de puntos de corte para los atributos continuos: ')

option_hot_vector = input('Ingrese los índices (comienzan en 0) de inicio y fin de los hot vectors (si tiene), separados por coma: ')
hot_vector = []
if (option_hot_vector):
    aux = option_hot_vector.split(',')
    for a in aux:
        hot_vector.append(int(a))

data_set = DataSet(continue_attributes)
data_set.load_data_set(float(option_data_set), hot_vector)

generator = Generator()
attributes = generator.generate_attributes(data_set, int(option_cant), continue_attributes)

id3 = Id3()
attributes_aux = attributes.copy()
tree = id3.generate_tree(data_set, attributes, attributes_aux)

print('Árbol generado:')
tree.print(0)

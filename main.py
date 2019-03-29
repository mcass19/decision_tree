from data_set import DataSet
from generate_attributes import Generator
from id3 import Id3

print('*****************************')
print('Árboles de decisión')
print('*****************************')

option_data_set = input('Ingrese 1 para generar un árbol a partir del data set Iris \no 2 para generar un árbol a partir del data set Covtype: ')

option_continue_attributes = input('Ingrese los índices (comienzan en 0) de los atributos conitnuos, separados por coma: ')
continue_attributes = []
aux = option_continue_attributes.split(',')
for a in aux:
    continue_attributes.append(int(a))

option_cant = input('Ingrese la cantidad de puntos de corte para los atributos continuos: ')

data_set = DataSet(continue_attributes)
data_set.load_data_set(float(option_data_set))

generator = Generator()
attributes = generator.generate_attributes(data_set, float(option_cant), continue_attributes)
print(attributes)
id3 = Id3()
attributes_aux = attributes.copy()
tree = id3.generate_tree(data_set, attributes, attributes_aux)

print('Árboles generado:')
tree.print(0)

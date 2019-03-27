from data_set import DataSet
from generate_attributes import Generator
from id3 import Id3

print('*****************************')
print('Árboles de decisión')
print('*****************************')

option_data_set = input('Ingrese 1 para generar un árbol a partir del data set Iris \no 2 para generar un árbol a partir del data set Covtype: ')
option_cant = input('Ingrese la cantidad de puntos de corte para los atributos: ')

# option_continue_attributes = input('Vemos como hacer')
continue_attributes = []
# continue_attributes = lista_con_indices_que_ingreso_el_usuario

data_set = DataSet(continue_attributes)
data_set.load_data_set(float(option_data_set))

generator = Generator()
attributes = generator.generate_attributes(data_set, float(option_cant), continue_attributes)

id3 = Id3()
tree = id3.generate_tree(data_set, attributes)

print('Árboles generado:')
tree.print(0)

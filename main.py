from data_set import DataSet

print('*****************************')
print('Árboles de decisión')
print('*****************************')

option_data_set = input('Ingrese 1 para generar un árbol a partir del data set Iris \no 2 para generar un árbol a partir del data set Covtype: ')
option_cant = input('Ingrese la cantidad de puntos de corte para los atributos: ')

data_set = DataSet(float(option_data_set))
generator = Generator()

print(data_set.data)

# conjuntos = generar_conjuntos(option_cant, data_set)

# tree = generar_tree(conjuntos)

# print('Árboles generado:')

# print_tree

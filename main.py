
print('*****************************')
print('Árboles de decisión')
print('*****************************')

option_data_set = input('Ingrese 1 para generar un árbol a partir del data set Iris \no 2 para generar un árbol a partir del data set Covtype: ')
option_cant = input('Ingrese la cantidad de puntos de corte: ')

print(type(option_data_set))

def load_dataset(data_id):
	data = []

	print("data_id: " + str(data_id))

	# Hardcodeado
	if data_id == 1:
		print('iris')
		file_name = 'iris.data'
		number_of_attributes = 4
		number_of_lines = 150
	else:
		print('covtype')
		file_name = 'covtype.data'
		number_of_attributes = 54
		number_of_lines = 581012

	with open(file_name, 'r') as file_to_read:
		for line in range(number_of_lines):
			aux = file_to_read.readline().split(',')
			for i in range(number_of_attributes):
				aux[i] = float(aux[i])
			data.append(aux)

	return data

# La matriz con atributos y etiquetas
data_set = load_dataset(float(option_data_set))

print(data_set)

# conjuntos = generar_conjuntos(option_cant, data_set)

# tree = generar_tree(conjuntos)

# print('Árboles generado:')

# print_tree

from operator import itemgetter
from data_set import DataSet

class Generator(object):

	def __init__(self):
		pass

	# Devuelve una lista donde cada elemento attributes[i] es una lista de valores que
	# puede tomar el atributo i. Para los valores continuos, los elementos de 
	# attributes[i] van a ser tuplas 
	# num_cut es la cantidad de cortes que ingresa el usuario
	def generate_attributes(self, data_set, num_cut, continues_attributes): 
		# Lista de indices en el que existe un cambio de clase en data_set
		toggles = data_set.toggle_list() 
		
		attributes = []			

		for att in range(data_set.cant_attributes()):
			if (att in continues_attributes):
				candidates = []

				# Para cada cambio calcula la ganancia del valor candidato
				for t in toggles:
					candidate = (data_set.data[t][att] + data_set.data[t + 1][att]) / 2
					gain = data_set.calculate_gain(att, candidate)
					if not (candidate, gain) in candidates:
						candidates.append((candidate, gain))
				
				# Ordena los candidatos por ganancia
				sorted(candidates, key=itemgetter(1))

				# Si la cantidad de candidatos se excede a la cantidad que me brindó
				# el usuario como límite, me quedo con num_cut candidatos
				if num_cut < len(candidates):
					candidates = candidates[(len(candidates) - num_cut):]
				
				_onlycandidates = []
				for i in range(len(candidates)):
					_onlycandidates.append(candidates[i][0])
				_onlycandidates.sort()

				# Agrega los extremos de la lista de candidatos, donde el extremo izquierdo
				# empieza con -inf, y el derecho termina con +inf
				candidates = []	
				candidates.append((float('-inf'), _onlycandidates[0]))	
				for i in range(len(_onlycandidates)-1):
					candidates.append((_onlycandidates[i], _onlycandidates[i + 1]))	
				candidates.append((_onlycandidates[-1], float('inf')))	
				
				# Agrego la lista de valores para el atributo att a la lista final
				attributes.append(candidates)
			else:
				aux = data_set.attributes_value(att)
				attributes.append(aux)

		return attributes

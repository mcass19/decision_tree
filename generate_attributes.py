# pedirle al dataset una lista con el indice de las lineas en donde cambia la etiqueta
# para cada atributo para cada valor de la lista anterior tengo que vera que valor tiene el atriuto en esa posicion y en esa posicion + 1, sumarlos y / 2
# -> agrego a la lista ese candidato
# ordenar cada lista de cada atributo por ganancia
# me quedocon los primeros n entradas de cada lista,donde n es el input del usuario o el largo de la lista si es menor al input del usuario

from data_set import DataSet
from operator import itemgetter

class Generator(object):

	def __init__(self):
		pass

	def generate_attributes(self, data_set, num_cut, continues_attributes): 
		# toggles = data_set.toggle_list()
		cant_attributes = data_set.cant_attributes()
		
		_attributes = []

		for att in range(cant_attributes):
			# if (att in continues_attributes):
			# 	_candidates = []
				
			# 	for t in toggles:
			# 		aux = float(data_set[t][att] + data_set[t + 1][att]) / 2
			# 		aux_gain = gain.calculate_gain(att, aux)
			# 		if not (aux, aux_gain) in _candidates:
			# 			_candidates.append((aux, aux_gain))
				
			# 	sorted(_candidates, key=itemgetter(1))

			# 	if num_cut < _candidates.len():
			# 		_aux.append( _candidates[(_candidates.len() - num_cut):])
			# 	else:
			# 		_aux.append(_candidates)
			# 	for i in range(_aux.len()):
			# 		_attributes[att].append(_aux[i][0])

			# 	_attributes[att].sort()
			# else:
				_attributes.append([])
				aux = data_set.attributes_value(att)
				_attributes[att].append(aux)

		return _attributes



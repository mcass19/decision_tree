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
		toggles = data_set.toggle_list()
		cant_attributes = data_set.cant_attributes()
		
		_attributes = []			
		print(toggles)
		for att in range(cant_attributes):
			if (att in continues_attributes):
				_candidates = []
				_aux = []

				for t in toggles:
					aux_candidate = (data_set.data[t][att] + data_set.data[t + 1][att]) / 2
					aux_gain = data_set.calculate_gain(att, aux_candidate)
					if not (aux_candidate, aux_gain) in _candidates:
						_candidates.append((aux_candidate, aux_gain))
				
				sorted(_candidates, key=itemgetter(1))

				if num_cut < len(_candidates):
					_aux.append(_candidates[(len(_candidates) - num_cut):])
				else:
					_aux = _candidates.copy()
				
				_aux_list = []
				for i in range(len(_aux)):
					_aux_list.append(_aux[i][0])

				_aux_list.sort()
				_aux_final_list = []	
				_aux_final_list.append((float('-inf'), _aux_list[0]))	
				for i in range(len(_aux_list)-1):
					_aux_final_list.append((_aux_list[i], _aux_list[i + 1]))	
				_aux_final_list.append((_aux_list[-1], float('inf')))	
				
				_attributes.append(_aux_final_list)
				# _attributes[att].sort()
			else:
				aux = data_set.attributes_value(att)
				_attributes.append(aux)

		return _attributes



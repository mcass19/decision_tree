from operator import itemgetter
from data_set import DataSet

class Generator(object):

	def __init__(self):
		pass

	def generate_attributes(self, data_set, num_cut, continues_attributes): 
		toggles = data_set.toggle_list()
		
		_attributes = []			

		for att in range(data_set.cant_attributes()):
			if (att in continues_attributes):
				_candidates = []

				for t in toggles:
					candidate = (data_set.data[t][att] + data_set.data[t + 1][att]) / 2
					gain = data_set.calculate_gain(att, candidate)
					if not (candidate, gain) in _candidates:
						_candidates.append((candidate, gain))
				
				sorted(_candidates, key=itemgetter(1))

				if num_cut < len(_candidates):
					_candidates = _candidates[(len(_candidates) - num_cut):]
				
				_only_candidates = []
				for i in range(len(_candidates)):
					_only_candidates.append(_candidates[i][0])
				_only_candidates.sort()

				_candidates = []	
				_candidates.append((float('-inf'), _only_candidates[0]))	
				for i in range(len(_only_candidates)-1):
					_candidates.append((_only_candidates[i], _only_candidates[i + 1]))	
				_candidates.append((_only_candidates[-1], float('inf')))	
				
				_attributes.append(_candidates)
			else:
				aux = data_set.attributes_value(att)
				_attributes.append(aux)

		return _attributes



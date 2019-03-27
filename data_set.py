from __future__ import division
import math

class DataSet(object):
    
    def __init__(self, continue_attributes):
        self.data = []
        self.continue_attributes = continue_attributes

    # creación de estructura a partir del data_set
    def load_data_set(self, data_id):    
        data = []

        # esto es porque tenemos dos chances de data_set según la letra del ejercicio
        # se debe modificar si se quiere tener en cuenta otros data_sets
        if data_id == 1:
            file_name = 'example.data'
            number_of_attributes = 5
            number_of_lines = 4
            # file_name = 'iris.data'
            # number_of_attributes = 4
            # number_of_lines = 150
        else:
            file_name = 'covtype.data'
            number_of_attributes = 54
            number_of_lines = 581012

        with open(file_name, 'r') as file_to_read:
            for _ in range(number_of_lines):
                aux = file_to_read.readline().split(',')
                # for i in range(number_of_attributes):
                #     aux[i] = float(aux[i])
                data.append(aux)

        self.data = data

    # retorna una lista con todas las posibles etiquetas
    def target_values(self):
        tags = []
        instance = []
        for instance in self.data:
            if instance[-1] not in tags:
                tags.append(instance[-1]) 
            
        return tags

    # retorna el subconjunto de los valores que cumplen con value para el atributo de indice attr
    def subset_of_value(self, attr, base, max):
        data_set_result = DataSet(self.continue_attributes)
        subset = []
        for instance in self.data:
            if ((attr in self.continue_attributes) and 
                ((instance[attr] > min and instance[attr] <= max))):
                    subset.append(instance)
            elif instance[attr] == base:
                subset.append(instance)

        data_set_result.data = subset
        return data_set_result

    # retorna una lista con los indices para los cuales cambia el valor de la etiqueta
    def toggle_list(self):
        indexes = []
        instance = []
        for instance in range(len(self.data)):
            if (instance != len(self.data)) and (self.data[instance][-1] != self.data[instance + 1][-1]):
                indexes.append(instance[-1]) 
        
        return indexes
    
    def most_common_target_value(self, target_values):
        cant_tags = []
        for _ in range(len(target_values)):
            cant_tags.append(0)
        
        instance = []
        for instance in self.data:
            for i in range(len(target_values)):
                if instance[-1] == target_values[i]:
                    cant_tags[i] += 1 

        return target_values[cant_tags.index(max(cant_tags))]

    def entropy(self):      
        entropy = 0
        for target in self.cant_target_values():
            entropy -= (target / len(self.data)) * math.log((target / len(self.data)), 2)

        return entropy

    def cant_target_values(self):
        tar_values = self.target_values()
        
        proportions = []
        for tar_val in range(len(tar_values)):
            proportions.append(0)
        
        for data in self.data:
            for tar_val in range(len(tar_values)):
                if data[-1] == tar_values[tar_val]:
                    proportions[tar_val] += 1 
        
        return proportions

    def max_gain_attribute(self, attributes):
        max_gain = 0
        index_attr = -1
        
        for attr in range(len(attributes)):
            gain = self.entropy()
            for value in attributes[attr]:

                subset = []
                if (attributes[attr] in self.continue_attributes):
                    if (value == attributes[attr][0]):
                        subset = self.subset_of_value(attr, float('-inf'), value)
                    elif (value == attributes[attr][-1]):
                        subset = self.subset_of_value(attr, value, float('inf'))
                    else:
                       subset = self.subset_of_value(attr, value, attributes[attr][attributes[attr].index(value) + 1])
                else:
                    subset = self.subset_of_value(attr, value, -1)

                gain -= (len(subset.data) / len(self.data)) * subset.entropy()

            if gain > max_gain: 
                max_gain = gain
                index_attr = attr

        return index_attr

    def cant_attributes(self):
        return (len(self.data[0]) - 1)

    def attributes_value(self, att):
        values = []
        instance = []
        for instance in self.data:
            if instance[att] not in values:
                values.append(instance[att]) 
            
        return values

    
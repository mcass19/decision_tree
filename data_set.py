from __future__ import division
import math
import random

class DataSet(object):
    
    def __init__(self, continue_attributes):
        self.data = []
        self.continue_attributes = continue_attributes

    # creación de estructura a partir del data_set
    def load_data_set(self, data_id, hot_vector):    
        data = []
        data_test = []

        # esto es porque tenemos dos chances de data_set según la letra del ejercicio
        # se debe modificar si se quiere tener en cuenta otros data_sets y
        # si se quiere otro porcentaje para generar y evaluar el árbol -> por defecto 80/20
        if data_id == 1:
            file_name = 'iris.data'
            number_of_lines = 150
            number_of_lines_test = 30
        else:
            file_name = 'covtype.data'
            number_of_lines = 1000
            number_of_lines_test = 200

        with open(file_name, 'r') as file_to_read:
            for _ in range(number_of_lines):
                aux = file_to_read.readline().split(',')
                for i in self.continue_attributes:
                    aux[i] = float(aux[i])
                aux[-1] = aux[-1].replace('\n', '')
                data.append(aux)

        # reduce el data_set -> para cada hot_vector lo reduce a un atributo, 
        # siendo 4 la máxima cantidad de clases para cada uno de estos
        data_aux = []
        if (len(hot_vector) != 0):
            for instance in range(len(data)):
                hot_vector_aux = hot_vector.copy()
                instance_aux = []
                att = 0
                while att < len(data[instance]): 
                    if (att in hot_vector_aux):   
                        cant_attributes = (hot_vector_aux[1] - hot_vector_aux[0]) + 1
                        cant_values = math.floor(cant_attributes / 4)
                        it = att
                        while it < (att + cant_attributes):
                            if (data[instance][it] == '1'):
                                if (cant_values > 0):
                                    if (it <= ((att + cant_values) - 1)):
                                        instance_aux.append('0')
                                    elif (it <= ((att + (cant_values * 2) - 1))):
                                        instance_aux.append('1')
                                    elif (it <= (att + ((cant_values * 3) - 1))):
                                        instance_aux.append('2')
                                    else:
                                        instance_aux.append('3')
                                else:
                                    # aquí el hot_vector tiene dos o tres atributos 
                                    # nota: si tiene uno sería un atributo discreto
                                    if (cant_attributes == 2):
                                        if (it == att):
                                            instance_aux.append('0')
                                        else:
                                            instance_aux.append('1')
                                    else:
                                        if (it == att):
                                            instance_aux.append('0')
                                        elif (it == att + 1):
                                            instance_aux.append('1')
                                        else:
                                            instance_aux.append('2')
                            it += 1
                        att += cant_attributes
                        hot_vector_aux.pop(0)
                        hot_vector_aux.pop(0)
                    else:
                        instance_aux.append(data[instance][att])
                        att += 1
                data_aux.append(instance_aux)
            data = data_aux.copy()
        
        # generar data_set_test
        for _ in range(number_of_lines_test):
            index = random.randint(0, len(data) - 1)
            data_test.append(data.pop(index))

        self.data = data
        return data_test

    # retorna una lista con todas las posibles etiquetas
    def target_values(self):
        tags = []
        instance = []
        for instance in self.data:
            if instance[-1] not in tags:
                tags.append(instance[-1]) 
            
        return tags

    # retorna el subconjunto de los valores que cumplen con value para el atributo de indice attr
    def subset_of_value(self, attr, value):
        data_set_result = DataSet(self.continue_attributes)
        subset = []

        for instance in self.data:
            if ((attr in self.continue_attributes) and 
                ((instance[attr] > value[0] and instance[attr] <= value[1]))):
                    subset.append(instance)
            elif instance[attr] == value:
                subset.append(instance)

        data_set_result.data = subset
        return data_set_result

    # retorna una lista con los indices para los cuales cambia el valor de la etiqueta
    def toggle_list(self):
        indexes = []

        for instance in range(len(self.data) - 1):
            if (self.data[instance][-1] != self.data[instance + 1][-1]):
                indexes.append(instance) 
        
        return indexes
    
    # retorna la etiqueta con mas apariciones en el data_set
    def most_common_target_value(self, target_values):
        cant_tags = []
        for _ in range(len(target_values)):
            cant_tags.append(0)
        
        for instance in self.data:
            if (instance[-1] in target_values):
                cant_tags[target_values.index(instance[-1])] += 1

        return target_values[cant_tags.index(max(cant_tags))]

    # calcula la entropia del data_set
    def entropy(self):      
        entropy = 0

        for target in self.cant_target_values():
            entropy -= (target / len(self.data)) * math.log((target / len(self.data)), 2)

        return entropy

    # retorna una lista con la cantidad de apariciones de cada etiqueta
    def cant_target_values(self):
        tar_values = self.target_values()
        
        proportions = []
        for _ in range(len(tar_values)):
            proportions.append(0)
        
        for instance in self.data:
            if (instance[-1] in tar_values):
                proportions[tar_values.index(instance[-1])] += 1
        
        return proportions

    # retorna el atributo con mayor ganancia
    def max_gain_attribute(self, attributes, attributes_aux):
        max_gain = 0
        index_attr = -1

        for attr in range(len(attributes_aux)):
            gain = self.entropy()
            for value in attributes_aux[attr]:
                subset = []
                subset = self.subset_of_value(attributes.index(attributes_aux[attr]), value)

                gain -= (len(subset.data) / len(self.data)) * subset.entropy()

            if gain > max_gain: 
                max_gain = gain
                index_attr = attr

        return index_attr
    
    # retorna la ganancia para el punto de corte value del atributo continuo con indice att
    def calculate_gain(self, att, value):
        greater = self.subset_of_value(att, (value, float('inf')))
        lower = self.subset_of_value(att, (float('-inf'), value))
        gain = self.entropy() - ((len(greater.data) / len(self.data)) * greater.entropy()) - ((len(lower.data) / len(self.data)) * lower.entropy())

        return gain
        
    # retorna la cantidad de atributos del data_set
    def cant_attributes(self):
        return (len(self.data[0]) - 1)

    # retorna todos los posibles valores de un atributo
    def attributes_value(self, att):
        values = []

        instance = []
        for instance in self.data:
            if instance[att] not in values:
                values.append(instance[att]) 
            
        return values
    
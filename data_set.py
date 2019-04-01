from __future__ import division
import math
import random

class DataSet(object):
    
    def __init__(self):
        self.data = []
        self.continue_attributes = [] # Indices de los atributos continuos
        self.hot_vector = [] # Indices del comienzo y final de los hot vectors

    # Carga los datos de iris o covtype (dependiendo de la eleccion hecha por el usuario)
    # a una lista, donde cada elemento de la lista es una instancia, representada como 
    # una lista donde cada elemento instance[i] es el valor del atributo i para esa instancia y 
    # el ultimo elemento de esta lista es la etiqueta de esa instancia  
    def load_data_set(self, data_id):    
        data = []

        # Esto es porque tenemos dos chances de data_set según la letra del ejercicio
        # Si se quiere otro porcentaje para generar y evaluar el árbol, cambiar
        # el valor de percentage -> por defecto 80 porciento es para generar y 
        # 20 porciento para evaluar
        if data_id == 1:
            self.continue_attributes = [0, 1, 2, 3]
            file_name = 'iris.data'
            number_of_lines = 150
            percentage = 0.2
            number_of_lines_test = math.floor(number_of_lines * percentage)
        else:
            self.continue_attributes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.hot_vector = [10, 13, 14, 53]
            file_name = 'covtype.data'
            number_of_lines = 581012
            percentage = 0.2
            number_of_lines_test = math.floor(number_of_lines * percentage)

        with open(file_name, 'r') as file_to_read:
            for _ in range(number_of_lines):
                aux = file_to_read.readline().split(',')
                for i in self.continue_attributes:
                    aux[i] = float(aux[i])
                aux[-1] = aux[-1].replace('\n', '')
                data.append(aux)

        # Hot vector
        # Reduce el data_set -> para cada hot_vector lo reduce a un atributo, 
        # siendo 4 la máxima cantidad de clases para cada uno de estos
        data_aux = []
        if (len(self.hot_vector) != 0):
            for instance in range(len(data)):
                hot_vector_aux = self.hot_vector.copy()
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
                                    # Aquí el hot_vector tiene dos o tres atributos 
                                    # Nota: si tiene uno sería un atributo discreto
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
                        # Popea los dos indices entre los que se encuentra el hot vector
                        hot_vector_aux.pop(0)
                        hot_vector_aux.pop(0)
                    else:
                        instance_aux.append(data[instance][att])
                        att += 1
                data_aux.append(instance_aux)
            data = data_aux.copy()
        
        # Genera data_set_test
        data_set_test = DataSet()
        data_set_test.set_continue_attributes(self.continue_attributes)
        for _ in range(number_of_lines_test):
            index = random.randint(0, len(data) - 1)
            data_set_test.data.append(data.pop(index))

        # Se reordena de forma aleatoria en cada ejecución
        random.shuffle(data)

        self.data = data
        return data_set_test

    def set_continue_attributes(self, continue_attributes):
        self.continue_attributes = continue_attributes
    
    # Retorna una lista con todas las posibles etiquetas del DataSet
    def target_values(self):
        tags = []
        instance = []
        for instance in self.data:
            if instance[-1] not in tags:
                tags.append(instance[-1]) 
            
        return tags

    # Retorna el DataSet con las instancias donde los valores del atributo de indice attr son value
    def subset_of_value(self, attr, value):
        data_set_result = DataSet()
        data_set_result.set_continue_attributes(self.continue_attributes)
        subset = []

        for instance in self.data:
            # Si es un atributo continuo compara entre los dos extremos
            if ((attr in self.continue_attributes) and 
                ((instance[attr] > value[0] and instance[attr] <= value[1]))):
                    subset.append(instance)
            # sino lo compara directamente
            elif instance[attr] == value:
                subset.append(instance)

        data_set_result.data = subset
        return data_set_result

    # Retorna una lista con los indices de las instancias e_i tal que e_i.etiqueta != e_(i + 1).etiqueta
    # y también que e_i no se encuentre ya en la lista (para no agregar repetidos)
    def toggle_list(self):
        indexes = [[],[]]

        for instance in range(len(self.data) - 1):
            first = self.data[instance][-1]
            second = self.data[instance + 1][-1]
            if ((first != second) and ((first, second) not in indexes[1])):
                indexes[0].append(instance)
                indexes[1].append((first, second)) # Guarda el cambio para asi no agregarlo de nuevo
        
        return indexes[0]
    
    # Retorna la etiqueta con mas apariciones en el data_set
    def most_common_target_value(self, target_values):
        cant_tags = [0] * len(target_values)
        
        for instance in self.data:
            if (instance[-1] in target_values):
                cant_tags[target_values.index(instance[-1])] += 1

        return target_values[cant_tags.index(max(cant_tags))]

    # Calcula la entropia del data_set
    def entropy(self):      
        entropy = 0

        for target in self.cant_target_values():
            entropy -= (target / len(self.data)) * math.log((target / len(self.data)), 2)

        return entropy

    # Retorna una lista con la cantidad de apariciones de cada etiqueta
    def cant_target_values(self):
        tar_values = self.target_values()
        proportions = [0] * len(tar_values)
        
        for instance in self.data:
            if (instance[-1] in tar_values):
                proportions[tar_values.index(instance[-1])] += 1
        
        return proportions
    
    # Retorna el DataSet con aquellas instancias donde la etiqueta asociada es label
    def data_set_class(self, label):
        data_set_class = DataSet()     
        data_set_class.set_continue_attributes(self.continue_attributes)

        for instance in self.data:
            if (instance[-1] == label):
                data_set_class.data.append(instance)
        
        return data_set_class

    # Retorna el atributo con mayor ganancia de la lista attributes_aux
    # attributes se utiliza para no perder el indice original de los atributos
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
    
    # Retorna la ganancia para el punto de corte value del atributo continuo con indice att
    def calculate_gain(self, att, value):
        greater = self.subset_of_value(att, (value, float('inf')))
        lower = self.subset_of_value(att, (float('-inf'), value))
        gain = self.entropy() - ((len(greater.data) / len(self.data)) * greater.entropy()) - ((len(lower.data) / len(self.data)) * lower.entropy())

        return gain
        
    # Retorna la cantidad de atributos del data_set
    def cant_attributes(self):
        return (len(self.data[0]) - 1)

    # Retorna una lista con todos los valores que toma el atributo att
    def attributes_value(self, att):
        values = []

        instance = []
        for instance in self.data:
            if instance[att] not in values:
                values.append(instance[att]) 
            
        return values
    
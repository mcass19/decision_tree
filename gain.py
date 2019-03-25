import math
from data_set import DataSet

class Gain(object):

    def __init__(self, data_set, target_values):
        self.data_set = data_set
        self.cant_total_data = data_set.len()

        self.target_values = target_values

        self.entropy = self.calculate_entropy(data_set)

        self.attributes_already_used = []

    def calculate_entropy(self, data_set):
        proportions = self.cant_target_values(data_set)

        entropy = 0
        for prop in proportions:
            entropy -= (prop / self.cant_total_data) * math.log((prop / self.cant_total_data), 2)

        return entropy

    def calculate_gain(self, attribute, value):

    # attributes está pensado como una lista de listas, donde por ejemplo el atributo en la posición
    # 0 tiene una lista con sus posibles valores 
    def calculate_max_gain(self, data_set, attributes):
        max_gain = 0
        index_attr = -1

        for attr in range(attributes.len()):
            if attr not in self.attributes_already_used:
                gain = self.entropy
                for value in attributes[attr]:
                    subset = self.data_set.return_subset_of_value(attr, value)
                    gain -= (subset.len() / self.cant_total_data) * self.calculate_entropy(subset)

                if gain > max_gain: 
                    max_gain = gain
                    index_attr = attr

        if index_attr != -1:
            self.attributes_already_used.append(index_attr)

        return index_attr

    def cant_target_values(self, data_set):
        target_values = self.target_values
        
        proportions = []
        for tar_val in range(target_values.len()):
            proportions[tar_val] = 0
        
        for data in data_set:
            for tar_val in range(target_values.len()):
                if data[-1] == target_values[tar_val]:
                    proportions[tar_val] += 1 
        
        return proportions

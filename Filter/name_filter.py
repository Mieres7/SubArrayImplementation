from Filter.filter import Filter
from subarray import Array
import numpy as np

class IdFilter(Filter):

    def __init__(self, ids):
        """
        :param name_criteria: Criterios para filtrar los nombres de las antenas
        """
        self.ids = ids

    def filter(self, array):
        """
        Aplica el filtro para seleccionar antenas que coincidan con el criterio de nombre.
        
        :param array: El objeto Array sobre el cual aplicar el filtro.
        :return: Un nuevo objeto Array con los datos filtrados según el criterio de nombre.
        """

        antenna_names_array = np.array(array.antenna_names)
        antenna_data_array = np.array(array.antenna_data)
        diameters_array = np.array(array.diameters)
        
        
        mask = np.isin(antenna_names_array, self.ids)
        
        filtered_antenna_data = antenna_data_array[mask]
        filtered_antenna_names = antenna_names_array[mask]
        filtered_diameters = diameters_array[mask]

        return Array(filtered_antenna_data, filtered_antenna_names, filtered_diameters, array.observatory, array.array_ref)
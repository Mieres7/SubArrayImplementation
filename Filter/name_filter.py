from Filter.filter import Filter
from Array.subarray import Array
import numpy as np
import dask.array as da

class IdFilter(Filter):

    def __init__(self, ids, filter_mode="exact"):
        """
        :param name_criteria: Criterios para filtrar los nombres de las antenas
        """
        self.ids = ids
        self.filter_mode = filter_mode

    def filter(self, array):
        """
        Aplica el filtro para seleccionar antenas que coincidan con el criterio de nombre.
        
        :param array: El objeto Array sobre el cual aplicar el filtro.
        :return: Un nuevo objeto Array con los datos filtrados según el criterio de nombre.
        """

        if isinstance(array.antenna_data, da.Array):
            antenna_data_array = array.antenna_data
        else:
            antenna_data_array = da.from_array(array.antenna_data, chunks='auto')

        antenna_names_array = np.array(array.antenna_names)
        diameters_array = da.asarray(array.diameters, chunks="auto")

        
        if self.filter_mode == 'exact':
            mask = np.isin(antenna_names_array, self.ids)
        elif self.filter_mode == 'partial':
            mask = np.array([any(id in name for id in self.ids) for name in antenna_names_array])

        filtered_antenna_data = antenna_data_array[mask]
        filtered_antenna_names = antenna_names_array[mask]
        filtered_diameters = diameters_array[mask]

        return Array(filtered_antenna_data, filtered_antenna_names, filtered_diameters, array.observatory, array.array_ref)
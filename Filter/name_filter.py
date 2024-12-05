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
            antenna_data_array = da.from_array(array.antenna_data, chunks='auto', asarray=False)

        antenna_names_array = np.array(array.antenna_names)
        diameters_array = np.array(array.diameters)

        # Dependiendo del modo de filtrado, usar la comparación adecuada
        if self.filter_mode == 'exact':
            # Modo exacto: Coincide exactamente con los nombres proporcionados
            mask = np.isin(antenna_names_array, self.ids)
        elif self.filter_mode == 'partial':
            # Modo parcial: Coincide con los nombres que contienen las cadenas dadas
            mask = np.array([any(id in name for id in self.ids) for name in antenna_names_array])

        # Filtrar los datos
        filtered_antenna_data = antenna_data_array[mask]
        filtered_antenna_names = antenna_names_array[mask]
        filtered_diameters = diameters_array[mask]

        return Array(filtered_antenna_data, filtered_antenna_names, filtered_diameters, array.observatory, array.array_ref)
import matplotlib.pyplot as plt
import dask.array as da
import numpy as np

from antenna_configs import ska_array_assembly


class Array: 
    def __init__(self, antenna_data, antenna_names, diameters, observatory, array_ref):
        
        self.antenna_data = antenna_data
        self.antenna_names = antenna_names
        self.diameters = diameters
        self.observatory = observatory
        self.array_ref = array_ref


    def plot_array_layout(self, axes=None, scale="kilo", title=None,**kwargs):
        """
        Utility function to plot the array layout
        """
        return_vals = False
        if axes is None:
            fig, axes = plt.subplots(1, 1)
            return_vals = True

        if scale.lower() in ["kilo"]:
            uscale = "k"
            fscale = 1000
        else:
            uscale = ""
            fscale = 1

        x = self.antenna_data[:, 0]
        y = self.antenna_data[:, 1]

        x = x.compute() if isinstance(x, da.Array) else x
        y = y.compute() if isinstance(y, da.Array) else y

        axes.scatter(
            x / fscale,
            y / fscale,
            s=kwargs.pop("s", 0.2),
            c=kwargs.pop("c", "k"),
            marker=kwargs.pop("marker", "o"),
            alpha=kwargs.pop("alpha", None),
            edgecolors=kwargs.pop("edgecolors", "face"),
            **kwargs,
        )

        axes.set_xlabel(f"X ({uscale}m)")
        axes.set_ylabel(f"Y ({uscale}m)")

        if title:
            axes.set_title(title)

        if return_vals:
            return fig, axes


    def get_ska_mid_atennas_by_stage(self, stage="AA*"):
        
        if stage.casefold() == "AA4".casefold():
            station_list = ska_array_assembly.MID_AA4.split(",")
        elif stage.casefold() == "AA*".casefold():
            station_list = ska_array_assembly.MID_AAstar.split(",")
        elif stage.casefold() == "AA2".casefold():
            station_list = ska_array_assembly.MID_AA2.split(",")
        elif stage.casefold() == "AA1".casefold():
            station_list = ska_array_assembly.MID_AA1.split(",")
        elif stage.casefold() == "AA0.5".casefold():
            station_list = ska_array_assembly.MID_AA05.split(",")
        else:
            raise ValueError("Invalid subarray type specified! Valid subarray names (case-insensitive) "
                f"are {ska_array_assembly.VALID_AA_MID}")

        ids = np.array([id_.decode('utf-8').strip() for id_ in self.antenna_names])

        mask = np.isin(ids, station_list)

        if not np.any(mask):  
            missing_ids = set(station_list) - set(ids)
            raise ValueError(f"The following antenna IDs were not found in the file: {missing_ids}")

        filtered_ids = ids[mask]
        filtered_data = self.antenna_data[mask]
        filtered_diameters = self.diameters[mask]

        filtered_data = filtered_data.compute()  
        filtered_diameters = filtered_diameters.compute()  

        sorted_indices = np.argsort(filtered_ids)

        antenna_data = da.from_array(filtered_data[sorted_indices], chunks="auto", asarray=False)
        diameters = da.from_array(filtered_diameters[sorted_indices], chunks="auto", asarray=False)

        self.antenna_names = filtered_ids[sorted_indices]
        self.antenna_data = antenna_data
        self.diameters = diameters

    def get_ska_low_atennas_by_stage(self, stage="AA*"):
        
        if stage.casefold() == "AA4".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA4)
        elif stage.casefold() == "AA*".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AAstar)
        elif stage.casefold() == "AA2".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA2)
        elif stage.casefold() == "AA1".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA1)
        elif stage.casefold() == "AA0.5".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA05)
        else:
            raise ValueError("Invalid subarray type specified! Valid subarray names (case-insensitive) "
                f"are {ska_array_assembly.VALID_AA_LOW}")

        ids = np.array([id_.decode('utf-8').strip() for id_ in self.antenna_names])

        mask = np.isin(ids, station_list)

        if not np.any(mask):  
            missing_ids = set(station_list) - set(ids)
            raise ValueError(f"The following antenna IDs were not found in the file: {missing_ids}")

        filtered_ids = ids[mask]
        filtered_data = self.antenna_data[mask]
        filtered_diameters = self.diameters[mask]

        filtered_data = filtered_data.compute()  
        filtered_diameters = filtered_diameters.compute()  

        sorted_indices = np.argsort(filtered_ids)

        antenna_data = da.from_array(filtered_data[sorted_indices], chunks="auto", asarray=False)
        diameters = da.from_array(filtered_diameters[sorted_indices], chunks="auto", asarray=False)

        self.antenna_names = filtered_ids[sorted_indices]
        self.antenna_data = antenna_data
        self.diameters = diameters
        return

    def formatStationsName(self, station_list):
        formatted_station_list = []
        for element in station_list.split(","):
            this_station = element.lstrip().rstrip()
            if this_station[0].isdigit():
                formatted_station_list.append(f"C{this_station}")
            else:
                formatted_station_list.append(this_station)
        return formatted_station_list



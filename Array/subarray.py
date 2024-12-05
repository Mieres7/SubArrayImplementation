import matplotlib.pyplot as plt
import dask.array as da

from utils.utils import ecef_to_enu


class Array: 
    def __init__(self, antenna_data, antenna_names, diameters, observatory, array_ref):
        
        antenna_data = ecef_to_enu(antenna_data=antenna_data, array_ref=array_ref)

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

        # for i, label in enumerate(self.antenna_names):  # Assuming the labels are in the 3rd column (index 2)
        #     axes.text(
        #         x[i] / fscale,
        #         y[i] / fscale,
        #         label,  # Antenna label
        #         color='blue',  # Color of the text
        #         fontsize=8,  # Font size
        #         ha='center',  # Horizontal alignment
        #         va='center',  # Vertical alignment
        # )

        axes.set_xlabel(f"X ({uscale}m)")
        axes.set_ylabel(f"Y ({uscale}m)")

        if title:
            axes.set_title(title)

        if return_vals:
            return fig, axes







import numpy as np
import dask.array as da
from antenna_configs.io import get_center_of_array
from Array.subarray import Array

from astropy.coordinates import EarthLocation, UnknownSiteException
from astropy import units as u
from utils import utils

def io(input_name):
    header = []
    with open(input_name) as input_file:
        for _ in range(2):
            li = next(input_file).strip()
            if li.startswith("#"):
                header.append(
                    list(map(str.strip, li.strip().replace("#", "").strip().split("=")))
                )
    header = dict(header)

    if "observatory" in header:
        observatory = header["observatory"].lower()
    else:
        observatory = "UnknownTelescope"

    dtypes_all_columns = [('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('D', '<f4'), ('id', 'S10')]
    dtypes_no_ids = [('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('D', '<f4')]
    dtypes_no_diameters_or_ids = [('x', '<f4'), ('y', '<f4'), ('z', '<f4')]
    dtypes_list = [dtypes_all_columns, dtypes_no_ids, dtypes_no_diameters_or_ids]

    errors = []
    for dtypes in dtypes_list:
        try:
            data = np.loadtxt(input_name, dtype=dtypes, skiprows=1)
        except Exception as e:
            errors.append(e)
        else:
            break
    else:
        raise OSError(
            "The antenna configuration file needs at least the xyz coordinates. {0}".format(errors)
        )

    x, y, z = data["x"], data["y"], data["z"]
    diameters = da.from_array(data["D"], chunks="auto", asarray=False)
    center_of_array = get_center_of_array(data, telescope_name=observatory)
    antenna_names = data["id"]

    ecef_coords = EarthLocation.from_geocentric(x,y,z, u.m)
    enu_coords = utils.earth_location_to_local_enu(ecef_coords, center_of_array)

    antenna_data = da.from_array(
        np.column_stack((enu_coords[0], enu_coords[1], enu_coords[2])),
        chunks="auto",
        asarray=False
    )

    return Array(antenna_data, antenna_names, diameters, observatory, center_of_array)

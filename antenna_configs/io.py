import numpy as np
import dask.array as da
from astropy.coordinates import EarthLocation, UnknownSiteException
from astropy import units as u
from utils import utils

def io(input_name, antenna_ids=None):
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
    

    ids = np.array([id_.decode('utf-8').strip() for id_ in data["id"]])


    mask = np.isin(ids, antenna_ids)

    if not np.any(mask):  
        missing_ids = set(antenna_ids) - set(ids)
        raise ValueError(f"The following antenna IDs were not found in the file: {missing_ids}")

    # filter and sort antenna_data, names & diameters
    filtered_ids = ids[mask]
    sorted_indices = [np.where(filtered_ids == id_)[0][0] for id_ in antenna_ids if id_ in filtered_ids]

    filtered_x, filtered_y, filtered_z, filtered_diameters = x[mask], y[mask], z[mask], diameters[mask]
    filtered_x, filtered_y, filtered_z = filtered_x[sorted_indices], filtered_y[sorted_indices], filtered_z[sorted_indices]
    sorted_diameters = filtered_diameters[sorted_indices]

    # trasnform data to enu 
    ecef_coords = EarthLocation.from_geocentric(filtered_x, filtered_y, filtered_z, u.m)
    enu_coords = utils.earth_location_to_local_enu(ecef_coords, center_of_array)

    antenna_data = da.from_array(
        np.column_stack((enu_coords[0], enu_coords[1], enu_coords[2])),
        chunks="auto",
        asarray=False
    )

    return antenna_data, observatory, sorted_diameters, center_of_array


def get_center_of_array(data, telescope_name):

    try:
        center_of_array = EarthLocation.of_site(telescope_name.lower())
    except UnknownSiteException:
        center_x = np.mean(data["x"])
        center_y = np.mean(data["y"])
        center_z = np.mean(data["z"])
        center_of_array = EarthLocation.from_geocentric(center_x, center_y, center_z, unit=u.m)

    return center_of_array

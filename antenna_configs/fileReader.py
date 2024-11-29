import numpy as np
import dask.array as da


def fileReader(input_name):

    header = []
    with open(input_name) as input_file:
        # Read only the first two lines
        for _ in range(2):
            li = next(input_file).strip()
            if li.startswith("#"):
                header.append(
                    list(map(str.strip,
                                li.strip().replace("#", "").strip().split("=")))
                )
    header = dict(header)

    if "observatory" in header:
        observatory = header["observatory"].lower()
    else:
        observatory = "UnknownTelescope"

    if "coordsys" in header:
        coordsys = header["coordsys"]

    dtypes_all_columns = [('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('D', '<f4'), ('id', 'S5')]
    dtypes_no_ids = [('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('D', '<f4')]
    dtypes_no_diameters_or_ids = [('x', '<f4'), ('y', '<f4'), ('z', '<f4')]
    dtypes_list = [dtypes_all_columns, dtypes_no_ids, dtypes_no_diameters_or_ids]
    
    errors = []
    # Try to load the data with all columns, if it fails, try to load it without 'id', if it fails, try to load it without 'D' and 'id'
    for dtypes in dtypes_list:
        try:
            data = np.loadtxt(input_name, dtype=dtypes, skiprows=1)
        except Exception as e:
            errors.append(e)
        else:
            break
    else:
        raise OSError(
            "The antenna configuration file needs at least the xyz coordinates. {0}".
            format(errors)
        )

    x, y, z = data["x"], data["y"], data["z"]
    antenna_data = da.from_array(np.column_stack((x, y, z)), chunks="auto", asarray=False)
    diameters = da.from_array(data["D"], chunks="auto", asarray=False)
    antenna_ids = da.from_array(
        np.char.decode(data["id"], 'utf-8'), chunks="auto", asarray=False
    )


    return antenna_data, observatory, diameters


# antenna_data, telescope_name, diameters, antenna_ids = fileReader("skamidcoordsNew.cfg")
# print(telescope_name)


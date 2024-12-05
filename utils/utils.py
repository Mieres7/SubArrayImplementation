import numpy as np
from astropy import units

def ecef_to_enu(array_ref, antenna_data):
    """Convert ECEF coordinates to ENU coordinates
        relative to reference location.
    :param location: Current WGS84 coordinate
    :param xyz: ECEF coordinate
    :result : enu
    """
    
    lon = array_ref.geodetic[0].to(units.rad).value
    lat = array_ref.geodetic[1].to(units.rad).value
    alt = array_ref.geodetic[2].to(units.m).value

    x, y, z = np.hsplit(antenna_data, 3)

    center_x, center_y, center_z = lla_to_ecef(lat, lon, alt)

    delta_x, delta_y, delta_z = x - center_x, y - center_y, z - center_z
    sin_lat, cos_lat = np.sin(lat), np.cos(lat)
    sin_lon, cos_lon = np.sin(lon), np.cos(lon)

    e = -sin_lon * delta_x + cos_lon * delta_y
    n = (
        -sin_lat * cos_lon * delta_x
        - sin_lat * sin_lon * delta_y
        + cos_lat * delta_z
    )
    u = (
        cos_lat * cos_lon * delta_x
        + cos_lat * sin_lon * delta_y
        + sin_lat * delta_z
    )

    return np.hstack([e, n, u])


def lla_to_ecef(lat, lon, alt):
    """Convert WGS84 spherical coordinates to ECEF cartesian coordinates.
    :param lat: latitude
    :param lon: longitude
    :param alt: altitude
    :result: ecef coordinates
    """
    WGS84_a = 6378137.00000000
    WGS84_b = 6356752.31424518
    N = WGS84_a**2 / np.sqrt(
        WGS84_a**2 * np.cos(lat) ** 2 + WGS84_b**2 * np.sin(lat) ** 2
    )

    x = (N + alt) * np.cos(lat) * np.cos(lon)
    y = (N + alt) * np.cos(lat) * np.sin(lon)
    z = ((WGS84_b**2 / WGS84_a**2) * N + alt) * np.sin(lat)

    return x, y, z
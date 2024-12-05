from Array.subarray import Array
from antenna_configs import io, ska_array_assembly
from astropy.coordinates import EarthLocation

MID_ARRAY_REF = EarthLocation.from_geodetic(
    21.44380263, -30.71292499, 1095.967, ellipsoid="WGS84"
)

class MidSubArray(Array):
    """MidSubArray Class"""
    def __init__(
        self, 
        stage="AA*",
    ):
        assert stage.casefold() in [
                x.casefold() for x in ska_array_assembly.VALID_AA_MID
            ], (
                "Invalid subarray type specified! Valid subarray names (case-insensitive) "
                f"are {ska_array_assembly.VALID_AA_MID}"
            )
        self.stage = stage

        coordinates_file = "./antenna_configs/ska_mid_coordinates.cfg"

        antenna_names = self.getStationNames()
        
        antenna_data, observatory, diameters= io.io(coordinates_file, antenna_names)   
        
        super().__init__(
            antenna_data,
            antenna_names,
            diameters,
            observatory,
            MID_ARRAY_REF
        )

    def getStationNames(self):
      
        if self.stage.casefold() == "AA4".casefold():
            station_list = ska_array_assembly.MID_AA4.split(",")
        elif self.stage.casefold() == "AA*".casefold():
            station_list = ska_array_assembly.MID_AAstar.split(",")
        elif self.stage.casefold() == "AA2".casefold():
            station_list = ska_array_assembly.MID_AA2.split(",")
        elif self.stage.casefold() == "AA1".casefold():
            station_list = ska_array_assembly.MID_AA1.split(",")
        elif self.stage.casefold() == "AA0.5".casefold():
            station_list = ska_array_assembly.MID_AA05.split(",")
    
        return station_list
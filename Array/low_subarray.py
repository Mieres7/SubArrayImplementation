from Array.subarray import Array
from antenna_configs import io, ska_array_assembly
from astropy.coordinates import EarthLocation

LOW_ARRAY_REF = EarthLocation.from_geodetic(
    116.7644482, -26.82472208, 365.0, ellipsoid="WGS84"
)


class LowSubarray(Array): 
    """LowSubarray Class"""
    def __init__(
        self, 
        stage="AA*"
    ):
        assert stage.casefold() in [
                x.casefold() for x in ska_array_assembly.VALID_AA_LOW
            ], (
                "Invalid subarray type specified! Valid subarray names (case-insensitive) "
                f"are {ska_array_assembly.VALID_AA_LOW}"
            )
        self.stage = stage

        stationFile = "./antenna_configs/ska_low_coordinates.cfg"

        antenna_names = self.getStationNames()

        antenna_data, observatory, diameters, center_of_array = io.io(stationFile, antenna_names)   
        

        super().__init__(
            antenna_data,
            antenna_names,
            diameters,
            observatory,
            center_of_array
        )

    def getStationNames(self):
      
        if self.stage.casefold() == "AA4".casefold():
            station_list = self._full_array_data["Label"].to_list() #ver esto
        elif self.stage.casefold() == "AA*".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AAstar)
        elif self.stage.casefold() == "AA2".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA2)
        elif self.stage.casefold() == "AA1".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA1)
        elif self.stage.casefold() == "AA0.5".casefold():
            station_list = self.formatStationsName(ska_array_assembly.LOW_AA05)
    
        return station_list
    
    def formatStationsName(self, station_list):
        formatted_station_list = []
        for element in station_list.split(","):
            this_station = element.lstrip().rstrip()
            if this_station[0].isdigit():
                formatted_station_list.append(f"C{this_station}")
            else:
                formatted_station_list.append(this_station)
        return formatted_station_list
        

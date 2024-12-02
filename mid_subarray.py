from subarray import Array
from antenna_configs import ska_array_assembly, fileReader


class MidSubArray(Array):
    """MidSubArray Class"""
    def __init__(
        self, 
        stage,
    ):

        assert stage.casefold() in [
                x.casefold() for x in ska_array_assembly.VALID_AA_MID
            ], (
                "Invalid subarray type specified! Valid subarray names (case-insensitive) "
                f"are {ska_array_assembly.VALID_AA_MID}"
            )
        self.stage = stage

        stationFile = "./antenna_configs/skamidcoordsNew.cfg"

        antenna_names = self.getStationNames()
        antenna_data, observatory, diameters= fileReader.fileReader(stationFile, True, antenna_names)   
        
        super().__init__(
            antenna_data,
            antenna_names,
            diameters,
            observatory
        )

    def getStationNames(self):
      
        if self.stage.casefold() == "AA4".casefold():
            station_list = self._full_array_data["Label"].to_list() # ver esto
        elif self.stage.casefold() == "AA*".casefold():
            station_list = ska_array_assembly.MID_AAstar.split(",")
        elif self.stage.casefold() == "AA2".casefold():
            station_list = ska_array_assembly.MID_AA2.split(",")
        elif self.stage.casefold() == "AA1".casefold():
            station_list = ska_array_assembly.MID_AA1.split(",")
        elif self.stage.casefold() == "AA0.5".casefold():
            station_list = ska_array_assembly.MID_AA05.split(",")
    
        return station_list
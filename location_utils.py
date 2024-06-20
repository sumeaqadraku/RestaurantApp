 # created new controller class for location operations
from base_enums import Location

class LocationManager:
    
    # added @staticmethod to mark method as static
    @staticmethod
    def get_location_from_id(location_id):
            for location in Location:
                if location.value == location_id:
                    return location
           
            raise Exception("No location could be found for given location parameter.")
            
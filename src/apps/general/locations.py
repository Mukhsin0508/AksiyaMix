import  os
import  json

# Load the data from the JSON files from data/
class Location:
    districts_file_path = os.path.join((os.path.dirname(__file__)),
                                       '/Users/mukhsinmukhtorov/projects/AksiyaMix/src/data/districts.json')
    regions_file_path = os.path.join((os.path.dirname(__file__)),
                                     '/Users/mukhsinmukhtorov/projects/AksiyaMix/src/data/regions.json')

    @classmethod
    def load_data(cls):
        """Load the data from the JSON files from src/data/"""
        try:
            with open ( cls.districts_file_path , 'r' , encoding = 'utf-8' ) as districts_file:
                cls.DISTRICTS_DATA = json.load ( districts_file )

            with open ( cls.regions_file_path , 'r' , encoding = 'utf-8' ) as regions_file:
                cls.REGIONS_DATA = json.load ( regions_file )

        except FileNotFoundError as error:
            raise FileNotFoundError(f"Error loading data: {error}")

        except json.JSONDecodeError as error:
            raise ValueError(f"Error decoding JSON: {error}")

    @classmethod
    def get_region_choices(cls):
        """Get the region choices for the form"""
        if not hasattr(cls, 'REGIONS_DATA'):
            cls.load_data()
        return [(region['id'], region['name_uz']) for region in cls.REGIONS_DATA]

    @classmethod
    def get_districts_by_regions(cls, region_id):
        """Get the districts by region id"""
        if not hasattr(cls, 'DISTRICTS_DATA'):
            cls.load_data()
        return [(district['id'], district['name_uz'])
                for district in cls.DISTRICTS_DATA if district['region_id'] == region_id]
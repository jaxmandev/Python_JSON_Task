# the json module is imported 
# to handle a .json file
import json

# class created and methods initiated
class Currency:
    def __init__(self):
        self.xchange_rates = self.load_dic()
        self.display_basic_info()
        self.display_rates()
    
    # store .json file data in a python object
    def load_dic(self):
        with open("exchange_rate.json", "r") as x:
            loaded_dic = json.load(x)
        return loaded_dic
    
    # iterate and displ the date and base currency
    def display_basic_info(self):
        for key, value in self.xchange_rates.items():
            if key == "date":
                print(f"{key}: {value}")
            elif key == "base":
                print(f"{key}: {value}")
            else:
                pass
    
    # iterate and display through the nested dictionary
    # containing country code and rates
    def display_rates(self):
        for key, value in self.xchange_rates["rates"].items():
            print(f"{key}: {value}")

# instabtiate the class
Currency()
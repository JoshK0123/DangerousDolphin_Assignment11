
import csv 
from CSVPackage.CSVProcessor import *

class RemovingDecimalsandDuplicates:
   def round_to_two_decimal_places(data):
    
    cleaned_data = []
    for item in data:
        new_item = {}
        for key, value in item.items():
            try:
                # Attempt to convert value to float and round to 2 decimal places
                new_item[key] = round(float(value), 2)
            except ValueError:
                # If conversion fails, keep the value as is (for non-numeric values)
                new_item[key] = value
        cleaned_data.append(new_item)
    return cleaned_data
    
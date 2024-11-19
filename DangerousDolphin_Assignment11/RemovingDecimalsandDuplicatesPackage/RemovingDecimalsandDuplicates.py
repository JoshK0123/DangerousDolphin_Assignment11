from mainPackage.main import *
import csv 
from CSVPackage.CSVProcessor import *

class RemovingDecimalsandDuplicates:

    def __init__(self, csv_processor):
        """
        Constructor
        
        Args:
            csv_processor (CSVProcessor): An instance of the CSVProcessor class.
        """
        self.csv_processor = csv_processor
    def round_column_to_two_decimal_places(input_file):
        """
        Rounds values in the 'Gross Price' column of a CSV file to 2 decimal places.
    
        Args:
            input_file (str): Path to the input CSV file.
    
        Returns:
            list: List of rows with the 'Gross Price' column values rounded to 2 decimal places.
        """
        cleaned_data = []

        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
        
            # Add the header to cleaned_data
            cleaned_data.append(header)

            for row in reader:
                try:
                    # Assuming 'Gross Price' is in the third column (index 2)
                    row[2] = f"{float(row[2]):.2f}"
                except (ValueError, IndexError):
                    pass  # Skip rows where the conversion fails
                cleaned_data.append(row)
    
        return cleaned_data

    
import csv

def delete_duplicate_rows(input_file):
    """
    Removes duplicate rows from a CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
    
    Returns:
        list: List of unique rows from the CSV file.
    """
    unique_data = []
    seen = set()

    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        
        # Add the header to unique_data
        unique_data.append(header)

        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
    
    return unique_data

    
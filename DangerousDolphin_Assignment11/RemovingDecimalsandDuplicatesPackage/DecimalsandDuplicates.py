# Name: Sarah Mahan, Luke Ransick, Josh Klingelhafer, Henry Gruber
# email:  mahansa@mail.uc.edu, ransiclg@mail.uc.edu, klingejh@mail.uc.edu, gruberhw@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   11/21/24
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:   Clean a csv file, store it in a new place.
# Brief Description of what this module does. What this module does is that it's a class, and inside this class is two functions that rounds the column Gross Price to two decimal places and gets rid of duplicates.
# Citations:
# Anything else that's relevant: Using (allowed) AI, Copilot

from mainPackage.main import *
import csv 
from CSVPackage.CSVProcessor import *

import csv

class RemovingDecimalsandDuplicates:

    def __init__(self, csv_processor):
        """
        Constructor
        @param: csv_processor (CSVProcessor): An instance of the CSVProcessor class
        """
        self.csv_processor = csv_processor

    def round_second_column_to_two_decimal_places(self, input_file, output_file):
        """
        Rounds numeric values in the 2nd column of a CSV file to 2 decimal places and writes to an output file.
        @param: input_file (str): Path to the input CSV file.
        @param: output_file (str): Path to the output CSV file.
        """
        cleaned_data = []

        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            
            # Add the header to cleaned_data
            cleaned_data.append(header)

            for row in reader:
                try:
                    # Assuming the 2nd column is index 1
                    row[2] = f"${float(row[2]):.2f}"
                except (ValueError, IndexError):
                    pass  # Skip rows where the conversion fails
                cleaned_data.append(row)
        
        # Write the cleaned data to the output CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleaned_data)
            
        print(f"Data has been updated with 2nd column values rounded to two decimal places and saved to {output_file}.")

    def delete_duplicate_rows(self, input_file, output_file):
        """
        Removes duplicate rows from a CSV file and writes to an output file.
        @param: input_file (str): Path to the input CSV file.
        @param: output_file (str): Path to the output CSV file.
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
        
        # Write the cleaned data to the output CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(unique_data)
            
        print(f"Duplicate rows removed and data saved to {output_file}.")

# Example usage:
csv_processor = RemovingDecimalsandDuplicates(None)
input_file = 'input.csv'
output_file = 'cleanedData.csv'


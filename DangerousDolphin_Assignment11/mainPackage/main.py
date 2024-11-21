# Name: Sarah Mahan, Luke Ransick, Josh Klingelhafer, Henry Gruber
# email:  mahansa@mail.uc.edu, ransiclg@mail.uc.edu, klingejh@mail.uc.edu, gruberhw@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   11/21/24
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Clean a csv file, store it in a new place.

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations:
# Anything else that's relevant: Using (allowed) AI

# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu
from RemovingDecimalsandDuplicatesPackage.DecimalsandDuplicates import *
from dataAnomaliesPackage.dataAnomalies import *
from CSVPackage.CSVProcessor import *
from apiPackage.api import *

if __name__ == "__main__":
    # Paths to the CSV files
    input_file = 'Data/fuelPurchaseData.csv'
    anomalies_file = 'Data/dataAnomalies.csv'

    # Process the CSV
    processor = CSVProcessor(input_file)

    # Remove decimals and duplicates
    round_second_column_to_two_decimal_places(input_file)
    delete_duplicate_rows(input_file)

    # Remove anomalies
    remover = RemoveAnomaliesInColumn(processor)
    remover.filter_anomalies(anomalies_file)

    # API Server Acces
    apiWaiter.submitToServer()
    zipCodes = apiWaiter.loadJSONtoDict(apiWaiter.submitToServer())
    fetchedZipCode = (zipCodes['results'][0])
    print(fetchedZipCode)


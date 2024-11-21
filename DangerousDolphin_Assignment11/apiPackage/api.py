# Name: Sarah Mahan, Luke Ransick, Josh Klingelhafer, Henry Gruber
# email:  mahansa@mail.uc.edu, ransiclg@mail.uc.edu, klingejh@mail.uc.edu, gruberhw@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   11/21/24
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Clean a csv file, store it in a new location

# Brief Description of what this module does. Api Accessor, zip code adding
# Citations:
# Anything else that's relevant: Using (allowed) AI

# api.py

import stat
import requests
import json
import csv

def extract_city(address):
    """
    isolates the city in the address line
    @param address: the original string to be checkedS
    """
    # Split the address by ", OH" to isolate the city part
    parts = address.split(", OH")
    if len(parts) > 1:
        city_part = parts[0] # The part before ", OH"
        # The city is typically the last part before the state
        city = city_part.split(",")[-1].strip()
        return city
    return None

def submitToServer(city):
    """
    Submits url to API server to receive results
    @return: the json results
    """
        
    response = requests.get("https://app.zipcodebase.com/api/v1/code/city?apikey=a0f42fd0-a762-11ef-8709-97910ef36bb5&city=" + city + "&state_name=ohio&country=us&limit=1")

    apiResults = response.content
        
    return apiResults

def loadJSONtoDict(jsonResponse):
    """
    Loads JSON data into a dictionary
    @param jsonResponse: the JSON data
    @return: the dictionary
    """
    parsed_json = json.loads(jsonResponse)

    return parsed_json 

def has_zip_code(address): 
    """
    Checks for zipcode in address string
    @param address: the string to be checked
    """
    for part in address.split(): 
        if len(part) == 5 and part.isdigit(): 
            return True 
    return False

class apiWaiter:
    """
    Performs interactions and requests data with API Server
    """
    def __init__(self):
        """
        Constructor
        """

    def addCitytoDict():
        """
        Read the CSV file and extract cities into a dictionary
        """
        input_file = 'Data/cleanedData.csv'
        city_dict = {}

        with open(input_file, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)  # Skip the header row if present

            for row in csvreader:
                address = row[3]  # City is in the 4th column (index 3)
                city = extract_city(address)
                if city:
                    city_dict[city] = None


        return city_dict

    def loadCityDict(city_dict):
        """
        Loading city dict with zip codes and processing multiple api calls
        @param city_dict: the dict to get new zips
        """
        # Print the dictionary to verify the results
        for city in city_dict.keys():
            zipCode = loadJSONtoDict(submitToServer(city))
            city_dict[city] = zipCode['results'][0]
            #print(f"City: {city} -> Value: {city_dict[city]}")

        print("Cities have been extracted and stored in the dictionary.")

        return city_dict

    def loadZipsToCSV(city_dict):
        """
        write the zip codes to the csv
        @param city_dict: the dict to with the zips to be added
        """
        # Read the CSV file again to append zip codes to the original address string
        input_file = 'Data/cleanedData.csv'
        output_file = 'Data/cleanedData2.csv'
        with open(input_file, newline='') as csvfile, open(output_file, 'w', newline='') as outputfile:
            csvreader = csv.reader(csvfile)
            csvwriter = csv.writer(outputfile)

            header = next(csvreader)
            csvwriter.writerow(header)

            for row in csvreader:
                address = row[3]  # Address is in the 4th column (index 3)
                city = extract_city(address)
                if city and city in city_dict:
                    zip_code = city_dict[city]
                    if zip_code and not has_zip_code(row[3]):
                        address_with_zip = f"{address} {zip_code}"
                        row[3] = address_with_zip
                csvwriter.writerow(row)

        print("Zip codes have been appended to the original address strings and saved to 'cleanedData.csv'")
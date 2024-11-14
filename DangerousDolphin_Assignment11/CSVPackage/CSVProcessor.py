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

# CSVProcessor.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv

class CSVProcessor:
    
    def __init__(self, filename):
        self.__filename = filename
        
    def process(self):
        print("Processing", self.__filename)
        data = self.readData()
        return data
    def readData(self):
        data = []
        with open(self.__filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)
        return data


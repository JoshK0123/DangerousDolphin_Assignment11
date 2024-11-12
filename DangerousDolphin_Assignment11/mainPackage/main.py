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


from CSVPackage.CSVProcessor import *

if __name__ == "__main__":
    print("main.py")
    myCSVProcessor = CSVProcessor("Data/fuelPurchaseData.csv")
    myCSVProcessor.process()
    print(myCSVProcessor.readData())
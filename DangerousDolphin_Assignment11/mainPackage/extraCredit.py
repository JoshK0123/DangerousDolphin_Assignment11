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



# EXTRA CREDIT: FINDINGS AND ISSUES WITH THE DATA
            # there are 4 different types of fuel types for 'liquefied natural gas'. those should have 		been condensed into one type. 
            # 2 of them have liquified misspelled, 1 is just liquid, the other is abbreviated as LNG.      
            #
            # There is 5 null/nan values in the Transaction number column.
            # Also, there is a transaction number with the value of -71649. 
            # Both these bad transaction numbers cause issues to the data of those 6 data entries.
            #  
            # Neither fuel quantity or gross price are rounded to 2 decimals for all entries.
            # Fuel is rounded to either 2-5 decimals and gross price is only rounded to 1.
            # That requires more cleanup to get the data to the same number of decimals.
            # 
            # Site IDs being either number values or text values could be confusing for people.
            # The Site IDs should be the type of value for easier understanding, whether text or numbers.
            #
            # There is some confusing ways of different spelling in address column.
            # For example, parkway is spelled as either parkway, pkwy, parkwy, 

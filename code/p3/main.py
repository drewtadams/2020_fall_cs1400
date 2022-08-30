'''
Project Name: Rabbits, Rabbits, Rabbits
Author: Trenton Howard
Due Date: 10/17/20
Course: CS1400-X03
 
This project is to print out an output in a CSV file. I will be using the file rabbits.csv and design a code to write the output of integers that consist of the number of months, adult rabbit pairs, baby rabbits, and the total number of pairs in the lab. I will then output the correct number of months when the cages will run out. 

Some good practice to help me write this code was learning from lessons 3.7 and 4.12 in Cengage MindTap, Fundamentals of Python: First Programs, 2e. I learned about creating opening files, file handlers, and magic numbers.
 
I am importing csv to use csv.writer and csv.DictWriter to output rows on the csv file.

'''

import csv

BEGINNING_MONTH = 1
BEGINNING_ADULTS = 1
BEGINNING_BABIES = 0
TOTAL_NUMBER_CAGES = 500

# open the rabbits.csv file and assign it to an object
with open('rabbits.csv', 'w', newline = '') as rabbits:

    # Using writer to output first comment to the file
    fileHandle = csv.writer(rabbits)
    fileHandle.writerow({'# Table of rabbit pairs'})

    # Create column variables
    fieldnames = ['c1','c2','c3','c4']
  
    # Create an object that maps dictionaries onto output rows
    fileHandle = csv.DictWriter(rabbits, fieldnames = fieldnames)

    # Assign strings to columns
    fileHandle.writerow({'c1':'Months', 'c2':' Adults', 'c3':' Babies', 'c4':' Total'})

    # Setting initial values
    months = BEGINNING_MONTH
    adults = BEGINNING_ADULTS 
    babies = BEGINNING_BABIES
    total = adults + babies

  # Use while loop to write each row to the file until the total number of cages is exceeded
    while total <= TOTAL_NUMBER_CAGES:
        fileHandle.writerow({'c1':months, 'c2': adults, 'c3': babies, 'c4':total})

        months = months + 1
        prevBabies = babies
        babies = adults
        adults = adults + prevBabies 
        total = adults + babies
    # Print out the final row that exceeds the max number of cages
    fileHandle.writerow({'c1':months, 'c2': adults, 'c3': babies, 'c4': total})

    # Changing it to a writer object to print out second comment
    fileHandle = csv.writer(rabbits)
    fileHandle.writerow({'# Cages will run out in month ' + str(months)})
# Problem Sheet - Weekly Task 07

# Instructions:
# Write a program that reads in a text file and outputs the number of e's it contains. 
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line.

import sys

filename = sys.argv[1]  # takes in command line argument. argv[0] would be a path to this file

letter = 'e' 
letter2 = letter.upper()  
# Could be letter2 = 'E'
# letter 2 = letter.upper() would be more useful if we were reading in user's input for the letter

def countEs(filename, letter):
    with open(filename) as f:
        text = f.read()
        numberLower = text.count(letter)   # counts instances of 'e'
        numberUpper = text.count(letter2)  # counts instances of 'E'
        totalNumber = numberLower + numberUpper # sums both for total number instances of the letter despite of case
        
        return (numberLower, numberUpper, totalNumber)

values = countEs (filename, letter)   # function countES () returns multiple values as a tuple

lower = values [0] # storing each value as a separte variable for use in message
upper = values [1]
total = values [2]

print (f'This file contains total of {total} instances of letter "e" {lower} of witch are lowercase and {upper} are uppercase')
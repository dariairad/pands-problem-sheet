# Problem Sheet - Weekly Task 07

# Instructions:
# Write a program that reads in a text file and outputs the number of e's it contains. 
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line.

import sys

filename = sys.argv[1]  # takes in command line argument. argv[0] would be a path to this file

def countEs(filename):
    with open(filename) as f:
        text = f.read()
        numberLower = 0
        numberUpper = 0
        numberTotal = 0
        for i in text:
            if i == 'e':
                numberLower = numberLower + 1   # counts instances of 'e'
                numberTotal = numberTotal + 1
            elif i == 'E':
                numberUpper = numberUpper + 1  # counts instances of 'E'
                numberTotal = numberTotal + 1
               
        return (numberLower, numberUpper, numberTotal)

values = countEs (filename)   # function countES () returns multiple values as a tuple

lower = values [0] # storing each value as a separte variable for use in message
upper = values [1]
total = values [2]

print (f'This file contains total of {total} instances of letter "e" {lower} of which are lowercase and {upper} are uppercase')
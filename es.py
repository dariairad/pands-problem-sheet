# Problem Sheet - Weekly Task 07

# Task Description:
# Write a program that reads in a text file and outputs the number of e's it contains. 
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line.

# Author: Daria Sep

import sys

# argv [1] reads in second command line argument.
# First argument, argv[0], is a path to this Python file. 
filename = sys.argv[1]  


def countEs(filename):      
    with open(filename) as f:
        text = f.read()
        numLower = numUpper = numTotal = 0  # Starts to count from 0.

        for i in text:
            if i == 'e':        
                numLower += 1   # Counts instances of 'e' in the file.
                numTotal += 1   
            elif i == 'E':
                numUpper += 1   # Counts instances of 'E' in the file.
                numTotal += 1                
                # numTotal counts every instance of 'e' in the file despite of its case.
        return(numLower, numUpper, numTotal)

values = countEs(filename)   # Function countEs() returns multiple values stored as a tuple.
lower = values [0] 
upper = values [1]
total = values [2]

print(f'This file contains a total of {total} instances of letter "e". \nOut of {total}, {lower} are lowercase and {upper} are uppercase.')
# Problem Sheet - Weekly Task 04

# Program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step program calculates the next value by taking the current value and, 
# if it is even, dividing it by two, 
# but if it is odd, multiplying it by three and adding one.
# Program ends if the current value is one.

# Author: Daria Sep

number = int (input ('Please input a number: '))

while number != 1: 

    print(number, end = ' ')  
    # ref: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
    
    if (number % 2) == 0:
        number = int (number / 2)
    else:
        number = int ((number * 3) + 1)

print (number)

# WIP -> add ValueError



# Problem Sheet - Weekly Task 04

# Program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step program calculates the next value by taking the current value and, 
# if it is even, dividing it by two, 
# but if it is odd, multiplying it by three and adding one.
# Program ends if the current value is one.

# Author: Daria Sep

numbers = []

number = int (input ('Please input a number: '))

while number != 1: 
    if (number % 2) == 0:
        number = number / 2
    else:
        number = (number * 3) + 1
    
    numbers.append (int (number))

print (numbers)

# output doesnt include initial input. Need to review



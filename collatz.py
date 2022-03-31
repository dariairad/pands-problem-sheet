# Problem Sheet - Weekly Task 04

# Program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step program calculates the next value by taking the current value and, if it is even, dividing it by two, but if it is odd, multiplying it by three and adding one.
# Program ends if the current value is one.

# Author: Daria Sep

while True:     # to prompt another input request in case of value error
    try:        # try/except to catch exceptions (0, negative, blank or non-int input)
        number = int (input ('Please input a positive integer: '))
        if number <= 0 or number == '':
            raise ValueError ('Incorrect value.')
        break
    except ValueError:
        print ('Incorrect input. Please try again.')

while number != 1:  # to continue calculations until number is equal to 1

    print(number, end = ' ')  # to return each calculations output, and keep them all in one line
        
    if (number % 2) == 0:
        number = int (number / 2)
    else:
        number = int ((number * 3) + 1)
    
print (number) # includes last calculation output (1) to the output message
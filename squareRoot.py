# Problem Sheet - Weekly Task 06

# Program that takes a positive floating-point number as input 
# and outputs an approximation of its square root.
# Program uses the newton method of estimating square roots.

# Author: Daria Sep



def sqrt(n):        
    approx = 0.5 * n    # root of n can't be less than half of the its value, we can therfore start approximating here
    better = 0.5 * (approx + (n / approx))      # Newton Method sqyare root approximation formula
    while better != approx :    # as long as closer approximation can be found, the program will keep running  
        approx = better         # initial approximation is being replaced with better approximation
        better = 0.5 * (approx + (n / approx))      # calculations continue
    return approx

n = float (input ('Please enter a positive number: '))   # User input for n
rounding = int (input ('Enter the number of decimals for the answer rounding: ')) # user input for rounding
roundedAnswer = round ((sqrt(n)), rounding)  # Rounding the number to the decimal places defined by user in the line above

print (f'The approximate root of {n} rounded to {rounding} decimal place(s) is {roundedAnswer}') 


# WIP - add error handling, fix comments. 
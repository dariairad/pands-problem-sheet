# Problem Sheet - Weekly Task 06

# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Program uses the newton method of estimating square roots.

# Author: Daria Sep


def sqrt(n):        
    approx = 0.5 * n    # Square root of n can't be less than half of the its value, we can therfore start approximating here.
    better = 0.5 * (approx + (n / approx))      # Newton Method square root approximation formula.
    while better != approx :    # As long as closer approximation can be found, the program will keep running  
        approx = better         # Initial approximation is being replaced with better approximation.
        better = 0.5 * (approx + (n / approx))      # Calculations continue until no better approximation can be found.
    return approx

print ('Please enter a positive number: ', end = '' )
# Catching invalid inputs and prompting user to input another value.
while True:
    try: 
        n = float (input(''))   # User input for n.
        if n == '' or n <= 0:
            raise ValueError ('Incorrect input.')
        break
    except ValueError:
        print (f'This is not a positive number. Try again: ', end ='')

rawResult = sqrt(n)

# Extra: Offering option of rounding the result to the chosen number of decimal places.
print('Do you want to round the result?', end = ' ')
while True: 
    try: 
        rounding = input('Press Y for \'yes\' \ N or leave blank for \'no\': ')
        
        if rounding == 'Y' or rounding == 'y': 
            print('Enter the number of decimals for the answer rounding: ', end = '')
            
            while True: 
                try:
                    r = int(input('')) # user input for rounding
                    if r < 0:
                        raise ValueError('Number of decimals cannot be negative.')
                    break
                except ValueError:
                        print('Invalid input. Please input a positive integer: ', end = '')
            
            if r == 0: 
                rAnswer = round(sqrt(n))
                print(f'The approximate square root of {n} rounded to the closest whole number is {round(rAnswer)}') 
            else: 
                rAnswer = round(sqrt(n), r)
                print(f'The approximate square root of {n} rounded to {r} decimal place(s) is {rAnswer}')
            break

        if rounding == 'N' or rounding == 'n' or rounding == '':
            print(f'The approximate square root of {n} is {rawResult}')
        else: 
            raise ValueError('Invalid input.')
        break
    except ValueError: 
        print('Invalid input.')
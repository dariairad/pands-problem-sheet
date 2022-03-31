# Problem Sheet - Weekly Task 02

# Task Description:
# Program that calculates Body Mass Index (BMI). 
# The inputs are the persons's height in centimetres and weight in kilograms. The output is thei

# Additions:
# - Personalised welcome message based on the user input
# - Error handling for weight and height inputs:
#       non-numerical inputs as well as numerical inputs lower or equal to 0 throw an error and prompt user to try again
# - BMI interpretation (Underweight, Normal, Overweight, Obese)

# Author: Daria Sep


name = input('Welcome to the BMI Calculator! \nWhat\'s your name?: ')
print (f'Hello {name}! Let\'s calculate your BMI.') 

# Defining function calculating BMI. 
def bmiIndex(weight, height):
    rawBmi = (weight / (height ** 2) * 10000)
    return rawBmi

# Using try/except to catch incorrect inputs and while loop to keep prompting the user for correct input   
while True:
    try: 
        weight = float (input ('Enter your weight in kg: '))
        if weight == "" or weight <= 0:
            raise ValueError ('Incorrect value entered.')
    except ValueError:
            print("Sorry, that's not right. Please try again")      
    else: 
        break   

while True: 
    try:
        height = float (input ('Enter your height in cm: '))
        if height == "" or height <= 0:
            raise ValueError ('Incorrect value entered.')
    except ValueError: 
        print("Sorry, that's not right. Please try again")
    else: 
        break
            
# Calling the function and using round() to round the calculation's output to 2 decimal places
bmi = round (bmiIndex (weight, height), 2)

# Interpreting the BMI result
if bmi < 18.5: 
    print (f'Your BMI is {bmi}. You might be underweight.')
elif  bmi < 25:
    print (f'Your BMI is {bmi}. You\'re a healthy weight.')
elif  bmi < 30:
    print(f'Your BMI is {bmi}. You might be overweight.')
else:
    print (f'Your BMI is {bmi}. You might be obese.')
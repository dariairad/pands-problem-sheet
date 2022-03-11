# Problem Sheet - Weekly Task 02

# Program that calculates Body Mass Index (BMI). 
# The inputs are the persons's height in centimetres and weight in kilograms. The output is their BMI.

# Author: Daria Sep

name = input('Enter your name: ')
print ('Hello {}! Let\'s calculate your BMI.' .format (name)) 

weight = int (input ('\nEnter your weight in kg: '))
height = int (input ('Enter your height in cm: '))
# Using constructor int() to convert weight and height inputs into int and allow calculations below
bmi = round (((weight / (height ** 2) * 10000)), 2) 
# Using round() to round the calculation's output to 2 decimal places 

print ('\nYour BMI is', bmi) 
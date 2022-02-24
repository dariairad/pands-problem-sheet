# Problem Sheet - Weekly Task 02

# Program that calculates Body Mass Index (BMI). 
# The inputs are the persons's height in centimetres and weight in kilograms.
# The output is their BMI.

# Author: Daria Sep

name = input('Enter your name: ')
print ('Hello {}! Let\'s calculate your BMI.' .format (name))

weight = int (input ('\nEnter your weight in kg: '))
height = int (input ('Enter your height in cm: '))
bmi = round (((weight / (height ** 2) * 10000)), 1)

print ('\nYour BMI is {}'.format(bmi))
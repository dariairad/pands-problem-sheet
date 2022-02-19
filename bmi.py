# Program calculating BMI
# Author: Daria Sep

name = input('Enter your name: ')
print('Hello '+name +"! \nLet's calculate your BMI")

weight = int(input('Enter your weight in kg: '))
height = int(input('Enter your height in cm: '))
bmi = round(((weight / (height ** 2) * 10000)),1)

print('Your BMI is {}'.format(bmi))
## pands-problem-sheet


#### Author
Daria Sep (G00411221@gmit.ie)
#### Course
Higher Diploma in Computing in Data Analytics
#### Module
52167 - Programming and Scripting
#### Lecturer
Andrew Beatty (andrew.beatty@gmit.ie)


## Overview

This repository is a submission to *Problem Sheet* assignment associated with the *Programming ans Scripting* module. 

The repository itself contains 7 .py files that present solutions to 7 weekly tasks set throughout the course. 
  
The purpose of this README file is to provide insights into the process of the author, their understanding of the code used, as well as research executed and refernences used.


## Week 02 - Statements

### Task description

Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
The inputs are the person's height in centimetres and weight in kilograms. The output is their BMI.

### Code

```
name = input('Enter your name: ')
print ('Hello {}! Let\'s calculate your BMI.' .format (name))

weight = int (input ('\nEnter your weight in kg: '))
height = int (input ('Enter your height in cm: '))
bmi = round (((weight / (height ** 2) * 10000)), 2)

print ('\nYour BMI is {}'.format(bmi))
```
[bmi.py](https://github.com/dariairad/pands-problem-sheet/blob/main/bmi.py)

### Code explanation

1. The `input()` function allows user input. User input being used in the program: *name* - for personalised welcome message, *weight* and *heigh*t - for BMI calculations.
2. The `int()` constructor returns an integer number. Converted weight and height inputs into integers to allow calculations.
4. The `round()` function rounds a number to the specified number of decimal. Initially rounded to 1 decimal point, changed to 2 decimal points as per interim feedback  

### References

1. diabetes.ca - Body Mass Index (BMI) Calculator. https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
2. geeksforgeeks.com - Python Arithmetic Operators. https://www.geeksforgeeks.org/python-arithmetic-operators/
4. w3schools.com - Built-in Functions. https://www.w3schools.com/python/python_ref_functions.asp


## Week 03 - Variables

### Task description

Write a program that asks a user to input a string and outputs every second letter in reverse order.

### .py file

### Code explanation

### References


## Week 04 - Controlling the flow

### Task description

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

### .py file

[weekday.py](https://github.com/dariairad/pands-problem-sheet/blob/main/weekday.py)

### Code explanation

### References


## Week 05 - Data

### Task description

Write a program that outputs whether or not today is a weekday.

### .py file

### Code explanation

### References


## Week 06

### Task description

### .py file

### Code explanation

### References


## Week 07

### Task description

### .py file

### Code explanation

### References


## Week 08

### Task description

### .py file

### Code explanation

### References

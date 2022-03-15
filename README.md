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

### Explanation

1. The `input()` function allows user input. User input being used in the program: *name* - for personalised welcome message, *weight* and *height* - for BMI calculations.
2. Value read with `input()` function is in a string format. Used the int() constructor, that returns an integer number, to convert *weight* and *height* inputs into integers thus allowing for arithmetic operations.
3. The `round()` function rounds a number to the specified number of decimal. Initially rounded to 1 decimal point, changed to 2 decimal points as per interim feedback  

### References

1. diabetes.ca - Body Mass Index (BMI) Calculator. https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
2. geeksforgeeks.com - Python Arithmetic Operators. https://www.geeksforgeeks.org/python-arithmetic-operators/
4. w3schools.com - Built-in Functions. https://www.w3schools.com/python/python_ref_functions.asp


## Week 03 - Variables

### Task description

Write a program that asks a user to input a string and outputs every second letter in reverse order.

### Code

```
sentence = input ('Please enter a sentence: ')
print (sentence [::-2])
```

[secondString.py](https://github.com/dariairad/pands-problem-sheet/blob/main/secondString.py)

### Explanation

1. The `slice()` function returns a slice object. A slice object is used to specify how to slice a sequence. Syntax: slice(start, end, step)
2. Reversd a string using a slice that steps backwards [x,y,-1]. Change step to -2 to satisfy task requirement of ouputing every second letter.
3. The function's start and end prameter remain unchanged as full input sentence is to be considered. 

### References

1. w3schools.com - How to Reverse a String in Python. https://www.w3schools.com/python/python_howto_reverse_string.asp
2. w3schools.com - Python slice() Function. https://www.w3schools.com/python/ref_func_slice.asp


## Week 04 - Controlling the flow

### Task description

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

### Code

```
number = int (input ('Please input a number: '))

while number != 1: 

    print(number, end = ' ')  
    
    if (number % 2) == 0:
        number = int (number / 2)
    else:
        number = int ((number * 3) + 1)

print (number)
```

[collatz.py](https://github.com/dariairad/pands-problem-sheet/blob/main/collatz.py)

### Explanation

1. Used `input()` to allow the user to choose the initial number, and `int()` to convert the input into an integer for calculations.
2. Set `while` condition to `!=` (not eqal to) 1 for the program to continue calculations until the output is  1.
3. Python’s `print()` function comes with an 'end' parameter. By default, the value of this parameter is `\n`. Set 'end' to spece to print outputs in one line. 
4. `(number % 2) == 0` checkes if a number is divisable by 2, ie. even. If condition is satisfied, the number is being divided by 2. Otherwise, for odd numbers, the program multiplies it by 3 and adds 1. 
5. `print(number)` in the last line adds number 1 into the final output.

### References

1. codippa.com - Check if number is even or odd. https://codippa.com/even-odd-python/
2. geeksforgeeks.com - Python end parameter in print(). https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print
3. pythonppl.com - Understanding Collatz Sequence in Python. https://www.pythonpool.com/collatz-sequence-python/
4. realpython.com - Python "while" Loops (Indefinite Iteration). https://realpython.com/python-while-loop/


## Week 05 - Data

### Task description

Write a program that outputs whether or not today is a weekday.

### Code

```
from datetime import date

if date.today().weekday() < 5:
    print('Yes, unfortunately today is a weekday')

else:
    print ('It is the weekend, yay!')
```

[weekday.py](https://github.com/dariairad/pands-problem-sheet/blob/main/weekday.py)

### Explanation
1. Used `Datetime` module that supplies classes to work with date and time.
2. `today()` function of date class returns the current local date, while `weekday()` returns the day of the week as integer where Monday is 0 and Sunday is 6
3. Integers 0-4 correspond to Monday-Friday respectively, therefore any integer lower than 5 (< 5) corresponds to a weekday. 

### References
1. geeksforgeeks.com - Python datetime module. https://www.geeksforgeeks.org/python-datetime-module/
2. python.org - Basic date and time types. https://docs.python.org/3/library/datetime.html?highlight=datetime%20module 
3. pythontic.com - Weekday Function In Python. https://pythontic.com/datetime/date/weekday


## Week 06

### Task description

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.

### Code

### Explanation

### References

1. Sweigart, A. (2020). *Automate the Boring Stuff with Python.* 2nd ed. San Francisco: No Starch Press.
2. geeksforgeeks.com - Find root of a number using Newton’s method. https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
3. runestone.academy - How to Think Like a Computer Scientist. https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
4. school-for-champions.com - Newton's Square Root Approximation. https://www.school-for-champions.com/algebra/square_root_approx.htm#.Yi-kwejP3GI
5. w3schools.com - Python Functions. https://www.w3schools.com/python/python_functions.asp

## Week 07

### Task description

### Code

### Explanation

### References


## Week 08

### Task description

### Code

### Explanation

### References

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

This repository is a submission to *Problem Sheet* assignment associated with the *Programming and Scripting* module. 

The repository itself contains 7 .py files that present solutions to 7 weekly tasks set throughout the course. 
  
The purpose of this README file is to provide insights into the process of writing the code, understanding of the code, as well as the research and refernences used.


## Week 02 - Statements

### Task description

Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
The inputs are the person's height in centimetres and weight in kilograms. The output is their BMI.

### Extras

- Personalised welcome message based on the user input
- Error handling for weight and height inputs: non-numerical input, numerical inputs equal to or lower that 0, and blank inputs throw an error and prompt the user to try again.
- BMI interpretation (Underweight, Normal, Overweight, Obese)

### Code

```
name = input('Welcome to the BMI Calculator! \nWhat\'s your name? ')
print (f'Hello {name}! Let\'s calculate your BMI.') 

def bmiIndex(weight, height):
    rawBmi = (weight / (height ** 2) * 10000)
    return rawBmi

while True:
    try: 
        weight = float (input ('Enter your weight in kg: '))
        if weight == "" or weight <= 0:
            raise ValueError ('Incorrect value entered.')
    except ValueError:
            print("Sorry, that's not right. Please try again.")      
    else: 
        break   

while True: 
    try:
        height = float (input ('Enter your height in cm: '))
        if height == "" or height <= 0:
            raise ValueError ('Incorrect value entered.')
    except ValueError: 
        print("Sorry, that's not right. Please try again.")
    else: 
        break
            
bmi = round (bmiIndex (weight, height), 2)

if bmi < 18.5: 
    print (f'Your BMI is {bmi}. You might be underweight.')
elif  bmi < 25:
    print (f'Your BMI is {bmi}. You\'re a healthy weight.')
elif  bmi < 30:
    print(f'Your BMI is {bmi}. You might be overweight.')
else:
    print (f'Your BMI is {bmi}. You might be obese.')
```
[bmi.py](https://github.com/dariairad/pands-problem-sheet/blob/main/bmi.py)

### Explanation

1. Used `input()` function to allow user input. User input being used in the program: *name* - for personalised welcome message, and later on, *weight* and *height* - for BMI calculations.
2. Created custom function `bmiIndex()` that takes in two arguments: *weight* and *height*, and includes formula for calculating BMI.
3. As the program takes in *weight* and *height* from user input I used `try / except` to catch `ValueErrors` - non-numerical input, blank input, and numerical input equal or less than 0.
4. Along with `try/except`, I used the `while` loop to keep prompting the user for correct input after the exception was raised.
5. As values read in with `input()` function are in a string format, I used the `float()` constructor that returns a float number to convert *weight* and *height* inputs into floats thus allowing for arithmetic operations.
6. I called in a function and rounded the utput to 2 decimal places using the `round()` function.
7. Used `if` statement to interpret the BMI and to provide the user with context regarding their result. 

### References

1. diabetes.ca - *Body Mass Index (BMI) Calculator.* https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
2. Elkner, J. (2020). - *Beginning Python Programming for Aspiring Web Developers.* https://www.openbookproject.net/books/bpp4awd/ch04.html  
3. geeksforgeeks.com - *Python Arithmetic Operators.* https://www.geeksforgeeks.org/python-arithmetic-operators/ 
4. stackoverflow.com - *BMI with exception handling python.* https://stackoverflow.com/questions/51125220/bmi-with-exception-handling-python 
5. Sweigart, A. (2020). *Automate the Boring Stuff with Python.* 2nd ed. San Francisco: No Starch Press.
6. w3schools.com - *Built-in Functions.* https://www.w3schools.com/python/python_ref_functions.asp


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

1. w3schools.com - *How to Reverse a String in Python.* https://www.w3schools.com/python/python_howto_reverse_string.asp
2. w3schools.com - *Python slice() Function.* https://www.w3schools.com/python/ref_func_slice.asp


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

1. codippa.com - *Check if number is even or odd.* https://codippa.com/even-odd-python/
2. geeksforgeeks.com - *Python end parameter in print().* https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print
3. pythonppl.com - *Understanding Collatz Sequence in Python.* https://www.pythonpool.com/collatz-sequence-python/
4. realpython.com - *Python "while" Loops (Indefinite Iteration).* https://realpython.com/python-while-loop/
5. Sweigart, A. (2020). *Automate the Boring Stuff with Python.* 2nd ed. San Francisco: No Starch Press.


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
1. geeksforgeeks.com - *Python datetime module.* https://www.geeksforgeeks.org/python-datetime-module/
2. python.org - *Basic date and time types.* https://docs.python.org/3/library/datetime.html?highlight=datetime%20module 
3. pythontic.com - *Weekday Function In Python.* https://pythontic.com/datetime/date/weekday


## Week 06

### Task description

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.

### Code

[squareRoot.py](https://github.com/dariairad/pands-problem-sheet/blob/main/squareRoot.py)

### Explanation

### References

1. geeksforgeeks.com - *Find root of a number using Newton’s method.* https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
2. runestone.academy - *How to Think Like a Computer Scientist.* https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
3. school-for-champions.com - *Newton's Square Root Approximation.* https://www.school-for-champions.com/algebra/square_root_approx.htm#.Yi-kwejP3GI
4. Sweigart, A. (2020). *Automate the Boring Stuff with Python.* 2nd ed. San Francisco: No Starch Press.
5. w3schools.com - Python Functions. https://www.w3schools.com/python/python_functions.asp

## Week 07

### Task description

Write a program that reads in a text file and outputs the number of e's it contains. 
Think about what is being asked here, document any assumptions you are making.
The program should take the filename from an argument on the command line. 

### Code

```
import sys

filename = sys.argv[1]  

def countEs(filename):      
    with open(filename) as f:
        text = f.read()
        numLower = numUpper = numTotal = 0  # starting to count from 0
        for i in text:
            if i == 'e':        
                numLower += 1   
                numTotal += 1   
            elif i == 'E':
                numUpper += 1   
                numTotal += 1                      
        return (numLower, numUpper, numTotal)

values = countEs (filename)

lower = values [0] 
upper = values [1]
total = values [2]

print (f'This file contains a total of {total} instances of letter "e". \nOut of {total}, {lower} are lowercase and {upper} are uppercase.')
```

[es.py](https://github.com/dariairad/pands-problem-sheet/blob/main/es.py)

### Explanation

### References

1. Coding Under Pressure - *Command Line Arguments in Python - How to Read Command Line Arguments in Python.* https://youtu.be/QJBVjBq4c7E
2. geeksforgeeks.com - *Count the number of times a letter appears in a text file.* https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
3. note.nkmk.me - *How to return multiple values from a function in Python.* https://note.nkmk.me/en/python-function-return-multiple-values/
4. python.org - *sys — System-specific parameters and functions.* https://docs.python.org/3/library/sys.html#module-sys
5. realpython.com - *Lists and Tuples in Python.* https://realpython.com/python-lists-tuples/

## Week 08

### Task description

Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

### Code

[plotTask.py](https://github.com/dariairad/pands-problem-sheet/blob/main/plottask.py)

### Explanation

### References



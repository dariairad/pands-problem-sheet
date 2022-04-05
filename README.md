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
print(f'Hello {name}! Let\'s calculate your BMI.') 


def bmiIndex(weight, height):
    rawBmi = (weight / (height ** 2) * 10000)
    return rawBmi

while True:
    try: 
        weight = float(input('Enter your weight in kg: '))
        if weight == '' or weight <= 0:
            raise ValueError('Incorrect value entered.')
    except ValueError:
            print('Sorry, that\'s not right. Please try again.')      
    else: 
        break   

while True: 
    try:
        height = float(input ('Enter your height in cm: '))
        if height == '' or height <= 0:
            raise ValueError('Incorrect value entered.')
    except ValueError: 
        print('Sorry, that\'s not right. Please try again.')
    else: 
        break
            
bmi = round(bmiIndex (weight, height), 2)

if bmi < 18.5: 
    print(f'Your BMI is {bmi}. You might be underweight.')
elif  bmi < 25:
    print(f'Your BMI is {bmi}. You\'re a healthy weight.')
elif  bmi < 30:
    print(f'Your BMI is {bmi}. You might be overweight.')
else:
    print(f'Your BMI is {bmi}. You might be obese.')
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

1. Canadian Diabetes Association (2022). *Body Mass Index (BMI) Calculator.* https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
2. Elkner, J. (2020). *Beginning Python Programming for Aspiring Web Developers.* https://www.openbookproject.net/books/bpp4awd/ch04.html  
3. Singh Rautelam, Y. (2020). *Python Arithmetic Operators.* https://www.geeksforgeeks.org/python-arithmetic-operators/ 
4. StackOverflow (2018). *BMI with exception handling python.* https://stackoverflow.com/questions/51125220/bmi-with-exception-handling-python 
5. Sweigart, A. (2020). *Automate the Boring Stuff with Python.* 2nd ed. San Francisco: No Starch Press.
6. W3Schools (n.d.). *Built-in Functions.* https://www.w3schools.com/python/python_ref_functions.asp


## Week 03 - Variables

### Task description

Write a program that asks a user to input a string and outputs every second letter in reverse order.

### Code

```
sentence = input('Please enter a sentence: ')
print(sentence [::-2])
```

[secondString.py](https://github.com/dariairad/pands-problem-sheet/blob/main/secondString.py)

### Explanation

1. The `slice()` function returns a slice object. A slice object is used to specify how to slice a sequence. Syntax: slice(start, end, step)
2. Reversd a string using a slice that steps backwards [x,y,-1]. Change step to -2 to satisfy task requirement of ouputing every second letter.
3. The function's start and end prameter remain unchanged as full input sentence is to be considered. 

### References

1. W3Schools (n.d.). *How to Reverse a String in Python.* https://www.w3schools.com/python/python_howto_reverse_string.asp
2. W3Schools (n.d.). *Python slice() Function.* https://www.w3schools.com/python/ref_func_slice.asp


## Week 04 - Controlling the flow

### Task description

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

### Code

```
while True:     
    try:       
        number = int(input ('Please input a positive integer: '))
        if number <= 0 or number == '':
            raise ValueError('Incorrect value.')
        break
    except ValueError:
        print('Incorrect input. Please try again.')

while number != 1:  
    print(number, end = ' ')  
        
    if (number % 2) == 0:
        number = int (number / 2)
    else:
        number = int((number * 3) + 1)
    
print(number)
```

[collatz.py](https://github.com/dariairad/pands-problem-sheet/blob/main/collatz.py)

### Explanation

1. Used `input()` to allow the user to choose the initial number, and `int()` to convert the input into an integer for calculations.
2. Used `try/except` to catch incorrect inputs (non-ints, blanks, numbers equal to or lower than 0) and `while` loop to keep prompting the user for input in case of exception being raised. 
3. Once correct input has been provided, the program proceed to calculations. 
4. Set `while` condition to `!=` (not eqal to) 1 for the program to continue calculations until the output is  1.
5. Python’s `print()` function comes with an `end` parameter - `\n` by default. I set `end` to space so the outputs are printed in single line. 
6. `(number % 2) == 0` checkes if a number is divisable by 2, ie. even. If condition is satisfied, the number is being divided by 2. Otherwise, for odd numbers, the program multiplies it by 3 and adds 1. 
7. `print(number)` in the last line adds number 1 into the final output.

### References

1. Codippa (n.d.). *Check if number is even or odd.* https://codippa.com/even-odd-python/
2. Bindal, A. (2021). *Python end parameter in print().* https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print
3. PythonPool (2021). *Understanding Collatz Sequence in Python.* https://www.pythonpool.com/collatz-sequence-python/
4. Sturtz, J. (2018). *Python "while" Loops (Indefinite Iteration).* https://realpython.com/python-while-loop/
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
    print('It is the weekend, yay!')
```

[weekday.py](https://github.com/dariairad/pands-problem-sheet/blob/main/weekday.py)

### Explanation
1. Used `Datetime` module that supplies classes to work with date and time.
2. `today()` function of date class returns the current local date, while `weekday()` returns the day of the week as integer where Monday is 0 and Sunday is 6
3. Integers from 0 to 4 correspond to Monday-Friday respectively, therefore any integer lower than 5 (< 5) corresponds to a weekday. 
4. Used `if` statement to set conditions for the output messages.  

### References
1. GeeksForGeeks (2021). *Python datetime module.* https://www.geeksforgeeks.org/python-datetime-module/
2. The Python Software Foundation (n.d.). *Basic date and time types.* https://docs.python.org/3/library/datetime.html?highlight=datetime%20module 
3. Pythontic (n.d). *Weekday Function In Python.* https://pythontic.com/datetime/date/weekday


## Week 06 - Functions

### Task description

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
Create your own sqrt function and do not use the built in functions x ** .5 or math.sqrt(x).
This is to demonstrate that you can research and code a process.
Suggestion: Look at the Newton's Method of estimating square roots.

### Code

```
def sqrt(n): 
    approx = 0.5 * n   
    better = 0.5 * (approx + (n / approx))
    while better != approx :   
        approx = better
        better = 0.5 * (approx + (n / approx))
    return approx

print('Please enter a positive number: ', end = '' )

while True:
    try: 
        n = float(input ('')) 
        if n == '' or n <= 0:
            raise ValueError('Incorrect input.')
        break
    except ValueError:
        print(f'This is not a positive number. Try again: ', end ='')

rawResult = sqrt(n)

print('Do you want to round the result?', end = ' ')
while True: 
    try: 
        rounding = input('Press Y for \'yes\' \ N or leave blank for \'no\': ')

        if rounding == 'Y' or rounding == 'y': 
            print('Enter the number of decimals for the answer rounding: ', end = '')
           
           while True: 
                try:
                    r = int(input ('')) 
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
```

[squareRoot.py](https://github.com/dariairad/pands-problem-sheet/blob/main/squareRoot.py)

### Explanation

1. Started with creating a custom function `sqrt(n)` that calculates the square root approximation based on Newton's Method.
   The function takes in one argument, a (positive) number.
    - The variable `approx` is a starting point for the calculations and stores value `0.5 * n` as the square root of a number can't be less than half of it's value.
    - The variable `better` stores output of the square root approximation method formula. The formula takes in the number (`n`) and the initial approximation (`approx`) for the calculations: `0.5 * (approx + (n / approx))`.
    - Once better approximation (`better`) is calculated the output of the calculation replaces the initial approximation and is now stored under `approx` variable. 
    - New value of the `approx`is now being used in the calculation to find even better approximation of the square root.
    - The cycle continues as long as better approximation can be found, i.e. until values  of `better` and `approx` aren't equal (`better != approx`).
 2. Next follows the `print()` function that includes a message asking user for an input. 
 3. The input itself, stored as `n`, is taken in separately preventing the same message from being displayed where exception is identified. 
 4. In order to allow for the calculations, the input taken in needs to be a positive float (or int). 
 5. `try/except` statement is used for input validation. Along with values of format other than str or int, the following are also identified as invalid inputs: negative numbers, 0, blank input. Due to the use of the `while` loop, the user is being prompted for an input until valid input is provided.
 6. Once valid input is provided, the function `sqrt(n)`is being called and stored under `rawResult` variable.
 7. Instead of displaying the result straight away, the user gets to choose whether they want to a raw or rounded result to be returned - Yes/No choice. The answer is validated using `try/except` block. The `while` loop is used to keep prompting for valid input where needed. 
 8. After a valid input is provided, the `if`statement is used to define next steps. If user chooses the rounding option, they can then also set the number of decimal places used for the rounding, incl. 0 to round to the closest whole number/int. In here the input needs to be a positive int or a 0. Again, the `try/except` block and `while` loop are being used. If valid input is provided, `round()`function is used to round the result. 
 9. If user chooses not to round the result, the raw value is given (`rawResult`).

### References

1. Agrawal, U. (2022). *Find root of a number using Newton’s method.* https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
2. Runestone Interactive (n.d.). *How to Think Like a Computer Scientist.* https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
3. Kurtus, R. (2022). *Newton's Square Root Approximation.* https://www.school-for-champions.com/algebra/square_root_approx.htm#.Yi-kwejP3GI
4. Sweigart, A. (2020). *Automate the Boring Stuff with Python.* 2nd ed. San Francisco: No Starch Press.
5. W3Schools - Python Functions. https://www.w3schools.com/python/python_functions.asp

## Week 07 - Files

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
        numLower = numUpper = numTotal = 0
        
        for i in text:
            if i == 'e':        
                numLower += 1   
                numTotal += 1   
            elif i == 'E':
                numUpper += 1   
                numTotal += 1                      
        return (numLower, numUpper, numTotal)

values = countEs(filename)
lower = values[0] 
upper = values[1]
total = values[2]

print(f'This file contains a total of {total} instances of letter "e".')
print(f'Out of {total}, {lower} are lowercase and {upper} are uppercase.')
```

[es.py](https://github.com/dariairad/pands-problem-sheet/blob/main/es.py)

### Explanation

### References

1. Coding Under Pressure (2021). *Command Line Arguments in Python - How to Read Command Line Arguments in Python.* https://youtu.be/QJBVjBq4c7E
2. Saha, R. (2022). *Count the number of times a letter appears in a text file.* https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
3. Nkmk (2019). *How to return multiple values from a function in Python.* https://note.nkmk.me/en/python-function-return-multiple-values/
4. The Python Software Foundation (n.d.). *sys — System-specific parameters and functions.* https://docs.python.org/3/library/sys.html#module-sys
5. Sturtz, J. (2018). *Lists and Tuples in Python.* https://realpython.com/python-lists-tuples/

## Week 08 - Looking Ahead

### Task description

Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on one set of axes.

### Code

```
import numpy as np
import matplotlib.pyplot as plot

xpoints = np.array(range (0, 5))
ypointsf = xpoints             
ypointsg = xpoints * xpoints    
ypointsh = xpoints ** 3         

plot.plot(xpoints, ypointsf, label='f(x)=x', color='red')
plot.plot(xpoints, ypointsg, label='g(x)=x\N{SUPERSCRIPT TWO}', color='green')
plot.plot(xpoints, ypointsh, label='h(x)=x\N{SUPERSCRIPT THREE}', color='blue')

plot.title('Exponents of x')
plot.legend()

plot.show()
```

[plotTask.py](https://github.com/dariairad/pands-problem-sheet/blob/main/plottask.py)

### Plot

![Figure_1](https://user-images.githubusercontent.com/98287400/161792510-b881d290-0b86-4d0a-b5f1-3273cca1327f.jpeg)

### Explanation

1. Started with importing `numpy` and `matplotlib.pyplot` modules that are used for working with arrays and graph plotting respectively. 
2. Created the `ndarray` object by passing a `range()` object into the `array()` function, and stored it in a `xpoints` variable. These are the values of parameter x shown on the x-axis.
3. The `range()` takes in 3 arguments: start, stop and (optional) step. As the the range of integers ends at `stop - 1`, therefore it needs to be set to (0,5) in order to stop at 4.   
4. The values of parameter y are depended on the function used. These values are stored under three seperate variables, one for each function. 
5. The `plot()` function is then used to draw points in a diagram. Three plots are drawn, one for each function (f(x), g(x) h(x)). 
6. For each graph, the `plot()` function: takes in the varaibles storing x and y parameters. Additionally `labels` and `colours` of the plot are defined within the `plot()` function. 
7. `\N{SUPERSCRIPT NUMBER}` was used to format the value of the exponent into superscript. 
8. `title()`function allows to set the title for the plot, while `legend()` displays the legend on the plot. 
9. Finally, `show()` function dsiplays the plot. 

### References

1. Programiz (n.d.). *Python range()*. https://www.programiz.com/python-programming/methods/built-in/range
2. StackOverflow (2021). *Printing subscript in Python.* https://stackoverflow.com/questions/24391892/printing-subscript-in-python/24391972#24391972
3. The Matplotlib Developement Team (n.p.). *matplotlib.pyplot* https://matplotlib.org/stable/api/pyplot_summary.html
4. W3Schools (n.p.). *Matplotlib Plotting.* https://www.w3schools.com/python/matplotlib_plotting.asp
5. W3Schools (n.p.). *NumPy Getting Started.* https://www.w3schools.com/python/numpy/numpy_getting_started.asp

##

### Additional References

1. GitHub (n.d.) *Basic writing and formatting syntax.* https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
2. Markdown Guide (n.d.). *Basic Syntax - The Markdown elements outlined in the original design document.* https://www.markdownguide.org/basic-syntax/#overview
3. Van Rossum, G., Warsaw, B., Coghlan, N. (2001). *PEP 8 – Style Guide for Python Code.* https://peps.python.org/pep-0008/![Uploading Figure_1.jpeg…]()


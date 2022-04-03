# Problem Sheet - Weekly Task 03

# Program that asks a user to input a string and outputs every second letter in reverse order.

# Author: Daria Sep

sentence = input('Please enter a sentence: ')
print(sentence [::-2])

# Reversing a string using a slice that steps backwards, -2. There is no built-in function.
# Syntax: slice(start, end, step)
# Ref: https://www.w3schools.com/python/python_howto_reverse_string.asp
# Ref 2: https://www.w3schools.com/python/ref_func_slice.asp
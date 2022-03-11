# Problem Sheet - Weekly Task 05

# Write a program that outputs whether or not today is a weekday.

# Author: Daria Sep

# ref: 
# https://www.geeksforgeeks.org/python-datetime-module/
# https://docs.python.org/3/library/datetime.html?highlight=datetime%20module 


from datetime import date
# Extracing today's date

if date.today().weekday() < 5:
    print('Yes, unfortunately today is a weekday')

# today() - returns the current local date
# weekday() - returns the day of the week as integer where Monday is 0 and Sunday is 6
# for < 5 it's weekday (mon-fri)

else:
    print ('It is the weekend, yay!')


    


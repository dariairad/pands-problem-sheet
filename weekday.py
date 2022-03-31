# Problem Sheet - Weekly Task 05

# Write a program that outputs whether or not today is a weekday.

# Author: Daria Sep


from datetime import date       # Extracting today's date

# today() - returns the current local date.
# weekday() - returns the day of the week as integer where Monday is 0 and Sunday is 6.
# Therefore for int < 5 ie.from 0 to 4, it's a weekday (Mon-Fri).

if date.today().weekday() < 5:
    print('Yes, unfortunately today is a weekday.')
else:
    print ('It is the weekend, yay!')


    


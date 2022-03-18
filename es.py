# Problem Sheet - Weekly Task 07

# Instructions:
# Write a program that reads in a text file and outputs the number of e's it contains. 
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line.



filename = (input('Input filename including directory: ')) # WIP - fix file path input

letter = 'e' # change all letters to lowercase first so Es are counted too. 
# assuming that both are to be counted but included separate numbers in the output message.
letter2 = letter.upper()

def countEs(filename, letter):
    with open(filename) as f:
        text = f.read()
        numberLower = text.count(letter)
        numberUpper = text.count(letter2)    
        totalNumber = numberLower + numberUpper 
        
        return totalNumber

number = countEs (filename, letter)
print (f'This file contains {number} instances of letter "e"')
# RTS Labs Coding Exercise
# Python Version: 3.9.5
# Author: James Overby
# Date: 6/3/2021

# Exercise 1
print("Exercise 1\n")

numbers = []

# While loop to ensure user input for length of array is valid and is not negative.
while True:
    try:
        n = int(input("Enter desired number of elements in array: "))

        if n <= 0:
            print("Value entered is a negative number or equal to zero, please try again!\n")
            continue
        else:
            break

    except ValueError:
        print("Value entered is not valid, please try again!\n")
        continue
    break

# For loop that takes necessary numer of elements to makeup the array
# while also ensuring the input given is valid.
for i in range(0, n):
    while True:
        try:
            element = int(input("Element " + str(i + 1) + ": ")) # Added 1 to i here for easier readability

        except ValueError:
            print("Value entered is not valid element, please try again!\n")
            continue
        break
    numbers.append(element)
    
print() # Print a new line here to seperate inputs

# While loop to ensure that user input is a valid integer.
while True:
    try:   
        user_input = int(input("Enter your value: "))

    except ValueError:
        print("Value entered is not an integer, please try again!\n")
        continue
    break

# Checks the number of values in array that are above user input.
above = sum(i > user_input for i in numbers)

# Subtracts above value from length of array to get the below value.  
below = len(numbers) - above

print("Above: " + str(above) + ", Below: " + str(below))

# -----------------------------------------------------------------------------------------------------------------

# Exercise 2
print("\n\nExercise 2\n")

# While loop to ensure inputted string is not blank and is capable of being rotated.
while True:
    string = input("Enter your desired string: ")
    if string == '' or len(string) <= 2:
        print("You entered nothing or input less than 3 characters, please try again!\n")
        continue
    else:
        break

# Seperate the string into two parts, the first part being the
# string without the last two characters and the second part
# containing the last two characters of the string.
first = string[0 : len(string) - 2]
second = string[len(string) - 2 : ]

print("Here is the string rotated by 2: ", (second + first))

# -----------------------------------------------------------------------------------------------------------------

# Exercise 3

'''
If you could change 1 thing about your favorite framework/language/platform (pick one), what would it be?

One thing that I would change regarding my favorite coding language, Python, would be to fix the incompatibility
between the two versions of Python, Python 2.x and 3.x. My issue with this is that both versions are updated regularly
even though Python 3.x is considered the "up-to-date" and "current" version of Python. I think this leads to unnecessary
amounts of confusion when having to switch between the two versions due to some libraries only being supported by specific
versions. Also the way functions are handles in 3.x are handled differently in 2.x. For example, in Python 2.x "print" is handled
as a statement whereas in Python 3.x it treats "print" as a function. Although this is a simple issue and is easy to fix these
inconsistencies between the two versions add up and it can be increasingly frustrating changing between the two versions.
From my previous experience of having to switch between the two versions it does not take much time for me to get used to the
version I am working with, but it may be more productive to keep one current and updated version of Python to prevent this.

'''

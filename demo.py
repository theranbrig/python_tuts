# Hello World

from random import choice, randint
from random import randint  # |  \
from random import randint
print("Hello World!")
print("Goodbye World!")
print("Goodbye World!")
print(44 + 1)

# Numbers and Math
print(10/5.0)

# Variables
variable_name = 5
print(variable_name + variable_name)
print(variable_name * variable_name)

# Define a variable named city and set it equal to any string
city = "Seoul"
# Define a variable named price and set it equal to any float
price = 3.0
# Define a variable named high_score and set it equal to any int
high_score = 200000
# Define a variable named is_having_fun and set it to a Boolean value
is_having_fun = True


# Escape Characters

new_line = "hi \nthere"
print(new_line)

# Set the message variable equal to any string containing a new-line escape sequence
message = "Hello \nWorld"

# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = "/\\/\\/\\"

# Set the quotation variable to any string that contains an escaped double quotation mark
quotation = "\"Hello\""

str_one = "your"
str_one += " face"
print(str_one)

greeting = "Hello"
name = "Heisenberg"
greet_name = greeting + " " + name

guess = 9
print(f"Your guess of {3 * guess} was incorrect!")

first = "Theran"
last = "Brigowatz"

# Two methods of string interpolation
formatted = "First Name: {}, Last Name: {}".format(first, last)
formatted = f"First Name: {first}, Last Name: {last}"

num = 12
print(type(num))
num = float(num)
print(type(num))
print(num)


# print("What is your name?")
# name = input()

# if name == "Theran":
#     print("You are cool.")
# else:
#     print("You are not cool.")

# NO TOUCHING PLEASE---------------
choice = randint(1, 10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
else:
    print("unlucky")

# NO TOUCHING ======================================
num = randint(1, 1000)  # picks random number from 1-1000
# NO TOUCHING ======================================

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if num % 2 == 0:
    print("even")
else:
    print('odd')
# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])
# if food == "apple" or food == "grape":
#     print("fruit")
# elif food == "bacon" or food == "steak":
#     print("meat")
# else:
#     print("yuck")
# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
x = randint(-100, 100)  # |   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)  # |     NO TOUCHING!!!!!! (please)
y = randint(-100, 100)  # |    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)  # |  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /


# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")

    # NO TOUCHING ======================================


# # randomly assigns values to these four variables
# actually_sick = choice([True, False])
# kinda_sick = choice([True, False])
# hate_your_job = choice([True, False])
# sick_days = randint(0, 10)

# # NO TOUCHING ======================================


# calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# # YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# if (actually_sick and sick_days > 0) or (kinda_sick and hate_your_job and sick_days > 0):
#     calling_in_sick = True
# else:
#     calling_in_sick = False

# # YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

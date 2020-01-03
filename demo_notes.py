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

for x in range(0, 100):
    print(x)
    print(x * x)

for letter in "coffee":
    print(letter)

for num in range(0, 100, 5):
    print(num)

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

for num in range(10, 20):
    if num % 2 != 0:
        x += num
# YOUR CODE GOES HERE:


for num in range(20):
    if num == 7 or num == 4 or num == 13:
        state = "Unlucky"
    elif num % 2 == 0:
        state = "Even"
    else:
        state = "Odd"
    print(f"{num} is {state}")

faces = 1

while faces < 11:
    print("\U0001f600" * faces)
    faces += 1

# print("Hey, How how's it going?")
# print('Pretty good, you?')
# phrase = input()

# while(phrase != "stop copying me"):
#     print(phrase)
#     phrase = input()

# print("UGH FINE. YOU WIN.")

demo_list = ['a', 1.45, 5, True, 'hello']

print(len(demo_list))
r = range(1, 10)
list(r)
print(r[3])
print(r[-1])

# DON'T TOUCH THIS PLEASE!
people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

# Change "Hanna" to "Hannah"
people[0] = "Hannah"

# Change "Geoffrey" to "Jeffrey"
people[-2] = "Jeffrey"

# Change "aparna" to "Aparna" (capitalize it)
people[5] = "Aparna"

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""
for sound in sounds:
    result += sound.upper()


sounds.insert(2, 'super')  # Insert at index
sounds.insert(len(sounds), 'docious')  # Insert at end
sounds.pop()  # Removes last and returns
# sounds.pop(1)  # Removes at index
sounds.index("cali")  # Returns 1 - second argument tells starting index
sounds.count('super')  # Counts number of times it exists
sounds.reverse()  # Updates.  Not immutable practice
sounds.sort()  # Ascending
# " ".sounds.join()  # Concats into string

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")

# Run the tests to make sure you've done this correctly!
# list[start:end:step] :goes to the end - Makes a copy - End is exclusive and does not include the last index.

instructors[::-1]  # Reverses List

# List Comprehension

nums = [1, 2, 3]
new_nums = [x*10 for x in nums]
print(new_nums)

evens = [x for x in nums if x % 2 == 0]
evens = [x for x in nums if x % 2 != 0]
print(evens)

names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]

nums = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in nums if num % 2 == 0]

first = [1, 2, 3, 4]
second = [3, 4, 5, 6]
answer = [x for x in first if x in second]

names = ["Elie", "Tim", "Matt"]
answer2 = [name.lower()[::-1] for name in names]

answer = [num for num in list(range(1, 100)) if num % 12 == 0]

# No Vowels
word = "amazing"
answer = [char for char in word if char not in "aeiou"]

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist['first'] + " " + artist['last']

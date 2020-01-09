# Hello World

import keyword
import math
from random import random
from random import choice  # DON'T CHANGE!
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

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for donation in donations.values():
    total_donations += donation

# This code picks a random food item:
# food = choice(["cheese pizza", "quiche", "morning bun",
#                "gummy bear", "tea cake"])  # DON'T CHANGE!

# # DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant": 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# # YOUR CODE GOES BELOW:
# quantity = bakery_stock.get(food)
# if quantity:
#     print("{quantity} left".format())
# else:
#     print("We don't make that")

# # DO NOT TOUCH game_properties!
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
#                    "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

# # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
# initial_game_state = dict.fromkeys(game_properties, 0)


# inventory = {'croissant': 19, 'bagel': 4,
#              'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!

# # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
# stock_list = inventory.copy()

# # add the value 18 to stock_list under the key "cookie"

# stock_list["cookie"] = 18


# # remove 'cake' from stock_list USE A DICTIONARY METHOD
# stock_list.pop("cake")

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0, 3)}

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# # use the person variable in your answer
# answer = {item[0]: item[1] for item in person}

# # # make sure your solution is assigned to the answer variable so the tests can work!
# # letters = 'aeiou'
# # answer = {letter: 0 for letter in l"aeiou"}

# # ASCII Dictionary
# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {letter: chr(letter) for letter in range(65, 91)}

# # 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
# numbers = (1, 2, 3, 4)

# # 2 - Create a variable called value which is a tuple with the the value 1 inside.
# value = (1,)

# # 3 - Given the following variable:

# values = [10, 20, 30]

# # Create a variable called static_values which is the result of the values variable converted to a tuple

# static_values = tuple(values)

# # 4 - Given the following variable

# stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# # Create a variable called unique_stuff which is a set of only the unique values in the stuff list

# unique_stuff = set(stuff)


def sing_happy_bday():
    print("hbdty")
    print("hbdty")
    print("hbdtdp")
    print("hbdty")


sing_happy_bday()
sing_happy_bday()

# Define your make_noise function below


def make_noise():
    print("THE CROWD GOES WILD")
# Then, call make_noise once:


make_noise()


def flip_coin():
    if random() <= 0.5:
        return "It was heads."
    else:
        return "It was tails"


print(flip_coin())


def speak_pig():
    return 'oink'

# Define a function called generate_evens
# It should return a list of even numbers between 1 and 50(not including 50)


def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]


def yell(string):
    return string.upper() + "!"

# Without adding any new lines of code, make count_dollar_signs work as intended


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count


# Define speak below:
noises = {
    "dog": "woof",
    "pig": "oink",
    "duck": "quack",
    "cat": "meow"
}


def speak(animal="dog"):
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# define product below:


def product(a, b):
    return a * b


days = {1: "Sunday", 2: "Monday", 3: "Tuesday",
        4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}


def return_day(day):
    is_day = days.get(day)
    if is_day:
        return is_day
    else:
        return None


def last_element(arr):
    if arr:
        return arr[-1]
    return None


def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    return "Numbers are equal"

# define single_letter_count below:


def single_letter_count(string, letter):
    return string.lower().count(letter)


'''
multiple_letter_count(
    "awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:


def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}


'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(arr, command, location, value=None):
    if (command == 'remove' and location == 'end'):
        return arr.pop()
    elif (command == 'remove' and location == 'beginning'):
        return arr.pop(0)
    elif (command == 'add' and location == 'end'):
        arr.append(value)
        return arr
    else:
        arr.insert(0, value)
        return arr


'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(phrase):
    return phrase == phrase[::-1]


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


def frequency(arr, value):
    return arr.count(value)


'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(arr):
    total = 1
    for num in arr:
        if num % 2 == 0:
            total = total * num
    return total


'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(string):
    return string[0:1].upper() + string[1::]


'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(arr):
    return [item for item in arr if item]


# flesh out intersection pleaseeeee
def intersection(arr1, arr2):
    return [val for val in arr1 if val in arr2]


'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def partition(arr, callback):
    true_list = []
    false_list = []
    for item in arr:
        if callback(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return [true_list, false_list]


def contains_purple(*args):
    if "purple" in args:
        return True
    return False

# Define combine_words below:


def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

# NO TOUCHING! =================================================================


def count_sevens(*args):
    return args.count(7)


nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23, 34, 45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17,
        11, 7, 11, 8, 4, 6, 2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1, 4, 7)

result2 = count_sevens(*nums)

'''
calculate(make_float=False, operation='add', message='You just added',
          first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide',
          first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), int(operation_value))
    return final


# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
def cube(a): return a**3


lambda a: a**3


def decrement_list(list_var):
    return list(map(lambda x: x - 1, list_var))


def remove_negatives(nums):
    return list(filter(lambda x: x >= 0, nums))

# Implement your is_all_strings function below:


def is_all_strings(var_list):
    return all(type(x) == str for x in var_list)

# Define extremes below:


def extremes(list_val):
    return (min(list_val), max(list_val))


def max_magnitude(list_var):
    return max(list(abs(x) for x in list_var))


def max_magnitude(nums):
    return max(abs(num) for num in nums)


'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)


'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''


def sum_floats(*args):
    return sum(var for var in args if type(var) == float)


def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))


'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct amount of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples

    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"


def divide(a, b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total


'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!


def reverse_string(str):
    # implement your function here
    return str[::-1]


'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(l_var):
    return all(type(l) == list for l in l_var)


'''
remove_every_other([1,2,3,4,5]) # [1,3,5]
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1]
'''


def remove_every_other(lst):
    return [val for i, val in enumerate(lst) if i % 2 == 0]

# Import the math module:


answer = math.sqrt(answer)

# Use math.sqrt  to find the square root of 15129 and save it to variable called answer:


def contains_keyword(*args):
    if any(keyword.iskeyword(arg) for arg in args):
        return True
    return False

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:48:34 2020

@author: crein
"""

VARIABLES

# Define variables by giving them a name and a value

age = 30

# Print their values out by using the print() function

print(age)

# You can print values directly 

print(30)

# But having variables means you can change them after the fact

age = 30
print(age)
age = 40
print(age)

# Variable names can contain letters, numbers, and underscores. However, they cannot start with a number.
# There are some reserved names because Python uses them for other things, like `print`


# Longer variable names are written in snake_case in Python:

friend_age = 23
countries_visited = 90

# Variable names you will never change are written in all uppercase

PI = 3.14159
RADIANS_TO_DEGREES = 180 / PI



NUMBERS

# Two main types of number: whole numbers and floating point numbers
# Also called integers and floats

age = 35  # integer
PI = 3.14159  # float



maths_operation = 1 + 3 * 4 / 2 - 2
print(maths_operation)

# Division always results in a float

float_division = 12 / 3
print(float_division)

# But you can drop everything after the decimal, doing
# "integer division"

integer_division = 12 // 3  # drops anything after the decimal (no rounding, therefore type is int)
print(integer_division)



# Modulo operator for remainder after division
remainder = 12 % 5
print(remainder)  # prints 2



# For every even number, the remainder when divided by 2 is always 0.
# For every odd number, the remainder when divided by 2 is always 1.

# We can check whether a number is odd or even just by checking the remainder!

x = 37
remainder = x % 2
print(remainder)  # should print 1, theref



my_string = "Hello, world!"
single_quote_string = "Hello, world!"

# Strings can use either single or double quotes. 
# pick one and stick to it throughout all your code.


string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing!" yesterday.'

# If your string has quotation marks, make sure to use the other mark for the string itself

escaped_quotes = 'He said "You are amazing!" yesterday.'

# Multi-line strings are useful when you have very long ones and you want to be able to write them a bit more easily.
# Multi-line strings keep the lines in the strings!

multiline = """Hello, world.

My name is Jose. Welcome to my program.
"""
print(multiline)


STRINGS

# You can add strings together to concatenate them (join them together).

name = "Mike"
greeting = "Hello, " + name

print(greeting)

# You cannot add strings and numbers, as that always results in an error:

age = 34
print("You are " + age)

# But you can if you turn the number into a string first:
age = 34
age_as_string = str(34)
print("You are " + age_as_string)



STRING FORMATTING

# You can add strings together to concatenate them (join them together).

name = "Mike"
greeting = "Hello, " + name

print(greeting)

# You can also use f-strings if you are using Python 3.6 or later.
# f-strings don't work in Python 3.5 or earlier.
# In f-strings, {name} gets replaced by the value of the variable name.

another_greeting = f"How are you, {name}?"
print(another_greeting)

# It's also possible to use the format method.

final_greeting = "How are you, {}?".format(name)
print(final_greeting)

# The {} gets replaced by whatever is inside the brackets of the .format()


# You can also give names to variables inside a formattable string:
friend_name = "Danielle"
goodbye = f"Goodbye, {friend_name}!"
print(goodbye)
goodbye_friend = goodbye.format(name=friend_name)
print(goodbye_friend)


# Another example of using `.format()` on a variable:

greeting = "How are you, {}?"
print(greeting.format(name))

# Usually you will be using f-strings, just because they are shorter and more readable.
# However sometimes you may need to re-use a format string, and that is when using .format() is useful.


USER INPUT

"""
We use input() to present the user with a prompt.
They can then type, and when they press Enter everything they typed gets returned.
We can assign that to a variable if we want!
"""

my_name = "Mike"
# your_name = '?'
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}.")

## Calculating months

age = input("Enter your age: ")  # Enter 3
print(
    f"You have lived for {age * 12} months.")
# Prints You have lived for 333333333333 months.
# Must convert our string to a number first.


age = input("Enter your age: ")  # Enter 3
age_num = int(age)
print(
    f"You have lived for {age_num * 12} months."
)  # Prints You have lived for 36 months.

"""
We could do it in one line, a bit more simply.
`age` doesn't need to be a string at any point.
"""

age = int(input("Enter your age: "))  # Enter 3
print(f"You have lived for {age * 12} months.")  # Prints You have lived for 36 months.

"""
A better option would be to create a `months` variable, as that is cleaner to read.
"""

age = int(input("Enter your age: "))  # Enter 3
months = age * 12
print(f"You have lived for {months} months.")  # Prints You have lived for 36 months.



BOOLEANS

"""
A Boolean is a true/false, yes/no, one/zero value.
We can use it to make decisions.
In Python, True and False are keywords to represent these values.
"""

truthy = True
falsy = False

# ----

age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20




"""
Other symbols are > and <=.

Comparing two variables, as below. We ask the user for a number, and check that it matches our 'secret number'.
"""

my_number = 5
user_number = int(input("Enter a number: "))

print(my_number == user_number)
print(my_number != user_number)


# Python has two keywords, `and` and `or`
# Here's how to use them:

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}")




age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65

print(f"At {age}, you are usually not working: {usually_not_working}")

# That could be better re-written to:

age = int(input("Enter your age: "))
usually_working = age > 17 and age < 66  # Notice the changes to the numbers!

print(f"At {age}, you are usually working: {usually_working}")


# How they work internally
# `and` gives you the first value if it is falsy, otherwise gives you the second value
# `or` gives you the first value if it is truthy, otherwise gives you the second value

# How to tell if a value is "truthy" or "falsy"?
# Pass it through `bool()`.

print(bool(35))
print(bool("Mike"))
print(bool(0))
print(bool(""))

# More examples linked in the resources section of the lecture

# --

print("" or "Mike")  # Mike, because "" is falsy
print("Mike" and "Danielle")  # "", because it is falsy

print("Mike" or "")  # "Mike", because it is truthy
print("Danielle" and "")  # "", because it is falsy



LISTS

friend1 = "Danielle"
friend2 = "Bob"
friend3 = "Anne"

friends = ["Danielle", "Bob", "Anne"]

print(friends[0])  # This is called a subscript
print(friends[1])

# You can put anything you like inside a list, but it's almost always a good idea to keep it homogeneous.

friends = ["Bob", 2, "Anne"]  # Generally a bad idea

# -- Length of a list --

friends = ["Bol", "Anne"]
print(len(friends))  # 2

# -- Lists inside lists --
# you can put anything inside a list—and that includes other lists.

friends = [["Danielle", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][1])  # 24
print(friends[1][0])  # Bob

# -- Long lists --

friends = [
    ["Danielle", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 37],
    ["Jen", 25],
    ["Adam", 29],
]

# -- Adding to a list --

friends = ["Rolf", "Bob", "Anne"]
friends.append("Jen")

print(friends)  # ["Rolf", "Bob", "Anne", "Jen"]

# -- Removing from a list --

friends.remove("Bob")
friends.insert(2,'Mike')

print(friends)  # ["Rolf", "Anne", "Jen"]

# Remember if you have a list of lists, for example, you still need the entire thing you want to remove:

friends = [["Danielle", 24], ["Bob", 30], ["Anne", 27]]

friends.remove(["Bob", 30])
friends.sort()



TUPLES

short_tuple = "Ray", "Bob"
a_bit_clearer = ("Ray", "Bob")
not_a_tuple = "Ray"

# -- Adding to a tuple --

friends = ("Ray", "Bob", "Anne")
friends.append("Jen")  # ERROR!

print(friends)  # ["Rolf", "Bob", "Anne", "Jen"]

# -- Removing from a tuple --

friends.remove("Bob")  # ERROR!

print(friends)  # ["Rolf", "Anne", "Jen"]

# Tuples are useful for when you want to keep it unchanged forever.
# Use lists when you specifically want to allow changes.


SETS

# -- Defining sets --

art_friends = {"Bob", "Anne"}
science_friends = {"Jen", "Charlie"}

# -- Adding to a set --

art_friends.add("Jen")

print(art_friends)

# -- No duplicate items --

art_friends.add("Jen")

print(art_friends)  # Same as before, "Jen" was not added twice

# -- Removing from a set --

science_friends.remove("Charlie")

print(science_friends)


art_friends = {"Bob", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

# -- Difference --
# Gives you members that are in one set but not the other.

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

# -- Symmetric difference --
# Gives you those members that aren't in both sets
# Order doesn't matter with symmetric_difference

not_in_both = art_friends.symmetric_difference(science_friends)

print(not_in_both)

# -- Intersection --
# Gives you members of both sets

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# -- Union --
# Gives you all members of all sets,  without duplicates

all_friends = art_friends.union(science_friends)
print(all_friends)


DICTIONARIES


friend_ages = {"Roly": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Roly"])  # 24
# friend_ages["Bob"]  ERROR

# -- Adding a new key to the dictionary --

friend_ages["Bob"] = 20
print(friend_ages)  # {'Roly': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# -- Modifying existing keys --

friend_ages["Roly"] = 25

print(friend_ages)  # {'Roly': 25, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# -- Lists of dictionaries --
# Imagine you have a program that stores information about your friends.
# This is the perfect place to use a list of dictionaries.
# That way you can store multiple pieces of data about each friend, all in a single variable.

friends = [
    {"name": "Ray Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends[0]['name'])

# You can turn a list of lists or tuples into a dictionary:

friends = [("Ray", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)




LENGTH AND SUM


# Imagine you're wanting a variable that stores the grades attained by a student in their class.
# Which of these is probably not going to be a good data structure?

grades = [80, 75, 90, 100]
grades = (80, 75, 90, 100)
grades = {80, 75, 90, 100} # a set allows no duplicates, not a good choice for possible dupicated data


total = sum(grades)
length = len(grades)

average = total / length


JOINING A LIST


# you've got all your friends in a list, and you want to print it out.
friends = ["Roly", "Anne", "Charlie"]
print(f"My friends are {friends}.")

# use `join' to create a string of your friends using a ",":
friends = ["Roly", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")



IF STATEMENT


friend = "Roly"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
else:
    print("Hello, stranger!")


# -- Checking whether the if statement will run --

print(bool(user_name == friend))  # if this is True, the if statement will run

# -- Using the `in` keyword --

friends = ["Roly", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")



WHILE LOOP

# Infinite loop
# When you want to repeat something 
#an undefined number of times.

is_learning = True

while is_learning:
    print("You're learning!")
    


# -- Ending a loop with user input --

user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")



number == 7

while True:
    user_input = input("Would you like to play a game? (Y/n) "))
    
    if user_input == "n":
        break
    
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1")
    else:
        print("Sorry, it's wrong!")
    




FOR LOOP

# -- Repeat once for each element of an iterable --

friends = ["Roly", "Jen", "Anne"]

for friend in friends:
    print(f'{friend} is my friend')


# -- Repeating something 10 times --
# You must create a "list-like" thing containing 10 elements.
# You can do this with a plain list:

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print(index)

# But Python comes with a function `range`which does the same thing and is even more powerful.

for index in range(10):
    print(index)

for index in range(5, 10):
    print(index)

for index in range(2, 20, 3):
    print(index)


# -- Using each value while you iterate --

students = [
    {"name": "Roly", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:  # student is a variable used for iteration
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}.")

# When to use?
# When you want to repeat something a defined number of times.
# For example, once for each element of a list, or even just "10 times"
    
    
# Given a tuple or list:
currencies = 0.8, 1.2
usd, eur = currencies

# -- Destructuring in a loop --
# If you've got a list of lists, such as friend names and ages, you can destructure
# in a loop like this:

#DECONSTRUCTING WITH A LIST OF TUPLES

friends = [("Roly", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:  # for friend in friends first
    print(f"{name} is {age} years old.")

#DECONSTRUCTING WITH A LIST OF LISTS
    
friends1 = [["Roly", 25], ["Anne", 37], ["Charlie", 31], ["Bob", 22]]
for name, age in friends1:  # for friend in friends first
    print(f"{name} is {age} years old.")
    

#ITERATING OVER DICTIONARIES
    
friend_ages = {"Roly": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(name)


for age in friend_ages.values():
    print(age)


for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")
    
    
    
    
#for loop for prime numbers
    
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
            print(f"{n} equals {x} * {n//x}")
            break
    else:  # if n was not divisible by any x, it means it is a prime number.
        print(f"{n} is a prime number.")
    
    
    
    
    
BREAK AND CONTINUE

BREAK
# Breaks out of the loop

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")

CONTINUE
# Terminates the current iteration and moves onto the next one.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue

    print(f"This car is {status}.")
    print("Shipping new car to customer!")
    
    


#ADDING AN ELSE CLAUSE TO A FOR LOOP
# On loops, you can add an `else` clause. This only runs if the loop does not encounter a `break` or an error.
# That means, if the loop completes successfully, the `else` part will run.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")


# Remove the "faulty" and you'll see the `else` part starts running.




LIST SLICING

friends = ["Roly", "Charlie", "Anna", "Bob", "Jen"]

print(friends[2:4])
print(friends[2:])
print(friends[:4])

print(friends[:])

print(friends[-3:])
print(friends[:-2])
print(friends[-3:-1])

# You can slice with tuples and strings as well.




LIST COMPREHENSIONS

numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# -- List comprehension --

numbers = [0, 1, 2, 3, 4]  # list(range(5)) is better
doubled_numbers = [num * 2 for num in numbers]
# [num * 2 for num in range(5)] would be even better.

print(doubled_numbers)

# -- You can add anything to the new list --

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)


# -- This includes things like --
names = ["Roly", "Bob", "Jen"]
lower = [name.lower() for name in names]

# Useful for working with user input.
# By turning everything to lowercase, it's less likely we'll miss a match.

friend = input("Enter your friend name: ")
friends = ["Roly", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"I know {friend}!")
    
    
CONDITIONALS WITH LIST COMPREHENSIONS

ages = [22, 35, 27, 21, 20]
odds = [n for n in ages if n % 2 == 1]

# -- with strings --

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.capitalize() for name in guests if name.lower() in friends_lower
]

# -- nested list comprehensions --
# Below is bad code because it's almost completely unreadable.
# Splitting things out into variables is better.

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = [
    name.capitalize() for name in guests if name.lower() in [f.lower() for f in friends]
]

    

SET AND DICTIONARY COMPREHENSIONS

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.capitalize() for name in friends_lower.intersection(guests_lower)}

print(present_friends)

# Transforming data for easier consumption and processing is a very common task.
# Working with homogeneous data is really nice, but often you can't (e.g. when working with user input!).

# -- Dictionary comprehension --
# Works just like set comprehension, but you need to do key-value pairs.

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)



ZIP FUNCTION
# create a dictionary out of two lists or tuples 
#zip produces a list of tuples

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

# Remember how we can turn a list of lists or tuples into a dictionary?
# `zip(friends, time_since_seen)` returns something like [("Rolf", 3), ("Bob", 7)...]
# We then use `dict()` on that to get a dictionary.

friends_last_seen = dict(zip(friends, time_since_seen))
print(friends_last_seen)




USING RANDOM

import random

value = random.random()# value between 0 and 1
print(value)


value1 = random.uniform(1,10)# random floating point value between 1 and 10
print(value1)

value2 = random.randint(0,1)# random int (inclusive) between 0 and 1, could be used for a coin flip
print(value2)
value3 = random.randint(1,6)# random int (inclusive) between 1 and 6, could be used for a dice throw
print(value3)


greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value4 = random.choice(greetings)# choose a selection from a collection with replacement
print(value4 + ' Mike')


colors = ['Red', 'Black', 'Green']
results = random.choices(colors, weights=[18,18,2], k=10)# returns a list of elements ot total `k` from a collection with replacement
print(results)
# weights = ('Red` 18/38, `Black` 18/38, `Green` 2/38)


deck = list(range(1,53))
print(deck)

random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)#returns a list of elements ot total `k` from a collection without replacement
print(hand)



RANDOM EXAMPLE

first_names = ['John', 'Jane']

last_names = ['Smith', 'Doe']

street_names = ['Main', 'High']

fake_cities = ['Metropolis', 'Eerie']

states = ['AL', 'AK']


for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    
    phone = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
    
    street_num = random.randint(100,999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(1000,99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'
    
    email = first.lower() + last.lower() + '@bogusemail.com'
    
    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')




USING RANDOM, SETS, FOR LOOP 

import random
 
# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))
 
# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
 
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
 
top_player = players[0]  # start by saying "the top matching player is the first one"
 
for player in players:  # Go over each player
    matched_numbers = len(player['numbers'].intersection(lottery_numbers))  # Calculate how many numbers they matched
    if matched_numbers > len(top_player['numbers'].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # Say this player is the new top player
 
# Calculate their winnings using the formula!
winnings = 100 ** len(top_player['numbers'].intersection(lottery_numbers))
 
print('{} won {}.'.format(top_player['name'], winnings))# re-using a formatted string with .format()




FUNCTIONS WITH ARGUMENTS


def calculate_mpg():
    car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")# Print() display data


calculate_mpg()

# But this is not a very reusable function since it only calculates the mpg of a single car.
# Below calculates the mpg of "any" arbitrary car

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}
car1 = {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900}


def calculate_mpg(car_to_calculate):  # This can be renamed to `car`
    mpg = round(car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"],2)
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg(car1)

# This means that given a list of cars with the correct data format, we can run the function for all of them!

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    calculate_mpg(car)




FUNCTIONS THAT RETURN VALUES


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg  # Ends the function, gives back the value


def car_name(car):
    return f"{car['make']} {car['model']}"



v = calculate_mpg(car)





def divide(x, y):
    
    try:
        return round(x/y,3)
    except:
        print('you can\'t divide by 0')



def divide(x, y):

    if y == 0:
        raise ValueError("You tried to divide by zero!")
    else:
        return x / y
    
    
    



DEFAULT ARGUMENTS

def add(x, y=3):  # x=2, y is not OK
    total = x + y
    print(total)


USING NAMED ARGUMENTS WITH DEFAULT ARGUMENTS

add(5)
add(2, 6)
add(x=3)
add(x=5, y=2)

# add(y=2)  # ERROR!
# add(x=2, 5)  # ERROR!


# -- More named arguments --

print(1, 2, 3, 4, 5, sep=" - ")  # default is " "

# You can use almost anything as a default parameter value.
# But using variables as default parameter values is discouraged, as that can introduce difficult to spot bugs

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

default_y = 4
print(default_y)  # 4

add(2)  # 5

"""

Referring to above, using lists or dictionaries as default parameter values  will update
if you modify the original list or dictionary. Unlike integers or strings.
This is due to a language feature called mutability which cause this difference
in thier behavior as compared to integers and strings 

"""



LAMBDA FUNCTIONS


"""
Lambda functions are functions that are almost solely used to get inputs and return outputs.
If you wanted a function that just divided two numbers, that might be suitable for a lambda function.
That's because that function takes inputs, processes them, and returns outputs.

"""

result = (lambda x, y: x + y)(15, 3)
print(result)



LAMBDA VS REGULAR FUNCTIONS


def divide(x, y):
    return x / y

print(divide(15, 3))


divide = lambda x, y: x / y



def average(sequence):
    return sum(sequence) / len(sequence)


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))

# Since the average function just takes inputs and returns an output, we could
# re-define it as a lambda function. 

average = lambda sequence: sum(sequence) / len(sequence)




OBJECT ORIENTED PROGRAMMING

'''unlike dictionaries objects are things that can store both
data and functions that relate to that data.
A class is very similar to the dictionary but it allows you to 
include methods as well that have access to the properties of the object you create'''

#When you have a class, you can create objects using it
class Student:
  def __init__(self, new_name, new_grades):
    self.name = new_name
    self.grades = new_grades
    
  def __len__(self):
      return len(self.grades)
 
  @property # turn the average property into a function
  def average(self): #method is a function that lives in a class
    return sum(self.grades) / len(self.grades)



student_one = Student('Roly Smith', [70, 88, 90, 99]) #these arguments map to the __init__ method in the class
student_two = Student('Jose', [50, 60, 99, 100])


print(student_one.grades)
print(student_one.name)
print(student_one.average)# could also use print(Student.average(student_one))



#from addition import Addition
from Addition import add
 
class Calculator:
    
    @classmethod
    def adds(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from Addition module
   
   
    @classmethod
    def subtract(cls, num1, num2):
        return cls.adds(num1, -num2)     # turn subtraction to adding a negative num2
 
    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num2):
            res = cls.adds(res, num1)    # add num1 for num2 times
        return res
 
    @classmethod
    def divide(cls, num1, num2):
        res = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
            res = cls.adds(res, 1)   # count the times of subtraction as the result
        return res



"""
Given an *iterable* (generally a list, tuple, set, or dictionary; something you can iterate over), `len()` gives you the number of elements. For example:
"""

movies = ['Matrix', 'Finding Nemo']

print(movies.__class__)  # what's this?

count = len(movies)
print(count)  # 2

"""
We can make `len()` work on our classes too, by adding the `__len__` method:
"""

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

ford_garage = Garage()
ford_garage.cars.append('Fiesta')
ford_garage.cars.append('Focus')

print(len(ford_garage))




"""
You can also use square bracket notation in your `Garage`
and now you can iterate over the 
garage using a for loop. To do this you need 
both `__len__` and `__getitem__`

"""

class Garage:
  def __init__(self):
    self.cars = []
    
  def __len__(self):
    return len(self.cars)

  def __getitem__(self, i):
    return self.cars[i]

ford_garage = Garage()
ford_garage.cars.append('Fiesta')
ford_garage.cars.append('Focus')

print(ford_garage[1])  # Focus


for car in ford_garage:
  print(car)
  
  
  


### String representation
"""
If you want to print your objects out (and sometimes during development it can be handy, as we’ll see),
 we can use `__repr__` and `__str__`:

* `__repr__` should be used to print out a string representing the object
 such that with that string you can re-create the object fully.
* `__str__` should be used when printing the object out to a user, 
for example—can be more descriptive or even miss out some details.
"""

class Garage:
  def __init__(self):
    self.cars = []

  def __repr__(self):
    return f'Garage {self.cars}'

  def __str__(self):
    return f'Garage with {len(self.cars)} cars'


garage = Garage()
garage.cars.append('Fiesta')
garage.cars.append('Focus')

print(garage)
print(str(garage))
print(repr(garage))




class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

number = FixedFloat(18.5746)
print(number)  





class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student("Anna", "Oxford")
anna.marks.append(5)
anna.marks.append(15)
anna.average()



# creating another class through inheritance of a parent class(Student)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


roly = WorkingStudent("Roly", "MIT", 15.50)

roly.marks.append(57)
roly.marks.append(99)
print(roly.average())
print(roly.salary)






# property decorator

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)

"""
Now the `average()` function can be used as if it were a property instead of a method; like so:
"""

jose = Student("Jose", "Stanford")
jose.marks.append(80)
jose.marks.append(90)
print(jose.average)

"""
You can do that with any method that doesn’t take any arguments.
But remember, this method only returns a value calculated
from the object’s properties. If you have a method that does
things (e.g. save to a database or interact with other things),
it can be better to stay with the brackets."""
 
''' 
* Brackets: this method does things, performs actions.
* No brackets: this is a value (or a value calculated 
from existing values, in the case of `@property`).
'''


'''
When you call `object.method()`, Python is in the background 
calling `Class.method(object)`, so that `self`
is always the object that called the method. This is an instance method'''

# Now a class method that takes the caller's class as the first argument

class Foo:
  @classmethod
  def hi(cls):
    print(cls.__name__)

my_object = Foo()
my_object.hi()  # prints Foo



## @staticmethod
"""
Takes nothing as the first argument
you're not getting `self` but you can still put the method 
in the class, since it is _related_ to the class.
"""

class Foo:
  @staticmethod
  def hi():
    print("I don't take arguments!")

my_object = Foo()
my_object.hi()


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

static_number = FixedFloat.from_sum(19.575, 0.789)
print(static_number)


# inherited class from FixedFloat
class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self): #this repr method will override parent repr method
        return f'<Euro {self.symbol}{self.amount:.2f}>'

    # Skip defining from_sum as that's inherited

"""
We’ve defined this new class that extends the `FixedFloat ` class. 
It’s got an `__init__` method that calls the parent’s `__init__`, and a 
`__repr__` method that overrides the parents’.
It doesn’t have a `from_sum` method as that’s inherited and we’ll 
just use the one the parent defined.
"""

euros = Euro(18.5963)
print(euros)  # <Euro €18.59>

result = Euro.from_sum(15.76, 19.905)
print(result)  # <FixedFloat 35.66>




'''In order to fix this, we must make the `from_sum` method 
return an object of the class that called it—so that:

* `FixedFloat.from_sum()` returns a `FixedFloat ` object; and
* `Euro.from_sum()` returns an `Euro` object, use a @classmethod'''



class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

"""
When we now call:

* `Euro.from_sum()`, `cls` is the `Euro` class.
* `FixedFloat.from_sum()`, `cls` is the `FixedFloat` class.
"""

result = Euro.from_sum(16.7565, 90)  # <Euro €106.75>
print(result)


#from addition import Addition
from Addition import add
 
class Calculator:
    
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from Addition module
   
   
    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)     # turn subtraction to adding a negative num2
 
    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num2):
            res = cls.add(res, num1)    # add num1 for num2 times
        return res
 
    @classmethod
    def divide(cls, num1, num2):
        res = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
            res = cls.add(res, 1)   # count the times of subtraction as the result
        return res




ERROR HANDLING

# One of Python’s core tenets is: “ask for forgiveness, not for permission”.

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    self.cars.append(car)

"""
We would use these classes in this way:
"""

ford_garage = Garage()
fiesta = Car('Ford', 'Fiesta')

ford_garage.add_car(fiesta)

"""
If we wanted to make sure that we’re only adding `Car` objects to the `Garage`, we could do this:
"""

car = Car('Ford', 'Focus')
if isinstance(car, Car):
  ford_garage.add_car(car)
else:
  print("Your car was not a Car!")


ASKING FOR PERMISSION
"""
if can_call_function():
  call_function()
else:
  say_error_happened()

What we do there is ask for permission (the `can_call_function()` statement).

"""

ASKING FOR FORGIVENESS

"""
Python suggests that, in many cases, our code can be made more readable by asking for forgiveness instead. Doing this (not real Python code):

try to call_function()
if failed:
  say_error_happened
  
"""

You could modify the `add_car()` method to do this:


class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
    self.cars.append(car)

"""
And then we could call it like so:
"""

car = Garage()
try:
  ford_garage.add_car(car)
except TypeError:
  print("Your car was not a Car!")

"""
There are two benefits:

1. Our code reads more nicely: we try to do something that we expect to be able to do, and if we cannot then we say an error happened;
2. Our check for whether it is something we can do is now encapsulated inside the `add_car()` method; we don’t need to have an if statement
every time we want to add a car.

The syntax is the `try-catch` syntax.

We try to do whatever is inside the `try` block, and then if an error happens we jump to the `except` block.
We only do so for errors that match the one in the block (in this case, `TypeError` would be caught, other errors would not be caught).

Catching multiple errors (even though our method won’t raise them):

"""

car = Car('Ford', 'Focus')
try:
  ford_garage.add_car(car)
except TypeError:
  print("Your car was not a Car!")
except ValueError:
  print("Something was wrong with your Car...")




"""
try` and `catch` also have a final counterpart: `finally`.

We can use `finally` to run a block of code no matter what happens: whether or not an exception is raised. For example:
"""

car = Car('Ford', 'Focus')
try:
  ford_garage.add_car(car)
except TypeError:
  print("Your car was not a Car!")
finally:
  print(f"Your garage has {len(ford_garage)} cars.")
  
  
  
RAISING ERRORS

"""
Let’s say you have the following code:
"""

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    print('This method is a work-in-progress.')

"""
We’re working on a class and we’ve not yet got around to implementing the `add_car` method. 
Instead of printing something out, we can raise a `NotImplementedError`.
"""

class Garage:
  def __init__(self):
    self.cars = []
f
  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    raise NotImplementedError("We can't add cars to the garage yet.")

Garage().add_car('Fiesta')  # raises error

"""
That way we can’t call the method and assume it works—it will now fail and crash our program.
We’ll know that we’re doing something that won’t work (because it’s not implemented yet).

That’s how you `raise` an error: use the keyword and create a new error object from the class you want.
All built-in errors are available everywhere for you to use.

Let’s say we’re implementing the method and we want to only allow cars of type `Car`:
"""

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
    self.cars.append(car)

ford_garage = Garage()
fiesta = Car('Ford', 'Fiesta')

ford_garage.add_car(fiesta)  # All good
ford_garage.add_car('Fiesta')  # raises error



CREATING CUSTOM ERRORS

"""
create and raise errors with names you define, as opposed to only using the built-in errors.

to create a custom error, you can do so very easily by subclassing the `Exception` class which means it behaves just like any other error.
"""

class MyCustomError(Exception):
    pass



raise MyCustomError('A message describing the error')

"""
You can create custom errors that have more than just the base `Exception` functionality. 
For example if you wanted to include an error code in your errors, you could do this:
"""

class MyErrorWithCode():
    """Exception raised when a specific error code is needed."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
        
        
raise MyCustomError('A message describing the error', 585)



RE-RAISING EXCEPTIONS AND THE ON SUCCESS BLOCK

"""
It can sometimes be handy to do something with an exception (handle it), but then not silence it.

For example, if an exception is raised in a function and you catch it:
"""

def get_user_score(user):
	try:
	  perform_calculation(user.engagement_metrics)
	except ValueError:
	  print('Incorrect values provided to our calculation function.')

"""
What happens is that the `ValueError` has been silenced. You caught the error, printed something out,
and the program can continue running.

That’s all good, except now whoever called the function `get_user_score()` is not aware that an error happened. 
For example, it could re-try if it did know.

If you want, you can _not silence_ the error. In some cases it can be useful so that the caller function will also receive the error:
"""

def get_user_score(user):
	try:
	    perform_calculation(user.engagement_metrics)
	except KeyError:
	    print('Incorrect values provided to our calculation function.')
	    raise

"""
The `raise` keyword used without an error class after it, just re-raises the exception that was caught in the current `except` block.
"""



"""
You can also do something when an exception *isn’t raised*. That can be useful, for example, to send a notification if the calculation succeeds:
"""

def most_engaged_user(user):
	try:
	    user.score = get_user_score(user)
	except ValueError:
	    print('Failed to get user score.')
	else:
	    if user.score > 500:
	        user.send_engagement_notification()

"""
Note that that’s different than the `finally` block, as it only runs if an exception isn’t raised. 
The `finally` block runs on all cases.

"""



HANDLING USER INPUT ERRORS

def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
        


print(power_of_two())
print(power_of_two())




def interact():
    while True:
        try:
            user_input = int(input('Please input an integer:'))     # try to turn user input into an integer
        except ValueError:
            print('Please input an integer only.')  # print a message if user didn't input an integer
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print even/odd if the user input an integer
        finally:    # regardless of the previous input being valid or not
            user_input = input('Do you want to play again? (y/N):')     # ask if the user wants to play again
            if user_input.lower() != 'y':       # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit





WORKING WITH FILES

my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()




file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')



USING SETS WITH FILES

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()




# read from questions.txt and append each line into a list
questions = open("questions.txt", "r")  # read from questions.txt
 
# read all lines and get rid of line break for each line, then append each stripped line to a list
question_list = [line.strip() for line in questions]
questions.close()
 
score = 0  # initialize score
total = len(question_list)  # set total score
 
for line in question_list:
    # split equation with `=` into question and answer
    q, a = line.split("=")
 
    # print question and wait for user to input their answer
    ans = input(f"{q}=")
 
    if a == ans:  # if user input matches answer
        score += 1  # increase score
 
result = open("result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()






USING THE CSV MODULE WITH FILES


file = open('csv_data.csv', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {universit}')




import csv

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
    ]

def write_to_file(output): # use this syntax if input argument is a list of dicts
    with open("file.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows(output)
        
        
def read_from_file():
    with open("file.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\tDirector: {line['director']}")
            # or return list(reader) to get back a list of ordered dicts
 

          
            
JSON FILES

import json

file = open('tslint.json','r')
file_contents = json.load(file) #json object into a python dict
                json.loads('for a string')

file.close()

print(file_contents)


cars = [
        {'make': 'Ford', 'model': 'Fiesta'},
        {'make': 'Ford', 'model': 'Focus'}
]

file = open('tslint.json', 'w')
json.dump(cars, file)# use json.dumps to turn a python dict into a json object
json.dumps('for a string)
file.close()





my_json_string = '[{"name": "Alfa Romero", "released": 1958}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])




CSV TO JSON CONVERTER

import json
 
json_list = []      # store the converted json data for each line
csv_file = open('csv_file.txt', 'r')
 
for line in csv_file.readlines():
    club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)
 
csv_file.close()
 
json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)     # write json data to a file
json_file.close()



CONTEXT MANAGERS

import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)  # reads file and turns it to dictionary

print(file_contents['friends'][0])


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])




CREATING FILE OPERATIONS MODULES

from ..json_operations import dict_to_json


def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

print(f'file_operations is {__name__}')#







#from addition import Addition
from Addition import add
 
class Calculator:
    
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from Addition module
   
   
    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)     # turn subtraction to adding a negative num2
 
    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num2):
            res = cls.add(res, num1)    # add num1 for num2 times
        return res
 
    @classmethod
    def divide(cls, num1, num2):
        res = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
            res = cls.add(res, 1)   # count the times of subtraction as the result
        return res
    
 
    
   
USING SQLALCHEMY IN PYTHON TO CONNECT TO A  SQLLITE DATABASE

# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())



AUTOLOAD TABLES FROM A DATABASE WITH REFLECTION

# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, MetaData, Table

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

# Print the column names
print(census.columns.keys())
# Print full table metadata
print(repr(metadata.tables['census']))




SELECTING DATA FROM TABLE USING RAW SQL

# Build select statement for census table: stmt
stmt = 'SELECT * FROM census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)



SELECTING DATA FROM TABLE USING SQLALCHEMY

# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
print(connection.execute(stmt).fetchall())





CONNECTING TO A POSTGRESQL DATABASE


# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())



FILTERING DATA FROM A TABLE WITH WHERE()

# Create a select query: stmt
stmt = select([census])

# Add a where clause to stmt filter the results to only those for New York : stmt_filtered
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2000 columns
for result in results:
    print(result.age, result.sex, result.pop2000)


 WITH WHERE AND in_()
# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
    
    
WITH WHERE AND  and_

# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)
    
    
    
ORDERING BY A SINGLE COLUMN

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])


ORDERING A SINGLE COLUMN IN DESCENDING ORDER

# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])



ORDERING BY MULTIPLE COLUMNS

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])



COUNTING DISTINCT DATA

from sqlalchemy import func

# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)


# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())


# Import func
from sqlalchemy import func

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())




SQLALCHEMY RESULT SET INTO A PANDAS DATAFRAME

# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)


# Import pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()



CONNECTING TO MYSQL DATABASE

 Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

# Print the table names
print(engine.table_names())



CALCULATING THE DIFFERENCE BETWEEN TWO COLUMNS

# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt_grouped
stmt_grouped = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt_ordered
stmt_ordered = stmt_grouped.order_by(desc('pop_change'))

# Return only 5 results: stmt_top5
stmt_top5 = stmt_ordered.limit(5)

# Use connection to execute stmt_top5 and fetch all results
results = connection.execute(stmt_top5).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))



DETERMINING AN OVERALL PERCENTAGE

# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([female_pop2000 / total_pop2000 * 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)



AUTOMATIC JOINS WITH AN ESTABLISHED RELATIONSHIP

# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))


USING JOIN

"""
If you aren't selecting columns from both tables or the
two tables don't have a defined relationship, you can 
still use the .join() method on a table to join it with
another table and get extra data related to our query. 

"""

# Build a statement to select the census and state_fact tables: stmt
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
stmt_join = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

# Execute the statement and get the first result: result
result = connection.execute(stmt_join).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))



# Build a statement to select the state, sum of 2008 population and census
# division name: stmt
stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])

# Append select_from to join the census and state_fact tables by the census state and state_fact name columns
stmt_joined = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name)
)

# Append a group by for the state_fact name column
stmt_grouped = stmt_joined.group_by(state_fact.columns.name)

# Execute the statement and get the results: results
results = connection.execute(stmt_grouped).fetchall()

# Loop over the results object and print each record.
for record in results:
    print(record)
    
    
    
    
SELF JOIN TABLES WITH HIERARCHICAL DATA USING ALIAS()

   # Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select names of managers and their employees: stmt
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Match managers id with employees mgr: stmt_matched
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Order the statement by the managers name: stmt_ordered
stmt_ordered = stmt_matched.order_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt_ordered).fetchall()

# Print records
for record in results:
    print(record)
    
    
    
    
USING FUNCTIONS AND GROUPBYS WITH HIERARCHICAL DATA

# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select names of managers and counts of their employees: stmt
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal: stmt_matched 
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name: stmt_grouped
stmt_grouped = stmt_matched.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt_grouped).fetchall()

# print manager
for record in results:
    print(record)


    
WORKING ON BLOCKS OF RECORDS

# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)


CREATING TABLES FROM SCRATCH WITH SQLALCHEMY


# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))



ADDING CONSTRAINTS AND DATA DEFAULTS WHEN CREATING TABLES

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))































GENERATORS IN PYTHON

def hundred_numbers():
  num = 0
  while num < 100:
    yield num
    num += 1

"""
The `yield` keyword is very much like a `return`, 
in that it gives the value back to the caller and 
returns execution control to them (show this with example run).
 However, the next time you run the function, execution
 continues from the very next line inside the function, 
 instead of from the top.
 
 """

GENERATOR COMPREHENSION

hundred_numbers = (n for n in range(100))
print(next(hundred_numbers))
print(next(hundred_numbers))

print(list(hundred_numbers))

"""
Notice that when we do the code snippet above,
 `next()` runs the function once up until the 
 `yield` (which would give you the first value).
 The following `next()` runs it again, which gives 
 you the second value. Then, turning it into a list 
 continues and builds a list from the remaining values.
 
 """
 
 
 
 """
A Generator is an iterator that generates a value from its current state
The below is class which implements `__next__`as if it was 
a function using the `yield` keyword:
"""

class FirstHundredGenerator():
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

gen = FirstHundredGenerator()
next(gen)  # 0


"""
Below is also an iterator that is not a generator because
its gets its values from a list

"""

class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0
    
    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()
            
            
"""
You can iterate over iterables but not
iterators which are used to get the next
value (either from a sequence or generated values)
 
"""

"""
An iterable is an object that has an `__iter__` method defined.
 The `__iter__` method *must return an iterator*.

"""

ITERABLES

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

"""
Now we have an iterable which uses the iterator to get the
next value of the sequence it generates. So now you can do this:
"""

print(sum(FirstHundredIterable()))  # gives 4950

for i in FirstHundredIterable():
    print(i)
 
"""
You can perform iteration over an iterable. An iterable either has:
* `__len__` and `__getitem__` defined; or
* An `__iter__` method that returns an iterator.
If you have either of those two, you have an iterable.

"""


GENERATOR AND AN ITERABLE

"""
You can also make the make the generator an iterator and an iterable
Like Below

"""

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self
    
    
    
    
FILTER() FUNCTION

# filter takes as arguments a function, and an iterable
friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Jary']
start_with_r = filter(lambda x: x.startswith('J'), friends)
print(start_with_r)  # generator!

print(list(start_with_r))
print(list(start_with_r)) # this will not work because the generator has already gone through all its elements
        
        
Basically, using the `filter()` function is identical to this generator expression:

(friend for friend in friends if friend.startswith('R'))

Which is pretty much identical to this function:

def my_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i       
        



MAP() FUNCTION
"""
Used to take an iterable and output a new 
iterable where each element has been modified
according to some function.

"""
friends = ['Ralph', 'Charlie', 'Anna']
friends_lower = map(lambda x: x.lower(), friends)

print(friends_lower)

print(list(friends_lower))


# Same as above but written as list and generator comprehensions
friends_lower = [friend.lower() for friend in friends]

friends_lower = (friend.lower() for friend in friends)




class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# imagine these users are coming from a database...

users = [
    { 'username': 'ralph', 'password': '123' },
    { 'username': 'tsawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)

# Same as above but written as a list comprehension

user_objects = [User.from_dict(u) for u in users]




ANY() AND ALL FUNCTIONS

"""
The `any()` function takes an iterable and returns `True` if any of the elements in it evaluate to `True`
The `all()` function returns `True` if all the elements evaluate to `True`.

"""



friends = [
  {
    'name': 'Rolf',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Anna',
    'location': 'San Francisco'
  },
  {
    'name': 'Charlie',
    'location': 'San Francisco'
  },
  {
    'name': 'Jose',
    'location': 'San Francisco'
  },
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
  print('You are not alone!')
  
  
  
ENUMERATE FUNCTION.
  
top_friends = ['Jose', 'Ralph', 'Anna']

for i, friend in enumerate(top_friends):
    print(f'My top {i+1} friend is {friend}')

"""
The `enumerate()` function takes in a list and outputs a
generator of `(index, element)` tuples—so that each element
of the list is now accompanied by its index in the list.

"""

# This also works
e = enumerate(top_friends)

first_tuple = next(e)
print(first_tuple)  # prints (0, 'Jose')

# Using  tuple destructuring:

i, friend = first_tuple  # i is 0, friend is 'Jose'



FUNCTIONS WITH DEFAULT ARGUMENTS AND TYPE HINTING

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

add_balance(500.00, 'savings')

print(accounts['savings'])  # remember, this has changed because the function mutated the dictionary!

"""
However, what you didn’t know is that you can also have default values for arguments. For example, if you wanted the account name to always be `'checking'` unless otherwise specified, you could do so.
"""

def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

"""
Then you could call the function only with an amount:
"""

add_balance(500.00)  # goes into `'checking'` by default

"""
*Important*: arguments with default values must go after
 arguments without default values. This would be 
 incorrect in Python (type hinting removed to make 
the point):
     
"""


def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders,
    }


a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Anne')






NON DEFAULT MUTABLE AND DEFAULT NON-MUTABLE ARGUMENTS WITH TYPE HINTING

## 1: no default argument
"""
In this option we always must pass in an (empty or otherwise) list to the function call. It makes things explicit, but it means we may require a lot of empty lists being passed in there.
"""

def create_account(name: str, holder: str, account_holders: list):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders,
    }

a1 = create_account('checking', 'Rolf', [])
a2 = create_account('savings', 'Anne', [])

print(a2)

## 2: non-mutable default argument
"""
In this option we have a default value of `None`, so that we don’t 
have to pass a list of account holders.

If it is `None`, we initialise a new list.
"""

def create_account(name: str, holder: str, account_holders = None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders,
    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Anne')

print(a2)




FUNCTION OPERATIONS WITH A LIST OF TRANSACTIONS USING ARGUMENT UNPACKING


accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

"""
Imagine we’ve got a list of transactions that we’ve downloaded from our bank page; and they look somewhat like this:
"""

transactions = [
  (-180.67, 'checking'),
  (-220.00, 'checking'),
  (220.00, 'savings'),
  (-15.70, 'checking'),
  (-23.90, 'checking'),
  (-13.00, 'checking'),
  (1579.50, 'checking'),
  (-600.50, 'checking'),
  (600.50, 'savings'),
]

"""
If we now wanted to add them all to our accounts, we’d do something like this:
"""

for t in transactions:
    add_balance(t[0], t[1])


"""
What we’re doing above is passing all elements 
of an iterable as arguments, one by one.

Whenever you need to do this, there’s a shorthand in Python 
using argument unpacking

"""

for t in transactions:
    add_balance(*t)  
    
    
    

HIGHER ORDER FUNCTIONS

# Functions that accept other functions as parameters and run them inside of their own body

def before_and_after(func):
    print("Before...")
    func()
    print("After...")
    
    
before_and_after(lambda: 5)





def shout(text):  
    return text.upper()  
    
def whisper(text):  
    return text.lower()  
    
# Higher Order function
def greet(func):  
    # storing the function in a variable  
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)   
    
greet(shout)  
greet(whisper)   



movies = [
        {"name": "The Irishman", "director": "Scorsese"},
        {"name": "1917", "director": "Mendes"}]







def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found
        
        
find_by = input("What property are you searching by? ")
looking_for = input("What are you looking for? ")
movie = find_movie(looking_for, lambda movie: movie[find_by])

print(movie or 'No movies found.')
    
    





    
    
    
USING CLASS METHOD FOR UNPACKING VALUES

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# users coming from a database

users = [
    { 'username': 'ralph', 'password': '123' },
    { 'username': 'daytime', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)

"""
Or you can use the list comprehension below:
"""

user_objects = [User.from_dict(u) for u in users]



"""
Instead of having a `from_dict` method in there, we could do this, using named argument unpacking:
"""

USING NAMED ARGUMENT UNPACKING VALUES



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = [User(**data) for data in users]

"""
If our data was not in dictionary format, we could do:
"""

users = [
    ('rolf', '123'),
    ('tecladoisawesome', 'youaretoo')
]

user_objects = [User(*data) for data in users]




QUEUES IN PYTHON

COLLECTIONS

USING COUNTER

# Using a list
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])  # 2


# Using a Dictionary
from collections import Counter

device_temperatures = {'a':13.5, 'b':14.0}

temperature_counter = Counter(device_temperatures)['a']
print(temperature_counter)




USING DEFAULTDICT

## defaultdict
"""
Defaultdict is a container like dictionaries present in the module collections.
 Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
The functionality of both dictionaries and defualtdict are almost same except
for the fact that defualtdict never raises a KeyError. It provides a default value
for the key that does not exist.
"""

alma_maters = {}

for coworker in coworkers:
    if coworker[0] in alma_maters:
        alma_maters[coworker[0]] = []
    alma_maters[coworker[0]].append(coworker[1])


from collections import defaultdict

coworkers = [('Ralph', 'MIT'), ('Jen', 'Oxford'), ('Ralph', 'Cambridge'), ('Charlie', 'Manchester')]  # Rolf got a master's

coworker_alma_maters = defaultdict(list)  # remember list is a function, returns []

for coworker, place in coworkers:
    coworker_alma_maters[coworker].append(place)

print(coworker_alma_maters['Ralph'])
print(coworker_alma_maters['Anne'])  # []

"""
When you need a dictionary and all keys of that dictionary should be associated
with an initial value, use `defaultdict`!

Another example is to initialise places where coworkers work:
"""

from collections import defaultdict

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Ralph', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies['Jen'])  # Teclado
print(coworker_companies['Ralph'])  # Apple Inc.

"""
If you want to change the default value in a `defaultdict`, just change its 
`default_factory` property:
"""

from collections import defaultdict

int_dict = defaultdict(int)

int_dict['first'] += 1
print(int_dict['first'])  # 1

int_dict.default_factory = list
int_dict['second'].append('Rolf')
print(int_dict['second'])  # ['Rolf']

int_dict.default_factory = None  # this is back to being a "normal dictionary"



USING ORDEREDDICT

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 10
o['Jen'] = 3

print(o)  # keys are always in the order in which they were inserted

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)

print(o)

o.popitem()

print(o)



USING NAMEDTUPLE

from collections import namedtuple

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
print(account.name)
print(account.balance)

# Or even print the account itself with a nice __repr__
print(account)

"""
A namedtuple is very much like defining a class (where `Account` is the class or the type)
except its still a tuple.

"""

name, balance = account  # tuple destructuring

Account('checking', balance=1850.90)  # use positional or named arguments


Account._make(('checking', 1850.90))

accounts = [
    ('checking', 1850.90),
    ('savings', 3658.00),
    ('credit', -450.00)
]

account_tuples = map(Account._make, accounts)


account._asdict()  # returns an OrderedDict representing the tuple

"""
Use a namedtuple when you’re dealing with data and it doesn’t warrant creating classes
for the data elements you’re working with.
"""


USING DEQUE

"""
In a `deque`, you can push elements at the start or the end, 
and you can also remove elements from the start or the end.

"""

from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)


MORE EXAMPLES FROM COLLECTION METHODS

from collections import defaultdict, OrderedDict, namedtuple, deque
 
 
def task1() -> defaultdict:
    dd = defaultdict(lambda: 'Unknown')
    dd['Alan'] = 'Manchester'
    return dd
 
 
def task2(arg_od: OrderedDict):
    arg_od.popitem()
    arg_od.popitem(False)
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)
 
 
def task3(name: str, club: str) -> namedtuple:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player
 
 
def task4(arg_deque: deque):
    arg_deque.pop()     # remove last element
    arg_deque.append(arg_deque.popleft())   # remove first element and append it to last
    arg_deque.appendleft('Zack')    # add Zack to start






WORKING WITH DATETIME
"""
The main date and time module in python is called `datetime`, and confusingly enough the main class in that module is also called `datetime`.
"""

from datetime import datetime

print(datetime.now())


"""
Normally I would recommend always working with UTC times—store UTC in your database and work with UTC in your code.

When a user gives you a time, convert it to UTC.

When you show the user a time, convert it to their timezone.

That way, you only have to deal with timezones when you show a time to a user; and you don’t have to work with timezones at any other point in your system.

"""




ADDING AND SUBTRACTING TIMEZONES

from datetime import datetime, timedelta, timezone

today = datetime.now(timezone.utc)
tomorrow_this_time = today + timedelta(days=1)   
print(tomorrow_this_time)                         

                                

FORMATTING TIMES

from datetime import datetime, timezone

today = datetime.now(timezone.utc)
print(today.strftime('%Y-%m-%d %H:%M'))  # string format time





FROM USER INPUT STRING TO DATETIME OBJECT

from datetime import datetime
import pytz
import tzlocal

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)



import datetime

timezone_aware_dt = datetime.datetime.now()(datetime.timezone.utc)



local_timezone = user_date #tzlocal.get_localzone() # get pytz tzinfo
utc_time = local_timezone.utcnow()#datetime.strptime("2011-01-21 02:37:21", "%Y-%m-%d %H:%M:%S")
local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
print(local_time)



from datetime import datetime
import arrow


user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)


#local_timezone = user_date #tzlocal.get_localzone() # get pytz tzinfo
utc_time = local_timezone.utcnow()#datetime.strptime("2011-01-21 02:37:21", "%Y-%m-%d %H:%M:%S")
print(utc_time)

now = datetime.utcnow()
print(now)

print(arrow.get(now).to('local').format())







import pytz, datetime
local = pytz.timezone ("America/Los_Angeles")
naive = datetime.datetime.strptime ("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
local_dt = local.localize(naive, is_dst=None)
utc_dt = local_dt.astimezone(pytz.utc)   





TIMING YOUR CODE


"""
As well as the `datetime` module, used to deal with objects containing both date and time, we have a `date` module and a `time` module.

Whenever you’re running some code, you can measure the start time and end time to calculate the total amount of time it took for the code to run.

"""

import time

def powers(limit):
    return [x**2 for x in range(limit)]

start = time.time()
p = powers(5000000)
end = time.time()

print(end - start)

"""
TURNING THIS INTO A FUNCTION
"""

import time

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(500000))

"""
Notice how the `measure_runtime` call passes a lambda function since the `measure_runtime` function does not allow us to pass arguments to the `func()` call.

This is a workaround to some other technique that we’ll look at very soon.

By the way, the `measure_runtime` function here is a higher-order function; and the `powers` function is a first-class function.


If you want to time execution of small code snippets, you can also look into the `timeit` module, designed for just that: [27.5. timeit — Measure execution time of small code snippets — Python 3.6.4 documentation](https://docs.python.org/3/library/timeit.html)
"""

import timeit

print(timeit.timeit("[x**2 for x in range(10)]")) 
print(timeit.timeit("map(lambda x: x**2, range(10))"))
print(timeit.timeit("filter(lambda x: x*2 < 8, range(10))"))

"""
This runs the statement a default of 10,000 times to check how long it runs for. Notice how `map()` is faster than list comprehension!
"""


  
    
REGULAR EXPRESSIONS


"""

The first thing to understand is that regular expressions are a language. Not a programming language, but a language nonetheless.

There’s a specific syntax and keywords that you can use in regular expressions to express what you want.

We use regular expressions to specify patterns in text

"""



THE MAIN COMPONENTS OF REGEX SYNTAX


* `.`;
* `+`;
* `*`; and
* `?`

The `.` means “anything”; such as a letter, number, symbol, space, etc… *but not newline characters*.

The `+` means “one or more of”. The `*` means “zero or more of”. The `?` means “zero or one of”.

So `.+` means “one or more of anything”. `.*` means “zero or more of anything”. `.?` means “zero or one of anything”.

For the string:


jose@tecladocode.com


`.*` would match the pattern, since it’s “zero or more of anything”.

`Mike@awesomecode\.com` would also match the entire pattern, since it is the pattern. Notice the `\.` so that the `.` doesn’t mean “anything”. With the backslash in front, it matches the actual `.` character.

Next, we have *character sets*. This is a character set: `[abc]`. For this string:

`charlie`, `[abc]` would match the `c` and the `a`. For `Charlie` though it would only match the `a`—these are case sensitive.

Another important one is the *range*. It allows us to define a range of characters, such as a to z: `[a-z]`.

For `jack`, `[a-z]` would match every letter individually.

For `jack`, `[a-z]+` would match as many consecutive set of letters in that range as possible; that’s the entire word.

For `ja.ck`, `[a-z]+` would match twice; `ja`, and `ck`.

Let’s look at the e-mails.


[A-z]+@[a-z]+\.[a-z]+


Of course this one won’t match the periods or the underscores on the e-mail. Let’s fix it:


[A-z\._]+@[a-z]+\.[a-z]+


If instead of matching all TLDs (that’s `net`, `com`, me`) we wanted to match only the ones we’ve seen, we could do:


[A-z\._]+@[a-z]+\.(com|me|net)



"""
Let’s look at how we can extract patterns from text using regular expressions 
in Python with the `re` module.
"""

import re

email = 'mike@home.com'
expression = '[a-z]+'

matches = re.findall(expression, email)# re.findall() returns all non-overlapping matches of pattern in string, as a list of strings
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'
print(name)
print(domain)




import re

email = 'mike@home.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

# btw you could also use the following for the same result:

email = 'mike@home.com'
print(email.split('@'))  # lol


# MORE EXAMPLES

import re

price = 'Price: $189.50'
expression = 'Price: \$(\d+\.\d+)' # \d returns a digit

matches = re.search(expression, price)''' re.search() returns None (if the pattern doesn’t match), or a re.MatchObject that contains
                                          information about the matching part of the string. This method stops after the first match'''
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets



import re

price = 'Price: $11,489.50'
expression = 'Price: \$([\d,]+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets


# turning the string matched into a float
num = '11,489.50'

num = num.replace(',', '')  # replace ',' for ''
print(float(num))





LOGGING FOR DEVELOPERS


"""
The `logging` module is used to print things out (to the console or to a file).

The `logging` module should be used to communicate with the developer (e.g. information about what’s happening; 
when an error happens; a critical problem; etc…).

To communicate with the user, continue using `print()` and `input()`.

"""

import logging

logger = logging.getLogger('test_logger')

logger.info("This won't show up.")
logger.warning('This will.')

"""
There are various logging levels (below in ascending order of criticality), for you to use depending on the circumstance:

DEBUG
INFO
WARNING
ERROR
CRITICAL

Use the `DEBUG` level (`logger.debug('message')`).if you’re logging for help while developing or debugging

Use `logger.critical()` if your program’s about to crash because a critical exception happened;

You can configure the output so all messages are shown, not just warning and above with the following:
"""

logging.basicConfig(level=logging.DEBUG)


# You can configure the output to include more than just the level and the logger used. You can add for example the time:
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)


# Below, an example of configuring  your logger for maximum readability and usefulness.
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',# 8 is for spaces desired, s returns a string, and d returns a number
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger('my_app')
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")


#Sending your applications logs to a file instead of the console:

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

"""
Calling the `logging.getLogger('my_app')` from many different files, always results in the same `Logger` object 
so any configuration changes and the handler added will be reflected throughout all the app.

To use a different name but want the configuration to be kept between handlers, use child handlers:
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('my_app')

another_logger = logging.getLogger('my_app.database')  # gets a child logger called 'database' of 'my_app'




WEB SCRAPING WITH PYTHON

import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1').string) # Returns the contents of the `title` keyword
print(soup.select_one('p a').attrs['href'])# Returns the contents of the `href` keyword within the first `a` of the first `p`

    




FUNCTIONS FOR HTML SCRAPING


from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    print(simple_soup.find('h1').string)


def find_list_items():
    list_items = simple_soup.find_all('li')# Returns all items within 'li` as a list of strings
    list_content = [e.string for e in list_items]
    print(list_content)


def find_paragraph():
    print(simple_soup.find('p', {'class': 'subtitle'}).string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]# Using the get method istead of p.attrs['class'] returns None instead of raising a key error
    print(other_paragraph[0].string)


find_title()
find_list_items()
find_paragraph()
find_other_paragraph()






import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a' # css locator
    item_name = soup.select_one(locator).attrs['title']
    return item_name


def find_item_page_link():
    locator = 'article.product_pod h3 a'
    item_url = soup.select_one(locator).attrs['href']
    return item_url


def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string

    pattern = '£([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    return float(matcher.group(1))''' This returns two groups, group 0 which is the entire thing that matches
                                      and group 1  which is the first group in the parantheses in the `pattern`'''


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_element = soup.select_one(locator)
    classes = star_rating_element.attrs['class']
    #rating_classes = [r for r in classes if r != 'star-rating']
    rating_classes = filter(lambda x: x != 'star-rating', classes)
    return next(rating_classes)


print(find_item_name())
print(find_item_page_link())
print(find_item_price())
print(find_item_rating())

# You can then turn it into a dictionary or whichever
# way is easiest to store and work with:

item = {
    'name': find_item_name(),
    'link': find_item_page_link(),
    'price': find_item_price(),
    'rating': find_item_rating()
}

print(item)

# Of course you could make a class which stores this data and
# has methods to extract it, more on the 'class_html_parsing.py file!






import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''




CREATING A CLASS FOR HTML SCRAPING



class ParsedItem:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """
    
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
        
    @property
    def name(self):
        locator = 'article.product_pod h3 a'
        item_name = self.soup.select_one(locator).attrs['title']
        return item_name
    
    @property
    def link(self):
        locator = 'article.product_pod h3 a'
        item_url = self.soup.select_one(locator).attrs['href']
        return item_url
    
    @property
    def price(self):
        locator = 'article.product_pod p.price_color'
        item_price = self.soup.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = 'article.product_pod p.star-rating'
        star_rating_element = self.soup.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        return next(rating_classes)


item = ParsedItem(ITEM_HTML)
print(item.price())





ASYNCHRONOUS DEVELOPMENT


THREADS


USING THREADING IN PYTHON

import time
from threading import Thread

####### SINGLE THREAD

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO THREADS


# With two threads, we can do them both at once...
thread = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread.start()
thread2.start()

thread.join()
thread2.join()

print('Two thread total time: ', time.time() - start)




USING CONCURRENT.FUTURES FOR THREADING 


import time
from concurrent.futures import ThreadPoolExecutor

####### SINGLE THREAD

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO THREADS


# With two threads, we can do them both at once...
start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(ask_user)

# You don't have to call pool.shutdown() because of the context manager

print('Two thread total time: ', time.time() - start)



MULTIPROCESSING 

USING MULTIPROCESSING


from multiprocessing import Process
import time

####### SINGLE PROCESS

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO PROCESSES


# With two processes, we can do them both at once...
process = Process(target=complex_calculation)
process.start()

start = time.time()

ask_user()

process.join()  # this waits for the process to finish

print('Two process total time: ', time.time() - start)




USING CONCURRENT.FUTURES FOR MULTIPROCESSING

import time
from concurrent.futures import ProcessPoolExecutor

####### SINGLE PROCESS

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO PROCESSES


# With two processes, we can do them both at once...
start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(complex_calculation)

print('Two process total time: ', time.time() - start)




SHARED STATE IN THREADS

from threading import Thread
import time
import random

counter = 0

def increment_counter():
	global counter
	time.sleep(random.randint(0, 2))
	counter += 1
	time.sleep(random.randint(0, 2))
	print(f'New counter value: {counter}')
	time.sleep(random.randint(0, 2))
	print('-----------')



for x in range(10):
	t = Thread(target=increment_counter)
	time.sleep(random.randint(0, 2))
	t.start()






QUEUING IN THREADS WITH SHARED STATE


from threading import Thread
import time
import random
import queue

counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()


def increment_manager():
	global counter
	while True:
		increment = counter_queue.get()  # this waits until an item is available and locks the queue
		time.sleep(random.random())
		old_counter = counter
		time.sleep(random.random())
		counter = old_counter + increment
		time.sleep(random.random())
		job_queue.put((f'New counter value {counter}', '------------'))
		time.sleep(random.random())
		counter_queue.task_done()  # this unlocks the queue


# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=increment_manager, daemon=True).start()



def printer_manager():
	while True:
		for line in job_queue.get():
			time.sleep(random.random())
			print(line)
		job_queue.task_done()

# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=printer_manager, daemon=True).start()


def increment_counter():
	counter_queue.put(1) 
	time.sleep(random.random())


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
	time.sleep(random.random())
	thread.start()

for thread in worker_threads:
	thread.join()  # wait for it to finish

counter_queue.join()  # wait for counter_queue to be empty
job_queue.join()  # wait for job_queue to be empty




USING PYTHON GENERATORS INSTEAD OF THREADS


def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')




YIELDING FROM ANOTHER ITERATOR


from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass


friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
print(next(g))




RECEIVING DATA THROUGH YIELD


from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')





USING THE ASYNC AND AWAIT KEYWORDS


from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)





PYTHON SINGLE ASYNC REQUEST


import aiohttp
import asyncio

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            return response.status

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('http://google.com'))






PYTHON MULTIPLE ASYNC REQUESTS



import asyncio
import aiohttp
import async_timeout
import time

async def fetch_page(session, url):
    async with async_timeout.timeout(10):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':

    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://tecladocode.com/blog'
        ]
        start = time.time()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()























INTERACTING WITH API'S IN PYTHON


import requests

APP_ID = "72dba35060b54cf9ad3ffbdc68de9174"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']

print(f"USD{usd_amount} is GBP{gbp_amount}")




import requests
import functools


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/"

    def __init__(self, app_id):
        self.app_id = app_id
    
    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()
    
    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == 'USD':
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate










USING TKINTER


import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, World!")


root = tk.Tk()
root.title("Hello")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)  # could use side="right"

root.mainloop()





import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, World!")


root = tk.Tk()
root.title("Hello")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)  # could use side="right"

root.mainloop()



import tkinter as tk
from tkinter import ttk


def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()


name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

root.mainloop()



PACKING COMPONENTS IN TKINTER












































    













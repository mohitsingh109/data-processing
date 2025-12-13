# if __name__ == "__main__":
#     print("Hello from basic!")

# print("Hello from basic!")

# Variable (Dynamic Typing)

name = "Mohit"
print(name, type(name))
name = 123
print(name, type(name))

# If Else
age = 18
if age < 18:
    print("You are a minor.")
    print("Enjoy your childhood!")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")

print("I am outside of if-else.")


number = 7

if number > 5 and number % 2 == 1:
    print(f"{number} is greater than 5 and odd.")

if number > 5 or number % 2 == 1:
    print(f"{number} is greater than 5 and odd.")

if not number < 5:
    print(f"{number} is not less than 5.")

# Loops
print("For Loop:")
for i in range(1, 50, 2): # for (int i = 1; i < 5; i++)
    print(i)

# Function

def greet(name):
    return f"Hello, {name}!" #(99.9% ) (f function)

value = greet("Aman")
print(value)

firstname = "John"
lastname = "Doe"

full_name = f"{firstname} {lastname}"
print(full_name)


def dummy(value):
    if value == 1:
        return "Mohit", "Aman"
    elif value == 2:
        return 13.5, 44
    elif value == 3:
        return True, 'A', "Ignore"

    return None # None == Null in java or kotlin

name1, name2 = dummy(1)
print(name1, name2)
num1, _ = dummy(2)

# _ is used to ignore value
_, _, _ = dummy(3)

# List (mutable, sequence of items)
empty_list1 = list()
empty_list = []
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.append("orange")
fruits.remove("Banana")

for fruit in fruits:
    print(fruit)

# tuple (immutable, sequence of items)
empty_tuple1 = tuple()
empty_tuple = ()
days_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday")

for day in days_tuple:
    print(day)


# set (mutable, unordered, unique items)
empty_set1 = set()
empty_set = {}

colors_set = {"Red", "Green", "Blue"}

for color in colors_set:
    print(color)

# Dict (HashMap of java or kotlin (key value pair)) (mutable, unordered, unique keys)
empty_dict1 = dict()
empty_dict = {}

person = {
    "name": ["Mohit", "ABC"],
    "age": 25,
    "city": "New York"
}

person["age"] = 26 # update
person["country"] = "USA" # Insert

for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(f"{key}")

for value in person.values():
    print(f"{value}")

# Module in python (it's plain .py file)
# import math
#
# print(math.sqrt(16))

from math import sqrt
print(sqrt(16))


# __init__, self, decorator, ABC class, index
# pandas, numpy
# sql alchemy
# CSV Module
# Flask
# App Build
# Docker
# k8s
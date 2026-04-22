# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Import the math module and print the value of pi and the square root of 144.
import random
import math as m
import os
import datetime
from random import randint
import math

print(math.pi)
print(math.sqrt(144))

# Q2. From the random module, import only randint and generate a random number between 1 and 100.

num = randint(1, 100)
print("Random number:", num)

# Q3. Import the datetime module and print today's date.

print(datetime.date.today())

# Q4. Use the os module to print your current working directory.

print(os.getcwd())

# Q5. What will this print and why?
print(m.ceil(4.3))  # 5    4.3 → next highest integer → 5
print(m.floor(4.9))  # 4   4.9 → next lowest integer → 4

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q6. Use dir() on the random module and find 3 functions inside it. Then use all 3 of them with examples.

print("Random int:", random.randint(1, 10))

print("Random choice:", random.choice(["apple", "banana", "mango"]))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffled list:", nums)

# Q7. Use the json module to:

# Convert this dictionary to a JSON string → {"name": "Ali", "age": 20}
# Then convert it back to a Python dictionary

import json

data = {"name": "Ali", "age": 20}

json_string = json.dumps(data)
print("JSON string:", json_string)

python_dict = json.loads(json_string)
print("Python dictionary:", python_dict)


# Q8. Use the random module to:

# Create a list ["rock", "paper", "scissors"]
# Shuffle it
# Then pick a random item from it

import random

list = ["rock", "paper", "scissors"]

random.shuffle(list)
print("Shuffled list:", list)

choice = random.choice(list)
print("Random choice:", choice)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================


# Q9. Use sys.argv to write a script that takes a name as a command-line argument and prints "Hello, <name>!". What happens if no argument is given?

import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("⚠️ No name given! Usage: python script.py <your_name>")


# Q10. Use importlib.import_module() to dynamically import the math module using a string variable and then call sqrt(64) from it.

import importlib

module_name = "math"
math = importlib.import_module(module_name)

result = math.sqrt(64)
print(f"Square root of 64 is: {result}")

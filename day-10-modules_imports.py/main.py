# ============================================
# 🐍 Day 10 - Modules & Imports
# 📅 Date: 22/04/2026
# 🎯 Goal: Goal is to understand how Python modules and imports work — how to create my own modules, use built-in ones like math, random, os and datetime, and learn how to import code efficiently using import, from...import, and importlib so that I can write cleaner, more organized, and reusable Python code.
# =============================================

# --- code starts from here ---

# modules
import json
import datetime
import sys
import os
import random
from math import *
from math import sqrt, pi
from math import pi, e
import math as m
import math
import example  # <- example.py

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)


# different ways to use import module


print(pi)
print(e)

# basic import
print(math.pi)
print(math.sqrt(16))

math.floor(4.7)
math.ceil(4.2)
math.pow(2, 10)

# import with alias as
# import numpy as np
# import pandas as pd   # industry standard short names!

#  import specific items with from
print(sqrt(25))  # 5.0  ← no need to write math.sqrt

# import everything with *
print(sin(0))    # works, but pollutes your namespace!

random.randint(1, 10)       # random number 1–10
random.choice(["a", "b", "c"])  # picks random item

os.getcwd()          # current working directory
os.listdir(".")      # list files in folder
os.path.exists("x")  # check if file/folder exists

sys.version          # Python version
sys.argv             # command-line arguments

datetime.date.today()         # today's date
datetime.datetime.now()       # current date + time

json.dumps({"a": 1})   # dict → JSON string
json.loads('{"a":1}')  # JSON string → dict

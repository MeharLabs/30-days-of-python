# ============================================
# 🐍 Day 11 - List Comprehensions
# 📅 Date: 23/04/2026
# 🎯 Goal: 
# =============================================

# --- code starts from here ---

# basic list comprehension syntax
new_list = [expression for item in iterable]

# basic list comprehension
values = []
for x in range(10):
  values.append(x)

# using list comprehension
values = [x for x in range(10)]
print(values)

# comprehension condition
evens = [number for number in range(50) if number % 2 == 0]
print(evens)

# comprehension with multiple conditions
options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = []

valid_string = [
  string
  for string in options 
  if len(string) >= 2 
  if string[0] == "a" 
  if string[-1] == "y"
  ]
print(valid_string)

# multiple list comprehension
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]]

flattened = [num for row in matrix for num in row]
print(flattened)

# if/else in a comprehension
categories = ["Even" if x % 2==0 else "odd" for x in range(10)]
print(categories)

# nested list comprehension
import pprint
printer = pprint.PrettyPrinter()

lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst)

# transformation in comprehension
def square(x):
  return x**2

squared_numbers = [square(x) for x in range(10)]
print(squared_numbers)

# dictionary comprehensions
pairs = [("a",1),("b",2),("c",3)]

my_dict = {k: v for k, v in pairs}
print(my_dict)

# set comprehension
nums = [1,2,2,3,3,3,4,4,4,4]

unique_squares = {x**2 for x in nums}
print(unique_squares)

# generator comprehension
sum_of_squares = sum(x**2 for x in range(1000000))
print(sum_of_squares)
# ============================================
# 🐍 Day 06 - Lists & Tuples
# 📅 Date: 15/04/2026
# 🎯 Goal:
# =============================================

# --- code starts from here ---

# modules
import copy

# create lists
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(fruits)
print(mixed)
print(type(fruits))


# emoty list
empty = []
empty = list()

print(empty)

letters = list("Python")
print(letters)

numbers = list(range(5))
print(numbers)


# nested list
matrix = [["a", "b", "c"],
          ["d", "e", "f"]]

mixed_matrix = [["a", "b"],
                [1, 2, 3],
                [True]]
print(matrix)
print(mixed_matrix)


# indexing & slicing
list = ["a", "b", "c", "d"]

print(list)
print(list[0])
print(list[-1])
print(list[1:])

matrix = [
    ["a", "b", "c"],   # row 1
    ["d", "e", "f"],  # row 2
    ["g", "h", "i"]   # row 3
]

print(matrix[1])
print(matrix[:2])
print(matrix[2][:2])

# unpacking (asterisk * & underscore _)

person = ["Maria", 29, "Software Engineer", "USA"]
name, age, role, country = person
print(name, role, age, country)

name, *details, country = person  # using *
print(name, country, details)

name, _, country, _ = person  # using _
print(name, country)

name, *_, country = person  # using combined *_
print(name, country)


# explore & analyze lists
numbers = [1, 5, 3, 4, 7, 2]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All:", all(["a", "", "b"]))

print("Any:", any(numbers))
print("Any:", any([1, 0, 2]))
print("Any:", any(["a", "", "b"]))
print("Any:", any([0, 0, 0]))

print("Count:", numbers.count(5))
print("Index:", numbers.index(5))

print(4 in numbers)
print(8 not in numbers)

# comparison
list1 = [5, 8, 3]
list2 = [5, 2, 3]
print(list1 < list2)
print(list1 is list2)


# add, remove, update lists

letters = ["a", "b", "c"]

letters.append("d")
letters.insert(0, "x")
letters.remove("a")
letters[0] = "z"

removed = letters.pop(0)
print(letters)


# order the list (sort, sorted, reversed)

list = [0, 5, 4, 8, 1, 2, 3]

list.sort()
list.sort(reverse=True)

print(list)

new_list = sorted(list)
print("Original List:", list)
print("Sorted List:", new_list)

letters = ["c", "a", "b"]
new_list = list(reversed(letters))
print(new_list)

# copy lists safely (shallow vs deep copy)

letters = ["c", "a", "b"]

letters_copy = copy.copy()  # shallow copy
letters_copy = copy.deepcopy(letters)  # deep copy

print("Original List:", letters)
print("Copy List:", letters_copy)

# is operator
original = [["a", "b"],
            ["c", "d"]]

# assignment
copy1 = original
print(original is copy1)

# shallow copy
copy1 = original.copy()
print(original is copy1)

# deep copy
copy1 = copy.deepcopy()
print(original is copy1)

# combine two or more lists
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

combine1 = letters + numbers
combine2 = [letters, numbers]
letters.extend(numbers)
combine3 = list(zip(numbers, letters))

print(combine3)

# Iteratir & Iterable
letters = ["a", "b", "c", "d"]
new_list = []

for l in letters:
    new_list.append(l.upper())
    print(new_list)

# enumerate, reveresed, zip, map, filter
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3]

for index, value in enumerate(letters):
    print(index, value)

for letter in reversed(letters):
    print(letter)

for index, value in zip(letters, numbers):
    print(index, value)

print(list(map(str.upper, letter)))
print(list(map(int, numbers)))

print(list(filter(bool, letters)))

items = ["sql", "123", "python", "42"]
for item in filter(str.isalpha, items):
    print(item)

# list comprehension
domains = ["www.google.com",
           "youtube.com",
           "facebook.com",
           "www.instagram.com"]
cleaned = [d.lower().replace("www", "") for d in domains if "." in d]
print(cleaned)

# tuples
my_list = ("a", "b", "c")

print(my_list)  # ordered # allows duplicates
print(my_list[1]) # indexed
my_list[3] = "d" # Immutable

print(sorted(my_list)) # output: list
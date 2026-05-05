# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Write a lambda function that takes a number and returns its cube.

cube = lambda x: x**3
print(cube(2))

# Q2. Use map() to convert a list of temperatures in Celsius to Fahrenheit.
# celsius = [0, 10, 25, 37, 100]

celsius = [0, 10, 25, 37, 100]

fahrenheit = list(map(lambda c: (9 / 5) * c + 32, celsius))
print(fahrenheit)


# Q3. Use filter() to get only the odd numbers from this list.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q4. Use map() to take a list of names and return them in this format → "Hello, Ali!"
# names = ["Peter", "Sarah", "Emily", "John"]

names = ["Peter", "Sarah", "Emily", "John"]

greetings = list(map(lambda name: f"Hello, {name}!", names))
print(greetings)


# Q5. Use filter() to get only the words that start with a vowel.
# words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]

words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
vowels = ["a", "e", "i", "o", "u"]

vowel_words = list(filter(lambda word: word[0].lower() in vowels, words))
print(vowel_words)


# Q6. Sort this list of tuples by the second element (score) in descending order.
# students = [("Peter", 85), ("Sarah", 92), ("Emily", 78), ("John", 92)]

students = [("Peter", 85), ("Sarah", 92), ("Emily", 78), ("John", 92)]

sorted_students = sorted(students, key=lambda elem: elem[1], reverse=True)
print(sorted_students)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q7. Chain filter() and map() together - filter out negative numbers, then square the remaining ones.

# numbers = [-3, -1, 0, 2, 4, -5, 6]

numbers = [-3, -1, 0, 2, 4, -5, 6]

result = list(map(lambda x: x**2, filter(lambda num: num >= 0, numbers)))
print(result)


# Q8. Sort this list of dictionaries by age (ascending), and if age is the same, sort by name (alphabetically).
# people = [
#     {"name": "Sarah", "age": 25},
#     {"name": "Peter",  "age": 30},
#     {"name": "Emily", "age": 25},
#     {"name": "John", "age": 20}
# ]

people = [
    {"name": "Sarah", "age": 25},
    {"name": "Peter", "age": 30},
    {"name": "Emily", "age": 25},
    {"name": "John", "age": 20},
]

sorted_people = sorted(people, key=lambda val: (val["age"], val["name"]))
print(sorted_people)


# Q9. Use map() + filter() + lambda together to:
# - Take a list of sentences
# - **Keep only sentences longer than 10 characters**
# - **Convert them to UPPERCASE**
# sentences = ["hi", "good morning", "bye", "how are you doing?", "ok"]

sentences = ["hi", "good morning", "bye", "how are you doing?", "ok"]

result = list(map(lambda s: s.upper(), filter(lambda s: len(s) >= 10, sentences)))
print(result)

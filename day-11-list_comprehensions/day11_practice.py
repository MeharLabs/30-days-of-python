# 🐍 Day 11 – List Comprehensions Practice Questions


# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Create a list of the first 10 square numbers using a list comprehension.
# Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = [num**2 for num in range(1, 11)]
print(squares)

# Q2. From this list [3, 7, 2, 9, 4, 11, 6, 8], extract only the numbers greater than 5.
# Expected: [7, 9, 11, 6, 8]

number_list = [3, 7, 2, 9, 4, 11, 6, 8]
expected_list = [num for num in number_list if num > 5]
print(expected_list)

# Q3. Given a list of words `["python", "java", "c++", "javascript"]`, convert all to UPPERCASE.
# Expected: ['PYTHON', 'JAVA', 'C++', 'JAVASCRIPT']

word_list = ["python", "java", "c++", "javascript"]
expected_word_list = [word.upper() for word in word_list]
print(expected_word_list)

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q4. From the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, create a new list that says "even" or "odd" for each number.
# Expected: ['odd', 'even', 'odd', 'even', ...]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expect_new_list = ["even" if num % 2 == 0 else "odd" for num in number_list]
print(expect_new_list)

# Q5. You have a list of names `[" John ", "SARA", "emily ", " Zara"]`. Clean and normalize them — strip spaces and make them Title Case.
# Expected: ['John', 'Sara', 'emily', 'Zara']

names_list = [" John ", "SARA", "Emily ", " Zara"]
expected_name_list = [name.strip().title() for name in names_list]
print(expected_name_list)

# Q6. Flatten this nested list into a single list:
# nested = [[10, 20], [30, 40], [50, 60]]

nested = [[10, 20], [30, 40], [50, 60]]

flatter = [num for row in nested for num in row]
print(flatter)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q7. Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a list of only the cubes of odd numbers.
# Expected: [1, 27, 125, 343, 729]

def cube(num):
    return num ** 3


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected_cube_list = [cube(num) for num in numbers if num % 2 == 1]

print(expected_cube_list)


# Q8. From the sentence "The quick brown fox jumps over the lazy dog", extract all unique words that have more than 3 characters, in lowercase.
# Expected: ['quick', 'brown', 'jumps', 'over', 'lazy']

sentence = "The quick brown fox jumps over the lazy dog"

seen = set()
result = [
    word.lower()
    for word in sentence.split()
    if len(word) > 3 and not (word.lower() in seen or seen.add(word.lower()))
]

print(result)

# **Q9.** Using two lists:
# keys = ["name", "age", "city"]
# values = ["John", 22, "NYC"]

# Create a **dictionary** from them using a comprehension.
# Expected: {'name': 'John', 'age': 22, 'city': 'NYC'}

keys = ["name", "age", "city"]
values = ["John", 22, "NYC"]

expected_result = {k: v for k, v in zip(keys, values)}
print(expected_result)

# ## 🏆 Bonus / Challenge

# Q10. Create a list of all numbers from 1 to 50 that are divisible by both 3 and 5.
# Expected: [15, 30, 45]

number_list = [num for num in range(1, 51) if num%3 == 0 and num%5 ==0
]
print(number_list)

# ============================================
# 🐍 Day 19 - Regex (Regular Expressions)
# 📅 Date: 06/05/2026
# 🎯 Goal: Learn how to use Python's re module to search, extract, validate, and replace text patterns in strings using Regular Expressions.
# =============================================

# --- code starts from here ---

import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input()

if re.search(pattern, user_input):
    print("Valid email")
else:
    print("Invalid email")

# regex methods
# match(): match at the START only

result = re.match(r"Hello", "Hello World")
print(result)
print(result.group())

result2 = re.match(r"World", "Hello World")
print(result2)


# search(): search anywhere in string

result = re.search(r"World", "Hello World")
print(result.group())

result2 = re.search(r"\d+", "My age is 25")
print(result2.group())


# findall(): find ALL matches -> returns a list

emails = "Send to john@gmail.com and sarah@yahoo.com"
result = re.findall(r"\w+@\w+\.\w+", emails)
print(result)

numbers = "Scores: 10, 45, 89, 100"
result2 = re.findall(r"\d+", numbers)
print(result2)


# sub(): replace pattern with something else

text = "My phone is 999-123-4567"
cleaned = re.sub(r"\d", "*", text)
print(cleaned)

messy = "Hello    World   Python"
clean = re.sub(r"\s+", " ", messy)
print(clean)

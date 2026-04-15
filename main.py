# ============================================
# 🐍 Day 05 - Strings
# 📅 Date: 15/04/2026
# 🎯 Goal:
# ============================================

# --- code starts from here ---

# strings
name = "John"
age = 25
greeting = 'Hello, ' + name
multiline = """This is
a multiline string"""

print(name)
print(age)
print(greeting)
print(multiline)

# type(value)
print(type(name))
print(type(age))

# str(value)
print("Your Age is: " + str(age))

# len(value)
password = "pass12345"
print(len(password))

# count(substring)
text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""

print(text.count("Python"))

# replace(old_value, new_value)
price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))

phone_number = "123-456-7890"
print(phone_number.replace("-", " "))

# plus(+) operator
first_name = "Red"
last_name = "John"
full_name = first_name + "-" + last_name
print(full_name)

# f-string (Always use this)
name = "Jane"
age = 35
profession = "CBI"
print(f"Name is {name}, {age} years old, and works with {profession}")

# split(separator)
stamp = "20-03-2026 12:25"
print(stamp.split(" "))

file = "123,CA,USA,25-01-2000,M"
print(file.split(","))

# repetition (*) operator
print("ha"*5)
print("="*30)

# indexes & slicing
text = "Python"

print(text[0:])
print(text[0:4])
print(text[::-1])


date = "15-04-2026"

print(date[0:2])
print(date[0:5])
print(date[-7:-5])


# lstrip() - left strip
text = " Engineering"
print(text.lstrip())

# rstrip() - right strip
text = "Engineering "
print(text.rstrip())

# strip() - left & right strip
text = "  Engineering  "
print(text.strip())

text = "###Something###"
print(text.strip("#"))


# lower()
text = "python PROGRAMMING"
print(text.lower())

# upper()
print(text.upper())


# startswith(substring)
phone = "+12-345-6789"
print(phone.startswith("+"))

# endswith(substring)
email = "john@gmail.com"
print(email.endswith(".com"))

# "substring" in "string"
url = "https://api.company.com/v1/data"
print("api" in url)

# find(substring)
print(phone.find("-"))


# isalpha()
country = "USA"
print(country.isalpha())

# isnumeric()
phone_num = "0123456789"
print(phone_num.isnumeric())

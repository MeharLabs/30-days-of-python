# 🟢 Level 1 — Easy (just getting started)
# =======================================


# Q1. Write a function greet(name) that takes a name and prints:
# Hello, John! Welcome to Python.


def greet(name):
    print(f"Hello, {name}! Welcome to Python")


greet("John")


# Q2. Write a function square(n) that returns the square of a number.
# square(4)  # returns 16
# square(7)  # returns 49


def square(n):
    return n**2


square_output = square(4)
print(square_output)


# Q3. Write a function is_even(n) that returns True if a number is even, False otherwise.
# is_even(4)   # True
# is_even(7)   # False


def is_even(n):
    return n % 2 == 0


print(is_even(3))

# Q4. Write a function calculator(a, b, op) that takes two numbers and an operator (+, -, *, /) and returns the result.
# calculator(10, 5, "+")  # 15
# calculator(10, 5, "/")  # 2.0


def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid operator"


print(calculator(10, 5, "+"))  # 15
print(calculator(10, 5, "/"))  # 2.0

# Q5. Write a function max_of_three(a, b, c) that returns the largest of three numbers without using max().
# max_of_three(3, 9, 5)  # 9


def max_of_three(a, b, c):

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(max_of_three(3, 9, 5))


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================


# Q6. Write a function count_vowels(text) that counts the number of vowels in a string.
# count_vowels("Hello World")  # 3


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))


# Q7. Write a function reverse_string(s) that returns the reversed version of a string without using [::-1].
# reverse_string("Python")  # "nohtyP"


def reverse_string(s):

    rev_str = ""

    for ch in s:
        rev_str = ch + rev_str

    return rev_str


print(reverse_string("Python"))


# Q8. Write a function flatten(nested_list) that takes a nested list and returns a flat list.
# flatten([[1, 2], [3, 4], [5]])  # [1, 2, 3, 4, 5]


def flatten(nested_list):

    flat = []

    for sublist in nested_list:
        for item in sublist:

            flat.append(item)

    return flat


print(flatten([[1, 2], [3, 4], [5]]))

# Q9. Write a function using *args called multiply_all() that multiplies all given numbers together.
# multiply_all(2, 3, 4)   # 24
# multiply_all(1, 5, 10)  # 50


def multiply_all(*args):
    result = 1

    for num in args:
        result *= num

    return result


print(multiply_all(2, 3, 4))

# 🔴 Level 3 — Hard (big brain mode 💀)
# ======================================= 


# Q10. Write a function celsius_to_fahrenheit(c) and another fahrenheit_to_celsius(f). Then write a third function convert(value, unit) that calls one of them based on the unit passed.
# convert(100, "C")   # 212.0
# convert(212, "F")   # 100.0

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
     return (f - 32) * 5/9

def convert(value, unit):
    if unit == "C":
        return celsius_to_fahrenheit(value)
    elif unit == "F":
        return fahrenheit_to_celsius(value)
    else:
        return "Invalid unit"


print(convert(100, "C"))  # 212.0
print(convert(212, "F"))  # 100.0

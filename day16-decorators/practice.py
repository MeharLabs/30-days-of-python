# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. What will this print?


def decorator(func):
    def wrapper():
        print("A")
        func()
        print("C")

    return wrapper


@decorator
def greet():
    print("B")


greet()


# Q2. What is wrong with this decorator?


def my_decorator(func):
    def wrapper(*arg, **kwargs):
        return func(*arg, **kwargs)

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(2, 3))

# *arg, **kwargs were missing
# result: 5


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================


# Q3. What will this print?


def bold(func):
    def wrapper():
        return "**" + func() + "**"

    return wrapper


def upper(func):
    def wrapper():
        return func().upper()

    return wrapper


@bold
@upper
def text():
    return "hello"


print(text())

# result: **HELLO**


# **Q4.** When should you use `@staticmethod` vs `@classmethod`? Give one example use case for each.

"""staticmethod -> “just a function inside a class”"""


class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(5, 3))

# result: 8

"""classmethod -> “function that knows about the class”"""


class User:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_fullname(cls, fullname):
        first_name = fullname.split()[0]
        return cls(first_name)


u = User.from_fullname("John Doe")
print(u.name)

# result: John Doe

# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# **Q5.** Write a decorator called `timer` that prints how long a function takes to run. ⏱️


import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")

        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)
    print("Done!")


slow_function()

# ============================================
# 🐍 Day 04 - Functions
# 📅 Date: 14/04/2026
# 🎯 Goal: Understand and practice Python Functions from scratch, including parameters, arguments, scope, *args, **kwargs, lambda, return values. so I can write clean, reusable, and efficient code like a pro. 💪🐍
# ============================================

# --- code starts from here ---


## Function
def greet():
    print("Hello, World!")


greet()  # Calling the function


## functions with parameters


def greet(name):
    print(f"Hello, {name}!")


greet("John")  # Hello, John!
greet("Sarah")  # Hello, Sarah!


## parameter, global and local variables

case_rule = "n/a"  # global variable


def clean_name(name):  # parameter
    cleaned = name.strip()  # local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned: ", cleaned)


clean_name("Maria")
print(f"The Rule is: {case_rule}")


## positional vs keyword argument


def clean_name(first_name, last_name="n/a", country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = f"{first} {last}"
    print(f"{full_name} from {country}")


# positional arguments
clean_name("Maria", "SMITH", "NYC")

# keyword arguments
clean_name(first_name="Maria", last_name="SMITH", country="NYC")

# mix arguments
clean_name(" Maria ", "SMITH", country="DE")

# default
clean_name("Maria")


## *args vs **kwargs


def total(*args):
    print(sum(args))
total(1, 2)
total(1, 2, 3, 4, 5)


def create_user(**kwargs):
    print(kwargs)
create_user(first_name="Mo", last_name="Salah", age=33, country="Egypt")
create_user(name="Ronaldo", country="Portugal")


## return function


def clean_name(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
    return cleaned
cln_name = clean_name("Maria ")
print(cln_name)

## lambda functions

square = lambda x: x ** 2
print(square(5))  # 25

nums = [1, 2, 3, 4, 5]

# map
squares = list(map(lambda x: x**2, nums))   # [1, 4, 9, 16, 25]

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# zip
names = ["John", "Sarah"]
ages  = [22, 25]
print(list(zip(names, ages)))  # [('John', 22), ('Sarah', 25)]

## functions as First-Class Objects

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, message):
    print(func(message))

speak(shout, "hello")    # HELLO
speak(whisper, "HELLO")  # hello


## docstrings - document your functions!

def add(a, b):
    """
    Adds two numbers and returns the result.
    Parameters: a (int), b (int)
    Returns: int
    """
    return a + b

print(add.__doc__)  # prints the description

## nested functions

def outer():
    print("I'm outer 🏠")

    def inner(): 
        print("I'm inner 🛋️")

    inner()  # called inside outer

outer()
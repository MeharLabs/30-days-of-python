# ============================================
# 🐍 Day 16 - Decorators
# 📅 Date: 30/04/2026
# 🎯 Goal: goal is to understand Python Decorators - how functions are first-class objects, what higher-order functions are, how to write and apply decorators using the @ syntax, how to pass arguments to decorators, and how to use common built-in decorators.
# =============================================

# --- code starts from here ---


# decorators
def decorator_function(original_function):
    def wrapper_function():
        return original_function

    return wrapper_function


def add_sprinkles(func):
    def wrapper():
        print("*You add sprinkles*")
        func()

    return wrapper


def add_fudge(func):
    def wrapper():
        print("*You add fudge*")
        func()

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream():
    print("Here is your ice cream")


get_ice_cream()


# @property decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle. Must be positive"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def diameter(self):
        """Get the diameter of the circle"""
        return self._radius * 2


c = Circle(5)
print(c.radius)
print(c.diameter)


# @staticmethod decorator
class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


print(Math.add(5, 7))
print(Math.multiply(5, 7))


# @classmethod decorator

class Person:
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
      return cls.species

print(Person.get_species())


# @functools decorators
import functools

def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
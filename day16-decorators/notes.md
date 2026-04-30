# 🎨 Day 16 – Decorators in Python

## 🎯 Goal

Understand Python Decorators — how functions are first-class objects, what higher-order functions are, how to write and apply decorators using the `@` syntax, how to pass arguments to decorators, and how to use common built-in decorators.

---

## 🧠 What is a Decorator?

A **decorator** is a function that **wraps another function** to extend or modify its behavior — *without changing its source code*.

Think of it like a **gift wrapper** 🎁 — the gift (function) stays the same, but the wrapper adds something extra around it.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper
```

---

## 1️⃣ Functions as First-Class Objects

In Python, functions are **first-class citizens** — meaning they can be:

- ✅ Assigned to a variable
- ✅ Passed as an argument
- ✅ Returned from another function
- ✅ Stored in a list/dict

```python
def greet():
    return "Hello!"

say_hi = greet          # assigned to variable
print(say_hi())         # Hello!

def run(fn):
    return fn()         # passed as argument

print(run(greet))       # Hello!
```

> 💡 **Tip:** This is the *foundation* of decorators. Without first-class functions, decorators wouldn't exist!

---

## 2️⃣ Higher-Order Functions

A **Higher-Order Function** is a function that either:

- 📥 **Takes** a function as an argument, OR
- 📤 **Returns** a function

```python
# Takes a function
def apply(fn, value):
    return fn(value)

print(apply(str.upper, "hello"))    # HELLO

# Returns a function
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(5))    # 10
```

> 🔥 **Trick:** `map()`, `filter()`, and `sorted()` are all built-in higher-order functions!

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))   # [1, 4, 9, 16, 25]
```

---

## 3️⃣ Basic Decorator Syntax `@`

The `@` symbol is **syntactic sugar** for wrapping a function manually.

```python
# Without @ syntax
def my_decorator(func):
    def wrapper():
        print("🚀 Before")
        func()
        print("✅ After")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)  # manual wrapping
say_hello()
```

```python
# With @ syntax (clean & elegant!)
def my_decorator(func):
    def wrapper():
        print("🚀 Before")
        func()
        print("✅ After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 🚀 Before
# Hello!
# ✅ After
```

### 🛡️ Preserving Function Metadata with `functools.wraps`

```python
import functools

def my_decorator(func):
    @functools.wraps(func)      # 👈 Always use this!
    def wrapper(*args, **kwargs):
        print("Running...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers"""
    return a + b

print(add.__name__)   # add ✅ (without wraps → wrapper ❌)
print(add.__doc__)    # Adds two numbers ✅
```

> ⚠️ **Always use `@functools.wraps`** inside your decorators to preserve the original function's name and docstring!

---

## 4️⃣ Decorator with Arguments

To pass arguments to a decorator, you need **3 levels of nesting** — a decorator factory:

```python
import functools

def repeat(times):                          # Level 1: accepts decorator argument
    def decorator(func):                    # Level 2: accepts the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):       # Level 3: the actual wrapper
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi! 👋")

say_hi()
# Hi! 👋
# Hi! 👋
# Hi! 👋
```

### 🔐 Real-World Example — Role Checker

```python
def require_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError(f"❌ Requires role: {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user, user_id):
    print(f"🗑️ Deleting user {user_id}")

admin = {"name": "Ali", "role": "admin"}
delete_user(admin, 42)      # ✅ Works

guest = {"name": "Bob", "role": "guest"}
delete_user(guest, 42)      # ❌ PermissionError
```

---

## 5️⃣ Common Built-in Decorators

### 🔷 `@staticmethod`

A static method **belongs to the class** but doesn't receive `self` or `cls`. It's just a regular function namespaced inside a class.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathUtils.add(3, 4))      # 7
print(MathUtils.is_even(10))    # True
```

> 💡 Use `@staticmethod` when the method doesn't need access to instance (`self`) or class (`cls`) data.

---

### 🔷 `@classmethod`

Receives the **class itself** as the first argument (`cls`). Often used as alternative constructors.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):     # "Ali-25"
        name, age = data_str.split("-")
        return cls(name, int(age))

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

p = Person.from_string("Ali-25")
print(p)    # Person(Ali, 25)
```

---

### 🔷 `@property`

Turns a **method into a read-only attribute**. Enables getter/setter logic with clean syntax.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("❌ Radius can't be negative!")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)     # 5  (no parentheses needed!)
print(c.area)       # 78.53...
c.radius = 10       # uses setter
c.radius = -1       # ❌ ValueError
```

---

## 🔁 Stacking Multiple Decorators

You can **stack decorators** — they apply **bottom-up**:

```python
@bold
@italic
def greet():
    return "Hello"

# Execution: italic runs first → bold wraps the result
# Output: <b><i>Hello</i></b>
```

> 🧠 The decorator **closest to `def`** runs **first**.

---

## 🛠️ Popular Real-World Decorator Patterns

| Decorator | Purpose |
|---|---|
| `@functools.lru_cache` | ⚡ Memoization / caching results |
| `@functools.cache` | ⚡ Simpler unbounded cache (Python 3.9+) |
| `@dataclasses.dataclass` | 🏗️ Auto-generate `__init__`, `__repr__` etc. |
| `@app.route(...)` | 🌐 Flask/Django URL routing |
| `@pytest.mark.parametrize` | 🧪 Parameterized tests |
| `@abstractmethod` | 🔒 Force subclasses to implement methods |
| `@property` | 🔷 Controlled attribute access |

```python
# ⚡ Memoization example
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))    # Blazing fast! ⚡
```

---

## 📝 What I Learned

- 🔹 **Functions are first-class objects** — they can be assigned to variables, passed as arguments, and returned from other functions
- 🔹 **Higher-order functions** — functions that take or return other functions like `map()`, `filter()` and custom ones
- 🔹 **Decorator basics** — a decorator wraps a function to extend its behavior without changing its source code
- 🔹 **`@` syntax** — it is just clean shorthand for `func = decorator(func)`
- 🔹 **`@functools.wraps`** — always use it inside decorators to preserve the original function's name and docstring
- 🔹 **`*args, **kwargs`** — use them in wrappers so your decorator works with any function signature
- 🔹 **Decorator with arguments** — requires 3 levels of nesting: factory → decorator → wrapper
- 🔹 **Stacking decorators** — you can apply multiple decorators, they execute bottom-up
- 🔹 **`@staticmethod`** — a method that belongs to the class but needs no `self` or `cls`
- 🔹 **`@classmethod`** — receives the class itself as `cls`, commonly used as alternative constructors
- 🔹 **`@property`** — turns a method into a clean attribute-style getter/setter
- 🔹 **`@lru_cache`** — a built-in decorator that caches results for faster repeated calls

---

## 💡 Key Takeaways

- 💡 **Decorators are just functions** — there is nothing magical about them, they are simply functions that wrap other functions
- 💡 **`@` is just sugar** — `@decorator` is exactly the same as writing `func = decorator(func)` manually
- 💡 **Always use `@functools.wraps`** — without it you lose the original function's name and docstring, which causes silent bugs
- 💡 **Always use `*args, **kwargs`** — in your wrapper so the decorator works with any function, not just specific ones
- 💡 **3 levels for argument decorators** — if your decorator needs arguments, you need one extra outer layer as a factory
- 💡 **Order matters when stacking** — decorators apply bottom-up, the one closest to `def` runs first
- 💡 **`@staticmethod` vs `@classmethod`** — static needs nothing, class needs `cls`. Use static for utilities, class for alternative constructors
- 💡 **`@property` is for clean code** — it lets you add validation and logic behind attribute access without changing the interface
- 💡 **Decorators are everywhere** — Flask routes, Django views, pytest, dataclasses all use decorators heavily in real projects

> 🔑 **The biggest takeaway** — once you understand that functions are first-class objects, decorators completely make sense. Everything else follows from that one idea. 🚀

---

## 🗺️ Full Mental Map

```
Decorators
├── 🧱 Built on: First-class functions + Higher-order functions
├── 🎯 Syntax: @decorator (sugar for func = decorator(func))
├── 📦 With arguments: 3-level nesting (factory → decorator → wrapper)
├── 🔁 Stackable: bottom-up application order
└── 🏷️ Built-ins
    ├── @staticmethod   → utility method, no self/cls
    ├── @classmethod    → class-level method, gets cls
    └── @property       → getter/setter as attribute
```

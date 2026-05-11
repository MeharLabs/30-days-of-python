# 🐍 Day 4 — Python Functions

> **Goal:** Understand and practice Python Functions from scratch to advanced, including parameters, arguments, scope, `*args`, `**kwargs`, return values, and lambda — so I can write **clean, reusable, and efficient code** like a pro. 💪

---

## 📖 What is a Function?

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code over and over, you define it once and **call it whenever you need it**.

> Think of it like a **recipe** 🍳 — you write the steps once, and anyone can follow it anytime.

```python
def greet():
    print("Hello, World!")

greet()  # Calling the function
```

`def` is the keyword to **define** a function. The function name is followed by `()` and a colon `:`.

---

## 📦 Parameters vs Arguments

- **Parameter** = the placeholder in the **definition** (when writing the function)
- **Argument** = the actual value you **pass in** when calling it

```python
def greet(name):      # 'name' is a PARAMETER 📋
    print(f"Hello, {name}!")

greet("John")          # "John" is the ARGUMENT 📦
```

> parameter = **empty seat** 💺 | argument = **person sitting in it** 🧍

---

## 🎛️ Default Parameters

Set a **default value** for a parameter in case none is provided.

```python
def greet(name="Stranger"):
    print(f"Hello, {name}!")

greet()         # Hello, Stranger!
greet("Emily")  # Hello, Emily!
```

---

## 🌍 Scope — Local vs Global Variables

| Type | Where it lives | Accessible from |
|---|---|---|
| Local 📦 | Inside the function | Only inside that function |
| Global 🌍 | Outside all functions | Everywhere |

```python
x = "global 🌍"

def my_func():
    x = "local 📦"
    print(x)   # local 📦

my_func()
print(x)       # global 🌍
```

 local = **your room** 🛏️ | global = **the living room** 🛋️


## 📍 Positional vs Keyword Arguments

**Positional** — order matters, Python assigns by position:

```python
def bio(name, age, city):
    print(f"{name}, {age}, from {city}")

bio("Ema", 22, "LA")   # order matters!
```

**Keyword** — you name them so order doesn't matter:

```python
bio(age=22, city="LA", name="Ema")   # same result ✅
```

positional = **assigned seat** 🎟️ | keyword = **pick your own seat** 🪑

---

## 💥 *args vs **kwargs

### 🎒 `*args` — unlimited values → gives a tuple

```python
def add_all(*nums):
    return sum(nums)

add_all(1, 2, 3, 4)   # 10
```

### 🗂️ `**kwargs` — unlimited named values → gives a dict

```python
def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="Ali", city="Lahore", age=22)
```

`*args` = **grab bag** 🛍️ of values | `**kwargs` = **labeled boxes** 📦 with names

---

## 🔁 Return Values

`return` sends a result **back** to the caller. Without it, the function returns `None`.

```python
# ❌ Just prints — can't use the result
def add(a, b):
    print(a + b)

# ✅ Returns — you can store and reuse it
def add(a, b):
    return a + b

result = add(3, 5)
print(result * 10)   # 80
```

**Return multiple values:**

```python
def stats(nums):
    return min(nums), max(nums), sum(nums)

lo, hi, total = stats([1, 2, 3, 4, 5])
# 1, 5, 15
```

no `return` = function gives `None` back = **left on read** 📵

---

## 🧬 Lambda Functions

A **one-liner** anonymous function, great for quick operations.

```python
square = lambda x: x ** 2
print(square(5))   # 25
```

**With `sorted()`:**

```python
people = [{"name": "Emily", "age": 25}, {"name": "Sarah", "age": 19}]
sorted_people = sorted(people, key=lambda p: p["age"])
# Sarah (19) comes first ✅
```

**With `map()` and `filter()`:**

```python
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, nums))          # [1, 4, 9, 16, 25]
evens   = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
```

---

## 🧰 Functions By Purpose

| Type | Description | Example Name |
|---|---|---|
| 🔧 Do-Something | Performs action, no return | `log_message()` |
| 🧮 Calculate & Return | Takes input, returns result | `calculate_tax()` |
| ✅ Validator | Returns `True` / `False` | `is_even()`, `has_vowel()` |

---

## 🧰 Useful Built-in Functions

| Function | What it does |
|---|---|
| `len()` | 📏 Length of an object |
| `range()` | 🔢 Generates a range of numbers |
| `map()` | 🗺️ Applies a function to every item |
| `filter()` | 🔍 Filters items based on a condition |
| `zip()` | 🤐 Combines two iterables |
| `sorted()` | 🔃 Returns a sorted list |
| `enumerate()` | 🔖 Adds index to iteration |

---

## 🧠 Docstrings — Document Your Functions!

```python
def add(a, b):
    """
    Adds two numbers and returns the result.
    Parameters: a (int), b (int)
    Returns: int
    """
    return a + b

print(add.__doc__)  # prints the description
```

---

## 💡 Tips & Tricks

- ✅ **One function = one job** — keep functions focused and small
- ✅ Use **descriptive names** — `calculate_tax()` beats `ct()`
- ✅ Always add a **docstring** for functions others will use
- ✅ Prefer `return` over `print()` inside functions — more reusable!
- ✅ Use **default parameters** to make functions flexible
- ⚠️ Avoid using too many **global variables** — leads to bugs
- ⚠️ Watch your **indentation** — Python is strict about it!
- 🔥 **Lambda** is great for short, throwaway logic — don't overuse it
- 🔥 Master `map()`, `filter()`, `zip()` — super powerful with functions

---

## 🔑 Key Takeaways

1. **Functions = Reusability** 🔁 — write once, use forever
2. **Parameters ≠ Arguments** 📋 — parameter is the placeholder, argument is the actual value
3. **Scope is Real** 🗺️ — local dies inside the function, global lives everywhere
4. **\*args & \*\*kwargs = Flexibility** 🎒 — handle unknown number of inputs
5. **Always Return, Don't Just Print** 🎁 — `return` lets you USE the result
6. **Lambda = Quick One-Liners** ⚡ — great inside `sorted()`, `map()`, `filter()`
7. **One Function, One Job** 🎯 — if it does too many things, split it up!

---
# Day 18 - Lambda & Map/Filter in Python 🐍✨

## 🎯 Goal

Lambda functions and Map/Filter in Python — learning how to write concise anonymous functions with `lambda`, transform data using `map()`, filter data using `filter()`, sort smartly with `sorted(key=)`, and know exactly when to use lambda versus a regular function.


## 🔷 What is a Lambda Function?

A **lambda** is an **anonymous (nameless) function** defined in a single line. Think of it as a quick, throwaway function you create on the spot — no `def`, no `return`, just pure logic in one expression.

> 💡 **Analogy:** If a regular function is a full meal you cook at home, a lambda is a quick snack you grab on the go!


## 1️⃣ Lambda Syntax

```python
lambda arguments: expression
```

### Regular Function vs Lambda 🔄

```python
# Regular function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x

print(square(5))  # 25
```

### Multiple Arguments 🔢

```python
add      = lambda x, y: x + y
multiply = lambda x, y, z: x * y * z

print(add(3, 5))          # 8
print(multiply(2, 3, 4))  # 24
```

### With Conditional (Ternary) Logic 🔀

```python
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
absolute = lambda x: x if x >= 0 else -x

print(even_odd(4))   # Even
print(absolute(-9))  # 9
```

### ⚠️ Rules to Remember

| ✅ CAN do              | ❌ CANNOT do           |
|------------------------|------------------------|
| Single expression      | Multiple statements    |
| Conditionals (ternary) | `if/elif/else` blocks  |
| Call other functions   | `for` / `while` loops  |
| Return any value       | `return` keyword       |

---

## 2️⃣ `map()` Function 🗺️

`map()` applies a function to **every item** in an iterable and returns a map object.

```python
map(function, iterable)
```

### Basic Example

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

### Multiple Iterables 🔗

```python
a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))
print(result)  # [11, 22, 33]
```

### Real-World Use Cases 🌍

```python
# 1. Convert types
str_nums = ["1", "2", "3", "4"]
integers = list(map(int, str_nums))           # [1, 2, 3, 4]

# 2. Celsius → Fahrenheit
celsius    = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0]

# 3. Capitalize names
names  = ["ali", "sara", "john"]
capped = list(map(str.upper, names))          # ['ALI', 'SARA', 'JOHN']

# 4. Strip whitespace from strings
dirty = ["  hello ", " world "]
clean = list(map(str.strip, dirty))           # ['hello', 'world']
```

---

## 3️⃣ `filter()` Function 🔍

`filter()` **keeps only the items** for which the function returns `True`.

```python
filter(function, iterable)
```

### Basic Example

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens   = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]
```

### Real-World Use Cases 🌍

```python
# 1. Filter positive numbers
nums      = [-3, -1, 0, 2, 5, -7, 9]
positives = list(filter(lambda x: x > 0, nums))        # [2, 5, 9]

# 2. Filter long strings
words      = ["hi", "hello", "hey", "howdy", "yo"]
long_words = list(filter(lambda w: len(w) > 3, words)) # ['hello', 'howdy']

# 3. Filter None / Falsy values
data  = [0, 1, None, 2, "", 3, False, 4]
clean = list(filter(None, data))  # [1, 2, 3, 4]  ✨ no lambda needed!

# 4. Filter passing students
students = [{"name": "Ali", "grade": 45}, {"name": "Sara", "grade": 80}]
passed   = list(filter(lambda s: s["grade"] >= 50, students))
```

### `map()` vs `filter()` at a Glance 👀

| Feature          | `map()`              | `filter()`           |
|------------------|----------------------|----------------------|
| Purpose          | **Transform** items  | **Select** items     |
| Output size      | Same as input        | ≤ input size         |
| Function returns | Transformed value    | `True` / `False`     |

---

## 4️⃣ `sorted()` with `key` 🔡

`sorted()` can take a `key=` argument — a function that tells Python **what to sort by**.

```python
sorted(iterable, key=function, reverse=False)
```

### Sort by Different Criteria

```python
# 1. Sort by string length
words = ["banana", "apple", "kiwi", "mango"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'mango', 'banana']

# 2. Sort by absolute value
nums = [-10, 3, -2, 7, -5]
print(sorted(nums, key=lambda x: abs(x)))
# [-2, 3, -5, 7, -10]

# 3. Sort list of dicts by a field
people = [
    {"name": "Ali",  "age": 25},
    {"name": "Sara", "age": 20},
    {"name": "Zaid", "age": 30}
]
by_age  = sorted(people, key=lambda p: p["age"])
by_name = sorted(people, key=lambda p: p["name"])

# 4. Sort by multiple criteria (tuples!)
students = [("Ali", 85), ("Sara", 92), ("Zaid", 85)]
result   = sorted(students, key=lambda s: (-s[1], s[0]))
# Sort by grade DESC, then name ASC
```

---

## 5️⃣ When to Use Lambda ✅❌

### ✅ USE Lambda When...

```python
# 1. Short, one-time-use logic
nums = [3, 1, 4, 1, 5]
nums.sort(key=lambda x: -x)           # Sort descending

# 2. As an argument to higher-order functions
result = list(map(lambda x: x * 2, range(5)))

# 3. Simple conditional transformation
grade = lambda score: "Pass" if score >= 50 else "Fail"
```

### ❌ AVOID Lambda When...

```python
# ❌ Complex multi-step logic — use def instead
process = lambda x: x**2 if x > 0 else abs(x) * 3 + len(str(x))  # 😵 unreadable!

# ✅ Much better as a regular function
def process(x):
    if x > 0:
        return x ** 2
    return abs(x) * 3 + len(str(x))

# ❌ Assigning and reusing by name (defeats the purpose)
double = lambda x: x * 2   # Why not just def double(x)?

# ❌ When you need docstrings or testing
# lambdas can't have docstrings!
```

> 📏 **Golden Rule:** Use lambda when the logic fits **naturally in one line** and is used **in-place**. The moment you feel the urge to add a comment explaining your lambda — switch to `def`. 🎯

---

## 🧰 Other Related Tools & Methods

```python
# ─── functools ────────────────────────────────
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  # 120

# ─── zip() + map() combo ──────────────────────
names    = ["Ali", "Sara"]
scores   = [90, 85]
combined = list(map(lambda n, s: f"{n}: {s}", names, scores))
# ['Ali: 90', 'Sara: 85']

# ─── List Comprehension (often cleaner!) ──────
squares = [x**2 for x in range(5)]               # vs map
evens   = [x for x in range(10) if x % 2 == 0]  # vs filter

# ─── any() / all() ────────────────────────────
nums = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in nums))  # True
print(any(x > 7 for x in nums))       # True

# ─── dict.get() as a key trick ────────────────
order        = {"banana": 2, "apple": 1, "kiwi": 3}
fruits       = ["banana", "apple", "kiwi"]
sorted_fruits = sorted(fruits, key=order.get)
# ['apple', 'banana', 'kiwi']
```

---

## 💡 Pro Tips & Tricks

🔹 **Tip 1 — Negate for reverse sort without `reverse=True`**
```python
data = [3, 1, 4, 1, 5]
data.sort(key=lambda x: -x)   # [5, 4, 3, 1, 1]
```

🔹 **Tip 2 — Chain `map` + `filter` together**
```python
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
# [0, 4, 16, 36, 64]
```

🔹 **Tip 3 — Use `operator` module instead of simple lambdas**
```python
from operator import itemgetter
people       = [{"name": "Ali", "age": 25}, {"name": "Sara", "age": 20}]
sorted_people = sorted(people, key=itemgetter("age"))  # cleaner than lambda!
```

🔹 **Tip 4 — `filter(None, list)` removes all falsy values instantly**
```python
clean = list(filter(None, [0, 1, "", "hi", None, [], [1, 2]]))
# [1, 'hi', [1, 2]]
```

🔹 **Tip 5 — Lambdas work great inside dictionaries (dispatch tables)**
```python
ops = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
}
print(ops["add"](3, 4))  # 7
print(ops["mul"](2, 5))  # 10
```

---

## 🗺️ Quick Reference Cheat Sheet

```
lambda x: x * 2                      → anonymous function
map(fn, iterable)                     → transform every item
filter(fn, iterable)                  → keep items where fn = True
sorted(data, key=lambda x: x[1])     → sort by custom rule
reduce(lambda x, y: x + y, data)     → fold list into one value
filter(None, data)                    → remove falsy values
```

---

## 📚 What I Learned

- **Lambda** is an anonymous one-line function using the syntax `lambda arguments: expression`
- **`map()`** applies a function to every item in a list and transforms it
- **`filter()`** keeps only the items where the function returns `True`
- **`sorted(key=)`** lets you sort by any custom rule using a lambda
- Lambda **cannot** have multiple statements, loops, or a `return` keyword
- **`filter(None, list)`** instantly removes all falsy values from a list
- **`reduce()`** from `functools` folds an entire list into a single value
- **`map()` + `filter()`** can be chained together for powerful one-liners
- Use lambda for **short, in-place, one-time logic** only
- Switch to **`def`** when logic is complex or needs to be reused
- **`operator.itemgetter()`** is a cleaner alternative to lambda for sorting dicts
- Lambdas work great inside **dictionaries as dispatch tables**

---

## 🎯 Key Takeaways

- ⚡ **Lambda = anonymous function** — no name, no `def`, just quick inline logic
- 🗺️ **`map()` = Transform** — changes every item, output size stays the same
- 🔍 **`filter()` = Select** — picks items, output size shrinks or stays same
- 🔡 **`sorted(key=)` = Custom Sort** — sort by anything using a lambda rule
- 🔗 **Chaining** `map()` + `filter()` together creates powerful one-liners
- 📏 **One expression only** — lambda can't handle complex multi-step logic
- 🧹 **`filter(None, list)`** is the quickest way to clean falsy values
- ⚙️ **`reduce()`** is the third musketeer alongside `map()` and `filter()`
- 🏆 **`operator.itemgetter()`** beats lambda when sorting lists of dictionaries
- 🎯 **Use lambda** when logic is short, simple, and used only once in-place
- 🚫 **Avoid lambda** when you need loops, multiple lines, or reusability
- 📖 **Readability wins** — if your lambda needs a comment, write a `def` instead

---

> 🏁 **Summary:** Lambda is your Swiss Army knife for quick inline functions. Pair it with `map()`, `filter()`, and `sorted()` to write expressive, clean Python — but always remember: **readability first!** When a lambda starts looking like a puzzle, reach for `def`. 🧠
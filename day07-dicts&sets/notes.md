# 📘 Day 7 – Dictionaries & Sets in Python


## 🎯 Goal
Understand how to store & organize data using Dictionaries and Sets — and know when to use which one.


## 🗂️ What is a Dictionary?

A **dictionary** is an **unordered, mutable** collection that stores data as **key-value pairs**. Think of it like a real-world dictionary — you look up a **word (key)** to find its **meaning (value)**.

```python
student = {
    "name": "John",
    "age": 20,
    "city": "NYC"
}
```

- 🔑 Keys must be **unique** and **immutable** (strings, numbers, tuples)
- 📦 Values can be **anything** (lists, dicts, functions, etc.)
- ✅ Ordered since **Python 3.7+** (insertion order is preserved)


## 🔧 Dictionary Methods

| Method | Description | Example |
|---|---|---|
| `.get(key)` | Get value safely (no error if missing) | `d.get("age")` |
| `.keys()` | Returns all keys | `d.keys()` |
| `.values()` | Returns all values | `d.values()` |
| `.items()` | Returns key-value pairs | `d.items()` |
| `.update({})` | Merge another dict in | `d.update({"x": 1})` |
| `.pop(key)` | Remove & return a key | `d.pop("age")` |
| `.popitem()` | Remove last inserted item | `d.popitem()` |
| `.setdefault(k, v)` | Set key only if it doesn't exist | `d.setdefault("age", 0)` |
| `.clear()` | Empty the dictionary | `d.clear()` |
| `.copy()` | Shallow copy | `d2 = d.copy()` |

```python
person = {"name": "Sara", "age": 25}

print(person.get("salary", "Not Found"))  # Not Found
print(person.keys())    # dict_keys(['name', 'age'])
print(person.items())   # dict_items([('name', 'Sara'), ('age', 25)])

person.update({"city": "NYC"})
print(person)  # {'name': 'Sara', 'age': 25, 'city': 'NYC'}
```


## 🔁 Looping Through a Dictionary

```python
data = {"a": 1, "b": 2, "c": 3}

# Loop keys
for key in data:
    print(key)

# Loop values
for val in data.values():
    print(val)

# Loop both 🔥
for key, val in data.items():
    print(f"{key} → {val}")
```


## ⚡ Dictionary Comprehension

```python
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```


## 🧠 Nested Dictionaries

```python
students = {
    "Ali":  {"age": 20, "grade": "A"},
    "Sara": {"age": 22, "grade": "B"},
}

print(students["Ali"]["grade"])  # A
```


## 💡 Dict Tips & Tricks

```python
# ✅ Merge two dicts (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2  # {'a': 1, 'b': 2}

# ✅ Check if key exists
if "name" in person:
    print("Key found!")

# ✅ Default value with get()
count = {}
count["apple"] = count.get("apple", 0) + 1

# ✅ Invert a dictionary
original = {"a": 1, "b": 2}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}

# ✅ Sort dict by value
scores = {"Ali": 90, "Sara": 75, "Zara": 95}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
```


## 🟣 What is a Set?

A **set** is an **unordered, mutable** collection of **unique elements**. It automatically removes duplicates! Think of it like a bag where every item can only appear **once**.

```python
fruits = {"apple", "banana", "mango", "apple"}
print(fruits)  # {'apple', 'banana', 'mango'} ← duplicate removed!
```

- 🚫 No duplicates allowed
- 🔀 Unordered (no index access)
- ✅ Great for membership testing & math operations


## 🔧 Set Methods

| Method | Description |
|---|---|
| `.add(x)` | Add a single element |
| `.update([])` | Add multiple elements |
| `.remove(x)` | Remove element (error if missing) |
| `.discard(x)` | Remove element (no error if missing) |
| `.pop()` | Remove a random element |
| `.clear()` | Empty the set |
| `.copy()` | Shallow copy |
| `.union(s)` | All elements from both sets |
| `.intersection(s)` | Only common elements |
| `.difference(s)` | Elements in A but not B |
| `.symmetric_difference(s)` | Elements not in both |
| `.issubset(s)` | Check if subset |
| `.issuperset(s)` | Check if superset |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))                # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))         # {3, 4}
print(a.difference(b))           # {1, 2}
print(a.symmetric_difference(b)) # {1, 2, 5, 6}
```


## ➕ Set Operators (Shorthand)

```python
a | b   # Union        ∪
a & b   # Intersection ∩
a - b   # Difference   −
a ^ b   # Symmetric Difference
```


## ⚡ Set Comprehension

```python
squares = {x**2 for x in range(1, 6)}
# {1, 4, 9, 16, 25}
```

---

## 🧊 Frozen Set (Immutable Set)

```python
fs = frozenset([1, 2, 3])
# fs.add(4)  ❌ Error — can't modify!
# Use as dict keys or inside other sets ✅
```

---

## 💡 Set Tips & Tricks

```python
# ✅ Remove duplicates from a list instantly
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))

# ✅ Fast membership test (much faster than list!)
big_set = {i for i in range(1_000_000)}
print(999999 in big_set)  # ✅ Lightning fast ⚡

# ✅ Find common items between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)  # {3, 4}

# ✅ Check for unique-only differences
missing = set(list1) - set(list2)  # {1, 2}
```


## 🆚 Dict vs Set — Quick Comparison

| Feature | Dictionary 🗂️ | Set 🟣 |
|---|---|---|
| Stores | Key-value pairs | Single values |
| Ordered | ✅ (Python 3.7+) | ❌ |
| Duplicates | Keys must be unique | No duplicates |
| Access | By key | No index access |
| Use case | Mapping/lookup | Uniqueness/math ops |
| Syntax | `{"key": val}` | `{val1, val2}` |

---

## ✅ What I Learned Today

### 🗂️ Dictionaries
- A dictionary stores data as **key-value pairs**
- Keys are **unique & immutable**, values can be anything
- Ordered since **Python 3.7+**
- Methods like `.get()`, `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`
- How to **loop** through keys, values, and both
- **Dictionary comprehension** `{k: v for ...}`
- **Nested dictionaries** for complex data
- Tricks like merging with `|`, inverting, sorting by value

### 🟣 Sets
- A set stores **unique values only** — no duplicates!
- **Unordered** — no index access
- Methods like `.add()`, `.remove()`, `.discard()`, `.update()`
- Math operations — **union, intersection, difference, symmetric difference**
- Shorthand operators `|`, `&`, `-`, `^`
- **Set comprehension** `{x for ...}`
- **Frozenset** — immutable version of a set
- Using sets to **remove duplicates** from a list instantly

### 🆚 Dict vs Set
- Dict = **key → value** | Set = **unique values**
- Both use `{}` but sets have **no colons**
- Empty set must be `set()` not `{}` ⚠️

---

## 🔑 Key Takeaway

### 🗂️ Dictionary
- Key-value pairs — every value has a **label**
- Keys are unique, values can be anything
- Access data by **key**, not index
- Best for — user profiles, word counters, mappings

### 🟣 Set
- Stores **unique values only** — no duplicates ever
- Unordered — no index access
- Best for — removing duplicates, finding common items
- Supports math ops — union, intersection, difference

### ⚠️ Never Forget
- `{}` = empty **dict** — use `set()` for empty set
- Both use `{}` but sets have **no colons**
- Sets are **faster** than lists for membership testing

### 💡 When to Use What
- Storing labeled data → **Dict** 🗂️
- Need only unique values → **Set** 🟣
- Counting frequency → **Dict** 🗂️
- Finding common elements → **Set** 🟣

---

## 🚀 Simple Rule — Labels? Dict. Unique? Set!
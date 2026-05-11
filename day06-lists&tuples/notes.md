# 🐍 Day 6 — Lists & Tuples

## 📋 What is a List?

A **List** is an ordered, mutable (changeable) collection of items. It can hold anything — numbers, strings, other lists, mixed types — all in one place.

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
```

🔑 **Key traits:** Ordered • Mutable • Allows duplicates • Uses square brackets `[ ]`

---

## 📦 What is a Tuple?

A **Tuple** is an ordered, immutable (unchangeable) collection. Once created, you can't add, remove, or change its items.

```python
coordinates = (10, 20)
rgb = (255, 0, 128)
```

🔑 **Key traits:** Ordered • Immutable • Allows duplicates • Uses parentheses `( )`


## 🎯 Goal

Master **Lists & Tuples** — understand the difference, practice the most important methods.


## ⚔️ List vs Tuple — Quick Comparison

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[ ]` | `( )` |
| Mutable? | ✅ Yes | ❌ No |
| Faster? | Slower | ✅ Faster |
| Use case | Dynamic data | Fixed data |
| Methods | Many | Few |

---

## 🛠️ List Methods

```python
my_list = [3, 1, 4, 1, 5, 9]
```

| Method | What it does | Example |
|---|---|---|
| `.append(x)` | Adds item to the end | `my_list.append(2)` |
| `.insert(i, x)` | Inserts at position `i` | `my_list.insert(0, 99)` |
| `.extend([x])` | Adds multiple items | `my_list.extend([7, 8])` |
| `.remove(x)` | Removes first match | `my_list.remove(1)` |
| `.pop(i)` | Removes & returns item at `i` | `my_list.pop(2)` |
| `.sort()` | Sorts in-place | `my_list.sort()` |
| `.reverse()` | Reverses in-place | `my_list.reverse()` |
| `.count(x)` | Counts occurrences | `my_list.count(1)` |
| `.index(x)` | Returns first index of `x` | `my_list.index(5)` |
| `.copy()` | Returns a shallow copy | `my_list.copy()` |
| `.clear()` | Removes all items | `my_list.clear()` |

---

## 🛠️ Tuple Methods

Tuples only have **2 built-in methods** (because they're immutable):

```python
t = (1, 2, 3, 2, 2)

t.count(2)   # → 3   (counts how many times 2 appears)
t.index(3)   # → 2   (returns index of first occurrence of 3)
```

---

## 🔍 Indexing & Slicing (works on both!)

```python
data = [10, 20, 30, 40, 50]

data[0]      # → 10        (first item)
data[-1]     # → 50        (last item)
data[1:3]    # → [20, 30]  (slice from index 1 to 2)
data[::-1]   # → [50, 40, 30, 20, 10]  (reversed!)
```

---

## 🔄 Looping Through Lists & Tuples

```python
fruits = ["apple", "banana", "cherry"]

# Basic loop
for fruit in fruits:
    print(fruit)

# With index using enumerate() 🌟
for i, fruit in enumerate(fruits):
    print(f"{i} → {fruit}")
```

---

## 🎨 List Comprehensions (Super Powerful! ⚡)

A clean, one-line way to build lists:

```python
# Normal way
squares = []
for x in range(5):
    squares.append(x ** 2)

# ✨ List comprehension way
squares = [x ** 2 for x in range(5)]
# → [0, 1, 4, 9, 16]

# With a condition
evens = [x for x in range(10) if x % 2 == 0]
# → [0, 2, 4, 6, 8]
```

---

## 📦 Useful Built-in Functions

```python
nums = [3, 1, 4, 1, 5, 9]

len(nums)      # → 6              (number of items)
sum(nums)      # → 23             (total sum)
min(nums)      # → 1              (smallest)
max(nums)      # → 9              (largest)
sorted(nums)   # → [1,1,3,4,5,9]  (returns NEW sorted list)
list(range(5)) # → [0,1,2,3,4]    (range → list)
```

---

## 🔗 Tuple Unpacking 🌟

One of the coolest tuple features:

```python
point = (10, 20)
x, y = point      # Unpacking!
print(x)  # → 10
print(y)  # → 20

# Swap variables in one line! 🤯
a, b = 5, 10
a, b = b, a
print(a, b)  # → 10 5
```

---

## 💡 Tips & Tricks

🔹 **Use a tuple when data shouldn't change** — coordinates, RGB values, days of the week. It's safer and faster.

🔹 **`sorted()` vs `.sort()`** — `sorted()` returns a *new* list, `.sort()` modifies the original. Don't mix them up!

🔹 **Avoid `list.copy()` pitfalls** — it's a *shallow* copy. Nested lists inside still share the same reference.

🔹 **Single-item tuple needs a comma:**
```python
not_a_tuple = (5)    # ❌ This is just an int!
is_a_tuple  = (5,)   # ✅ This is a tuple
```

🔹 **Convert between them freely:**
```python
my_list  = list((1, 2, 3))   # tuple → list
my_tuple = tuple([1, 2, 3])  # list  → tuple
```

🔹 **Check membership with `in`:**
```python
"apple" in ["apple", "banana"]  # → True ✅
```

---

## 🧠 Summary Cheatsheet

```
List   → [ ]  → mutable   → use when data changes
Tuple  → ( )  → immutable → use when data is fixed
Both   → ordered, indexed, allow duplicates, sliceable
```

---

## ✅ Key Takeaways

🔹 **Lists** are mutable — you can change them anytime using `[ ]`

🔹 **Tuples** are immutable — fixed data, faster, safer using `( )`

🔹 **Indexing & Slicing** works on both — `data[0]`, `data[-1]`, `data[1:3]`

🔹 **List methods** like `.append()`, `.remove()`, `.sort()`, `.pop()` are your best friends

🔹 **Tuple unpacking** is powerful — `x, y = (10, 20)` 🤯

🔹 **List comprehensions** keep your code clean and short — `[x**2 for x in nums]`

🔹 A **single-item tuple** needs a comma — `(5,)` not `(5)` ⚠️

🔹 Use `sorted()` for a **new list**, `.sort()` to modify the **original**

🔹 When data **shouldn't change** → use a Tuple. When it **should** → use a List
# 🐍 Day 11 – List Comprehensions

## 🎯 Goal

**Understand List Comprehensions deeply** — know *what* they are, *why* they exist, and *when* to use them over a regular loop.


## 📖 What is a List Comprehension?

A **List Comprehension** is a concise, elegant way to **create a new list** from an existing iterable (like a list, range, string, tuple, etc.) — all in **a single line of code**.

Instead of writing a full `for` loop to build a list, you can compress it into one readable expression.

### 🔷 Basic Syntax:
```python
new_list = [expression for item in iterable]
```

### 🔁 For Loop vs List Comprehension:
```python
# Traditional for loop
squares = []
for x in range(5):
    squares.append(x ** 2)

# ✅ List Comprehension (same result!)
squares = [x ** 2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]
```

---

## 🧱 Core Structure Breakdown

```python
[expression   for item in iterable   if condition]
#   ↑               ↑                     ↑
# What to add   Loop variable         Optional filter
```

---

## 🔥 Types & Variations

### 1️⃣ Basic
```python
names = ["ali", "sara", "umar"]
upper = [name.upper() for name in names]
# ['ALI', 'SARA', 'UMAR']
```

### 2️⃣ With `if` Condition (Filtering)
```python
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
# [2, 4, 6]
```

### 3️⃣ With `if-else` (Inline Ternary)
```python
result = ["even" if n % 2 == 0 else "odd" for n in range(6)]
# ['even', 'odd', 'even', 'odd', 'even', 'odd']
```

### 4️⃣ Nested List Comprehension
```python
matrix = [[j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

### 5️⃣ Flattening a Nested List
```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in nested for x in row]
# [1, 2, 3, 4, 5, 6]
```

### 6️⃣ With Strings
```python
sentence = "hello world"
vowels = [ch for ch in sentence if ch in "aeiou"]
# ['e', 'o', 'o']
```

### 7️⃣ With `enumerate()`
```python
fruits = ["apple", "banana", "cherry"]
indexed = [(i, f) for i, f in enumerate(fruits)]
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### 8️⃣ With `zip()`
```python
names = ["Ali", "Sara"]
scores = [90, 85]
paired = [(n, s) for n, s in zip(names, scores)]
# [('Ali', 90), ('Sara', 85)]
```

### 9️⃣ With `range()`
```python
cubes = [x**3 for x in range(1, 6)]
# [1, 8, 27, 64, 125]
```

### 🔟 With Functions
```python
def double(x):
    return x * 2

result = [double(n) for n in range(5)]
# [0, 2, 4, 6, 8]
```

---

## 🛠️ Methods You Can Use ON the Result

| Method | Example | Result |
|--------|---------|--------|
| `.append()` | `lst.append(99)` | Adds item |
| `.sort()` | `lst.sort()` | Sorts in-place |
| `.reverse()` | `lst.reverse()` | Reverses in-place |
| `.count(x)` | `lst.count(2)` | Counts occurrences |
| `.index(x)` | `lst.index(4)` | Finds index |
| `.remove(x)` | `lst.remove(3)` | Removes first match |
| `len()` | `len(lst)` | Length of list |
| `sum()` | `sum(lst)` | Sum of elements |
| `min/max()` | `max(lst)` | Min/max value |
| `sorted()` | `sorted(lst)` | Returns new sorted list |

```python
result = sorted([x**2 for x in range(5)], reverse=True)
# [16, 9, 4, 1, 0]
```

---

## 🧠 Comprehension Family (Not Just Lists!)

```python
# 📋 List Comprehension → returns list
[x for x in range(5)]

# 🔢 Set Comprehension → returns set (no duplicates)
{x for x in [1, 1, 2, 3]}

# 📚 Dict Comprehension → returns dictionary
{k: v for k, v in zip("abc", [1,2,3])}

# ⚡ Generator Expression → memory efficient (lazy)
(x**2 for x in range(100))
```

---

## 💡 Tips & Tricks

**✅ Tip 1 – Transform data quickly**
```python
prices = [100, 200, 300]
discounted = [p * 0.9 for p in prices]
```

**✅ Tip 2 – Remove duplicates with Set Comprehension**
```python
words = ["hi", "hello", "hi", "hey"]
unique = {w for w in words}
```

**✅ Tip 3 – Filter + Transform in one go**
```python
data = [" Ali ", " ", "Sara", "  "]
clean = [d.strip() for d in data if d.strip()]
# ['Ali', 'Sara']
```

**✅ Tip 4 – Walrus operator `:=` (Python 3.8+)**
```python
results = [y for x in range(10) if (y := x**2) > 10]
# [16, 25, 36, 49, 64, 81]
```

**✅ Tip 5 – Readable over clever**
```python
# ❌ Hard to read
res = [x for x in [y**2 for y in range(10)] if x % 2 == 0]

# ✅ Break it up
squares = [y**2 for y in range(10)]
evens = [x for x in squares if x % 2 == 0]
```

---

## ⚠️ Common Mistakes

```python
# ❌ Wrong if-else placement
[x if x > 0 for x in nums]      # SyntaxError!

# ✅ Correct: if-else goes BEFORE for
[x if x > 0 else 0 for x in nums]

# ❌ Over-nesting (unreadable)
[[[...]]]   # Just use a loop at this point 😅
```

---

## ⚡ Performance Note

```python
# List — stores everything in memory
big = [x**2 for x in range(1_000_000)]

# Generator — computes on the fly 💚
big = (x**2 for x in range(1_000_000))
```

> 🚀 Use **generator** `()` over **list** `[]` for large datasets to save memory!

---

## 🗂️ Quick Reference Card

```
[expr for item in iterable] → basic
[expr for item in iterable if cond] → filter
[expr1 if cond else expr2 for item in iter] → ternary
[expr for a in iter1 for b in iter2] → nested
```

---

## 📝 What I Learned

- 📖 What a List Comprehension is and why we use it
- 🔷 Basic syntax — `[expression for item in iterable]`
- 🔍 Filtering with `if` condition
- ↔️ Inline `if-else` (ternary) inside comprehensions
- 🔁 Nested list comprehensions
- 📐 Flattening a nested list
- 🛠️ Methods you can use on the result (sort, reverse, len, sum etc.)
- 🧠 The full comprehension family — List, Set, Dict & Generator
- ⚡ Performance tip — generators over lists for large data
- ⚠️ Common mistakes to avoid


## 🏁 Key Takeaways

- 🚀 List Comprehensions are **faster & cleaner** than regular for loops
- 📝 One line can replace **4-5 lines** of traditional loop code
- 🎯 `if` for filtering, `if-else` for transforming — know the difference in placement
- 🧠 Not just lists — **Set, Dict & Generator** comprehensions exist too
- ⚡ For **large data**, always prefer a **generator** `()` over a list `[]` to save memory
- ✅ Readable code > Clever code — **don't over-nest** comprehensions
- 🔗 The result is just a list — all **list methods work** on it normally

🧠 **Remember:** List Comprehensions = **Readable + Fast + Pythonic!**
> When in doubt, ask: *"Can I say this in plain English as one sentence?"* — If yes, a comprehension fits perfectly. 🎯
# 🐍 Day 5 — Python Strings


## 📖 What is a String?

A **String** is a sequence of characters enclosed in quotes. It can contain letters, numbers, symbols, and spaces. In Python, strings are **immutable** — once created, they can't be changed in place.

```python
name = "Python"
greeting = 'Hello, World!'
multiline = """This is
a multiline string"""
```

💡 You can use single `' '`, double `" "`, or triple `''' '''` / `""" """` quotes!

---

## 📅 Goal

**Today's goal is to fully understand and practice Python Strings by going through all the concepts, methods, and tricks, then solving practice questions so that by the end of the day you can confidently manipulate strings, use methods like `.split()`, `.join()`, `.replace()`, and format strings using f-strings without any help! 💪🔥**

---

## 📚 Topics Covered


## 🧱 String Basics

```python
s = "Hello, Python!"

print(len(s))        # 14 — length of string
print(s[0])          # 'H' — indexing (starts at 0)
print(s[-1])         # '!' — negative indexing (from end)
print(s[0:5])        # 'Hello' — slicing
print(s[::2])        # every 2nd character
print(s[::-1])       # reverse the string ✨
```

---

## 🔧 String Methods

### ✂️ Case Methods

| Method | What it does |
|---|---|
| `s.upper()` | ALL CAPS |
| `s.lower()` | all lowercase |
| `s.title()` | Title Case |
| `s.capitalize()` | First letter capital |
| `s.swapcase()` | sWAP cASE |

### 🔍 Search & Check Methods

| Method | What it does |
|---|---|
| `s.find("lo")` | Returns index of first match, or `-1` |
| `s.index("lo")` | Like find but raises error if not found |
| `s.count("l")` | Count occurrences |
| `s.startswith("He")` | Returns `True`/`False` |
| `s.endswith("!")` | Returns `True`/`False` |
| `"ello" in s` | Returns `True` ✅ |

### 🧹 Clean-up Methods

| Method | What it does |
|---|---|
| `s.strip()` | Remove spaces from both ends |
| `s.lstrip()` | Remove from left only |
| `s.rstrip()` | Remove from right only |
| `s.replace("old", "new")` | Replace substring |

### ✂️ Split & Join

```python
s = "apple,banana,mango"
fruits = s.split(",")        # ['apple', 'banana', 'mango']

words = ["Hello", "World"]
result = " ".join(words)     # "Hello World" 🔗
```

### 🔲 Padding & Alignment

```python
s = "hi"
s.center(10, "-")   # '----hi----'
s.ljust(10, ".")    # 'hi........'
s.rjust(10, ".")    # '........hi'
s.zfill(5)          # '000hi'  (zero-fill)
```

### ✅ Validation Methods

| Method | Returns `True` if... |
|---|---|
| `s.isalpha()` | only letters |
| `s.isdigit()` | only digits |
| `s.isalnum()` | letters or digits |
| `s.isspace()` | only whitespace |
| `s.isupper()` | all uppercase |
| `s.islower()` | all lowercase |

---

## 🎨 String Formatting

### 1️⃣ f-strings (Modern & Recommended ✅)

```python
name = "John"
age = 20
print(f"My name is {name} and I am {age} years old.")
print(f"2 + 2 = {2 + 2}")           # expressions work too!
print(f"{3.14159:.2f}")             # format decimals → 3.14
```


## ⚡ Tips & Tricks

**🔁 Repeat a string:**
```python
print("ha" * 3)       # 'hahaha'
print("-" * 30)       # a nice divider line ----
```

**🔗 Concatenation:**
```python
first = "Hello"
second = "World"
print(first + " " + second)   # 'Hello World'
```

**🔄 String is iterable:**
```python
for char in "Python":
    print(char)       # prints each letter one by one
```

**🧮 Check membership:**
```python
print("Py" in "Python")    # True ✅
print("py" in "Python")    # False ❌ (case-sensitive!)
```

**🪄 Escape characters:**

| Code | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

```python
print("Line1\nLine2")     # prints on two lines
print("Name:\tJohn")       # tab spacing
```

**🔤 Raw strings (ignore escape):**
```python
path = r"C:\Users\new_folder"    # r prefix = raw string
print(path)   # C:\Users\new_folder  ✅
```

---

## 🧠 Quick Summary

| Concept | Key Point |
|---|---|
| 📦 Definition | Sequence of characters in quotes |
| 🔒 Immutable | Can't modify in place, create new instead |
| 🔢 Indexing | Starts at `0`, negative from end |
| ✂️ Slicing | `s[start:stop:step]` |
| 🎨 Formatting | f-strings are the modern best practice |
| 🔧 Methods | `.upper()`, `.split()`, `.strip()`, `.replace()` and many more |

---

## 🧪 What I Built / Practiced

- 📖 Definition of Strings
- 🔢 Indexing & Slicing
- 🔧 String Methods like `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`
- ✅ Validation Methods like `.isalpha()`, `.isdigit()`, `.isupper()`
- 🎨 String Formatting using f-strings, `.format()`, and `%`
- ⚡ Tips & Tricks like reversing, repeating, and escaping strings
- 💻 16 Practice Questions from Beginner to Hard level
- 🏆 1 Bonus Challenge

---

## 💡 Key Takeaways

- 🔒 Strings are **immutable** — can't change them in place, always create a new one
- 🔢 Indexing starts at **0** and negative indexing starts from the end
- ✂️ Slicing with `s[start:stop:step]` is super powerful, especially `s[::-1]` to reverse
- 🔧 Python has **tons of built-in string methods** so you rarely need to write logic from scratch
- 🎨 **f-strings** are the modern and best way to format strings
- 🔁 Strings are **iterable** — you can loop through each character
- 🧹 Always **clean user input** using `.strip()` to remove unwanted spaces
- 🔍 Use `in` keyword to quickly **check membership** in a string
- ⚡ You can **repeat** a string using `*` operator like `"ha" * 3`
- 🧠 Case sensitivity matters — `"python" != "Python"` always keep that in mind
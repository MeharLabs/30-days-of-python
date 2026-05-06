# Day 18 – Regular Expressions (Regex) in Python 🧩🔍

## 🎯 Goal

Learn how to use Python's `re` module to **search, extract, validate, and replace** text patterns in strings using Regular Expressions.

## 🤔 What is Regex?

**Regular Expression (Regex)** is a sequence of characters that defines a **search pattern**. It's like a mini-language for describing text patterns — used to **search, match, extract, or replace** strings.

💡 Think of it as a supercharged `Ctrl+F` — but programmable!

## 📦 The `re` Module

Python's built-in `re` module gives you all regex powers.

```python
import re  # Always import first!
```

## 🛠️ Core Methods

### 1️⃣ `re.match()` — Match at the START only

```python
import re

result = re.match(r"Hello", "Hello World")
print(result)         # <re.Match object>
print(result.group()) # Hello

# ❌ Won't match if pattern isn't at start
result2 = re.match(r"World", "Hello World")
print(result2)  # None
```

> 📌 `re.match()` only checks the **beginning** of the string!

---

### 2️⃣ `re.search()` — Search Anywhere in string

```python
import re

result = re.search(r"World", "Hello World")
print(result.group())  # World

result2 = re.search(r"\d+", "My age is 25")
print(result2.group())  # 25
```

> 📌 `re.search()` scans the **entire string** and returns the **first match**.

---

### 3️⃣ `re.findall()` — Find ALL matches → returns a list

```python
import re

emails = "Send to ali@gmail.com and sara@yahoo.com"
result = re.findall(r"\w+@\w+\.\w+", emails)
print(result)  # ['ali@gmail.com', 'sara@yahoo.com']

numbers = "Scores: 10, 45, 89, 100"
result2 = re.findall(r"\d+", numbers)
print(result2)  # ['10', '45', '89', '100']
```

> 📌 `re.findall()` never returns `None` — worst case it returns `[]`

---

### 4️⃣ `re.sub()` — Replace pattern with something else

```python
import re

text = "My phone is 0300-1234567"
cleaned = re.sub(r"\d", "*", text)
print(cleaned)  # My phone is ****-*******

# Replace multiple spaces with single space
messy = "Hello    World   Python"
clean = re.sub(r"\s+", " ", messy)
print(clean)  # Hello World Python
```

> 📌 `re.sub(pattern, replacement, string)` — like `.replace()` but with regex power!

---

## 🎯 Common Patterns

| Pattern | Meaning | Example Match |
|---------|---------|---------------|
| `\d` | Any digit (0-9) | `"5"`, `"9"` |
| `\D` | Any NON-digit | `"a"`, `"!"` |
| `\w` | Word char (a-z, A-Z, 0-9, _) | `"hello"`, `"x9"` |
| `\W` | NON-word character | `"!"`, `" "` |
| `\s` | Whitespace (space, tab, newline) | `" "`, `"\t"` |
| `\S` | NON-whitespace | `"a"`, `"3"` |
| `.` | Any character except newline | `"a"`, `"9"`, `"!"` |
| `^` | Start of string | `^Hello` |
| `$` | End of string | `world$` |

```python
import re

text = "Hello World 123"

print(re.findall(r"\d", text))   # ['1', '2', '3']
print(re.findall(r"\w+", text))  # ['Hello', 'World', '123']
print(re.findall(r"\s", text))   # [' ', ' ']
```


## ➕ Quantifiers

Quantifiers control **HOW MANY TIMES** a pattern repeats

| Quantifier | Meaning | Example |
|------------|---------|---------|
| `*` | 0 or more | `\d*` |
| `+` | 1 or more | `\d+` |
| `?` | 0 or 1 (optional) | `colou?r` → color/colour |
| `{n}` | Exactly n times | `\d{4}` → 4 digits |
| `{n,m}` | Between n and m times | `\d{2,4}` |

```python
import re

# + = one or more digits
print(re.findall(r"\d+", "abc 123 def 45"))      # ['123', '45']

# {4} = exactly 4 digits
print(re.findall(r"\d{4}", "Year 2024 code 99")) # ['2024']

# ? = optional character
print(re.findall(r"colou?r", "color colour"))     # ['color', 'colour']
```

## 🎁 Groups `()`

> Groups let you **capture specific parts** of a match

```python
import re

# Capture area code and number separately
phone = "Call us at (021) 34567890"
match = re.search(r"\((\d{3})\)\s(\d+)", phone)

if match:
    print(match.group(0))  # Full match: (021) 34567890
    print(match.group(1))  # Group 1:    021
    print(match.group(2))  # Group 2:    34567890
```

### 🏷️ Named Groups

```python
import re

text = "Born: 1995-08-21"
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)

print(match.group("year"))   # 1995
print(match.group("month"))  # 08
print(match.group("day"))    # 21
```

---

## 🔧 Extra Useful Methods

### ⚡ `re.compile()` — Pre-compile for reuse

```python
import re

# Compile once → use many times (faster!)
pattern = re.compile(r"\d+")

print(pattern.findall("Scores: 10, 20, 30"))  # ['10', '20', '30']
print(pattern.findall("Ages: 25, 30"))         # ['25', '30']
```

### ✂️ `re.split()` — Split string by pattern

```python
import re

text = "one1two2three3four"
result = re.split(r"\d", text)
print(result)  # ['one', 'two', 'three', 'four']
```

### ✅ `re.fullmatch()` — Must match the ENTIRE string

```python
import re

# Validate a 4-digit PIN
pin = "1234"
if re.fullmatch(r"\d{4}", pin):
    print("✅ Valid PIN")
else:
    print("❌ Invalid PIN")
```

---

## 🚩 Flags

```python
import re

# re.IGNORECASE — case insensitive
print(re.findall(r"hello", "Hello HELLO hello", re.IGNORECASE))
# ['Hello', 'HELLO', 'hello']

# re.MULTILINE — ^ and $ work per line
text = "line1\nline2\nline3"
print(re.findall(r"^\w+", text, re.MULTILINE))
# ['line1', 'line2', 'line3']
```

---

## 🌍 Real-World Examples

```python
import re

# ✅ Email Validator
def is_valid_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w{2,}$"
    return bool(re.fullmatch(pattern, email))

print(is_valid_email("ali@gmail.com"))  # True
print(is_valid_email("not-an-email"))   # False

# ✅ Extract all hashtags from a tweet
tweet = "Loving #Python and #Regex today! #coding"
tags = re.findall(r"#\w+", tweet)
print(tags)  # ['#Python', '#Regex', '#coding']

# ✅ Remove HTML tags
html = "<h1>Hello</h1> <p>World</p>"
clean = re.sub(r"<.*?>", "", html)
print(clean)  # Hello World

# ✅ Pakistani phone number
phone = "0312-4567890"
if re.fullmatch(r"03\d{2}-\d{7}", phone):
    print("📞 Valid PK number!")
```

---

## 📊 Quick Comparison Table

| Method | Returns | Use When |
|--------|---------|----------|
| `re.match()` | Match object / None | Check start of string |
| `re.search()` | Match object / None | Find first match anywhere |
| `re.findall()` | List of strings | Get ALL matches |
| `re.sub()` | New string | Replace patterns |
| `re.split()` | List of strings | Split by pattern |
| `re.fullmatch()` | Match object / None | Validate entire string |
| `re.compile()` | Pattern object | Reuse same pattern |

---

## 💡 Tips & Tricks

- 🔹 Always use **raw strings** `r"..."` — avoids accidental escape issues (`\n`, `\t` etc.)
- 🔹 Use `re.compile()` when using the **same pattern multiple times** — it's faster
- 🔹 Test your regex at **[regex101.com](https://regex101.com)** before writing code
- 🔹 `.*` is **greedy** (matches as much as possible) — use `.*?` to be **lazy**
- 🔹 `re.search()` + `.group()` is better than `re.match()` for most real tasks
- 🔹 Use **named groups** `(?P<name>...)` for readable, maintainable patterns
- 🔹 **Escape special chars** like `.` `(` `)` `+` with `\` when matching literally

---

## 🧠 Mental Model

```
"Hello123"
   ↑
   \w+ → matches "Hello123"  (word chars)
   \d+ → matches "123"       (digits only)
   \D+ → matches "Hello"     (non-digits)
```

---

## 📚 What I Learned

- 📦 **re module** — Python's built-in module for regex
- 🔍 **re.match()** — checks pattern at start of string
- 🔎 **re.search()** — finds first match anywhere in string
- 📋 **re.findall()** — returns all matches as a list
- 🔄 **re.sub()** — replaces pattern with something else
- ✂️ **re.split()** — splits string by a pattern
- ✅ **re.fullmatch()** — validates entire string
- ⚡ **re.compile()** — pre-compiles pattern for reuse
- 🎯 **Common Patterns** — `\d` `\w` `\s` and their opposites
- ➕ **Quantifiers** — `+` `?` `{n}` `{n,m}`
- 🎁 **Groups** — capture specific parts using `()`
- 🏷️ **Named Groups** — `(?P<name>...)` for readable patterns
- 🚩 **Flags** — like `re.IGNORECASE` and `re.MULTILINE`

---

## 🔑 Key Takeaways

- 🧠 Regex is a **pattern language** — not just Python, it works everywhere
- 📝 Always use **raw strings** `r"..."` to avoid escape issues
- ⚡ Use `re.compile()` when using the **same pattern repeatedly**
- 🔍 `re.search()` is more **flexible** than `re.match()` for most tasks
- 📋 `re.findall()` never returns `None` — safe to use directly
- ✅ `re.fullmatch()` is best for **validation** tasks
- 💡 `.*` is greedy — use `.*?` when you need **lazy matching**
- 🌍 Real use cases — emails, phone numbers, hashtags, cleaning data
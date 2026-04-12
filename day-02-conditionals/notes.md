# 📅 Day 2 - Conditionals

Conditionals are **decision-making statements** that allow your program to **execute different blocks of code** based on whether a condition is `True` or `False`. Think of them as the brain of your program — they let your code *think* and *choose*!

In simple words: *"IF this is true, do this. OTHERWISE, do that."*


## 🎯 Day 2 Goal — Conditionals

**"Learn how to make decisions in Python by using `if`, `elif`, and `else` statements along with comparison, logical, membership, and identity operators — so your program can think, choose, and respond based on different conditions."**


## 🧱 The Basic Building Blocks

`if` , `if...else` , `if...elif...else`

### 1. `if` statement
Runs a block **only if** the condition is `True`.
```python
age = 18
if age >= 18:
    print("You are an adult! ✅")
```

### 2. `if...else` statement
Runs one block if `True`, another if `False`.
```python
age = 15
if age >= 18:
    print("You are an adult! ✅")
else:
    print("You are a minor! ❌")
```

### 3. `if...elif...else` statement
Checks **multiple conditions** one by one.
```python
marks = 75
if marks >= 90:
    print("Grade: A 🏆")
elif marks >= 70:
    print("Grade: B 👍")
elif marks >= 50:
    print("Grade: C 😐")
else:
    print("Grade: F 😢")
```


## 🔗 Things You Can Use WITH Conditionals

### 🔵 Comparison Operators
These go *inside* your conditions:

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal | `x >= 5` |
| `<=` | Less than or equal | `x <= 5` |

---

### 🟣 Logical Operators
Combine **multiple conditions** together:

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both must be True | `age > 18 and age < 60` |
| `or` | At least one must be True | `day == "Sat" or day == "Sun"` |
| `not` | Reverses the condition | `not is_raining` |

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed! 🎉")
```

---

### 🟡 Membership Operators
Check if something **exists inside** a list, string, etc.:

```python
fruits = ["apple", "banana", "mango"]

if "mango" in fruits:
    print("Mango is available! 🥭")

if "grape" not in fruits:
    print("No grapes here! 🍇")
```

---

### 🟠 Identity Operators
Check if two variables point to the **same object**:

```python
x = None

if x is None:
    print("x has no value yet! 🚫")
```

---

### 🔴 Nested Conditionals
An `if` **inside** another `if`:

```python
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome, Admin! 👑")
    else:
        print("Welcome, User! 👤")
else:
    print("Please log in first! 🔒")
```

---

### ⚡ Ternary / Inline `if` (One-liner!)
Write a simple conditional in **one line**:

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult
```


## 📖 Short Definitions

### 🏗️ Conditionals
| Name | Definition |
|---|---|
| `if` | Runs code **only if** the condition is True |
| `elif` | Checks **another condition** if the previous one was False |
| `else` | Runs code when **no condition** above was True |

### 🔵 Comparison Operators
| Name | Definition |
|---|---|
| `==` | Checks if two values are **equal** |
| `!=` | Checks if two values are **not equal** |
| `>` | Checks if left value is **greater than** right |
| `<` | Checks if left value is **less than** right |
| `>=` | Checks if left value is **greater than or equal** to right |
| `<=` | Checks if left value is **less than or equal** to right |

### 🟣 Logical Operators
| Name | Definition |
|---|---|
| `and` | Returns True if **both** conditions are True |
| `or` | Returns True if **at least one** condition is True |
| `not` | **Reverses** the result — True becomes False, False becomes True |

### 🟡 Membership Operators
| Name | Definition |
|---|---|
| `in` | Checks if a value **exists** inside a sequence |
| `not in` | Checks if a value does **not exist** inside a sequence |

### 🟠 Identity Operators
| Name | Definition |
|---|---|
| `is` | Checks if two variables point to the **same object** |
| `is not` | Checks if two variables point to **different objects** |

### ⚡ Special Forms
| Name | Definition |
|---|---|
| **Nested `if`** | An `if` statement **inside** another `if` statement |
| **Ternary `if`** | A **one-line** shorthand for a simple if-else |

---

## 🧪 What I Built

### 1. Decision-making programs (core logic skill)
- Positive / negative / zero
- Even / odd
- Voting eligibility 🗳️
- Traffic light system 🚦
- Login system 🔐

👉 This is called: **program flow control**

### 2. Real-world logic systems
- 🏦 Login system (username + password)
- 🧮 Calculator (with error handling)
- 🎓 Grading system (marks → grades)
- 🚦 Traffic rules system
- 📅 Day checker (weekday/weekend)

👉 This is basically **mini backend logic of real applications**

---

## 🧩 Practice Questions

### 🟢 Easy Level
- **Q1.** Check if a number is **positive, negative, or zero**
- **Q2.** Check if a person is a **minor or adult** based on age
- **Q3.** Check if a number is **even or odd**
- **Q4.** Print the **greater of two numbers**
- **Q5.** Check if a letter is a **vowel or consonant**

### 🟡 Medium Level
- **Q6.** Print the **grade** based on marks (A, B, C, D, F)
- **Q7.** Check if a year is a **leap year**
- **Q8.** Find the **largest of 3 numbers**
- **Q9.** Check if a person can **vote** (age >= 18 AND has CNIC)
- **Q10.** Check if a number is **divisible by 3, 5, both, or neither**

### 🔴 Hard Level
- **Q11.** Build a simple **login system** (username + password match)
- **Q12.** Check if a number is **between 1–100** and also **even or odd**
- **Q13.** Check if a day is a **weekday or weekend**
- **Q14.** Build a **calculator** using conditionals (`+`, `-`, `*`, `/`)
- **Q15.** Build a **traffic light** program (red/yellow/green → action)

---


## 🔑 Key Takeaways

- ✅ `if`, `elif`, `else` are the **core building blocks** of decision making in Python
- ✅ **Comparison operators** (`==`, `!=`, `>`, `<`) are used to **compare values** inside conditions
- ✅ **Logical operators** (`and`, `or`, `not`) help you **combine multiple conditions** together
- ✅ **Membership operators** (`in`, `not in`) check if a value **exists in a sequence**
- ✅ **Identity operators** (`is`, `is not`) check if two variables point to the **same object**
- ✅ **Nested conditionals** allow you to check conditions **inside other conditions**
- ✅ **Ternary `if`** lets you write simple conditions in just **one line**
- ✅ Clean and simple conditionals make your code **more readable and professional**

 **Bottom Line:** Conditionals give your program the ability to **think and make decisions** — it's what makes code smart! 💡


## 💡 Tips, Tricks & Tweaks

### ✅ Tip 1 — Don't compare Booleans unnecessarily
```python
# ❌ Bad
if is_active == True:

# ✅ Good
if is_active:
```

### ✅ Tip 2 — Use `in` for multiple OR checks
```python
# ❌ Messy
if color == "red" or color == "blue" or color == "green":

# ✅ Clean
if color in ["red", "blue", "green"]:
```

### ✅ Tip 3 — Chained Comparisons 🦸 (Python Superpower!)
```python
# ❌ Long way
if x > 0 and x < 100:

# ✅ Pythonic way
if 0 < x < 100:
```

### ✅ Tip 4 — Avoid Deep Nesting
```python
# ❌ Hard to read
if is_logged_in:
    if has_permission:
        run()

# ✅ Cleaner
if is_logged_in and has_permission:
    run()
```

### ✅ Tip 5 — Falsy Values 🎭
These all automatically act as `False`:
```python
0, "", [], {}, None, False
```
```python
name = ""
if not name:
    print("Name is empty! ⚠️")
```

### ✅ Tip 6 — Use Ternary for Simple Conditions ⚡
```python
# ❌ Long way
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# ✅ One liner
status = "Adult" if age >= 18 else "Minor"
```

### ✅ Tip 7 — `elif` is Better than Multiple `if`s
```python
# ❌ Bad — checks ALL conditions even after match
if marks >= 90:
    grade = "A"
if marks >= 70:
    grade = "B"
if marks >= 50:
    grade = "C"

# ✅ Good — stops after first match
if marks >= 90:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
```

### ✅ Tip 8 — `is` vs `==` Know the Difference! ⚠️
```python
# == checks VALUE
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # ✅ True — same values

# is checks OBJECT (memory)
print(x is y)  # ❌ False — different objects
```

### ✅ Tip 9 — Always Handle the `else` Case 🛡️
```python
# ❌ Risky — no fallback
if role == "admin":
    give_access()

# ✅ Safe — always has a fallback
if role == "admin":
    give_access()
else:
    deny_access()
```

### ✅ Tip 10 — Use `not in` for Cleaner Checks 🧹
```python
# ❌ Confusing
if not name in blocked_users:

# ✅ Cleaner
if name not in blocked_users:
```

---
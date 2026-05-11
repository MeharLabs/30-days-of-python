# 🔄 Day 3 — Python Loops


## 📖 What is a Loop?

A **loop** is a way to repeat a block of code multiple times without writing it over and over. Instead of copy-pasting the same line 100 times, you let the loop do the repetition for you. Think of it like a song on repeat 🎵 — it keeps playing until you say stop.


## 🔁 Types of Loops in Python

### 1. `for` Loop
Used when you know **how many times** you want to repeat something, or when you're going through a collection item by item.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

### 2. `while` Loop
Used when you want to repeat something **as long as a condition is true**. You may not know in advance how many times it'll run.

```python
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
```


## 🧰 Things You Can Use WITH Python Loops

### 🔢 `range()` — Generate a sequence of numbers
```python
for i in range(5):        # 0, 1, 2, 3, 4
for i in range(1, 10):    # 1 to 9
for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step by 2)
```

### 🛑 `break` — Exit the loop early
```python
for i in range(10):
    if i == 5:
        break   # stops at 5
    print(i)
```

### ⏭️ `continue` — Skip the current iteration
```python
for i in range(5):
    if i == 3:
        continue  # skips 3
    print(i)
```

### 🔂 `pass` — Do Nothing (Placeholder)
```python
for i in range(5):
    pass  # 🚧 "I'll fill this later"
```

### 🔄 `else` — Runs after the loop finishes (if no `break`)
```python
for i in range(3):
    print(i)
else:
    print("Loop finished! ✅")
```

### 🔢 `enumerate()` — Get index + value at the same time
```python
names = ["Ali", "Sara", "Zain"]

for index, name in enumerate(names):
    print(index, name)
# 0 Ali
# 1 Sara
# 2 Zain
```

### 🤐 `zip()` — Loop through two lists at once
```python
names = ["Ali", "Sara"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, "scored", score)
```

### 🔃 `reversed()` — Loop backwards
```python
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0
```

### 🗂️ Loop through a Dictionary
```python
student = {"name": "Ali", "age": 20}

for key, value in student.items():
    print(key, ":", value)
```


## 🌀 Nested Loops — A loop inside a loop

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```
⚠️ Be careful — nested loops can get slow with large data!


## 😱 The Infinite Loop (Danger Zone!)

```python
while True:
    print("I will never stop!")  # 💀 Don't run this!
```

Always have an exit:
```python
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break  # ✅ Safe exit
```

---

## 🔑 Key Takeaways

| # | Takeaway |
|---|----------|
| 1️⃣ | A loop = Repetition made simple |
| 2️⃣ | `for` → known count / collection, `while` → condition based |
| 3️⃣ | Controllers: `break` 🛑, `continue` ⏭️, `pass` 🚧 |
| 4️⃣ | Power tools: `range()`, `enumerate()`, `zip()`, `reversed()` |
| 5️⃣ | Infinite loop = Danger ☠️ — always have exit condition |
| 6️⃣ | Think in loops! 🧠 See repetition → loop it! |


## 💡 Tips, Tricks & Tweaks

### ⚡ Performance
```python
# ✅ Use set for membership checks (faster)
if x in {1, 2, 3, 4, 5}:  # Fast
if x in [1, 2, 3, 4, 5]:  # Slow ❌

# ✅ Store len() before loop
n = len(mylist)
for i in range(n):  # Good
```

### 🎯 Clean Code
```python
# Use _ for throwaway variables
for _ in range(5):
    print("Hello!")

# Unpack directly in loop
for num, word in [(1, "one"), (2, "two")]:
    print(num, word)

# enumerate with custom start
for i, name in enumerate(["Ali", "Sara"], start=1):
    print(i, name)  # 1 Ali, 2 Sara
```

### 🛠️ Useful Tweaks
```python
# Step in range
for i in range(0, 20, 2):   # 0, 2, 4, 6...
for i in range(10, 0, -1):  # 10, 9, 8... (countdown)

```


## 🎯 Goal for Day 3

**"Be able to look at a repetitive problem and immediately know how to solve it with a loop — the right loop, the right way."**

---

## 📝 What I Learned

- 📖 Learned what loops are
- 🔄 Studied `for` and `while` loops
- 🧰 Learned tools like `break`, `continue`, `enumerate`, `zip`, `itertools` etc.
- 🧠 Got 16 practice questions to solve

---

🎯 **Loops are the backbone of automation in Python. Master them and you can handle data, automate tasks, and build powerful programs with very few lines of code!** 💪🐍
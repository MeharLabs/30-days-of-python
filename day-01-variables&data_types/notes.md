# 🗒️ Day 1 Notes — Variable & Data Types

---

## 📖 Concepts

### Concept 1 → Variables:
A variable is just a name you give to some data so you can use it later.
👉 Variable = label + value

```python
name = "Mehar"
age = 24
vibe = "coding"
```

💡 Python be like: "don't worry about types, I got you" → it auto-detects everything (dynamic typing 🧠)

---

### String Concatenation:
String concatenation is the process of joining two or more strings together to form a single string.
👉 Adding text + text = one combined text

```python
print("You are the " + vibe)
```

---

### Type Casting:
Type Casting = when you change one data type into another

```python
24 -> "24"
str(age)  # type casting, changing number to string
```

---

### Separate Arguments:
Separate arguments = when you pass multiple values into a function, and you split them using commas ( , )

```python
print("Your name is ", name)
```

---

### f-string:
f-string = modern way to put variables inside text

```python
print(f"My name is {name} and I am {age} years old")
```

---

### Concept 2 → Data Types:
Data Types = different kinds of data you can store in Python.
👉 Basically: "what type of value a variable is holding or what kind of vibe your data has"

🔥 Main types:
- `int` 🔢 → whole numbers (10, 50)
- `float` 🌊 → decimal numbers (3.14)
- `str` 💬 → text ("hello")
- `bool` ✅❌ → True / False
- `list` 📋 → multiple items
- `tuple` 🔒 → fixed items
- `dict` 🗂️ → key-value pairs

# 🧩 Practice Questions — Variables, Data Types & Collections


## 🟢 Level 1 — Easy (Just Getting Started)


**Q1.** Create 3 variables — your name, age, and city. Print them using f-string.

**Q2.** Create a list of 5 of your favorite foods. Print the first and last item.


**Q3.** Create a dict of your profile with keys — `name`, `age`, `hobby`. Print your hobby.



**Q4.** Check the type of these values using `type()`:

```python
42, "hello", 3.14, True, [1,2,3]
```


**Q5.** Store your birthday as a tuple `(day, month, year)` and print each value separately.



## 🟡 Level 2 — Mid (Thinking Required 🧠)

**Q6.** Take a number stored as string `"25"` and add `5` to it. Print the result.


**Q7.** Create a list of 5 numbers. Add a new number, remove the 2nd item, then print the final list.


**Q8.** Create a student dict with `name`, `marks`, and `grade`. Update the marks and add a new key `passed = True`.


**Q9.** Concatenate your first name and last name using both `+` and f-string. Print both results.


**Q10.** Create a tuple of 3 cities. Try to change the 2nd city — what error do you get? 👀


## 🔴 Level 3 — Hard (Big Brain Mode 💀)


**Q11.** Create a dict where keys are subject names and values are marks. Print only the subject names, then only the marks.


**Q12.** You have this: `info = ("John", 20, "NYC")`. Unpack it into 3 separate variables and print each one.

## 🟦 Tips, Tricks & Gotchas 😎

### 🚀 Tips & Tricks

**1. 🐍 Use snake_case always**
```python
user_name = "Mehar"
first_age = 24
```

**2. 📦 Meaningful names > short names**
```python
x = 24    # ❌
age = 24  # ✅
```

**3. 🔄 Check type anytime**
```python
print(type(age))
```
👉 helps avoid confusion

**4. 💬 Use f-strings (best upgrade)**
```python
print(f"My age is {age}")
```
👉 clean + pro level

**5. 📦 Multiple assignment = shortcut hack**
```python
a, b, c = 1, 2, 3
x = y = z = 1
```

**6. 🔒 Use ALL CAPS for constants**
```python
PI = 3.14
MAX_USERS = 100
```

---

### ⚠️ Gotchas / Mistakes (warning zone 🚨)

**1. ❌ Mixing types without conversion**
```python
print("Age: " + 24)  # ERROR 💀
```
✔ Fix:
```python
print("Age: " + str(24))
```

**2. ❌ Using wrong variable names**
```python
2name = "Mehar"  # ❌
name = "Mehar"   # ✅
```

**3. ❌ Forgetting quotes for strings**
```python
name = Mehar    # ❌
name = "Mehar"  # ✅
```

**4. ❌ Overwriting variable by accident**
```python
x = 10
x = "hello"  # now x changed type 😵
```

**5. ❌ Thinking Python is strict about types**
👉 Python is chill (dynamic typing 😎) but that can confuse you

**6. ❌ Forgetting int() / str() when needed**
```python
age = "24"
print(age + 5)  # ❌
```
✔ Fix:
```python
print(int(age) + 5)
```
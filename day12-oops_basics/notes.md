# 🐍 Day 12: OOP Basics in Python

## 🎯 Goal
Understanding and absorbing Python OOP Basics — using `class`, `__init__`, `self`, instance methods, and instance vs class variables from scratch.

---

## 🧠 What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into **objects** — bundled units of **data (attributes)** and **behavior (methods)**. Instead of writing a bunch of loose functions, you model real-world things as objects.

> 💡 Think of a **class** as a blueprint, and an **object** as the actual thing built from that blueprint.

---

## 🏗️ 1. The `class` Keyword

**Definition:** The `class` keyword is used to define a new class — a template/blueprint for creating objects.

```python
class Dog:
    pass  # Empty class for now
```

**What it does:**
- Creates a new **type** in Python
- Groups related data and functions together
- Acts as a **factory** for making multiple objects of the same kind

**Tips & Tricks:**
| Tip | Example |
|-----|---------|
| Class names use **PascalCase** | `class BankAccount:` ✅ |
| Keep one class per file for large projects | `bank_account.py` |
| Use `pass` as placeholder | `class Todo: pass` |

---

## 🔧 2. The `__init__` Constructor

**Definition:** `__init__` is a special (dunder/magic) method that is automatically called when a new object is created. It initializes the object's attributes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)
print(dog1.name)   # Rex
print(dog2.name)   # Bella
```

**What it does:**
- Runs **automatically** on object creation
- Sets up the **initial state** of the object
- Receives arguments passed during object creation

```python
# 🔥 Default values in __init__
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

p1 = Player("Ali")        # health = 100
p2 = Player("Zara", 80)   # health = 80
```

> 💡 `__init__` is NOT the constructor itself — `__new__` is. But `__init__` is what you'll use 99% of the time!

---

## 🪄 3. The `self` Keyword

**Definition:** `self` is a reference to the current instance of the class. It's how the object refers to itself — its own attributes and methods.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)
print(c1.area())   # 78.5
print(c2.area())   # 314.0
```

**What it does:**
- Always the **first parameter** of any instance method
- Python passes it **automatically** — you don't pass it manually
- Connects method calls back to the specific object

> 🧠 Think of `self` as the word **"my"** — `self.name` = "my name"

> ⚠️ `self` is a CONVENTION, not a keyword. You can technically name it anything — but always use `self`!

---

## ⚙️ 4. Instance Methods

**Definition:** Instance methods are functions defined inside a class that operate on a specific object (instance). They always take `self` as the first parameter.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            self.balance -= amount
            print(f"💸 Withdrew {amount}. Balance: {self.balance}")

    def show_balance(self):
        print(f"🏦 {self.owner}'s balance: {self.balance}")

acc = BankAccount("Ali", 1000)
acc.deposit(500)      # 💰 Deposited 500. Balance: 1500
acc.withdraw(200)     # 💸 Withdrew 200. Balance: 1300
acc.show_balance()    # 🏦 Ali's balance: 1300
```

**Types of Methods:**
| Method Type | Decorator | First Param | Access |
|-------------|-----------|-------------|--------|
| Instance method | none | `self` | instance + class data |
| Class method | `@classmethod` | `cls` | class data only |
| Static method | `@staticmethod` | none | neither |

---

## 📦 5. Instance vs Class Variables

| | Instance Variable | Class Variable |
|---|---|---|
| **Defined in** | `__init__` (with `self`) | class body (outside methods) |
| **Belongs to** | Each object individually | The class itself (shared) |
| **Unique per object?** | ✅ Yes | ❌ No (shared by all) |

```python
class Student:
    school = "Python High"      # 🏫 class variable — SHARED by all

    def __init__(self, name, grade):
        self.name = name        # 👤 instance variable — UNIQUE per student
        self.grade = grade

s1 = Student("Ali", "A")
s2 = Student("Sara", "B")

print(s1.name)    # Ali
print(s2.name)    # Sara
print(s1.school)  # Python High  ← same for both
print(s2.school)  # Python High  ← same for both

Student.school = "OOP Academy"
print(s1.school)  # OOP Academy ← changed for ALL
print(s2.school)  # OOP Academy ← changed for ALL
```

**⚠️ Gotcha with mutable class variables:**
```python
# 🚨 DANGEROUS — shared list
class Team:
    members = []
    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add("Ali")
print(t2.members)   # ['Ali'] ← t2 sees it too! 😱

# ✅ FIX — use instance variable
class Team:
    def __init__(self):
        self.members = []   # each team gets its OWN list
```

---

## 🔮 Other Useful OOP Tools

### 🪞 Dunder (Magic) Methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):       # print(book) → human readable
        return f"📖 {self.title}"

    def __repr__(self):      # developer representation
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):       # len(book)
        return self.pages

    def __eq__(self, other): # book1 == book2
        return self.title == other.title
```

## 🗺️ Full Cheat Sheet

```python
class Animal:
    species = "Unknown"                    # 📦 class variable

    def __init__(self, name, sound):       # 🔧 constructor
        self.name = name                   # 👤 instance variable
        self.sound = sound

    def speak(self):                       # ⚙️ instance method
        return f"{self.name} says {self.sound}!"

    @classmethod
    def get_species(cls):                  # 🏛️ class method
        return cls.species

    @staticmethod
    def breathe():                         # 🔒 static method
        return "Inhale... Exhale..."

    def __str__(self):                     # 🪞 dunder method
        return f"Animal: {self.name}"
```

---

## 📝 What I Learned

- `class` keyword to create a blueprint 🏗️
- `__init__` to initialize an object's data 🔧
- `self` to refer to the current object 🪄
- Instance methods to define object behavior ⚙️
- Instance vs Class variables and their differences 📦

---

## 🏆 Key Takeaways

- Classes are blueprints, objects are the real things 🏗️
- `self` is always the object talking to itself 🪄
- `__init__` runs automatically on object creation 🔧
- Instance variables are unique, class variables are shared 📦
- Methods are just functions that belong to an object ⚙️
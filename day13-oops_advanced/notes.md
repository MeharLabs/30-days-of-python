# 🐍 Day 13 — OOP Advanced in Python


## 🎯 Goal

Understand and learn OOP Advanced concepts in Python including Multiple & Multilevel Inheritance, Abstract Classes, Polymorphism, Duck Typing, Aggregation, Composition, Nested Classes, Static Methods, and Class Methods.

---

## 📚 Topics Covered


## 1. 🧬 Inheritance (Parent → Child)

**Definition:** Inheritance is when a **child class** acquires the properties and methods of a **parent class**. Think of it like a child inheriting traits from their parents — but they can also have their own unique traits!

**Why use it?** ♻️ Code reusability — write once, reuse everywhere.

```python
class Animal:          # 👴 Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):     # 🐶 Child class inherits from Animal
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):     # 🐱 Child class inherits from Animal
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()   # Buddy says: Woof!
cat.speak()   # Whiskers says: Meow!
```

**🔑 Key Points:**
- Child class is written as `class Child(Parent):`
- Child gets ALL methods and attributes of the parent
- Child can have its OWN extra methods too
- Python supports **multi-level** and **multiple** inheritance

```python
# 🔀 Multiple Inheritance (two parents!)
class Flyable:
    def fly(self): print("I can fly! ✈️")

class Swimmable:
    def swim(self): print("I can swim! 🏊")

class Duck(Flyable, Swimmable):   # inherits BOTH
    pass

d = Duck()
d.fly()    # I can fly! ✈️
d.swim()   # I can swim! 🏊
```

💡 **Tip:** Use `issubclass(Dog, Animal)` to check if a class is a child of another. Use `isinstance(dog, Animal)` to check if an object belongs to a class or its parent!

---

## 2. 🦸 `super()` Keyword

**Definition:** `super()` is a built-in function that gives you access to the **parent class's methods and constructor** from inside the child class. It literally means *"go up to my super/parent class"*.

**Why use it?** Instead of rewriting the parent's `__init__`, you call it with `super()` and just **add** to it.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"👤 Person created: {self.name}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)   # ⬆️ calls Person's __init__
        self.grade = grade            # extra attribute for Student
        print(f"🎓 Student grade: {self.grade}")

    def info(self):
        print(f"{self.name}, Age: {self.age}, Grade: {self.grade}")

s = Student("Ali", 20, "A+")
s.info()   # Ali, Age: 20, Grade: A+
```

**🔑 Key Points:**
- `super().__init__()` — calls parent's constructor
- `super().method()` — calls any parent method
- Prevents code duplication 🙅‍♂️
- Works perfectly in multi-level inheritance chains

```python
class A:
    def greet(self): print("Hello from A 👋")

class B(A):
    def greet(self):
        super().greet()        # calls A's greet first
        print("Hello from B 👋")

class C(B):
    def greet(self):
        super().greet()        # calls B's greet (which calls A's too!)
        print("Hello from C 👋")

C().greet()
# Hello from A 👋
# Hello from B 👋
# Hello from C 👋
```

> 💡 **Tip:** Always prefer `super()` over hardcoding the parent name like `Person.__init__(self, ...)` — it's safer in complex inheritance trees!

---

## 3. 🔄 Method Overriding

**Definition:** Method overriding happens when a **child class redefines a method** that already exists in the parent class. The child's version **replaces** the parent's version for that object.

**Why use it?** To customize or completely change parent behavior for a specific child. 🎨

```python
class Shape:
    def area(self):
        print("Calculating area of generic shape...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):              # 🔄 Overrides Shape's area()
        result = 3.14 * self.radius ** 2
        print(f"🔵 Circle area: {result}")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):              # 🔄 Overrides Shape's area()
        print(f"🟥 Rectangle area: {self.w * self.h}")

c = Circle(5)
r = Rectangle(4, 6)
c.area()    # 🔵 Circle area: 78.5
r.area()    # 🟥 Rectangle area: 24
```

**⚔️ Override vs Overload:**

| Feature | Overriding | Overloading |
|---|---|---|
| Where | Child class redefines parent method | Same class, different params |
| Python support | ✅ Yes | ⚠️ Not natively (use `*args`) |

```python
# 🤝 You can STILL call parent's version with super()
class Dog(Animal):
    def speak(self):
        super().speak()                  # runs Animal's speak first
        print(f"{self.name} also barks! 🐕")
```

> 💡 **Tip:** Use `# override` comments or the `@override` decorator (Python 3.12+) to make overrides explicit and easier to spot in code reviews!

---

## 4. 🔒 Encapsulation (Private Variables)

**Definition:** Encapsulation means **hiding the internal data** of a class from the outside world and only exposing what's necessary. It's like a capsule 💊 — the medicine is inside, you don't touch it directly.

**Why use it?** To protect data from accidental modification and control access. 🛡️

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # ✅ Public   — accessible anywhere
        self._account_no = "PK123"   # ⚠️ Protected — convention, be careful
        self.__balance = balance     # 🔒 Private  — double underscore, hidden!

    # Getter — controlled READ access
    def get_balance(self):
        return f"💰 Balance: {self.__balance}"

    # Setter — controlled WRITE access with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited {amount}. New balance: {self.__balance}")
        else:
            print("❌ Invalid deposit amount!")

acc = BankAccount("Ahmed", 5000)
print(acc.owner)           # ✅ Ahmed
print(acc.get_balance())   # ✅ 💰 Balance: 5000
acc.deposit(1000)          # ✅ Deposited 1000

# print(acc.__balance)     # ❌ AttributeError! Can't access directly
```

**🔑 The Three Levels:**

```python
self.name       # ✅ PUBLIC    — anyone can access
self._name      # ⚠️ PROTECTED — "please don't, but you can"
self.__name     # 🔒 PRIVATE   — name-mangled to _ClassName__name
```

**🏠 Using `@property` (Pythonic way!):**

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):              # getter — use like attribute, not method!
        return self.__celsius

    @celsius.setter
    def celsius(self, value):       # setter with validation
        if value < -273.15:
            raise ValueError("❄️ Below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):           # computed property!
        return self.__celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0
t.celsius = 30        # uses setter automatically
```

> 💡 **Tip:** Always use `@property` instead of manually naming methods `get_x()` / `set_x()` — it's the **Pythonic way** and looks cleaner!

---

## 5. 🖨️ `__str__` Method

**Definition:** `__str__` is a **magic/dunder method** that defines how your object looks when **printed or converted to a string**. Without it, Python shows something ugly like `<__main__.Dog object at 0x...>` 🤢

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # 👥 For USERS — readable, pretty
        return f"📖 '{self.title}' by {self.author}"

    def __repr__(self):
        # 🛠️ For DEVELOPERS — unambiguous, debuggable
        return f"Book(title='{self.title}', author='{self.author}')"

b = Book("Atomic Habits", "James Clear")
print(b)       # 📖 'Atomic Habits' by James Clear
print(repr(b)) # Book(title='Atomic Habits', author='James Clear')
```

| Method | Called by | Audience | Purpose |
|---|---|---|---|
| `__str__` | `print()`, `str()` | 👥 Users | Pretty display |
| `__repr__` | `repr()`, debugger | 🛠️ Devs | Debug/recreate |

> 💡 **Tip:** Always define **both** `__str__` and `__repr__`. Rule of thumb — `__repr__` should ideally return something you could paste back into Python to recreate the object!

---

## 6. 🔀 Multiple Inheritance

**Definition:** A child class inherits from **two or more parent classes** at the same time. One child, many parents! 👨‍👩‍👦

```python
class Father:
    def hardworking(self):
        print("💪 I am hardworking!")

class Mother:
    def caring(self):
        print("❤️ I am caring!")

class Child(Father, Mother):   # inherits BOTH
    def identity(self):
        print("👦 I am their child!")

c = Child()
c.hardworking()   # 💪 I am hardworking!
c.caring()        # ❤️ I am caring!
```

**⚠️ The Diamond Problem & MRO:**

```python
class A:
    def hello(self): print("Hello from A")

class B(A):
    def hello(self): print("Hello from B")

class C(A):
    def hello(self): print("Hello from C")

class D(B, C):   # 💎 Diamond problem!
    pass

D().hello()        # Hello from B  ← Python follows MRO!
print(D.__mro__)   # D → B → C → A → object
```

> 💡 **MRO (Method Resolution Order)** — Python uses **C3 Linearization** — goes **Left → Right → Up**. Always check `ClassName.__mro__` when confused!

---

## 7. 🪜 Multilevel Inheritance

**Definition:** A chain of inheritance — Child inherits from Parent, which itself inherited from Grandparent. **Generation by generation!** 👴→👨→👦

```python
class Grandparent:
    def legacy(self):
        print("🏛️ I built the family legacy!")

class Parent(Grandparent):
    def business(self):
        print("💼 I run the business!")

class Child(Parent):
    def future(self):
        print("🚀 I shape the future!")

c = Child()
c.legacy()     # 🏛️ from Grandparent
c.business()   # 💼 from Parent
c.future()     # 🚀 own method
```

**Multiple vs Multilevel:**

| | Multiple | Multilevel |
|---|---|---|
| Structure | `class C(A, B)` | `A → B → C` |
| Parents | Two+ at same level | One per level, chained |
| Analogy | 👨‍👩‍👦 Two parents | 👴👨👦 Grandparent chain |

---

## 8. 🚫 Abstract Classes

**Definition:** An abstract class is a **blueprint that cannot be instantiated**. It forces child classes to implement specific methods. Think of it as a **contract** 📄 — sign it or Python yells at you!

```python
from abc import ABC, abstractmethod   # 📦 must import this

class Shape(ABC):
    @abstractmethod
    def area(self):                   # 📋 child MUST implement this
        pass

    @abstractmethod
    def perimeter(self):              # 📋 child MUST implement this
        pass

    def describe(self):               # ✅ normal method — optional to override
        print("📐 I am a shape!")

# s = Shape()   ❌ TypeError: Can't instantiate abstract class!

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):        return 3.14 * self.r ** 2
    def perimeter(self):   return 2 * 3.14 * self.r

c = Circle(5)
print(c.area())      # 78.5
print(c.perimeter()) # 31.4
c.describe()         # 📐 I am a shape!
```

**🔑 Key Points:**
- Import `ABC` and `abstractmethod` from `abc` module
- Any class with even **one** `@abstractmethod` is abstract
- Child must implement **ALL** abstract methods or it also becomes abstract
- Abstract classes **can** have normal methods and `__init__`

> 💡 **Tip:** Use abstract classes when you want to enforce a common interface across many child classes — great for large codebases and team projects! 🏢

---

## 9. 🎭 Polymorphism

**Definition:** Poly = Many, Morph = Forms. **Same method name, different behavior** depending on the object. One interface, many implementations!

```python
class Dog:
    def speak(self): print("🐶 Woof!")

class Cat:
    def speak(self): print("🐱 Meow!")

class Parrot:
    def speak(self): print("🦜 Hello human!")

animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    animal.speak()    # each responds differently!
```

**Polymorphism Types:**
```
🔄 Method Overriding  → child redefines parent method (runtime)
➕ Operator Overload  → __add__, __mul__, __eq__ etc
🎯 Function Poly      → same function accepts different object types
```

---

## 10. 🦆 Duck Typing

**Definition:** *"If it walks like a duck and quacks like a duck, it IS a duck."* 🦆 Python doesn't care about the **type** of object — only whether it has the **method you're calling**. No inheritance needed!

```python
class Duck:
    def quack(self): print("🦆 Quack quack!")

class Person:
    def quack(self): print("👨 I'm quacking like a duck!")

class RubberDuck:
    def quack(self): print("🟡 Squeak squeak!")

def make_it_quack(duck):    # no type checking!
    duck.quack()

make_it_quack(Duck())        # ✅
make_it_quack(Person())      # ✅
make_it_quack(RubberDuck())  # ✅
```

| | Duck Typing | Abstract Class |
|---|---|---|
| Relationship | No inheritance needed | Must inherit |
| Checking | At runtime | At class definition |
| Flexibility | 🔓 Very loose | 🔒 Strict contract |
| Pythonic? | ✅ Very Pythonic | ✅ Good for large teams |

---

## 11. 🔗 Aggregation

**Definition:** A **"has-a"** relationship where one class contains a reference to another, but **both can exist independently**. If the container is destroyed, the contained object **lives on**. 🏠➡️👤

```python
class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __str__(self):
        return f"📍 {self.city}, {self.country}"

class Employee:
    def __init__(self, name, address):   # address passed IN — not created here
        self.name = name
        self.address = address           # 🔗 just a reference

    def info(self):
        print(f"👤 {self.name} lives at {self.address}")

addr = Address("Lahore", "Pakistan")
emp = Employee("Ahmed", addr)
emp.info()    # 👤 Ahmed lives at 📍 Lahore, Pakistan

del emp
print(addr)   # 📍 Lahore, Pakistan  ✅ still alive!
```

---

## 12. 🧱 Composition

**Definition:** Also a **"has-a"** relationship, but **stronger** — the contained object is **created inside** the container and **dies with it**. 💀

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"🔧 Engine started! {self.horsepower}hp roaring!")

class Car:
    def __init__(self, brand, hp):
        self.brand = brand
        self.engine = Engine(hp)    # 🧱 created INSIDE — composition!

    def drive(self):
        self.engine.start()
        print(f"🚗 {self.brand} is driving!")

car = Car("Toyota", 150)
car.drive()
# delete car → engine is gone too 💀
```

**Aggregation vs Composition:**

| | Aggregation | Composition |
|---|---|---|
| Relationship | Weak "has-a" | Strong "has-a" |
| Lifetime | Independent ✅ | Dependent 💀 |
| Object creation | Passed in | Created inside |
| Example | Employee & Address | Car & Engine |

> 💡 **Tip:** Ask yourself — *"Can this object exist without the other?"* YES → Aggregation. NO → Composition.

---

## 13. 📦 Nested Classes

**Definition:** A class defined **inside another class**. The inner class is closely tied to the outer and hidden from the outside world. 🪆

```python
class Laptop:
    brand = "Dell"

    def __init__(self, model):
        self.model = model
        self.battery = self.Battery(100)   # using inner class

    def info(self):
        print(f"💻 {self.brand} {self.model}")
        self.battery.status()

    class Battery:                         # 📦 Nested class
        def __init__(self, capacity):
            self.capacity = capacity

        def status(self):
            print(f"🔋 Battery: {self.capacity}%")

laptop = Laptop("XPS 15")
laptop.info()
# 💻 Dell XPS 15
# 🔋 Battery: 100%
```

**When to use nested classes? 🤔**
- Inner class is **only relevant** to the outer class
- Hiding implementation details 🙈
- Organizing logically grouped code

---

## 14. ⚙️ Static Methods

**Definition:** A method that belongs to the **class itself**, not to any instance. It has **no access** to `self` or `cls`. Just a plain utility function living inside a class. 🔧

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

# Call WITHOUT creating an object!
print(MathUtils.add(5, 3))                    # 8
print(MathUtils.is_even(4))                   # True
print(MathUtils.celsius_to_fahrenheit(100))   # 212.0
```

---

## 15. 🏛️ Class Methods

**Definition:** A method that belongs to the **class**, receives `cls` as first argument, and can access/modify **class-level data**. Decorated with `@classmethod`.

```python
class Student:
    school = "Python Academy"    # 🏫 class variable
    count = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1

    @classmethod
    def get_school(cls):
        return f"🏫 School: {cls.school}"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

    @classmethod
    def from_string(cls, data_str):    # 🏭 Alternative constructor!
        name, grade = data_str.split(",")
        return cls(name, int(grade))

    @staticmethod
    def is_passing(grade):
        return grade >= 50

s1 = Student("Ali", 85)
s2 = Student.from_string("Sara,92")   # 🏭 factory method!
print(Student.get_school())           # 🏫 School: Python Academy
print(Student.count)                  # 2
```

**The Big Three — Side by Side:**

| | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | none | `@classmethod` | `@staticmethod` |
| First arg | `self` | `cls` | nothing |
| Access instance? | ✅ | ❌ | ❌ |
| Access class? | ✅ | ✅ | ❌ |
| Call on class? | ❌ | ✅ | ✅ |

---

## 🎁 Bonus: Useful Dunder Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):    return f"Vector({self.x}, {self.y})"
    def __add__(self, o): return Vector(self.x+o.x, self.y+o.y)  # v1 + v2
    def __len__(self):    return int((self.x**2 + self.y**2)**0.5) # len(v)
    def __eq__(self, o):  return self.x==o.x and self.y==o.y       # v1 == v2

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)   # Vector(4, 6)
print(len(v1))   # 5
print(v1 == v2)  # False
```

---

## 🗺️ Quick Reference Cheat Sheet

```
🧬 Inheritance     → class Child(Parent):
🦸 super()         → super().__init__() / super().method()
🔄 Overriding      → redefine parent method in child
🔒 Encapsulation   → self.__var, @property, getters/setters
🖨️ __str__         → def __str__(self): return "..."
🚫 Abstract        → from abc import ABC, abstractmethod
🎭 Polymorphism    → same method name, different behavior
🦆 Duck Typing     → behavior over type, no inheritance needed
🔗 Aggregation     → passed in, lives independently
🧱 Composition     → created inside, dies together
📦 Nested Class    → class inside a class
⚙️ Static Method   → @staticmethod, no self or cls
🏛️ Class Method    → @classmethod, uses cls
```

---

## ⚡ Pro Tips & Tricks

> 🧪 **Use `vars(obj)`** to see all attributes of an object as a dict

> 🔍 **Use `dir(obj)`** to list ALL methods and attributes available

> 🧬 **Use `obj.__class__.__name__`** to get the class name as a string

> 🏗️ **Use `__slots__`** to restrict attributes and save memory in large-scale apps

> 🎯 **Favor composition over inheritance** when the relationship is "has-a" not "is-a"

> 🏭 **`@classmethod` as Factory** — most Pythonic way to provide multiple constructors (`from_string`, `from_json`, `from_dict`)

> 🦆 **Prefer Duck Typing** over `isinstance()` checks — more flexible and Pythonic

> 🔍 **`__mro__`** — always check Method Resolution Order in multiple inheritance to avoid surprises

> 📦 **Use Nested Classes** sparingly — only when the inner class has zero meaning outside the outer one

> 🚫 **Abstract Classes** = perfect for defining APIs that other developers must implement

---

## ✅ What I Learned

- 🧬 Inheritance — single, multiple, multilevel
- 🦸 `super()` keyword to access parent class
- 🔄 Method Overriding — child redefines parent method
- 🔒 Encapsulation — private variables & `@property`
- 🖨️ `__str__` & `__repr__` dunder methods
- 🚫 Abstract Classes — blueprint with `ABC` & `@abstractmethod`
- 🎭 Polymorphism — same method, different behavior
- 🦆 Duck Typing — behavior over type
- 🔗 Aggregation — weak "has-a" relationship
- 🧱 Composition — strong "has-a" relationship
- 📦 Nested Classes — class inside a class
- ⚙️ Static Methods — utility, no `self` or `cls`
- 🏛️ Class Methods — works with class via `cls`

---

## 💡 Key Takeaways

- 🧬 Inheritance avoids code repetition — write once, reuse everywhere
- 🦸 Always use `super()` instead of hardcoding parent class name
- 🔒 Never expose sensitive data directly — use `@property` for controlled access
- 🎭 Polymorphism makes code flexible — one function works with many object types
- 🦆 Python doesn't care about type — only whether the method exists (Duck Typing)
- 🧱 Favor **Composition over Inheritance** when relationship is "has-a" not "is-a"
- 🚫 Use Abstract Classes to enforce a contract across child classes
- ⚙️ Use `@staticmethod` for utilities that don't need class or instance data
- 🏛️ Use `@classmethod` as a factory method for alternative constructors
- 📦 Use Nested Classes only when inner class has zero meaning outside outer class
- 🔀 Always check `__mro__` in Multiple Inheritance to avoid method confusion
- 💡 `__str__` is for users, `__repr__` is for developers — always define both
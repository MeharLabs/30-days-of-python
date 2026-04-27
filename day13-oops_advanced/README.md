## 📋 Day 13 — Quick Summary

### 🎯 Short Goal

Understand and learn OOP Advanced concepts in Python including Multiple & Multilevel Inheritance, Abstract Classes, Polymorphism, Duck Typing, Aggregation, Composition, Nested Classes, Static Methods, and Class Methods.

---

### 📚 Topics Covered
Inheritance, super(), Method Overriding, Encapsulation, __str__, Multiple & Multilevel Inheritance, Abstract Classes, Polymorphism, Duck Typing, Aggregation, Composition, Nested Classes, Static Methods, and Class Methods

---

### 🔨 What I Learned

✅ Inheritance — single, multiple, multilevel

✅ `super()` keyword to access parent class

✅ Method Overriding — child redefines parent method

✅ Encapsulation — private variables & `@property`

✅ `__str__` & `__repr__` dunder methods

✅ Abstract Classes — blueprint with `ABC` & `@abstractmethod`

✅ Polymorphism — same method, different behavior

✅ Duck Typing — behavior over type

✅ Aggregation — weak "has-a" relationship

✅ Composition — strong "has-a" relationship

✅ Nested Classes — class inside a class

✅ Static Methods — utility, no `self` or `cls`

✅ Class Methods — works with class via `cls`



## 🔑 Key Takeaways

- Inheritance avoids code repetition — write once, reuse everywhere
- Always use `super()` instead of hardcoding parent class name
- Never expose sensitive data directly — use `@property` for controlled access
- Polymorphism makes code flexible — one function works with many object types
- Python doesn't care about type — only whether the method exists (Duck Typing)
- Favor **Composition over Inheritance** when relationship is "has-a" not "is-a"
- Use Abstract Classes to enforce a contract across child classes
- Use `@staticmethod` for utilities that don't need class or instance data
- Use `@classmethod` as a factory method for alternative constructors
- Use Nested Classes only when inner class has zero meaning outside outer class
- Always check `__mro__` in Multiple Inheritance to avoid method confusion
- `__str__` is for users, `__repr__` is for developers — always define both


## ⏱️ Time Spent
~ 5.5 hrs
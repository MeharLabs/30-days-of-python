# ============================================
# 🐍 Day 12 - OOPs Basic
# 📅 Date: 24/04/2026
# 🎯 Goal: Understanding and absorbing Python OOP Basics. Using class, __init__, self, instance methods, and instance vs class variables from scratch.
# =============================================

# --- code starts from here ---


# class keyword
class Car:
    brand = "Toyota"  # class variable


my_car = Car()  # object/instance created from class
print(my_car.brand)  # Toyota


# __init__ constructor
class Dog:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age


dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name)  # Rex
print(dog2.name)  # Bella


# self Keyword
class Circle:
    def __init__(self, radius):
        self.radius = radius  # "this circle's" radius

    def area(self):
        return 3.14 * self.radius**2


c1 = Circle(5)
c2 = Circle(10)

print(c1.area())  # 78.5  → uses c1's radius
print(c2.area())  # 314.0 → uses c2's radius


# instance methods
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):  # instance method
        self.balance += amount
        print(f"💰 Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):  # instance method
        if amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            self.balance -= amount
            print(f"💸 Withdrew {amount}. Balance: {self.balance}")

    def show_balance(self):  # instance method
        print(f"🏦 {self.owner}'s balance: {self.balance}")


acc = BankAccount("Ali", 1000)
acc.deposit(500)  # 💰 Deposited 500. Balance: 1500
acc.withdraw(200)  # 💸 Withdrew 200. Balance: 1300
acc.show_balance()  # 🏦 Ali's balance: 1300


# class variable
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # ✅ modify via class name


c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)  # 3

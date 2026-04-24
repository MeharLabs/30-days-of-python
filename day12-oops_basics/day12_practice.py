# 🟢 Level 1 — Easy (just getting started)
# =======================================
# Q1. Create a Dog class with name and breed, and a method that prints "Rex is a Labrador".


class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def dog_breed(self):
        return f"{self.name} is a {self.breed}"


dog1 = Dog("Rex", "Labrador")
print(dog1.dog_breed())


# Q2. Create a Student class with a class variable school = "Python High" and instance variables name and grade.


class Student:
    school = "Python High"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


student1 = Student("John", 85)
print(student1.name)
print(student1.grade)
print(student1.school)

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q3. Create a Counter class that counts how many objects have been created using a class variable.


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)


# Q4. Create a Rectangle class with width and height, and methods to return area() and perimeter().
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


r1 = Rectangle(5, 5)
print(r1.area())
print(r1.perimeter())

# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================
# Create a BankAccount class with deposit() and withdraw() methods and track the balance.

class BankAccount :
    
    def __init__(self, owner, balance=0 ):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        f"Deposited {amount}. Balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"💸 Withdrew {amount}. Balance: {self.balance}")
    
    def show_balance(self):
        print(f"🏦 {self.owner}'s balance: {self.balance}")

acc = BankAccount("Ali", 1000)
acc.deposit(200)  
acc.withdraw(100)
acc.show_balance()
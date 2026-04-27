# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Create a class Vehicle with a method fuel_type(). Inherit Car from it, then inherit ElectricCar from Car. Override fuel_type() in ElectricCar to print "⚡ Electric". Create an object of ElectricCar and call the method.

from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def fuel_type(self):
        return "Fuel"


class Car(Vehicle):
    pass


class ElectricCar(Car):
    def fuel_type(self):
        return "⚡ Electric"


car1 = ElectricCar("M1", "Tesla")
print(car1.fuel_type())


# Create a BankAccount class with a private __balance. Add a @property to read it and a @property.setter that rejects negative deposits. Test both valid and invalid deposits.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return (f"Your balance is: {self.__balance}")

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            print("You can't do negative deposits!")
        else:
            self.__balance = new_balance


account = BankAccount(1000)

account.balance = 1500
print("Balance:", account.balance)

account.balance = -500
print("Balance:", account.balance)

# Create a Book class with title, author, pages. Define __str__ to print it nicely like:
# 📖 'Atomic Habits' by James Clear — 320 pages


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"📖 '{self.title}' by {self.author} — {self.pages} pages"


book1 = Book("Atomic Habits", "James Clear", "320")
print(book1)

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q4. Create a base class Employee with a method calculate_salary(). Create three child classes — FullTime, PartTime, Freelancer — each overriding calculate_salary() differently. Loop through a list of all three and call the method on each.


class Employee:

    def calculate_salary(self):
        return 0


class FullTime(Employee):
    def calculate_salary(self):
        return "Full-Time Salary: 100,000 USD"


class PartTime(Employee):
    def calculate_salary(self):
        return "Part-Time Salary:  8,000 USD"


class Freelancer(Employee):
    def calculate_salary(self):
        return "Freelance Salary:  75,000 USD"


employees = [
    FullTime(),
    PartTime(),
    Freelancer()
]

for emp in employees:
    print(emp.calculate_salary())

# Create an abstract class Appliance with abstract methods turn_on() and power_consumption(). Create two child classes WashingMachine and Refrigerator that implement both. Try instantiating Appliance directly and observe the error.


class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def power_consumption(self):
        pass


class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing Machine is ON"

    def power_consumption(self):
        return "Consumes 500W"


class Refrigerator(Appliance):

    def turn_on(self):
        return "Refrigerator is ON"

    def power_consumption(self):
        return "Consumes 200W"


machine1 = WashingMachine()
fridge1 = Refrigerator()

print(machine1.turn_on())
print(machine1.power_consumption())

print(fridge1.turn_on())
print(fridge1.power_consumption())


# Create a class Temperature with:

# A class variable unit = "Celsius"
# A class method set_unit(cls, unit) to change it
# A static method convert(value) that converts Celsius → Fahrenheit
# A normal __init__ storing a temperature value

class Temperature:
    unit = "Calsius"

    def __init__(self, value):
        self.temp = value

    @classmethod
    def set_unit(cls, unit):
        cls.unit = unit

    @staticmethod
    def convert(value):
        return (value * 1.8) + 32


temp1 = Temperature(25)

print("Original unit:", Temperature.unit)
print("Value stored:", temp1.value)

Temperature.set_unit("Fahrenheit")
print("Updated unit:", Temperature.unit)

print("Converted:", Temperature.convert(25), "°F")


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q8. Create three unrelated classes — Printer, Scanner, FaxMachine — each with a send_document(doc) method doing different things. Write a function office_send(device, doc) that works with any of them without checking type.

class Printer:
    def send_document(self, doc):
        print(f"🖨️ Printing document: {doc}")


class Scanner:
    def send_document(self, doc):
        print(f"📄 Scanning document: {doc}")


class FaxMachine:
    def send_document(self, doc):
        print(f"📠 Faxing document: {doc}")


def office_send(device, doc):
    device.send_document(doc)


printer = Printer()
scanner = Scanner()
fax = FaxMachine()

office_send(printer, "Report.pdf")
office_send(scanner, "ID Card")
office_send(fax, "Contract.pdf")

# Q9. 🔀 Multiple Inheritance + MRO
# Create classes A, B, C where both B and C inherit from A. All three have a method role(). Create class D(B, C). Call D().role() and also print D.__mro__ — explain which role() gets called and why.

class A:
    def role(self):
      print("This is A")

class B(A):
    def role(self):
      print("This is B")

class C(A):
    def role(self):
      print("This is C")

class D(B, C):
    pass

d = D()
d.role()
print(D.__mro__)
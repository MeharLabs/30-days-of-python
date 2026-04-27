# ============================================
# 🐍 Day 13 - OOPs Advanced
# 📅 Date: 27/04/2026
# 🎯 Goal: Understand and learn OOP Advanced concepts in Python including Multiple & Multilevel Inheritance, Abstract Classes, Polymorphism, Duck Typing, Aggregation, Composition, Nested Classes, Static Methods, and Class Methods. 🎯🐍
# =============================================

# --- code starts from here ---


# Inheritance (parent → child)


class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

cat.speak()

# multiple Inheritance (inherit from more than one parent class)
#                       C(A,B)


class Prey:
    def flee(self):
        print("This animal is fleeing")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.hunt()

# multilevel Inheritance (inherit from a parent which inherits from another parent)
#                         C(B) <- B(A) <- A


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()

# abstract class
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()

# super()

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
  def __init__(self,color, is_filled, radius):
      super().__init__(color, is_filled)
      self.radius = radius

class Square(Shape):
  def __init__(self,color, is_filled, width):
      super().__init__(color, is_filled)
      self.width = width

class Triangle(Shape):
  def __init__(self,color, is_filled, width, height):
      super().__init__(color, is_filled)
      self.width = width
      self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

# polymorphism: poly = many,
#               morphe = form
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(4), Square(5), Triangle(6,7)]

for shape in shapes:
    print(f"{shape.area()}cm^2")

# duck typing
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

# Aggregation 
class Library:
    def __init__(self, name):
      self.name = name
      self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return[f"{book.title} by {book.author}" for book in self.books]

class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit...", "J.R.R. Tolkein")

library.add_book(book1)
library.add_book(book2)

print(library.name)

for book in library.list_books():
    print(book)

# composition

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car1 = Car(make="Ford",model= "Mustang",horse_power= 500, wheel_size=18)
car2 = Car(make="Chevrolet",model= "Corvette",horse_power= 670, wheel_size=19)

print(car1.display_car())
print(car2.display_car())

# nested class

class Company:
  class Employee:
      def __init__(self, name, position):
          self.name = name
          self.position = position

      def get_details(self):
          return f"{self.name} {self.position}"
  
  def __init__(self, company_name):
      self.company_name = company_name
      self.employees = []

  def add_employee(self, name, position):
      new_employee = self.Employee(name, position)
      self.employees.append(new_employee)
  
  def list_employees(self):
      return [employee.get_details() for employee in self.employees]
  
company = Company("Krusty Krab")

company.add_employee("Eugene", "Manager")
company.add_employee("Sponge bob", "Cook")

for employee in company.list_employees():
    print(employee)

# static methods
class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
  
employee1 = Employee("Eugine", "Manager")  
employee2 = Employee("Spongebob", "Cook")  

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
        
# class methods
class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"


student1 = Student("Sponge bob", 3.2)
student2 = Student("Sandy", 3.8)

print(Student.get_count())
print(Student.get_average_gpa())

# magic methods
class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else: 
            return f"Key {key} not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)

print(book1)
print(book2)
print(book1 < book2)

# property
class Rectangle:
    
    def __init__(self, width, height):
        self._width = width
        self._height = height 

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3,4)

rectangle.width = 5
rectangle.height = 6

del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)
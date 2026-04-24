class Dog:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name)   # Rex
print(dog2.name)   # Bella
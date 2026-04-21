# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Write a program that asks the user to enter a number and divides 100 by it. Handle the case where the user enters 0 or a non-numeric value.

try:
    user_input = float(input("Enter a number: "))
    total = 100 / user_input
    print(total)
except (ZeroDivisionError):
    print("You can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")

# Q2. Open a file called data.txt and print its contents. Handle the case where the file doesn't exist using the correct exception.

try:
    file_name = "data.txt"

    with open(file_name, "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print(f"File {file_name} doesn't exist.")

# Q3. Given this list:
# items = ["apple", "banana", "cherry"]
# Ask the user for an index and print the item. Handle IndexError and ValueError separately.


try:
    items = ["apple", "banana", "cherry"]

    user_input = int(input("Enter index (0,1,2): "))
    print(items[user_input])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Please enter a valid number.")
   

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q6. Write a function safe_divide(a, b) that:

# Returns the result of a / b
# Raises a custom DivisionError with a helpful message if b is 0
# Handles TypeError if either argument is not a number

def safe_divide(a,b):
    try:
      if b == 0:
          raise DivisionError("Cannot divide by zero.")
      return a / b
    except TypeError:
        raise TypeError("Both inputs must be numbers.")
    
print(safe_divide(10, 2))     # 5.0


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q7. Create a custom exception called AgeError. Write a function set_age(age) that raises AgeError if the age is below 0 or above 150. Test it with a try/except block.

class AgeError(Exception):
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise AgeError("Age must be between 0 and 150.")
    
    return f"Age set to {age}"

try:
    user_age = int(input("Enter your age: "))
    result = set_age(user_age)
    print(result)

except AgeError as e:
    print("Invalid age:", e)

except ValueError:
    print("Please enter a valid number.")
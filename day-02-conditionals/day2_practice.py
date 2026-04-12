# =======================================
# 🐍 Day 2 Practice Questions — Conditionals
# =======================================

# 🟢 Level 1 — Easy (just getting started)
# =======================================
# Q1. Write a program that checks if a number is positive, negative, or zero.
number = 15

if number == 0:
    print("Number is Zero.")
elif number > 0:
    print("Number is Positive.")
else:
    print("Number is Negative.")


# Q2. Ask the user for their age and print whether they are a minor or adult.
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are an adult.")
else:
    print("You are minor.")


# Q3. Check if a number is even or odd.
number = 3

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# Q4. Take two numbers from the user and print the greater one.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    print(f"First Number is greater: {first_number}")
elif second_number > first_number:
    print(f"Second Number is greater: {second_number}")
else:
    print(f"Both Numbers are equal")


# Q5. Check if a given letter is a vowel or consonant.
letter = "b"
vowels = ["a", "e", "i", "o", "u"]

if letter in vowels:
    print(f"{letter} is the vowel")
else:
    print(f"{letter} is the consonant")


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q6. Write a program that takes marks as input and prints the grade (A, B, C, D, F).
marks = int(input("Enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Q7. Check if a year is a leap year or not.
year = 2026

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is the leap year.")

else:
    print(f"{year} is not the leap year.")


# Q8. Take 3 numbers and print the largest one.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number >= second_number and first_number >= third_number:
    print(f"{first_number} is the greater one.")
elif second_number >= first_number and second_number >= third_number:
    print(f"{second_number} is the greater one.")
else:
    print(f"{third_number} is the greater one.")

# Q9. Write a program that checks if a person can vote (age >= 18) and has an id (True/False).
person_age = int(input("Enter your age: "))
has_id = True

if person_age >= 18 and has_id:
    print("You can vote.")
else:
    print("You can't vote")

# Q10. Check if a number is divisible by both 3 and 5, only 3, only 5, or neither.
number = 18

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} number is divisible by both 3 and 5")
elif number % 3 == 0:
    print(f"{number} is divisible only by 3")
elif number % 5 == 0:
    print(f"{number} is divisible only by 5")
else:
    print(f"{number} number is not divisible by both 3 and 5")


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q11. Build a simple login system — check if username AND password both match.
username = "person123"
password = "anything"

correct_username = "person123"
correct_password = "person123"

if username == correct_username and password == correct_password:
    print("You logged in")

else:
    print("Credentials don't match")

# Q12. Write a program that takes a number and checks if it's between 1 and 100, and also if it's even or odd.
number = int(input("Enter the number between 1 and 100: "))

if 1 <= number <= 100:  # chain comparison
    if number % 2 == 0:
        print(f"{number} number is in range and even")
    else:
        print(f"{number} number is in range and odd")
else:
    print("Please enter the number from 1 to 100.")


# Q13. Take a day name as input and print if it's a weekday or weekend.

day = input("Write the day name: ")

if day == "Saturday" or day == "Sunday":
    print(f"{day} is the weekend day")
else:
    print(f"{day} is not the week day ")


# Q14. Write a calculator that takes two numbers and an operator (+, -, *, /) and performs the operation using conditionals.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(f"Result: {first_number} + {second_number} = {first_number + second_number}")
elif operator == "-":
    print(f"Result: {first_number} - {second_number} = {first_number - second_number}" )
elif operator == "*":
    print(f"Result: {first_number} * {second_number} = {first_number * second_number}" )
elif operator == "/":
    if second_number != 0:
        print(
            f"Result: {first_number} / {second_number} = {first_number / second_number}")
    else:
        print("Error: Can't divide by zero")
else:
    print("Invalid Operator")

# Q15. Build a program that checks a traffic light color (red, yellow, green) and tells the driver what to do.
light = input("Enter traffic light color (red, yellow, green): ")

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")

else:
    print("Invalid Color")

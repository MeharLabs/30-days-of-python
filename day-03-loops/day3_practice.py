# =======================================
# 🐍 Day 3 Practice Questions — Loops
# =======================================

# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Print numbers from 1 to 20 using a for loop.
for number in range(1, 21):
    print(f"Number: {number}")


# Q2. Print all even numbers from 1 to 50.
for number in range(1, 51):
    if number % 2 == 0:
        print(f"Numbers are even: {number}")


# Q3. Print the multiplication table of any number entered by the user.
user_input = int(input("Enter any number for its multiplication: "))

for number in range(1, 11):
    print(f"{user_input} x {number} = {user_input * number}")

# Q4. Loop through this list and print only the fruits that start with "a":
fruits = ["apple", "banana", "avocado", "cherry", "apricot", "grape"]

fruits = ["apple", "banana", "avocado", "cherry", "apricot", "grape"]

for fruit in fruits:
    if fruit.startswith("a"):
        print(f"Fruits start with the name 'a': {fruit}")


# Q5. Count how many times the letter "o" appears in this string using a loop:
text = "loops are cool tools for coding"

text = "loops are cool tools for coding"
count = 0

for ch in text:
    if ch == "o":
        count += 1

print(f"letter 'o' appears {count} times in this string.")

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q6. Write a program that asks the user to guess a secret number (7). Keep asking until they get it right. (Use a while loop)
secret_number = 7

while True:
    user_input = int(input("Guess a secret number from 1 to 10: "))
    if user_input == secret_number:
        print("You guessed it")
        break
    else:
        print("Try Again")


# Q7. Given a list of numbers, print the sum and average using a loop (without using sum()):
numbers = [10, 20, 30, 40, 50]
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number
average = total / len(numbers)

print(f"Final Total: {total}")
print(f"Final Average: {average}")


# Q8. Use a loop to reverse a string without using [::-1]:
word = "Python"

word = "Python"
reverse_word = ""

for ch in word:
    reverse_word = ch + reverse_word
print(reverse_word)


# Q9. Print this pattern using nested loops:
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# Q10. FizzBuzz 🎯 — Print numbers 1 to 50, but:
# Print "Fizz" for multiples of 3
# Print "Buzz" for multiples of 5
# Print "FizzBuzz" for multiples of both

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q11. Write a program that finds all prime numbers between 1 and 100.

for number in range(2, 101):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)


# Q12. Flatten this nested list into a single list using loops:
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = []

for sublist in nested:
    for num in sublist:
        flat.append(num)
print(flat)
    
# Q13. User will get 3 attempts, and will need to get "Glad we're on the same page" in three attempts. Otherwise "3 strikes. You're out!"

attempts = 0

while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts +=1
else: 
  print("3 strikes. You're out")

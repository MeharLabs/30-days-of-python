# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Store your full name in a string and print:
# Total length of the name
# Name in ALL CAPS
# Name in all lowercase

name = input("What is your full name: ")

print(f"The length of your name {name} is: {len(name)}")
print(f"Name in ALL CAPS is: {name.upper()}")
print(f"Name in all lower is: {name.lower()}")


# Q2. Given s = "Hello, World!", print:
# First character
# Last character
# Characters from index 2 to 7

s = "Hello, World!"

print(f"First Character of s is: {s[0]}")
print(f"Last Character of s is: {s[-1]}")
print(f"Characters from index 2 to 7 in s are: {s[2:8]}")


# Q3. Ask the user to enter their name and greet them using an f-string like:
# Hello, John! Welcome to Python. 🎉

user = input("Please enter your name: ")
print(f"Hello, {user}! Welcome to Python. 🎉")


# Q4. Given s = "  python is fun  ", remove the extra spaces from both sides and print the result.
s = "  python is fun  "
print(s.strip())


# Q5. Count how many times the letter "o" appears in "Hello, how are you doing today?"

string = "Hello, how are you doing today?"
print(string.count("o"))

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q6. Given s = "apple,banana,mango,grape", split it into a list and print each fruit on a new line.

s = "apple,banana,mango,grape"

fruits = s.split(",")

for fruit in fruits:
    print(fruit)

# Q7. Reverse the string "Python" using slicing.

string = "python"
print(string[::-1])


# Q8. Check if the string "racecar" is a palindrome (same forwards and backwards). Print "Yes" or "No".

string = "racecar"

if string[::-1] == string:
    print("Yes")
else:
    print("No")


# Q9. Given s = "i love python programming", convert it to Title Case and replace the word "python" with "🐍 Python".

s = "i love python programming"
print(s.title().replace("Python", "🐍 Python"))


# Q10. Ask the user to enter a sentence and print:
# Total number of words
# Total number of characters (without spaces)

sentence = input("Enter any sentence you would like: ")

# total words
words = sentence.split()
print(words)
print(f"Total words: {len(words)}")

# total characters
characters = sentence.replace(" ", "")
print(f"Total charcters: {len(characters)}")

# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q11. Write a program that counts the number of vowels and consonants in a user-inputted string. (ignore spaces)

user_input = input("Enter any sentence you would like: ").lower()
vowels = 'aeiou'
vowel_count = 0
consonant_count = 0

for char in user_input:
    if char == " ":
      continue
    elif char in vowels:
       vowel_count += 1
    elif char.isalpha():
       consonant_count +=1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


# Q12. Given a list ["Ali", "Sara", "Ahmed", "Zara"], join them into a single string separated by | and display:

# Ali | Sara | Ahmed | Zara

list = ["Ali", "Sara", "Ahmed", "Zara"]

result = " | ".join(list)
print(result)


# Q13. Ask the user to enter a string and check:

# Is it all digits? → isdigit()
# Is it all letters? → isalpha()
# Is it all uppercase? → isupper()
# Print results for all three checks.

text = input("Enter a string: ")

print("Is all digits?", text.isdigit())
print("Is all letters?", text.isalpha())
print("Is all uppercase?", text.isupper())

# Q14. Write a program that takes a sentence and replaces every vowel with *.

# "Hello World" → "H*ll* W*rld"

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
result = ""

for char in sentence:
    if char in vowels:
        result += "*"
    else:
        result += char

print(result)

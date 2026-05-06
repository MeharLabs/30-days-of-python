# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Extract all numbers from this string:
# "I have 3 cats, 2 dogs, and 10 fish"
import re

text = "I have 3 cats, 2 dogs, and 10 fish"

numbers = re.findall(r"\d+", text)

for num in numbers:
    print(num)


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# **Q2.** Validate if this is a valid email:
# "hello.world@gmail.com"

email = "hello.@world@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.(com|edu|net)$"

if re.search(pattern, email):
    print("valid email")
else:
    print("Invalid email")


# Q3. Replace all spaces with a hyphen '-' in:
# "Python is very fun to learn"

text = "Python is very fun to learn"

cleaned = re.sub(r"\s", "-", text)

print(cleaned)

# Q4. Extract all hashtags from:
# "I love #Python #coding and #regex"

text = "I love #Python #coding and #regex"

cleaned = re.findall(r"\#\w+", text)

for hash in cleaned:
    print(hash)

# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================


# Q5. Check if a string starts with "Hello":
# "Hello, my name is John"

text = "Hello, my name is John"

if re.match(r"Hello", text):
    print("Starts with Hello")
else:
    print("Does not start with Hello")


# Q6. Split this string by digits:
# "apple1banana2cherry3mango"

text = "apple1banana2cherry3mango"

result = re.split(r"\d", text)

print(result)

# 🟢 Level 1 — Easy (just getting started)
# =======================================


# Q1: Write a generator function even_numbers(n) that yields all even numbers from 0 to n.

def even_numbers(n):
  for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(100):
    print(num)



# Q2: Write a generator expression that yields the **cubes** of numbers from `1` to `10` and print each value using `next()`.

cubes = (i**3 for i in range(1, 11))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================


# Q3: Write a generator function fibonacci() that yields an infinite Fibonacci sequence. Use itertools.islice() to print only the first 10 numbers.

from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:          
        yield a          
        a, b = b, a + b

for num in islice(fibonacci(), 10):
    print(num)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================


# Q4: Write a generator function pipeline() that chains three generator expressions together:
# - Generate numbers 1 to 20
# - Filter only odd numbers
# - Square each odd number

# Print the final result as a list.

def pipeline():
    nums = (i for i in range(1, 21))        
    odds = (i for i in nums if i % 2 != 0)  
    squares = (i**2 for i in odds)          
    return squares                          

# Convert to list and print
result = list(pipeline())
print(result)
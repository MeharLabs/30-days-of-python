# ============================================
# 🐍 Day 17 - Generators
# 📅 Date: 04/05/2026
# 🎯 Goal: Understand how to use yield, generator functions, and expressions to write memory-efficient, lazy, and clean Python code that produces values on demand instead of all at once.
# =============================================

# --- code starts from here ---

# generator
import sys


def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)


# next() function
def gen():
    yield 1
    print("Pause 1")
    yield 2
    print("Pause 2")
    yield 3
    print("Pause 3")
    yield 4


x = gen()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# generators with list comprehensions
my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(my_nums)

for num in my_nums:
    print(num)

# iterator
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = map(lambda i: i**2, x)

print(sys.getsizeof(x))
print(sys.getsizeof(y))

print(next(y))
print(next(y))
print(next(y))
print(next(y))

for i in y:
    print(i)

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done")
        break

x = range(1,11)

print(next(iter(x)))

for i in iter(x):
    print(i)
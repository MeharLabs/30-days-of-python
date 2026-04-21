# ============================================
# 🐍 Day 09 - Error Handling
# 📅 Date: 21/04/2026
# 🎯 Goal: Understand Python Error Handling — not just knowing the syntax, but thinking like a developer who writes safe, reliable, and crash-proof code.
# =============================================

# --- code starts from here ---

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please!")
finally:
    print('Do some cleanup here')

# core structure (try / except / else / finally)

try:
    # 🔍 Code that might cause an error
    result = 10 / 0

except ZeroDivisionError:
    # 🚨 What to do IF that specific error occurs
    print("You can't divide by zero!")

else:
    # ✅ Runs ONLY if NO exception occurred
    print(f"Result: {result}")

finally:
    # 🔒 ALWAYS runs — error or not (cleanup code goes here)
    print("Done!")

# catch multiple exceptions
try:
    x = int(input("Enter a number: "))
    print(10 / x)

except (ValueError, ZeroDivisionError) as e:
    print(f"Error caught: {e}")

# catch all exceptions
try:
    risky_code()

except Exception as e:       # catches almost everything
    print(f"Something went wrong: {e}")

# raise

age = -1

if age < 0:
    raise ValueError("Age cannot be negative! 🚫")
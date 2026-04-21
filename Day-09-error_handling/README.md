## 📋 Day 9 — Quick Summary

### 🎯 Short Goal
Understand Python Error Handling — not just knowing the syntax, but thinking like a developer who writes safe, reliable, and crash-proof code.

---

### 📚 Topics Covered
Python Error Handling — from basic try/except structure to built-in exceptions, raise, and custom exceptions

---

### 🔨 What I Learned / Built

✅ Error handling prevents programs from crashing unexpectedly
✅ Errors in Python are called Exceptions
✅ The core structure is try / except / else / finally
✅ try block contains the risky code
✅ except block runs only if an error occurs
✅ else block runs only if no error occurred
✅ finally block always runs — error or not
✅ Always catch specific exceptions before broad ones
✅ Common exceptions — ValueError, TypeError, IndexError, KeyError, ZeroDivisionError, FileNotFoundError
✅ All exceptions inherit from BaseException
✅ Use as e to capture and read the error message
✅ Multiple exceptions can be caught in one line using a tuple
✅ Never use bare except: — it hides real problems
✅ raise is used to manually trigger an exception
✅ raise inside an except block re-raises the same error
✅ Custom exceptions are made by inheriting from Exception
✅ with statement handles errors and closes resources automatically
✅ finally is the best place for cleanup code
✅ Never silently ignore errors — always log them at minimum
✅ Error handling is what separates beginner code from professional code


## 🔑 Key Takeaways

🎯 Be specific — always catch the most specific exception, not everything blindly

🔕 Never silence errors — at minimum, log them

🧱 Custom exceptions make code readable and maintainable

🔁 finally is your cleanup hero — always use it for resources

🚫 Never use bare except: — it hides real problems


## ⏱️ Time Spent
~ 2 hrs
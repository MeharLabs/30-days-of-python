## 📋 Day 22 — Quick Summary

### 🎯 Short Goal
To learn how to write automated tests in Python using pytest - covering why testing matters, how to write test functions with the test_ naming convention, use assert statements to verify code behavior, and run tests from the terminal.

### 📚 Topics Covered

**What is Testing**, **Why Testing Matters**, **What is Pytest**, **Assert Statements**, **Test Function Naming with `test_`**, **Running Pytest in Terminal**, **Pytest Methods & Features**, **Recommended Project Structure**, and **Tips & Tricks**.

### 🔨 What I Learned

✅  **What pytest is** and how it differs from manual testing

✅  **Why testing matters** — catching bugs early, refactoring safely, and saving time

✅  **Assert statements** — the heart of every test, checking if conditions are True

✅  **Test naming convention** — functions and files must start with `test_`

✅  **Running pytest in terminal** — using flags like `-v`, `-x`, `-s`, `-k` etc.

✅  **parametrize** — running one test function with multiple inputs

✅  **Fixtures** — reusable setup code injected into test functions

✅  **conftest.py** — sharing fixtures across multiple test files

✅  **pytest.raises()** — testing that exceptions are raised correctly

✅  **Skipping tests** — using `@pytest.mark.skip` and `@pytest.mark.xfail`

✅  **Project structure** — organizing `src/` and `tests/` folders properly

✅  **Tips & Tricks** — like `approx` for floats, `capsys` for output, and `tmp_path` for files


## 🔑 Key Takeaways

-  **Tests are a safety net** — they protect your code from breaking when you make changes or add new features
-  **Automate over manual** — running `pytest` once beats manually printing and checking outputs every time
-  **Naming is everything** — pytest won't find your tests if they don't start with `test_`
-  **Assert is simple but powerful** — one line can verify equality, types, exceptions, membership and more
-  **parametrize saves repetition** — instead of writing 10 similar tests, write one with multiple inputs
-  **Fixtures keep tests clean** — reusable setup code means no copy-pasting across test functions
-  **One idea per test** — focused, small tests are easier to debug than large ones testing everything at once
-  **Structure matters** — keeping `tests/` separate from `src/` keeps your project organized and professional
-  **Test edge cases too** — zero values, negative numbers, empty inputs, and exceptions are just as important as happy paths
-  **Good tests = confidence** — when all tests pass, you can ship code knowing it works as expected

## ⏱️ Time Spent
~ 2.0 hrs
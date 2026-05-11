# 🧪 Day 22 - Testing with Pytest

## 🎯 Goal

To learn how to write automated tests in Python using **pytest** — covering why testing matters, how to write test functions with the `test_` naming convention, use `assert` statements to verify code behavior, and run tests from the terminal.


## 🤔 What is Testing?

**Testing** is the process of writing code that **verifies your code works correctly**. Instead of manually running your program and checking outputs, you write automated checks that do it for you — every single time.

> 💡 Think of it like a **safety net** — before shipping code, your tests catch bugs automatically.

```python
# Without testing — you manually check every time 😫
result = add(2, 3)
print(result)  # Is it 5? Hope so...

# With testing — automated, instant feedback ✅
def test_add():
    assert add(2, 3) == 5  # Either passes or fails clearly
```


## ❓ Why Testing Matters

| Reason | Explanation |
|---|---|
| 🐛 **Catch bugs early** | Find errors before they reach production |
| 🔁 **Refactor safely** | Change code without fear of breaking things |
| 📖 **Documents behavior** | Tests show *how* your code is supposed to work |
| 🤝 **Team confidence** | Everyone knows what's working and what's not |
| ⚡ **Saves time** | Automated > manual testing every time |


## 🚀 What is Pytest?

**pytest** is the most popular Python testing framework. It's simple, powerful, and requires minimal boilerplate compared to the built-in `unittest` module.

```bash
# Install pytest
pip install pytest

# Check version
pytest --version
```

### 🆚 pytest vs unittest

```python
# ❌ unittest — verbose and clunky
import unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# ✅ pytest — clean and simple
def test_add():
    assert add(2, 3) == 5
```

---

## ✅ Assert Statements

`assert` is the **heart of every test**. It checks if a condition is `True` — if not, the test **fails** with a clear error.

### 📌 Basic Syntax

```python
assert expression          # Simple check
assert expression, "msg"   # With custom failure message
```

### 🔢 Common Assert Patterns

```python
# ✅ Equality
assert add(2, 3) == 5
assert name == "Alice"

# ❌ Inequality
assert result != 0
assert status != "error"

# 📏 Comparisons
assert age >= 18
assert price < 100

# 🔍 Membership
assert "admin" in roles
assert "banned_user" not in users

# 🔘 Boolean checks
assert is_valid == True
assert is_empty == False
assert is_active        # shorthand for True
assert not is_deleted   # shorthand for False

# 🧱 Type checks
assert isinstance(result, int)
assert isinstance(name, str)

# 📦 None checks
assert result is not None
assert empty_var is None

# 📐 Length checks
assert len(my_list) == 3
assert len(response) > 0
```

### 💬 Custom Failure Messages

```python
def test_age_validation():
    age = get_user_age()
    assert age >= 0, f"❌ Age cannot be negative! Got: {age}"
    assert age <= 150, f"❌ Age too large to be real! Got: {age}"
```

---

## 🏷️ Test Function Naming — `test_`

pytest **automatically discovers** test files and functions using naming conventions. This is called **test discovery**.

### 📁 File Naming Rules

```
✅ test_calculator.py      ← pytest finds this
✅ calculator_test.py      ← pytest finds this too
❌ calculator.py           ← NOT picked up
❌ check_calculator.py     ← NOT picked up
```

### 🔤 Function Naming Rules

```python
# ✅ VALID — starts with test_
def test_add():         pass
def test_subtract():    pass
def test_empty_input(): pass

# ❌ INVALID — pytest ignores these
def add_test():         pass   # wrong position
def check_add():        pass   # wrong prefix
def adding():           pass   # no test_ at all
```

### 🏗️ Full Example

```python
# test_calculator.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# 🧪 Tests below

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)
```

> 💡 **Naming tip:** Be descriptive! `test_add_two_positive_numbers` is better than `test_add`.

---

## 💻 Running Pytest in Terminal

### ▶️ Basic Commands

```bash
pytest                                    # Run ALL tests
pytest test_calculator.py                 # Run a specific file
pytest test_calculator.py::test_add       # Run a specific function
pytest -v                                 # Verbose output
pytest -vv                                # Very verbose output
```

### 📊 Reading Terminal Output

```bash
$ pytest -v

===== test session starts =====
collected 4 items

test_calculator.py::test_add_positive_numbers  PASSED  ✅
test_calculator.py::test_add_negative_numbers  PASSED  ✅
test_calculator.py::test_add_zero              PASSED  ✅
test_calculator.py::test_divide_by_zero        FAILED  ❌

===== 3 passed, 1 failed in 0.12s =====
```

### 🛠️ Useful Terminal Flags

```bash
pytest -q                  # 🔇 Quiet mode
pytest -x                  # 🛑 Stop at first failure
pytest --maxfail=3         # 🛑 Stop after 3 failures
pytest -s                  # 🖨️ Show print() output
pytest -k "add"            # 🔍 Run tests matching keyword
pytest -k "not divide"     # 🔍 Skip tests matching keyword
pytest --durations=5       # 📋 Show 5 slowest tests
pytest --lf                # 🔁 Re-run last failed tests
pytest -W error            # ⚠️ Show warnings
```

---

## 🗂️ Pytest Methods & Features

### 1️⃣ `pytest.raises()` — Testing Exceptions

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0

def test_value_error_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
```

### 2️⃣ `pytest.mark.skip` — Skip Tests

```python
@pytest.mark.skip(reason="Feature not implemented yet 🚧")
def test_future_feature():
    assert some_future_function() == 42

@pytest.mark.skipif(condition=True, reason="Skip on this platform")
def test_platform_specific():
    pass
```

### 3️⃣ `pytest.mark.parametrize` — Multiple Inputs 🔥

```python
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
# Runs 4 separate tests with one function! 🎯
```

### 4️⃣ `fixtures` — Reusable Setup Code 🔧

```python
@pytest.fixture
def sample_user():
    return {"name": "Alice", "age": 30, "role": "admin"}

def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

def test_user_is_admin(sample_user):
    assert sample_user["role"] == "admin"
```

### 5️⃣ `conftest.py` — Shared Fixtures Across Files 📁

```python
# conftest.py — pytest loads this automatically!
@pytest.fixture
def db_connection():
    conn = create_test_database()
    yield conn          # 👈 yield = setup/teardown
    conn.close()        # runs AFTER every test
```

### 6️⃣ `pytest.mark.xfail` — Expected Failures

```python
@pytest.mark.xfail(reason="Known bug #123 🐛")
def test_known_broken_feature():
    assert broken_function() == 42
# Shows as 'x' not 'F'
```

---

## 📁 Recommended Project Structure

```
my_project/
│
├── src/
│   ├── calculator.py
│   ├── utils.py
│   └── models.py
│
├── tests/
│   ├── conftest.py          ← shared fixtures
│   ├── test_calculator.py
│   ├── test_utils.py
│   └── test_models.py
│
├── pytest.ini               ← pytest config
└── requirements.txt
```

### ⚙️ pytest.ini Configuration

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

---

## 💡 Tips & Tricks

```python
# 🎯 Tip 1 — One assert idea per test
def test_user_created():
    user = create_user("Alice")
    assert user.name == "Alice"

# 🏷️ Tip 2 — Use markers to group tests
@pytest.mark.slow
def test_heavy_computation(): ...
# pytest -m "not slow"   → skip slow tests
# pytest -m "api"        → run only api tests

# 🧹 Tip 3 — Use tmp_path for temp files
def test_file_creation(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"

# 📸 Tip 4 — Capture output with capsys
def test_print_output(capsys):
    print("Hello World")
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

# 🔢 Tip 5 — approx for floating point
from pytest import approx
def test_float_math():
    assert 0.1 + 0.2 == approx(0.3)  # ✅
    # assert 0.1 + 0.2 == 0.3        # ❌ FAILS
```

---

## 🗺️ Quick Reference Cheat Sheet

```
pytest                      → run all tests
pytest -v                   → verbose output
pytest -x                   → stop at first fail
pytest -k "keyword"         → filter by name
pytest -s                   → show print output
pytest --lf                 → re-run last failures
pytest --durations=5        → show 5 slowest tests

assert a == b               → equality
assert a != b               → inequality
assert a in b               → membership
assert isinstance(a, type)  → type check
pytest.raises(Error)        → exception testing
@pytest.mark.parametrize    → multiple inputs
@pytest.fixture             → reusable setup
@pytest.mark.skip           → skip a test
@pytest.mark.xfail          → expected failure
```

---

## 📝 What I Learned

- 🧪 **What pytest is** and how it differs from manual testing
- ❓ **Why testing matters** — catching bugs early, refactoring safely, and saving time
- ✅ **Assert statements** — the heart of every test, checking if conditions are True
- 🏷️ **Test naming convention** — functions and files must start with `test_`
- 💻 **Running pytest in terminal** — using flags like `-v`, `-x`, `-s`, `-k` etc.
- 🔥 **parametrize** — running one test function with multiple inputs
- 🔧 **Fixtures** — reusable setup code injected into test functions
- 📁 **conftest.py** — sharing fixtures across multiple test files
- 🐛 **pytest.raises()** — testing that exceptions are raised correctly
- ⏭️ **Skipping tests** — using `@pytest.mark.skip` and `@pytest.mark.xfail`
- 📁 **Project structure** — organizing `src/` and `tests/` folders properly
- 💡 **Tips & Tricks** — like `approx` for floats, `capsys` for output, and `tmp_path` for files

---

## 🏁 Key Takeaways

- 🛡️ **Tests are a safety net** — they protect your code from breaking when you make changes or add new features
- 🤖 **Automate over manual** — running `pytest` once beats manually printing and checking outputs every time
- 📝 **Naming is everything** — pytest won't find your tests if they don't start with `test_`
- 💬 **Assert is simple but powerful** — one line can verify equality, types, exceptions, membership and more
- 🔁 **parametrize saves repetition** — instead of writing 10 similar tests, write one with multiple inputs
- 🔧 **Fixtures keep tests clean** — reusable setup code means no copy-pasting across test functions
- 🎯 **One idea per test** — focused, small tests are easier to debug than large ones testing everything at once
- 🏗️ **Structure matters** — keeping `tests/` separate from `src/` keeps your project organized and professional
- 🐛 **Test edge cases too** — zero values, negative numbers, empty inputs, and exceptions are just as important as happy paths
- 🚀 **Good tests = confidence** — when all tests pass, you can ship code knowing it works as expected

---

🏁 **Golden Rule of Testing:** Write tests that are **F.I.R.S.T** — **Fast**, **Independent**, **Repeatable**, **Self-validating**, **Timely**. A good test suite is as important as the code itself! 🚀
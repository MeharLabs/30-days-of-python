# 🐍 Day 23 — Python Type Hints
**Goal:** Understand and apply Python Type Hints from annotations to types and learn how `mypy` catches bugs before runtime to write safer, cleaner, and more maintainable code.


## 📌 What Are Type Hints?

Type hints are **annotations** in Python that tell you (and tools) what **data type** a variable, parameter, or return value is expected to be.

> Python is **dynamically typed** — but type hints let you add **optional static typing** for clarity, safety, and tooling support.

```python
# Without type hints 😕
def greet(name):
    return "Hello, " + name

# With type hints 😍
def greet(name: str) -> str:
    return "Hello, " + name
```

> ⚠️ Type hints are **NOT enforced at runtime** — Python still runs even if types mismatch. They're for **humans + tools**, not the interpreter.


## 🧱 Basic Type Hints — `int`, `str`, `bool`

```python
# Variable annotations
age: int = 25
name: str = "Ali"
is_active: bool = True
price: float = 9.99

# Function parameters + return types
def add(a: int, b: int) -> int:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0

def get_username(user_id: int) -> str:
    return f"user_{user_id}"
```

| Type    | Meaning          |
|---------|------------------|
| `int`   | Integer numbers  |
| `str`   | Text / strings   |
| `bool`  | True or False    |
| `float` | Decimal numbers  |
| `bytes` | Raw byte data    |
| `None`  | No return value  |


## 📦 `List`, `Dict`, `Optional` Types

### 🔹 List
```python
from typing import List

def get_scores(names: List[str]) -> List[int]:
    return [len(name) for name in names]

scores: List[int] = [90, 85, 100]
```

🆕 Python 3.9+ shortcut: use `list[str]` instead of `List[str]`

```python
# Python 3.9+ — no import needed!
def get_names() -> list[str]:
    return ["Ali", "Sara", "Ahmed"]
```

### 🔹 Dict
```python
from typing import Dict

user: Dict[str, int] = {"Ali": 25, "Sara": 30}

def word_count(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

### 🔹 Optional — when a value can be `None`
```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Ali", 2: "Sara"}
    return users.get(user_id)  # Returns str or None

# Optional[str] is the same as Union[str, None]
```

### 🔹 Tuple, Set
```python
from typing import Tuple, Set

def get_point() -> Tuple[int, int]:
    return (10, 20)

def unique_tags(tags: List[str]) -> Set[str]:
    return set(tags)
```

### 🔹 Union — multiple possible types
```python
from typing import Union

def parse_input(value: Union[str, int]) -> str:
    return str(value)

# Python 3.10+ shortcut:
def parse_input(value: str | int) -> str:
    return str(value)
```

### 🔹 Any — escape hatch (use sparingly!)
```python
from typing import Any

def process(data: Any) -> Any:
    return data  # 🚨 Loses all type safety — avoid if possible
```

---

## 🔁 Function Return Types

```python
# Returns nothing
def log_message(msg: str) -> None:
    print(f"[LOG]: {msg}")

# Returns a value
def multiply(a: float, b: float) -> float:
    return a * b

# Returns Optional
def divide(a: int, b: int) -> Optional[float]:
    if b == 0:
        return None
    return a / b

# Returns a List
def repeat(word: str, times: int) -> List[str]:
    return [word] * times
```

---

## 🧩 More Typing Tools

### 🔹 `TypedDict` — typed dictionaries
```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

def create_user(data: User) -> str:
    return f"{data['name']} ({data['age']})"

user: User = {"name": "Ali", "age": 25, "email": "ali@example.com"}
```

### 🔹 `Callable` — for functions as arguments
```python
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

apply(lambda x, y: x + y, 3, 5)  # ✅
```

### 🔹 `ClassVar` — class-level vs instance variables
```python
from typing import ClassVar

class Config:
    MAX_USERS: ClassVar[int] = 100  # class variable
    name: str                        # instance variable
```

### 🔹 `Final` — constant values
```python
from typing import Final

MAX_RETRIES: Final = 3
# MAX_RETRIES = 5  ← mypy will catch this! 🚨
```

### 🔹 `Literal` — only specific values allowed
```python
from typing import Literal

def set_direction(dir: Literal["left", "right", "up", "down"]) -> None:
    print(f"Moving {dir}")

set_direction("left")   # ✅
set_direction("back")   # ❌ mypy error
```

### 🔹 Generics — reusable typed functions
```python
from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

first_item([1, 2, 3])    # returns int
first_item(["a", "b"])   # returns str
```

### 🔹 `dataclass` with type hints
```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True

p = Product("Laptop", 999.99)
print(p.name)   # "Laptop"
```

---

## 🔍 `mypy` — Static Type Checker

`mypy` reads your code **without running it** and finds type errors.

### 📥 Install
```bash
pip install mypy
```

### ▶️ Run
```bash
mypy your_file.py
mypy your_project/          # whole folder
mypy --strict your_file.py  # strictest mode
```

### 💥 Example — mypy catching a bug
```python
# buggy.py
def double(n: int) -> int:
    return n * 2

result = double("hello")  # 🚨 passing str instead of int
```
```bash
$ mypy buggy.py
buggy.py:4: error: Argument 1 to "double" has incompatible type "str"; expected "int"
```

### ⚙️ `mypy.ini` config file
```ini
[mypy]
strict = true
ignore_missing_imports = true
disallow_untyped_defs = true
warn_return_any = true
```

---

## 🧪 Type Hints + Python Testing

### ✅ With `pytest`
```python
# calculator.py
def add(a: int, b: int) -> int:
    return a + b

# test_calculator.py
from calculator import add

def test_add_integers() -> None:
    assert add(2, 3) == 5

def test_add_negative() -> None:
    assert add(-1, 1) == 0
```

### ✅ With `pytest` + type-checked fixtures
```python
import pytest

@pytest.fixture
def sample_data() -> list[int]:
    return [1, 2, 3, 4, 5]

def test_sum(sample_data: list[int]) -> None:
    assert sum(sample_data) == 15
```

### ✅ `Protocol` for duck typing
```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable) -> None:
    obj.draw()

# Any class with .draw() satisfies this — no inheritance needed! 🦆
```

---

## 💡 Tips & Tricks

| 💡 Tip | Details |
|--------|---------|
| 🔸 Start gradually | Add hints to new functions first — don't rewrite everything |
| 🔸 Use `reveal_type()` | Inside mypy run — shows inferred type of a variable |
| 🔸 Avoid `Any` | It disables type checking — defeats the purpose |
| 🔸 `Optional[X]` = `X \| None` | Use whichever is clearer to you |
| 🔸 Use `--strict` on CI | Catch type errors in your pipeline automatically |
| 🔸 Type aliases | `Vector = list[float]` — name complex types for readability |
| 🔸 `TYPE_CHECKING` guard | Import types only during checking, not at runtime |

```python
# TYPE_CHECKING trick — avoids circular imports at runtime
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mymodule import HeavyClass

def process(obj: "HeavyClass") -> None:
    ...
```

---

## 🏗️ Why Type Hints Help Big Codebases

```
Small script (50 lines)     →  type hints: optional luxury
Medium project (5k lines)   →  type hints: strongly recommended
Large codebase (50k+ lines) →  type hints: ESSENTIAL 🔥
```

| 🎯 Benefit | Why It Matters |
|-----------|----------------|
| 🐛 Catch bugs early | Before runtime, before tests even run |
| 📖 Self-documenting code | Types ARE the documentation |
| 🤝 Team collaboration | New devs understand code instantly |
| 🔧 Better IDE support | Autocomplete, jump-to-def, refactoring |
| 🔄 Safe refactoring | Change a type → mypy tells you every broken place |
| ⚡ Faster code reviews | Reviewers see intent without reading full logic |
| 🧪 Better tests | Types guide what inputs/outputs to test |

---

## 🗺️ Quick Reference Cheat Sheet

```python
from typing import Optional, Union, List, Dict, Tuple
from typing import Callable, TypeVar, Literal, Final
from typing import TypedDict, Protocol

# Variables
x: int = 5
name: str = "Ali"
flag: bool = True

# Functions
def func(a: int, b: str = "default") -> Optional[bool]: ...

# Collections (Python 3.9+)
nums: list[int] = []
mapping: dict[str, int] = {}
pair: tuple[int, str] = (1, "a")

# Flexible
val: int | str | None = None     # Python 3.10+

# Constant
MAX: Final[int] = 100

# Type alias
Matrix = list[list[float]]
```

---

## 📚 What I Learned

- 🏷️ **Type hints** are optional annotations that tell what data type a variable or function expects
- 🔤 **Basic types** like `int`, `str`, `bool`, `float` can annotate variables and function parameters
- 📋 **`List`, `Dict`, `Tuple`** let you type collections with specific inner types
- ❓ **`Optional`** means a value can be its type **or** `None`
- 🔀 **`Union`** allows multiple possible types for one variable
- 🔁 **Return types** are declared with `->` arrow syntax in functions
- 🔍 **`mypy`** is a static checker that catches type errors **without running the code**
- 🧪 **Type hints + pytest** work together to write cleaner, more reliable tests
- 📝 **`TypedDict`** lets you define dictionaries with specific key-value types
- 🔒 **`Final`** marks constants that should never be reassigned
- 🎯 **`Literal`** restricts a variable to only specific allowed values
- 🦆 **`Protocol`** enables duck typing in a type-safe way
- 🏗️ Type hints are **essential in big codebases** for safety, readability, and team collaboration
- 💡 **Avoid `Any`** — it disables type checking and defeats the purpose

---

## 🎯 Key Takeaways

- 🐍 Python is **dynamically typed** but type hints add **optional static typing**
- ⚠️ Type hints are **NOT enforced at runtime** — they're for humans and tools only
- 🔍 **`mypy`** catches bugs **before** running or testing your code
- 📖 Type hints act as **self-documenting code** — no extra comments needed
- 🛡️ They **prevent whole bug categories** before tests even run
- 🤝 Makes **team collaboration easier** — new devs understand code instantly
- 🔄 Makes **refactoring safer** — change a type and mypy shows every broken spot
- ⚡ Better **IDE support** — autocomplete, jump-to-definition, smarter suggestions
- 🚀 Start **gradually** — add hints to new functions first, don't rewrite everything
- ❌ **Avoid `Any`** — it kills type safety and defeats the whole purpose
- 📦 Use **`Optional`** when a value can be `None` — don't ignore it
- 🏗️ The **bigger the codebase**, the more valuable type hints become
- 🧪 Type hints + **pytest** = cleaner, more reliable, self-explanatory tests
- 💡 Run **`mypy --strict`** in CI/CD pipeline to catch errors automatically

---
# Day 10 — Python Modules & Imports 🐍


## 🎯 Goal

Understand how Python modules and imports work — how to create my own modules, use built-in ones like `math`, `random`, `os` and `datetime`, and learn how to import code efficiently using `import`, `from...import`, and `importlib` so that I can write cleaner, more organized, and reusable Python code. 💪🐍


## 📦 What is a Module?

A **module** is simply a Python file (`.py`) that contains code — functions, classes, variables — that you can **reuse** in other programs. Instead of rewriting the same code everywhere, you put it in a module and import it wherever you need it.

🧰 Think of a module as a **toolbox** — you open it and grab the tool you need.

```python
# mytools.py  ← this IS a module
def greet(name):
    return f"Hello, {name}!"
```


## 📥 What is an Import?

An **import** is how you bring a module's code into your current file so you can use it.

```python
import mytools
print(mytools.greet("Ali"))  # Hello, Ali!
```


## 🔑 Ways to Import

### 1️⃣ Basic Import
```python
import math
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
```

### 2️⃣ Import with Alias `as` — give it a nickname
```python
import numpy as np
import pandas as pd   # industry standard short names!
```

### 3️⃣ Import specific items with `from`
```python
from math import sqrt, pi
print(sqrt(25))  # 5.0  ← no need to write math.sqrt
```

### 4️⃣ Import everything with `*` ⚠️ (use carefully!)
```python
from math import *
print(sin(0))    # works, but pollutes your namespace!
```

---

## 🗂️ Types of Modules

| Type | Description | Example |
|------|-------------|---------|
| 🏛️ **Built-in** | Come with Python, always available | `math`, `os`, `sys`, `random` |
| 📚 **Standard Library** | Included with Python install | `datetime`, `json`, `re`, `csv` |
| 🌍 **Third-party** | Install via `pip` | `numpy`, `pandas`, `requests` |
| 🏠 **Custom/Local** | Your own `.py` files | `mymodule.py` |

---

## 🛠️ Useful Built-in Modules

```python
import math
math.sqrt(9)       # 3.0
math.floor(4.7)    # 4
math.ceil(4.2)     # 5
math.pow(2, 10)    # 1024.0

import random
random.randint(1, 10)        # random number 1–10
random.choice(["a","b","c"]) # picks random item
random.shuffle(my_list)      # shuffles in place

import os
os.getcwd()           # current working directory
os.listdir(".")       # list files in folder
os.path.exists("x")  # check if file/folder exists

import sys
sys.version   # Python version
sys.argv      # command-line arguments

import datetime
datetime.date.today()      # today's date
datetime.datetime.now()    # current date + time

import json
json.dumps({"a": 1})    # dict → JSON string
json.loads('{"a":1}')   # JSON string → dict
```

---

## 🔍 Key Methods & Functions

### `dir()` — see everything inside a module 👀
```python
import math
print(dir(math))
# ['__doc__', 'ceil', 'cos', 'floor', 'pi', 'sqrt', ...]
```

### `help()` — read the docs inline 📖
```python
help(math.sqrt)
```

### `__name__` — check if file is run directly or imported
```python
if __name__ == "__main__":
    print("Running directly!")
else:
    print("I was imported!")
```
> 💡 One of the most important Python patterns you'll ever learn!

### `__file__` — find where a module lives
```python
import math
print(math.__file__)
```

### `__doc__` — read the module's docstring
```python
import math
print(math.__doc__)
```

---

## 📁 Packages — Modules on Steroids

A **package** is a **folder** of modules with a special `__init__.py` file inside it.

```
mypackage/
│── __init__.py      ← makes it a package
│── greetings.py
│── farewell.py
```

```python
from mypackage import greetings
from mypackage.farewell import bye_message
```

---

## 🧹 Best Practices

### ✅ Import order — PEP8 convention
```python
# 1. Standard library
import os
import sys

# 2. Third-party libraries
import numpy as np
import requests

# 3. Your own modules
import mymodule
```

### ✅ Only import what you need
```python
# ❌ Bad
from math import *

# ✅ Good
from math import sqrt, pi
```

### ✅ Avoid circular imports 🔄
Don't have `module_a.py` import `module_b.py` while `module_b.py` also imports `module_a.py` — this causes errors!

### ✅ Use aliases for long names
```python
import matplotlib.pyplot as plt
```

---

## 💎 Pro Tips & Tricks

🔹 **Dynamic import with `importlib`**
```python
import importlib
mod = importlib.import_module("math")
print(mod.pi)
```

🔹 **Lazy imports** — speed up startup time
```python
def process():
    import pandas as pd   # only loads when function is called
```

🔹 **Safely check if module is installed**
```python
try:
    import numpy
    print("numpy is available ✅")
except ImportError:
    print("numpy not installed ❌")
```

🔹 **`sys.path`** — where Python looks for modules
```python
import sys
print(sys.path)
sys.path.append("/my/custom/folder")
```

🔹 **`sys.argv`** — pass command-line arguments
```python
import sys
if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}!")
else:
    print("No name given!")
```

---

## 🧠 Quick Recap Table

| Concept | What it does |
|---------|--------------|
| `import module` | Load full module |
| `from module import x` | Load specific item |
| `import module as alias` | Load with a nickname |
| `dir(module)` | See what's inside |
| `help(module)` | Read docs |
| `__name__` | Check run context |
| `__init__.py` | Turns folder into package |
| `sys.argv` | Command-line arguments |
| `importlib` | Dynamic imports via string |

---

## ✅ What I Learned

- 📦 A **module** is just a `.py` file that contains reusable code
- 📥 **Importing** lets you bring that code into any other file
- 🔑 There are multiple ways to import — `import`, `from...import`, and `as` for aliases
- 🗂️ Modules come in 4 types — built-in, standard library, third-party, and custom
- 🛠️ Useful built-in modules like `math`, `random`, `os`, `datetime`, and `json`
- 📁 A **package** is a folder of modules with a `__init__.py` file inside
- 🔍 `dir()` lets you see everything inside a module
- 📖 `help()` lets you read a module's documentation directly in the terminal
- 🧠 `__name__ == "__main__"` tells you if a file is being run directly or imported
- 💻 `sys.argv` lets you pass **command-line arguments** into your script
- 🔓 `importlib.import_module()` lets you import modules **dynamically** using strings
- 🛡️ Always use `try/except ImportError` to safely handle missing modules
- ✅ Follow **PEP8 import order** — standard library first, then third-party, then your own
- 🚫 Avoid `from module import *` as it pollutes your namespace

---

## 🎯 Key Takeaways

- 🧰 **Modules are toolboxes** — you don't rewrite tools, you just import and use them
- 🏗️ **Good code is modular** — split your code into separate files and import what you need, where you need it
- 🔓 **`importlib` is powerful** — when the module name isn't known upfront, you can import dynamically using just a string
- 🛡️ **Always handle missing modules** — never let an uninstalled module crash your whole program, use `try/except`
- 💡 **`__name__ == "__main__"`** is one of the most important Python patterns — it separates reusable code from executable code
- 🧹 **Clean imports = clean code** — be specific about what you import, follow PEP8 order, and use aliases for long names
- 🌍 **You don't have to build everything yourself** — Python's massive library ecosystem means most tools already exist, just import them
- 🚀 **Modules are the backbone of Python's power** — every big framework like Django, Flask, and NumPy is just well-organized modules under the hood
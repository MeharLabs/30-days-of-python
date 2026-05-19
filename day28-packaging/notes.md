# 📦 Day 28 — Python Packaging


## 🎯 Goal

Write, test, and package your own Python project end-to-end — from setting up the folder structure and `__init__.py` files, to installing it in editable mode with `pip install -e .`, and optionally publishing it to PyPI.


## 🧩 What is Python Packaging?

**Python Packaging** is the process of bundling your Python code into a **distributable, reusable unit** — so others (or your future self) can install and use it with a simple `pip install yourpackage`.

Think of it like wrapping your code into a neat box 🎁 with a label, instructions, and everything needed to use it.

> Without packaging → your code only lives on your machine.
> With packaging → your code can live on **PyPI**, be installed anywhere, and shared with the world 🌍.


## 🗂️ Project Folder Structure

A well-organized package looks like this:

```
my_package/
│
├── my_package/           ← Your actual source code lives here
│   ├── __init__.py       ← Makes it a package
│   ├── module_one.py
│   └── module_two.py
│
├── tests/                ← Your test files
│   └── test_module.py
│
├── setup.py              ← OR pyproject.toml (modern way)
├── README.md             ← Describe your package
├── LICENSE               ← Open-source license
└── requirements.txt      ← Optional: list dependencies
```

💡 **Rule of thumb:** The inner folder with the same name as the project is your actual **importable package**.


## 📄 `setup.py` vs `pyproject.toml`

### 🧓 Old Way — `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="A short description",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28",
        "numpy",
    ],
    python_requires=">=3.8",
)
```

### 🚀 Modern Way — `pyproject.toml`

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my_package"
version = "0.1.0"
description = "A short description"
authors = [{ name = "Your Name", email = "you@example.com" }]
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28",
    "numpy",
]
```

| Feature | `setup.py` | `pyproject.toml` |
|---|---|---|
| Style | Old (but still works) | ✅ Modern & recommended |
| Format | Python script | TOML config file |
| PEP standard | PEP 517/518 partial | ✅ Full PEP 517/518 |
| Readability | Medium | ✅ Very clean |

> 🏆 **Use `pyproject.toml`** for any new project. It's the official PEP 517/518 standard.


## 🔤 `__init__.py` Files

The `__init__.py` file is the **magic file** that turns a plain folder into a Python **package** 🪄.

### What it does:

```python
# my_package/__init__.py

# 1️⃣ Can be completely empty — just signals "this is a package"

# 2️⃣ OR expose things at the top level
from .module_one import MyClass
from .module_two import helper_function

# 3️⃣ Define package metadata
__version__ = "0.1.0"
__author__ = "Your Name"
```

### Why it matters:

```python
# Without __init__.py exposing things:
from my_package.module_one import MyClass   # ← need full path

# With __init__.py exposing MyClass:
from my_package import MyClass              # ← clean import ✅
```

💡 **Tip:** Use `__init__.py` to define your package's **public API** — what you *want* users to import.


## ⚡ Building with `pip install -e .`

The `-e` flag stands for **editable mode** (also called *development mode*).

```bash
pip install -e .
```

### What it does:

Instead of copying your code to `site-packages`, it **links** your project folder directly. So any changes you make are **instantly reflected** without reinstalling 🔄.

### Normal install vs Editable:

```bash
pip install .        # ← Copies code. Change code? Reinstall needed.
pip install -e .     # ← Links code. Change code? Instantly works! ✅
```

### Typical dev workflow:

```bash
# 1. Clone / create your project
cd my_package/

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3. Install in editable mode
pip install -e .

# 4. Now import and test it anywhere
python -c "import my_package; print(my_package.__version__)"
```

> 🧠 `pip install -e .` is the **#1 trick** every Python developer should know.


## 🌍 Publishing to PyPI (Optional)

**PyPI** = Python Package Index → [pypi.org](https://pypi.org) — the official public package registry.

### Step-by-step:

#### 1️⃣ Install build tools
```bash
pip install build twine
```

#### 2️⃣ Build your distribution files
```bash
python -m build
```

This creates a `dist/` folder with:
```
dist/
├── my_package-0.1.0.tar.gz             ← source distribution
└── my_package-0.1.0-py3-none-any.whl  ← wheel (binary)
```

#### 3️⃣ Test on TestPyPI first (recommended!)
```bash
twine upload --repository testpypi dist/*
# Then install from test:
pip install --index-url https://test.pypi.org/simple/ my_package
```

#### 4️⃣ Upload to real PyPI
```bash
twine upload dist/*
# Enter your PyPI username + password (or API token)
```

#### 5️⃣ Anyone can now install it! 🎉
```bash
pip install my_package
```


## 🛠️ Key Methods, Tools & Concepts

### 📦 Core Tools

| Tool | Purpose |
|---|---|
| `setuptools` | Most popular build backend |
| `build` | PEP 517 frontend build tool |
| `twine` | Securely upload to PyPI |
| `wheel` | Binary distribution format (.whl) |
| `flit` | Simpler alternative to setuptools |
| `poetry` | All-in-one dependency + packaging tool |
| `hatch` | Modern, fast project manager |

### 🔑 Key Concepts

| Term | Meaning |
|---|---|
| **sdist** | Source distribution (`.tar.gz`) — raw source code |
| **wheel** | Binary distribution (`.whl`) — pre-built, installs faster |
| **entry_points** | Register CLI commands from your package |
| **extras_require** | Optional dependencies (`pip install pkg[dev]`) |
| **namespace packages** | Packages without `__init__.py` (PEP 420) |
| **virtual environment** | Isolated Python environment per project |

### 🖥️ Entry Points — Register CLI Commands

```toml
# pyproject.toml
[project.scripts]
my-cli = "my_package.cli:main"

# Now users can run:
# $ my-cli --help
```

### 🎛️ Optional / Extra Dependencies

```toml
[project.optional-dependencies]
dev = ["pytest", "black", "mypy"]
viz = ["matplotlib", "seaborn"]

# Install with:
# pip install my_package[dev]
# pip install my_package[dev,viz]
```

### 📋 `MANIFEST.in` — Include Extra Files

```
include README.md
include LICENSE
recursive-include data *.json
```


## 💡 Tips & Tricks

🔹 **Always use a virtual environment** — never pollute your global Python.

🔹 **Version your package** using [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH` → `1.2.3`

🔹 **Use `__all__`** in `__init__.py` to explicitly control what `from pkg import *` exposes:
```python
__all__ = ["MyClass", "helper_function"]
```

🔹 **Automate version bumping** with tools like `bump2version` or `hatch version patch`

🔹 **Check your package before uploading:**
```bash
twine check dist/*
```

🔹 **Use API tokens** instead of passwords for PyPI uploads — much safer 🔐

🔹 **`find_packages()` vs `find_packages(where="src")`** — if using a `src/` layout, tell setuptools where to look:
```python
packages=find_packages(where="src"),
package_dir={"": "src"},
```

🔹 **Poetry** handles everything in one tool — dependencies, packaging, and publishing:
```bash
poetry new my_package
poetry add requests
poetry publish --build
```

---

## 🗺️ The Full Packaging Journey

```
Write code → Organize structure → Add __init__.py
     ↓
setup.py / pyproject.toml → pip install -e . (dev)
     ↓
python -m build → dist/*.whl + dist/*.tar.gz
     ↓
twine upload → PyPI → pip install your_package 🎉
```


## 📝 Quick Reference Cheatsheet

```bash
# Dev install (editable)
pip install -e .

# Build distributions
python -m build

# Check before upload
twine check dist/*

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Install your published package
pip install my_package
```


## 📚 What I Learned

- 📦 **Python Packaging** is the process of bundling your code into a distributable, installable unit that others can use via `pip install`
- 🗂️ **Project folder structure** matters — your inner folder with `__init__.py` is the actual importable package
- 📄 **`pyproject.toml`** is the modern, recommended way to configure your package over the older `setup.py`
- 🪄 **`__init__.py`** turns a plain folder into a Python package and defines its public API
- ⚡ **`pip install -e .`** installs your package in editable mode so code changes reflect instantly without reinstalling
- 🏗️ **`python -m build`** creates distribution files — a `.tar.gz` source dist and a `.whl` wheel file
- 🌍 **PyPI** is the official Python Package Index where you publish packages using `twine upload`
- 🔐 **API tokens** are safer than passwords when uploading to PyPI
- 🛠️ **Tools like Poetry and Hatch** can handle dependencies, packaging, and publishing all in one place
- 🎯 **Semantic Versioning** (`MAJOR.MINOR.PATCH`) is the standard way to version your package


## 🏆 Key Takeaways

- 📦 **Packaging = Sharing** — without packaging, your code only lives on your machine; with it, the whole world can use it
- 🏗️ **Structure is everything** — a well-organized folder structure is the foundation of any good Python package
- 🆕 **`pyproject.toml` is the future** — always use it for new projects instead of the old `setup.py`
- 🪄 **`__init__.py` is the gatekeeper** — it controls what users can import from your package and defines your public API
- ⚡ **`pip install -e .` is your best friend** — use it always during development to save time and avoid constant reinstalls
- 🔄 **Build → Check → Upload** — always follow this order and test on TestPyPI before pushing to the real PyPI
- 🛡️ **Test before you publish** — once something is on PyPI, you can't delete a version, only yank it
- 🔢 **Version your package properly** — semantic versioning keeps users informed about breaking changes vs minor fixes
- 🧰 **Right tool for the right job** — use `setuptools` for control, `Poetry` for simplicity, `Hatch` for speed
- 🌍 **One `pip install` away** — a well-packaged project means anyone, anywhere can use your work instantly

---

> 🎯 **Day 28 Summary:** Packaging transforms your scripts into **shareable, installable software**. Master `pyproject.toml`, use `pip install -e .` during development, and use `build` + `twine` when you're ready to share with the world. 🚀
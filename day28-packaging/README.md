## 📋 Day 28 — Quick Summary

### 🎯 Short Goal
Write, test, and package your own Python project end-to-end — from setting up the folder structure and `__init__.py` files, to installing it in editable mode with `pip install -e .`, and optionally publishing it to PyPI.

### 📚 Topics Covered
Project folder structure, `setup.py` vs `pyproject.toml`, `__init__.py` files, building with `pip install -e .`, and publishing to PyPI.

## 🔨 What I Learned


✅ **Python Packaging** is the process of bundling your code into a distributable, installable unit that others can use via `pip install`

✅ **Project folder structure** matters — your inner folder with `__init__.py` is the actual importable package

✅ **`pyproject.toml`** is the modern, recommended way to configure your package over the older `setup.py`

✅ **`__init__.py`** turns a plain folder into a Python package and defines its public API

✅ **`pip install -e .`** installs your package in editable mode so code changes reflect instantly without reinstalling

✅ **`python -m build`** creates distribution files — a `.tar.gz` source dist and a `.whl` wheel file

✅ **PyPI** is the official Python Package Index where you publish packages using `twine upload`

✅ **API tokens** are safer than passwords when uploading to PyPI

✅ **Tools like Poetry and Hatch** can handle dependencies, packaging, and publishing all in one place

✅ **Semantic Versioning** (`MAJOR.MINOR.PATCH`) is the standard way to version your package
 

## 🔑 Key Takeaways

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

## ⏱️ Time Spent
~ 1.0 hrs
# 🗂️ Day 14: JSON Handling in Python


## 🎯 Goal

Master reading, writing, and manipulating JSON data in Python — converting between strings, dictionaries, and files using `json.loads()`, `json.dumps()`, `json.load()`, and `json.dump()`, while keeping output clean with pretty printing.

---

## 🤔 What is JSON?

**JSON** stands for **JavaScript Object Notation**. It is a **lightweight, human-readable data format** used to store and exchange data between systems — like between a server and a web app, or between two Python programs.

🌍 Think of JSON as a **universal language** that almost every programming language understands.

### 📦 JSON looks like this:
```json
{
  "name": "Ali",
  "age": 25,
  "skills": ["Python", "Django", "SQL"],
  "is_employed": true
}
```

### 🧠 JSON Supports These Data Types:

| JSON Type | Python Equivalent |
|-----------|-------------------|
| `string`  | `str`             |
| `number`  | `int` / `float`   |
| `boolean` | `bool` (`true`→`True`) |
| `null`    | `None`            |
| `array`   | `list`            |
| `object`  | `dict`            |

---

## 📥 Importing JSON in Python

```python
import json  # Built-in — no pip install needed! ✅
```

---

## 🔄 `json.loads()` — String → Dict

`loads` = **Load String**
Converts a **JSON-formatted string** into a **Python dictionary**.

```python
import json

json_string = '{"name": "Ali", "age": 25, "city": "Lahore"}'

data = json.loads(json_string)

print(data)          # {'name': 'Ali', 'age': 25, 'city': 'Lahore'}
print(type(data))    # <class 'dict'>
print(data["name"])  # Ali
```

💡 **Tip:** The input MUST be a valid JSON string, or you'll get a `json.JSONDecodeError`!

```python
# ✅ Valid — double quotes
good = '{"key": "value"}'

# ❌ Invalid — single quotes are NOT valid JSON
bad = "{'key': 'value'}"  # Will CRASH with JSONDecodeError
```

---

## 🔁 `json.dumps()` — Dict → String

`dumps` = **Dump String**
Converts a **Python dictionary** into a **JSON-formatted string**.

```python
import json

data = {
    "name": "Ali",
    "age": 25,
    "skills": ["Python", "SQL"]
}

json_string = json.dumps(data)

print(json_string)       # {"name": "Ali", "age": 25, "skills": ["Python", "SQL"]}
print(type(json_string)) # <class 'str'>
```

### 🧰 Useful Parameters of `json.dumps()`:

```python
json.dumps(data, indent=4)                # Pretty print with spaces
json.dumps(data, sort_keys=True)          # Sort keys alphabetically
json.dumps(data, separators=(',', ':'))   # Compact output (no spaces)
json.dumps(data, ensure_ascii=False)      # Support Urdu/Arabic/Chinese characters
```

💡 **Tip:** `json.dumps()` is perfect when you need to **send data over a network or API**!

---

## 📂 `json.load()` — File → Dict

`load` = **Load from File**
Reads a **JSON file** from disk and converts it into a **Python dictionary**.

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
```

💡 **Tip:** Always use `with open(...)` — it **automatically closes** the file after reading! ✅

---

## 💾 `json.dump()` — Dict → File

`dump` = **Dump to File**
Converts a **Python dictionary** and **writes it directly to a JSON file**.

```python
import json

data = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ JSON saved to output.json!")
```

💡 **Tip:** Use `indent=4` inside `json.dump()` to keep your saved files **clean and readable**!

---

## 🎨 Pretty Printing JSON

Pretty printing means displaying JSON in a **nicely formatted, indented, human-readable** way.

### ✅ Method 1 — `json.dumps()` with `indent`
```python
import json

data = {"name": "Ali", "skills": ["Python", "SQL", "Django"], "age": 25}
print(json.dumps(data, indent=4, sort_keys=True))
```

### ✅ Method 2 — `pprint`
```python
from pprint import pprint

data = {"name": "Ali", "skills": ["Python", "SQL"], "age": 25}
pprint(data)
```

> ⚠️ `pprint` shows Python dict format (single quotes). Use `json.dumps(indent=4)` for true JSON output.

---

## 🧩 Extra: Things You Should Know

### 🔍 Accessing Nested JSON
```python
data = {"user": {"address": {"city": "Lahore"}}}
print(data["user"]["address"]["city"])  # Lahore
```

### 🛡️ Safe Access with `.get()`
```python
print(data.get("email", "Not Found"))  # Not Found — no crash!
```

### 🔁 Looping Over JSON
```python
person = {"name": "Ali", "age": 25, "city": "Lahore"}
for key, value in person.items():
    print(f"{key}: {value}")
```

### ⚠️ Handling JSON Errors
```python
import json

try:
    data = json.loads("this is not valid json!!!")
except json.JSONDecodeError as e:
    print(f"❌ JSON Error: {e}")
```

---

## ⚡ Quick Comparison Table

| Method        | Direction            | Works With       |
|---------------|----------------------|------------------|
| `json.loads()` | JSON String → Dict  | String in memory |
| `json.dumps()` | Dict → JSON String  | String in memory |
| `json.load()`  | JSON File → Dict    | File on disk     |
| `json.dump()`  | Dict → JSON File    | File on disk     |

---

## 🏆 Tips & Tricks

| 💡 Tip | Details |
|--------|---------|
| 🔤 Always double quotes | JSON requires `"double quotes"`, not `'single'` |
| 📁 Use `with open()` | Auto-closes files, prevents resource leaks |
| 🎨 Use `indent=4` | Makes JSON files human-readable |
| 🔑 Use `.get()` | Safe key access without crashes |
| 🌍 `ensure_ascii=False` | Properly handle Urdu/Arabic/Chinese characters |
| 🔃 `sort_keys=True` | Alphabetically sort keys for consistency |
| 🛡️ Wrap in `try/except` | Always handle `json.JSONDecodeError` |
| 🚀 `separators=(',',':')` | Compact JSON for sending over APIs |

---

## 🧪 Full Practice Example

```python
import json

# Step 1: Python dict
student = {
    "name": "Ali Raza",
    "age": 22,
    "courses": ["Python", "Django", "SQL"],
    "passed": True,
    "score": 95.5
}

# Step 2: Dict → JSON String
json_str = json.dumps(student, indent=4)
print("📤 JSON String:\n", json_str)

# Step 3: Save to file
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)
    print("\n✅ Saved to student.json")

# Step 4: Read from file
with open("student.json", "r") as f:
    loaded = json.load(f)
    print("\n📥 Loaded from file:", loaded)

# Step 5: JSON String → Dict
back_to_dict = json.loads(json_str)
print("\n🔁 Back to dict:", back_to_dict["name"])
```

---

## 📚 What I Learned

- 🔵 JSON is a lightweight data format used to exchange data between systems
- 🔵 `json.loads()` converts a **JSON string → Python dict**
- 🔵 `json.dumps()` converts a **Python dict → JSON string**
- 🔵 `json.load()` reads a **JSON file → Python dict**
- 🔵 `json.dump()` writes a **Python dict → JSON file**
- 🔵 `indent=4` makes JSON output clean and human-readable
- 🔵 `sort_keys=True` sorts keys alphabetically
- 🔵 `ensure_ascii=False` supports non-English characters
- 🔵 Always use `with open()` to safely handle files
- 🔵 Use `.get()` for safe key access without crashes
- 🔵 Always wrap JSON parsing in `try/except` to catch `json.JSONDecodeError`
- 🔵 JSON only accepts **double quotes** — single quotes will break it

---

## ⚡ Key Takeaways

- ⚡ JSON is the **backbone of APIs and data exchange** in real-world projects
- ⚡ `loads/dumps` → work with **strings in memory**, `load/dump` → work with **files on disk**
- ⚡ Always **pretty print** with `indent=4` when saving or debugging JSON files
- ⚡ **Never trust raw JSON input** — always wrap in `try/except` for safety
- ⚡ `with open()` is the **right way** to handle files — always use it
- ⚡ JSON and Python dicts look similar but are **not the same thing**
- ⚡ Mastering JSON means you can **work with any API response** confidently

---

> 🎯 **Day 12 Done!** JSON is the backbone of APIs, configs, and data exchange in the real world. Master it and you'll handle real projects like a pro! 💪🐍
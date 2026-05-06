## 📋 Day 18 — Quick Summary

### 🎯 Short Goal

Learn how to use Python's re module to `search`, `extract`, `validate`, and `replace` text patterns in strings using Regular Expressions.

---

### 📚 Topics Covered

`re module`, `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, `re.split()`, `re.fullmatch()`, `re.compile()`, common patterns like `\d \w \s`, quantifiers, groups, named groups, and flags,

---

### 🔨 What I Learned
 
✅ **re module** — Python's built-in module for regex

✅ **re.match()** — checks pattern at start of string

✅ **re.search()** — finds first match anywhere in string

✅ **re.findall()** — returns all matches as a list

✅ **re.sub()** — replaces pattern with something else

✅ **re.split()** — splits string by a pattern

✅ **re.fullmatch()** — validates entire string

✅ **re.compile()** — pre-compiles pattern for reuse

✅ **Common Patterns** — `\d` `\w` `\s` and their opposites

✅ **Quantifiers** — `+` `?` `{n}` `{n,m}`

✅ **Groups** — capture specific parts using `()`

✅ **Named Groups** — `(?P<name>...)` for readable patterns

✅ **Flags** — like `re.IGNORECASE` and `re.MULTILINE`


## 🔑 Key Takeaways


- 🧠 Regex is a **pattern language** — not just Python, it works everywhere
- 📝 Always use **raw strings** `r"..."` to avoid escape issues
- ⚡ Use `re.compile()` when using the **same pattern repeatedly**
- 🔍 `re.search()` is more **flexible** than `re.match()` for most tasks
- 📋 `re.findall()` never returns `None` — safe to use directly
- ✅ `re.fullmatch()` is best for **validation** tasks
- 💡 `.*` is greedy — use `.*?` when you need **lazy matching**
- 🌍 Real use cases — emails, phone numbers, hashtags, cleaning data


## ⏱️ Time Spent
~ 4 hrs
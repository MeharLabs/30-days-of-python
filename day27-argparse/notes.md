# 🐍 Day 26 — Python `argparse` CLI


## 🎯 Goal

Learn how to use Python's `argparse` module to build CLI tools that accept and validate arguments from the terminal.


## 📦 What is `argparse`?

`argparse` is Python's **built-in module** for building **Command Line Interface (CLI)** programs. It lets your script accept arguments from the terminal — just like how `git`, `pip`, or `ls` work.

```bash
python script.py input.txt --output result.txt --verbose
```

Instead of manually parsing `sys.argv`, `argparse` handles everything: parsing, validation, help generation, and error messages — **automatically**.

```python
import argparse

parser = argparse.ArgumentParser(description="My awesome CLI tool")
```


## 🔧 `ArgumentParser` — The Core Object

This is the **root object** that everything else hangs off of.

```python
parser = argparse.ArgumentParser(
    prog="mytool",                          # Name shown in help
    description="Does something awesome",  # Shown at top of --help
    epilog="Thanks for using mytool!",     # Shown at bottom of --help
    formatter_class=argparse.RawTextHelpFormatter  # Preserve formatting
)
```

| Parameter | Purpose |
|---|---|
| `prog` | Override program name |
| `description` | Short description shown in help |
| `epilog` | Text shown after help |
| `add_help` | Set `False` to disable `-h/--help` |


## ➕ `add_argument()` — The Heart of argparse

This method **registers** every argument your CLI accepts.

```python
parser.add_argument("name")                            # positional
parser.add_argument("--output", "-o")                  # optional flag
parser.add_argument("--count", type=int)               # with type
parser.add_argument("--verbose", action="store_true")  # boolean flag
```

### 🗂️ Full Parameter Breakdown

| Parameter | What it does | Example |
|---|---|---|
| `type` | Convert input to a type | `type=int`, `type=float` |
| `default` | Value if arg is not given | `default=10` |
| `required` | Force optional arg to be given | `required=True` |
| `help` | Description in `--help` output | `help="Output file"` |
| `choices` | Restrict to allowed values | `choices=["a","b","c"]` |
| `nargs` | Number of values | `nargs="+"`, `nargs=2` |
| `metavar` | Name shown in help output | `metavar="FILE"` |
| `dest` | Variable name to store result | `dest="output_file"` |
| `action` | Special behaviour | `"store_true"`, `"append"` |
| `const` | Value used with some actions | `const=42` |


## 📌 Positional vs Optional Arguments

### 📍 Positional Arguments
- **Required by default**, order matters
- No `--` prefix
- Think of them as the **main input**

```python
parser.add_argument("filename",    help="File to process")
parser.add_argument("destination", help="Where to save it")
```

```bash
python script.py data.csv output/    # ✅ correct order matters!
```

### 🚩 Optional Arguments
- Start with `--` (long form) or `-` (short form)
- **Not required by default** (unless `required=True`)
- Order **doesn't** matter

```python
parser.add_argument("--verbose", help="Enable verbose mode")
parser.add_argument("--count",   help="Number of items")
```

```bash
python script.py --verbose --count 5    # ✅
python script.py --count 5 --verbose    # ✅ same result
```

### 🆚 Quick Comparison

| Feature | Positional | Optional |
|---|---|---|
| Syntax | `"filename"` | `"--filename"` |
| Required? | ✅ Yes (default) | ❌ No (default) |
| Order matters? | ✅ Yes | ❌ No |
| Has `--` prefix? | ❌ No | ✅ Yes |


## 🏳️ Flags & `-f` Shortcuts

You can define **both** a long flag and a short one-letter alias:

```python
parser.add_argument("--output",  "-o", help="Output file path")
parser.add_argument("--verbose", "-v", help="Enable verbose output")
parser.add_argument("--force",   "-f", help="Force overwrite")
parser.add_argument("--dry-run", "-n", help="Simulate without changes")
```

```bash
python script.py -o result.txt -v                    # short form ✅
python script.py --output result.txt --verbose       # long form ✅
```

> 💡 **Convention:** Short flags are for convenience in the terminal. Long flags are for scripts and readability.


## 💬 Help Messages — `--help` / `-h`

argparse **auto-generates** a help page. You just need to fill in the `help=` values.

```python
parser = argparse.ArgumentParser(
    description="🔧 A file processing tool",
    epilog="Example: python tool.py data.csv -o result.txt -v"
)

parser.add_argument("input",          help="📄 Input file to process")
parser.add_argument("--output", "-o", help="💾 Output file path", default="out.txt")
parser.add_argument("--verbose", "-v",help="🔊 Print detailed logs", action="store_true")
parser.add_argument("--limit",  "-l", help="🔢 Max lines to process", type=int, default=100)
```

Running `python tool.py --help` outputs:

```
🔧 A file processing tool

positional arguments:
  input              📄 Input file to process

options:
  -h, --help         show this help message and exit
  -o, --output       💾 Output file path
  -v, --verbose      🔊 Print detailed logs
  -l, --limit        🔢 Max lines to process

Example: python tool.py data.csv -o result.txt -v
```


## ⚙️ `action=` — Special Behaviours

```python
# ✅ store_true / store_false — Boolean toggles
parser.add_argument("--verbose", action="store_true")   # True if flag present
parser.add_argument("--quiet",   action="store_false")  # False if flag present

# ✅ count — Count how many times flag is used
parser.add_argument("-v", action="count", default=0)
# -v → 1,  -vv → 2,  -vvv → 3 (like verbosity levels!)

# ✅ append — Collect multiple values into a list
parser.add_argument("--tag", action="append")
# --tag python --tag cli → ["python", "cli"]

# ✅ store_const — Store a fixed constant
parser.add_argument("--pi", action="store_const", const=3.14159)
```

---

## 🔢 `nargs` — Multiple Values

```python
parser.add_argument("--files", nargs="+")   # 1 or more
parser.add_argument("--range", nargs=2)     # exactly 2
parser.add_argument("--items", nargs="*")   # 0 or more
parser.add_argument("--maybe", nargs="?")   # 0 or 1
```

```bash
python script.py --files a.txt b.txt c.txt   # → ["a.txt", "b.txt", "c.txt"]
python script.py --range 10 20               # → ["10", "20"]
```


## 🎛️ `choices=` — Restrict Valid Values

```python
parser.add_argument("--mode",  choices=["read","write","append"])
parser.add_argument("--level", choices=[1, 2, 3], type=int)
parser.add_argument("--env",   choices=["dev","staging","prod"])
```

```bash
python script.py --mode delete   # ❌ Error: invalid choice
python script.py --mode read     # ✅
```


## 🧩 Subparsers — Git-style Subcommands

Build CLIs with sub-commands like `git commit`, `git push`:

```python
parser = argparse.ArgumentParser(prog="mytool")
subparsers = parser.add_subparsers(dest="command")

# 'upload' subcommand
upload = subparsers.add_parser("upload", help="Upload a file")
upload.add_argument("file",    help="File to upload")
upload.add_argument("--force", action="store_true")

# 'download' subcommand
download = subparsers.add_parser("download", help="Download a file")
download.add_argument("url", help="URL to download from")

args = parser.parse_args()

if args.command == "upload":
    print(f"Uploading {args.file}")
elif args.command == "download":
    print(f"Downloading {args.url}")
```

```bash
python tool.py upload data.csv --force
python tool.py download https://example.com/file.zip
```


## 🗂️ Argument Groups — Organize Help Output

```python
parser = argparse.ArgumentParser()

# Group 1
input_group = parser.add_argument_group("📥 Input Options")
input_group.add_argument("--file",   help="Input file")
input_group.add_argument("--stream", help="Input stream")

# Group 2
output_group = parser.add_argument_group("📤 Output Options")
output_group.add_argument("--output", help="Output path")
output_group.add_argument("--format", help="Output format")
```


## 🔒 Mutually Exclusive Groups

Ensure **only one** of a set of flags can be used at a time:

```python
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", action="store_true")
group.add_argument("--quiet",   action="store_true")
```

```bash
python script.py --verbose --quiet   # ❌ Error: not allowed together
python script.py --verbose           # ✅
```


## 🧪 `parse_args()` vs `parse_known_args()`

```python
# Standard — errors on unknown args
args = parser.parse_args()

# Lenient — returns (known, unknown) tuple
args, unknown = parser.parse_known_args()
print(unknown)   # ["--some-unknown-flag"]
```


## 💡 Tips & Tricks

```python
# 🔹 Set defaults in bulk
parser.set_defaults(verbose=False, count=10)

# 🔹 Parse a custom list (great for testing!)
args = parser.parse_args(["--output", "test.txt", "--verbose"])

# 🔹 Convert result to a dict
args_dict = vars(parser.parse_args())

# 🔹 Custom type validator
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be positive")
    return ivalue

parser.add_argument("--count", type=positive_int)

# 🔹 Custom error message
parser.error("Something went wrong!")   # prints error + help, then exits
```


## 🏁 Full Working Example

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog        = "filetools",
        description = "🛠️  A powerful file processing CLI",
        epilog      = "Example: filetools data.csv -o out.txt -v --limit 50"
    )

    # Positional
    parser.add_argument("input",
        help="📄 Input CSV file")

    # Optional with shortcut
    parser.add_argument("--output", "-o",
        default = "output.txt",
        metavar = "FILE",
        help    = "💾 Output file (default: output.txt)")

    # Boolean flag
    parser.add_argument("--verbose", "-v",
        action  = "store_true",
        help    = "🔊 Enable verbose logging")

    # Typed with default
    parser.add_argument("--limit", "-l",
        type    = int,
        default = 100,
        help    = "🔢 Max rows to process (default: 100)")

    # Choices
    parser.add_argument("--format", "-f",
        choices = ["csv", "json", "txt"],
        default = "csv",
        help    = "📦 Output format")

    args = parser.parse_args()

    print(f"📂 Input   : {args.input}")
    print(f"💾 Output  : {args.output}")
    print(f"📦 Format  : {args.format}")
    print(f"🔢 Limit   : {args.limit}")
    print(f"🔊 Verbose : {args.verbose}")

if __name__ == "__main__":
    main()
```

```bash
$ python filetools.py data.csv -o result.json -v --limit 50 --format json

📂 Input   : data.csv
💾 Output  : result.json
📦 Format  : json
🔢 Limit   : 50
🔊 Verbose : True
```


## 🗺️ Full argparse Cheatsheet

| Thing | Syntax |
|---|---|
| Create parser | `ArgumentParser(description="...")` |
| Positional arg | `add_argument("name")` |
| Optional flag | `add_argument("--name", "-n")` |
| Boolean toggle | `action="store_true"` |
| Count flag uses | `action="count"` |
| Collect list | `action="append"` or `nargs="+"` |
| Restrict values | `choices=[...]` |
| Set type | `type=int` / `type=float` |
| Set default | `default=value` |
| Force required | `required=True` |
| Subcommands | `add_subparsers()` |
| Mutual exclusion | `add_mutually_exclusive_group()` |
| Group args | `add_argument_group("label")` |
| Parse args | `parser.parse_args()` |
| To dict | `vars(args)` |


## ✅ What I Learned

- 📦 What `argparse` is and why it's better than manually parsing `sys.argv`
- 🔧 How to create a parser using `ArgumentParser()`
- ➕ How to register arguments using `add_argument()`
- 📍 The difference between **positional** and **optional** arguments
- 🏳️ How to use `--flags` and `-f` shortcuts together
- 💬 How to write help messages that auto-generate with `--help`
- ⚙️ How `action=` works like `store_true`, `count`, and `append`
- 🔢 How to accept multiple values using `nargs`
- 🎛️ How to restrict valid inputs using `choices=`
- 🧩 How to build git-style subcommands using `subparsers`
- 🔒 How to make flags mutually exclusive
- 🗂️ How to organize arguments into groups for cleaner help output
- 💡 Tips like custom type validators, `vars(args)`, and `parse_known_args()`
- 🌍 Where `argparse` is used in real life like DevOps, ML, and automation


## 🔑 Key Takeaways

- 🐍 `argparse` is **built-in** — no installation needed, just `import argparse`
- 🎯 It turns your script into a **professional CLI tool** with minimal code
- 📍 **Positional args** are required and order matters, **optional args** are flexible
- 🏳️ Always add **both** `--long` and `-s` short forms for better user experience
- 💬 Always write `help=` for every argument — it's free documentation
- ⚙️ Use `action="store_true"` for simple on/off boolean flags
- 🔒 Use `mutually_exclusive_group()` to prevent conflicting flags
- 🧩 Use `subparsers` when your tool has multiple commands like `git`
- ✅ `choices=` and `type=` handle **validation automatically** — no extra if/else needed
- 📦 `vars(args)` converts your parsed args into a **plain dictionary** for easy use
- 🌍 Real-world tools like `pip`, `git`, and `docker` are all built on this same concept
- 💡 The bigger your script, the more `argparse` **saves you time and errors**
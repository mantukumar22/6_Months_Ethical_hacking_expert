# Day 1: Python variables, data types and conditions
**Date:** 28 Oct 2026 · **Time:** 60 min

## Learn (20 min)
- Variables and data types
- Strings, integers and booleans
- `input()` and `print()`
- `if`, `elif` and `else`
- Comparison operators

## Practice (30 min)
Create `system_info.py` (starter: [scripts/day01_system_info.py](../scripts/day01_system_info.py)), then run:
```
python system_info.py
```

## Notes (10 min)

## Notes: Python Variables, Data Types and Conditions

### Variables
A **variable** is a name that points to a value. You create it by assigning with `=`, and there's no type declaration, because Python works out the type from the value.

```python
username = "kali"       # str
port = 22               # int
is_open = True          # bool
```

**Naming rules:**
- Letters, digits and `_` only, and it can't start with a digit.
- Case-sensitive: `port` and `Port` are different.
- Use `snake_case` (`target_ip`, `open_ports`) and meaningful names.
- Don't reuse built-in names like `print`, `input` or `type`.

A variable can be reassigned, even to a different type: `port = 80`. Check a type with `type(port)`.

### Data types

| Type | Name | Example | Used for |
|---|---|---|---|
| `str` | String | `"kali"`, `'192.168.1.1'` | Text: usernames, IPs, URLs |
| `int` | Integer | `22`, `443`, `-1` | Whole numbers: ports, counts |
| `float` | Float | `0.5`, `3.14` | Decimals: timeouts, scores |
| `bool` | Boolean | `True`, `False` | Yes/no results: is the port open? |

**Strings**
- Quotes: `"..."` or `'...'` (same thing). `"""..."""` for multi-line.
- Join: `"Port " + str(22)`. Better: an **f-string**: `f"Port {port} is open"`.
- Handy methods: `.lower()`, `.upper()`, `.strip()` (remove surrounding spaces), `.startswith("http")`, `.replace("a", "b")`.
- `"22" + "80"` gives `"2280"` (joined text), not 102.

**Integers**
- Arithmetic: `+ - * /`, `//` (floor division), `%` (remainder), `**` (power). Note `/` always gives a float.
- `"22"` (string) and `22` (int) are different and are **not equal**.

**Booleans**
- Only `True` and `False` (capitalized). They come from comparisons: `port == 22` is `True` or `False`.
- **Falsy** values: `False`, `0`, `""` (empty string), `[]`, `None`. Almost everything else is **truthy**.

**Converting types (casting)**

| Function | Result |
|---|---|
| `int("22")` | `22` |
| `str(22)` | `"22"` |
| `float("1.5")` | `1.5` |
| `bool(0)` | `False` |

`int("abc")` raises a `ValueError`, so converting **untrusted input** needs checking (Day 3 covers `try/except`).

### input() and print()

**`input(prompt)`** shows the prompt, waits for the user to press Enter, and **always returns a string**, even if they typed digits.

```python
port = input("Port: ")          # user types 80 -> port is "80" (a str)
port = int(input("Port: "))     # now an int
```

**`print()`** shows output.
```python
print("Username:", username)                 # separates items with a space
print(f"Scanning port {port}")               # f-string
print("a", "b", sep="-")                     # a-b
print("Done", end="")                        # no newline at the end
```

### Comparison operators
They compare two values and return a **boolean**.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `port == 22` | `True` if port is 22 |
| `!=` | Not equal to | `port != 80` | |
| `>` / `<` | Greater / less than | `port > 1023` | |
| `>=` / `<=` | Greater / less than or equal | `port <= 1023` | |
| `in` | Is contained in | `"admin" in "administrator"` | `True` |
| `not in` | Is not contained in | `80 not in [22, 443]` | `True` |

**Common mistake:** `=` **assigns**, `==` **compares**. `if port = 22:` is a syntax error.

**Combining conditions with logical operators:**

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both must be true | `port > 0 and port < 65536` |
| `or` | At least one is true | `system == "kali" or system == "windows"` |
| `not` | Reverses the result | `not is_open` |

Chained comparison also works: `0 < port < 65536`.

### if, elif and else
Conditions let the program choose what to run. Python checks them **top to bottom** and runs the **first** one that is true, then skips the rest.

```python
system = input("Enter your operating system: ")

if system.lower() == "kali":
    print("Linux security lab detected.")
elif system.lower() == "windows":
    print("Windows environment detected.")
else:
    print("Other operating system.")
```

| Part | Role |
|---|---|
| `if` | First condition to test |
| `elif` | "Else if", extra conditions (as many as needed) |
| `else` | Runs if nothing above was true (optional, has no condition) |

**Rules:**
- End each condition line with a **colon** `:`.
- The block that follows must be **indented** (4 spaces is standard). Indentation *is* the syntax in Python.
- Don't mix tabs and spaces.

Why `.lower()` matters: `"Kali" == "kali"` is `False`. Lowercasing the input makes the check case-insensitive.

Other tools: `.strip()` removes accidental spaces (`" kali "`), and `in` can replace repeated `or`:
```python
if system.lower() in ("kali", "ubuntu", "debian"):
    print("Linux detected.")
```

### Handling unexpected input (today's task)
Your script should accept three OS names and cope with anything else. Hints, without giving the whole answer away:
- Normalize first: `system = input(...).strip().lower()`.
- Use `in` with a tuple/list of the allowed names for the "known" branch.
- Keep a final `else` that prints a clear message, and handle an **empty** answer (`if not system:`).
- Try these test inputs: `Kali`, ` WINDOWS `, `macos`, an empty line, `123`, `kali; rm -rf /` (it's just text here, and nothing runs it).

### Common mistakes
| Mistake | Fix |
|---|---|
| `if x = 5:` | Use `==` |
| Forgot the `:` after `if`/`else` | Add the colon |
| Wrong or mixed indentation | Use 4 spaces consistently |
| `"Port " + 22` (`TypeError`) | `"Port " + str(22)` or `f"Port {22}"` |
| Comparing `"22" == 22` and getting `False` | Convert: `int("22") == 22` |
| `True` written as `true` | Capitalize: `True` |
| `input()` result treated as a number | Wrap with `int()` |

### Why it matters for security work
- **Everything users or files give you starts as text**, so validate and convert before you trust it.
- Conditions are how a tool decides: *is this port open? is this status code 200? is this target allowed?*
- A simple check like `if target not in ("127.0.0.1", "localhost")` is how you keep a tool inside its authorized scope (you'll use this on Day 5).
- Never use unvalidated input to build shell commands (Day 4).

### Quick self-check
1. What type does `input()` return, even if you type `42`?
2. What is the difference between `=` and `==`?
3. What does `"22" + "80"` give, and what does `22 + 80` give?
4. If `x = 5`, which branch runs: `if x > 10 / elif x > 3 / else`?
5. Why use `system.lower()` when comparing OS names?

*Answers: a string; `=` assigns a value and `==` compares two values; `"2280"` and `102`; the `elif` branch (the first true condition wins); so `Kali`, `KALI` and `kali` all match.*

## Mistake I fixed today
-

## Key takeaways
-

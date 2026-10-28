# Day 3: Files, exceptions and logging
**Date:** 30 Oct 2026 · **Time:** 60 min

## Learn (20 min)
- Reading and writing text files
- `with open(...)`
- `try` and `except`
- Handling invalid input
- Basic logging

## Practice (30 min)
Create `security_notes.py` (starter: [scripts/day03_security_notes.py](../scripts/day03_security_notes.py)). Run it and inspect `findings.txt`.

## Notes (10 min)
## Day 3 Notes: Files, Exceptions and Logging

### Reading and writing text files
Programs use files to load targets, save findings and keep logs. Python gives you two common ways: `pathlib` (short, good for whole files) and `open()` (more control, good for line-by-line work).

**With `pathlib` (used in `security_notes.py`):**
```python
from pathlib import Path

file_path = Path("findings.txt")
file_path.write_text("Finding: Missing security header\n", encoding="utf-8")
content = file_path.read_text(encoding="utf-8")
print(content)
```

| Method | What it does |
|---|---|
| `write_text(text)` | Writes a string and **overwrites** the file if it exists |
| `read_text()` | Reads the whole file as one string |
| `exists()` | `True` if the path exists |
| `is_file()` / `is_dir()` | Checks the type |
| `mkdir(parents=True, exist_ok=True)` | Creates a folder (and any missing parents) |
| `Path("a") / "b.txt"` | Joins paths correctly on Linux and Windows |

Always pass `encoding="utf-8"`. Otherwise Python uses the system default, and the same script can behave differently on Windows and Kali.

### `with open(...)`
```python
with open("findings.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```
`with` **closes the file automatically**, even if an error happens inside the block. Without it you must remember to call `file.close()`, and a leaked file handle can lose data or lock the file.

**File modes:**

| Mode | Meaning | Caution |
|---|---|---|
| `"r"` | Read (default) | Error if the file doesn't exist |
| `"w"` | Write | **Erases** existing content, creates the file if missing |
| `"a"` | Append | Adds to the end, creates the file if missing |
| `"x"` | Create only | Error if the file already exists (protects against overwriting) |
| `"rb"` / `"wb"` | Binary read/write | For images, executables, captures |

**Reading options:**

| Code | Result |
|---|---|
| `file.read()` | The whole file as one string |
| `file.readline()` | One line |
| `file.readlines()` | A list of all lines |
| `for line in file:` | One line at a time. **Best for big files** such as logs, because it doesn't load everything into memory |

Each line ends with `\n`, so use `.strip()` when comparing or printing.

**Writing and appending:**
```python
with open("findings.txt", "a", encoding="utf-8") as file:
    file.write("Finding: Server header reveals version\n")
```
`write()` doesn't add a newline for you, so include `\n`.

**Example: read targets from a file, skipping blanks and comments**
```python
targets = []
with open("targets.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith("#"):
            targets.append(line)
```

### try and except
Things outside your control go wrong: a file is missing, permission is denied, the disk is full, a user types nonsense. An **exception** is Python's way of reporting this. Unhandled, it stops the program with a traceback.

```python
try:
    content = Path("findings.txt").read_text(encoding="utf-8")
    print(content)
except FileNotFoundError:
    print("findings.txt does not exist yet.")
except PermissionError:
    print("No permission to read findings.txt.")
except OSError as error:
    print("File operation failed:", error)
```

How it flows: the `try` block runs. If an exception occurs, Python jumps to the **first matching** `except` and skips the rest of the `try`. If none occurs, the `except` blocks are skipped.

| Block | Runs when |
|---|---|
| `try` | Always first. Holds the risky code |
| `except Type` | That type of error happened |
| `else` | The `try` finished **without** errors |
| `finally` | **Always**, whether or not an error happened (cleanup) |

```python
try:
    file = open("findings.txt", encoding="utf-8")
except OSError as error:
    print("Could not open:", error)
else:
    print("Opened fine")
    file.close()
finally:
    print("Done")
```

**Common exceptions:**

| Exception | Typical cause |
|---|---|
| `FileNotFoundError` | The file or folder doesn't exist |
| `PermissionError` | You're not allowed to read or write it |
| `IsADirectoryError` | You tried to open a folder as a file |
| `OSError` | **Parent of the three above** and of network/socket errors |
| `ValueError` | Right type, wrong value, e.g. `int("abc")` |
| `KeyError` | Dictionary key missing |
| `IndexError` | List position out of range |
| `TypeError` | Wrong type, e.g. `"a" + 1` |
| `ZeroDivisionError` | Division by zero |
| `UnicodeDecodeError` | File isn't valid in the encoding you chose |

**Rules of good error handling:**
- Catch **specific** exceptions. Avoid a bare `except:`, since it also hides `Ctrl+C` and real bugs.
- Never write `except Exception: pass`. Swallowing errors silently makes a tool look like it worked when it didn't.
- Keep the `try` block **small**, so you know which line failed.
- Tell the user **what failed and why**, using the error message.
- Raise your own when input is unacceptable: `raise ValueError("Port must be 1-65535")`.
- Use `raise SystemExit("message")` to stop a script cleanly with a message.

**What happens if the file can't be created or read** (your Day 3 note): without `try/except`, Python prints a traceback and the script **stops immediately**, so any later work, like saving other results, never happens. With handling, the script reports the problem and can continue or exit cleanly.

Test it: change the path to a folder that doesn't exist, such as `Path("nonexistent/findings.txt")`, and watch the `except` branch run.

### Handling invalid input
Anything a user (or a file, or the network) gives you can be wrong. **Validate before you trust it.**

```python
def read_port():
    while True:
        raw = input("Port (1-65535): ").strip()
        try:
            port = int(raw)
        except ValueError:
            print("Please enter a number.")
            continue
        if 1 <= port <= 65535:
            return port
        print("Port must be between 1 and 65535.")
```

Three layers to check:

| Check | Example |
|---|---|
| **Type** (can it be converted?) | `int(raw)` inside `try/except ValueError` |
| **Range** (is it sensible?) | `1 <= port <= 65535` |
| **Allowed value** (is it permitted?) | `if target not in ("127.0.0.1", "localhost")` |

Checking an IP with the standard library:
```python
import ipaddress

try:
    ip = ipaddress.ip_address(raw)
except ValueError:
    print("Not a valid IP address.")
```

Principle: **allow known-good input** rather than trying to block known-bad. This idea reappears in web testing (input validation flaws, injection).

### Basic logging
`print()` is fine for quick output. A **log** is a permanent, timestamped record, which matters when a tool runs unattended or you need evidence of what it did and when.

```python
import logging

logging.basicConfig(
    filename="scan.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("Scan started")
logging.warning("Port 22 timed out")
logging.error("Could not save results")
```
Example line in `scan.log`:
```
2026-10-30 10:15:02,431 INFO Scan started
```

**Levels (lowest to highest):**

| Level | Use for |
|---|---|
| `DEBUG` | Detailed information while developing |
| `INFO` | Normal events: started, finished, 3 ports checked |
| `WARNING` | Something unexpected but the program continues |
| `ERROR` | An operation failed |
| `CRITICAL` | The program can't continue |

`level=logging.INFO` means INFO and above are recorded. DEBUG messages are hidden.

**Useful format fields:** `%(asctime)s` time, `%(levelname)s` level, `%(message)s` text, `%(name)s` logger name, `%(funcName)s` function.

**Log to the screen and a file:**
```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("scan.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
```

**Log an error together with its traceback:**
```python
try:
    Path("nonexistent/findings.txt").read_text(encoding="utf-8")
except OSError:
    logging.exception("Could not read findings file")
```
`logging.exception()` works only inside an `except` block.

Use f-strings or `%s` placeholders: `logging.info("Checking %s:%d", host, port)`.

**Security cautions:**
- **Never log secrets** (passwords, tokens, session cookies, API keys).
- Log files can contain targets, IPs and findings, so keep them out of Git (`*.log` is already in `.gitignore`) and out of public repos.
- Logs are evidence. Attackers delete or alter them, and defenders protect them (remember Event ID 1102, log cleared).
- If you log user-supplied text, remember it may contain odd characters or fake log lines.

### Practice, step by step
1. Create `security_notes.py` and run it. Open `findings.txt` and confirm the contents.
2. Change the text and run it again. The file is **overwritten**.
3. Switch to append mode with `open(..., "a")` and run it three times. Compare.
4. Break it on purpose: write to `Path("nonexistent/findings.txt")` and read the exception.
5. Add `except FileNotFoundError` and `except PermissionError` before the general `OSError`, each with a clear message.
6. Add logging: INFO when the file is written, ERROR when it fails.
7. Stretch: read `findings.txt` line by line and count the lines that contain the word `Missing`.

### Common mistakes

| Mistake | Fix |
|---|---|
| Used `"w"` and erased the file | Use `"a"` to append, or `"x"` to refuse overwriting |
| Forgot the `\n` in `write()` | Add `\n` at the end of each line |
| No `encoding="utf-8"` | Always specify it |
| Relative path and the file "isn't found" | Check the current folder (`Path.cwd()`) |
| Bare `except:` or `except: pass` | Catch specific exceptions and report them |
| `try` block wraps the whole program | Keep it around only the risky lines |
| Forgot `with`, file left open | Use `with open(...)` |
| Printed `input()` text with the newline issue | Use `.strip()` |
| Logged a password or token | Never log secrets |
| `logging.basicConfig` called after other logging | Call it **once**, at the start |

### Why it matters for security automation
- A scan across many hosts will **hit failures**: timeouts, missing files, no permissions. A tool that crashes on the first one loses the rest of the results.
- Silent failures are dangerous: if a check fails but the script reports "nothing found", you may wrongly conclude a system is secure.
- Logs show **what the tool did, when and against what**, which supports scope and authorization records.
- Validated input keeps the tool within its authorized scope and prevents it from being tricked by bad data.

### Quick self-check
1. What is the difference between `"w"` and `"a"` file modes?
2. Why use `with open(...)` instead of `open(...)` alone?
3. Why should you catch specific exceptions instead of a bare `except:`?
4. What does `int("abc")` raise, and how would you handle it?
5. What is the difference between `print()` and `logging`, and which log level fits "port 22 timed out"?

*Answers: `"w"` erases and rewrites, `"a"` adds to the end; it closes the file automatically even if an error occurs; a bare `except:` hides real bugs and `Ctrl+C`, and specific ones let you respond properly; `ValueError`, handled with `try/except ValueError` and asking again; `print` shows text on screen, `logging` records timestamped, leveled messages to a file or the screen, and WARNING fits a timeout that doesn't stop the scan.*
## Mistake I fixed today
-

## Key takeaways
-

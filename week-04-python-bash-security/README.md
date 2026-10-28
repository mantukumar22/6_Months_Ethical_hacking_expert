# Week 4: Python & Bash for Cybersecurity

**27 October – 2 November 2026 · 7 days · 1 hour per day**

Goal: learn enough Python and Bash to automate simple security tasks, inspect data, and build a first cybersecurity tool. Skip general programming theory (I already have web-dev experience) and focus on Python fundamentals, files, subprocesses, networking libraries and safe automation.

> **Safety rules**
> - Network code runs against `127.0.0.1` or a lab machine I **own or am explicitly authorized** to test. Never scan public IPs or third-party systems.
> - Never build shell commands from untrusted input. Use fixed commands or argument lists.
> - A port scanner finds reachable ports. It is **not** a vulnerability assessment.
> - Never commit results containing real IPs, hostnames or credentials.

## Daily routine (1 hour)
**20 min** focused lesson → **30 min** write and run code → **10 min** notes and fix one mistake.

## Schedule

| Day | Date | Topic | Notes | Script |
|---|---|---|---|---|
| 1 | 28 Oct | Python variables, data types, conditions | [day-01](notes/day-01-python-basics.md) | `day01_system_info.py` |
| 2 | 29 Oct | Loops, lists, dictionaries, functions | [day-02](notes/day-02-loops-functions.md) | `day02_port_reference.py` |
| 3 | 30 Oct | Files, exceptions, logging | [day-03](notes/day-03-files-exceptions.md) | `day03_security_notes.py` |
| 4 | 31 Oct | Modules, subprocess, Bash | [day-04](notes/day-04-modules-bash.md) | `day04_*.py`, `day04_system_check.sh` |
| 5 | 1 Nov | Networking with Python sockets | [day-05](notes/day-05-sockets.md) | `day05_tcp_check.py` |
| 6 | 2 Nov | Build a Python port scanner | [day-06](notes/day-06-port-scanner.md) | `day06_port_scanner.py` |
| 7 | 3 Nov | Revision and mini-project | [day-07](notes/day-07-revision.md) | [project](project/mini-project.md) |

> **Date note:** the original plan header says 27 Oct – 2 Nov, but its daily dates start on 28 Oct and end with Day 6 on 2 Nov. I kept the daily dates and added **Day 7 on 3 Nov** (revision and mini-project). Adjust if you prefer.

## Repo layout
```
notes/          daily notes (one file per day)
scripts/        starter scripts for each day (write your own versions first)
project/        Day 7 mini-project plan and report
resources/      Python, Bash and sockets cheat sheets, links
raw-private/    UNREDACTED output. git-ignored, never commit
checklist.md    weekly completion checklist
```
## What is Python?

**Python** is a high-level, interpreted, general-purpose programming language. It's known for readable syntax, and it's the most common language for security scripting and tooling.

| Feature | What it means |
|---|---|
| **Interpreted** | Code runs line by line through the Python interpreter, with no separate compile step |
| **Dynamically typed** | You don't declare types: `port = 22` just works |
| **Indentation-based** | Blocks are defined by indentation, not `{ }` |
| **"Batteries included"** | A large standard library: `socket`, `subprocess`, `pathlib`, `ipaddress`, `hashlib`, `logging` |
| **Cross-platform** | The same script runs on Kali, Windows and macOS |

### Why Python for cybersecurity
- **Automation:** repeat checks across many hosts, files or logs in seconds.
- **Networking:** `socket` and libraries like `requests` let you write scanners, banner checkers and HTTP testers.
- **Parsing data:** logs, JSON, CSV and scan output are easy to process.
- **Tooling ecosystem:** many security tools are written in Python or have Python APIs (e.g. Scapy, impacket, pwntools).
- **Fast prototyping:** you can build a working tool in an hour.

**Limits:** it's slower than C or Go for heavy workloads, and a script that finds open ports doesn't find vulnerabilities by itself.

### Check your installation
```
python3 --version        # Kali / Linux / macOS
python --version         # Windows (or: py --version)
```
Kali ships with Python 3. On Windows, install it from python.org and tick **"Add python.exe to PATH"** during setup.

### Three ways to run Python

| Way | How | Good for |
|---|---|---|
| **Interactive shell (REPL)** | Type `python3`, then `exit()` to leave | Trying one line quickly |
| **Script file** | `python3 system_info.py` | Real programs (what you'll do this week) |
| **Executable script** | First line `#!/usr/bin/env python3`, then `chmod +x file.py` and `./file.py` | Linux tools |

Try the REPL:
```
>>> 22 + 80
102
>>> "kali".upper()
'KALI'
>>> type(22)
<class 'int'>
```

### Writing and running your first script
```
nano system_info.py        # or any editor (VS Code works well)
python3 system_info.py
```
Save files with a `.py` extension, and run them from the folder that contains them (check with `pwd` or `dir`).

### Packages and virtual environments
The standard library covers most of this week. For extra packages:
```
python3 -m venv .venv                 # create an isolated environment
source .venv/bin/activate             # Linux (Windows: .venv\Scripts\activate)
pip install requests                  # install a package into it
pip list                              # see what's installed
deactivate                            # leave the environment
```
A **virtual environment** keeps each project's packages separate, so installs don't clash with system Python. On Kali, `pip install` outside a venv is often blocked by design, so use a venv.

### Getting help
```
help(print)                 # inside the REPL
python3 -c "import socket; help(socket.socket)"
```
Official docs: docs.python.org. Read the error message from the **bottom up**: the last line says what went wrong, and the lines above show where.

### Common beginner errors

| Error | Usual cause |
|---|---|
| `SyntaxError` | Missing colon, bracket or quote |
| `IndentationError` | Inconsistent spaces or tabs |
| `NameError` | Typo in a variable name, or using it before assigning |
| `TypeError` | Mixing types, e.g. `"Port " + 22` |
| `ValueError` | e.g. `int("abc")` |
| `command not found: python` | Use `python3` on Linux |
| `ModuleNotFoundError` | Package not installed (use a venv + `pip install`) |

### Quick self-check
1. Why is Python called an interpreted language?
2. What's the difference between the REPL and running a script file?
3. Why use a virtual environment?
4. Which standard-library modules will you use this week for networking and files?

*Answers: code is executed by the interpreter at run time, not compiled ahead; REPL runs one line at a time interactively while a script runs a whole saved file; to keep each project's packages isolated; `socket` and `pathlib` (plus `subprocess` and `ipaddress`).*


## Run the scripts
```
python3 scripts/day01_system_info.py
bash scripts/day04_system_check.sh
```
Use `python` instead of `python3` on Windows.

## Progress
See [checklist.md](checklist.md). **0/7** done.

## Standard before Week 5
I can write, from a blank file, a script that takes a validated target, checks a few TCP ports with timeouts and error handling, and saves the results to a file, and I can explain what the results do and do not prove.

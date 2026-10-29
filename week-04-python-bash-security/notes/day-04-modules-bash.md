# Day 4: Python modules, subprocesses and Bash
**Date:** 31 Oct 2026 · **Time:** 60 min

## Learn (20 min)
- Python imports and standard-library modules
- `pathlib`, `os` and `subprocess`
- Bash variables and loops
- Command exit codes
- Why shell commands must be handled carefully

## Practice (30 min)
1. Python system info with built-in libraries: [scripts/day04_sysinfo.py](../scripts/day04_sysinfo.py)
2. In Kali, the Bash script: [scripts/day04_system_check.sh](../scripts/day04_system_check.sh)
```
chmod +x system_check.sh
./system_check.sh
```
3. Extras: [scripts/day04_subprocess_demo.py](../scripts/day04_subprocess_demo.py) and [scripts/day04_exit_codes.sh](../scripts/day04_exit_codes.sh)

## Notes (10 min)
# Python and Shell Notes

Simple notes on imports, files, running commands, Bash basics, exit codes, and staying safe with shell commands.

## 1. Python imports and standard-library modules

The **standard library** is the set of modules that come with Python. You do not need to install them.

```python
import os                      # whole module: use os.getcwd()
import os.path as osp          # give it a short name
from pathlib import Path       # take one thing out of a module
from subprocess import run     # use run(...) directly
```

Tips:

- Put imports at the top of the file.
- Order them: standard library first, then third-party packages, then your own modules.
- Avoid `from module import *`. You cannot tell where names come from, and names can clash.
- Use `import x` when you use many things from a module. Use `from x import y` when you use one or two.
- A file named `random.py` or `os.py` in your project can hide the real standard-library module. Pick different names.

Useful standard-library modules: `sys`, `json`, `re`, `datetime`, `shutil`, `argparse`, `logging`.

Run-as-script pattern:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

This runs `main()` only when you run the file directly, not when another file imports it.

## 2. `pathlib`, `os` and `subprocess`

### `pathlib`: work with file paths

`pathlib` treats paths as objects. It is the modern, recommended way.

```python
from pathlib import Path

p = Path("data") / "notes.txt"   # use / to join parts
p.exists()                       # does it exist?
p.is_file()                      # is it a file?
p.is_dir()                       # is it a folder?
p.name                           # "notes.txt"
p.stem                           # "notes"
p.suffix                         # ".txt"
p.parent                         # Path("data")
p.resolve()                      # full absolute path

p.read_text(encoding="utf-8")
p.write_text("hello", encoding="utf-8")
Path("out/logs").mkdir(parents=True, exist_ok=True)

for f in Path(".").glob("*.py"): # find files by pattern
    print(f)
```

Always set `encoding="utf-8"` when reading or writing text so it works the same on every computer.

### `os`: talk to the operating system

```python
import os

os.getcwd()                      # current folder
os.environ["HOME"]               # environment variable (error if missing)
os.environ.get("API_KEY")        # returns None if missing
os.getenv("MODE", "dev")         # with a default value
os.cpu_count()
```

`os.path` and `os.listdir` still work, but `pathlib` is easier to read for paths. Use `os` mainly for environment variables and process or system information.

### `subprocess`: run other programs

```python
import subprocess

result = subprocess.run(
    ["ls", "-l", "my folder"],   # a LIST, not one long string
    capture_output=True,         # collect stdout and stderr
    text=True,                   # get strings, not bytes
    check=True,                  # raise an error if the command fails
    timeout=30,                  # do not wait forever
)
print(result.stdout)
print(result.returncode)         # the exit code
```

Key points:

- Pass the command as a **list**. Each item is one argument, so spaces in names are safe.
- `check=True` raises `CalledProcessError` when the exit code is not 0.
- `capture_output=True` lets you read `result.stdout` and `result.stderr`.
- `timeout=` raises `TimeoutExpired` if the command runs too long.
- Handle failures:

```python
try:
    subprocess.run(["git", "pull"], check=True)
except FileNotFoundError:
    print("git is not installed.")
except subprocess.CalledProcessError as e:
    print(f"git failed with code {e.returncode}")
```

## 3. Bash variables and loops

### Variables

```bash
name="Ada"            # NO spaces around =
echo "Hello, $name"   # use the value with $
echo "${name}_file"   # braces when text follows the name
today=$(date +%F)     # save a command's output
export MODE=dev       # make it visible to programs you start
```

Special variables:

| Variable | Meaning |
|----------|---------|
| `$1`, `$2` | First and second argument to the script |
| `"$@"` | All arguments, each kept separate |
| `$#` | Number of arguments |
| `$?` | Exit code of the last command |
| `$0` | Name of the script |

**Always put double quotes around variables:** `"$name"`, not `$name`.

### Loops

```bash
# for loop over a list
for color in red green blue; do
    echo "$color"
done

# for loop over files
for f in *.txt; do
    echo "Processing: $f"
done

# counting loop
for i in {1..5}; do
    echo "$i"
done

# while loop
count=0
while [ "$count" -lt 3 ]; do
    echo "$count"
    count=$((count + 1))
done

# read a file line by line
while IFS= read -r line; do
    echo "$line"
done < input.txt
```

If statements use the same style:

```bash
if [ -f "$file" ]; then
    echo "File exists"
else
    echo "Missing"
fi
```

Good habit at the top of a script:

```bash
set -euo pipefail
```

This stops the script on errors (`-e`), on unset variables (`-u`), and on failures inside pipes (`pipefail`).

## 4. Command exit codes

Every command returns a number when it finishes. This is the **exit code**.

- `0` means success.
- Any other number means some kind of failure.

Common codes:

| Code | Usual meaning |
|------|---------------|
| `0` | Success |
| `1` | General error |
| `2` | Wrong usage or bad arguments |
| `126` | Found, but cannot be run (permissions) |
| `127` | Command not found |
| `130` | Stopped with Ctrl+C |

In Bash:

```bash
ls /nonexistent
echo "Exit code: $?"          # 2

mkdir build && echo "made it"          # && runs the next command only on success
mkdir build || echo "mkdir failed"     # || runs the next command only on failure

if grep -q "error" log.txt; then
    echo "Found an error"
fi
```

Note: `$?` is overwritten by every command, so save it right away if you need it: `code=$?`.

In Python:

```python
import sys

result = subprocess.run(["false"])
print(result.returncode)      # 1

sys.exit(0)                   # exit with success
sys.exit(1)                   # exit with failure
```

A negative `returncode` in `subprocess` (like `-9`) means the program was killed by a signal.

## 5. Why shell commands must be handled carefully

Shell commands are powerful, so mistakes can be costly.

### 1. Spaces and special characters break things

```bash
file="my report.txt"
rm $file          # BAD: runs rm my report.txt (two files!)
rm "$file"        # GOOD
```

### 2. An empty variable can delete the wrong thing

```bash
rm -rf $dir/      # if $dir is empty, this becomes rm -rf /
rm -rf "${dir:?}/"   # GOOD: stops with an error if dir is empty
```

### 3. Wildcards expand before the command runs

`*` becomes a list of real files. A file named `-rf` or `--help` can then be read as an option. Use `--` to mark the end of options: `rm -- "$file"`.

### 4. Shell injection

If you build a command from user input and run it through a shell, the user can add their own commands.

```python
# DANGEROUS
name = input("Name: ")            # user types:  x; rm -rf ~
subprocess.run(f"echo {name}", shell=True)

# SAFE
subprocess.run(["echo", name])    # input is just data, not code
```

Rules:

- Prefer `subprocess.run([...])` with a list and the default `shell=False`.
- Use `shell=True` only when you truly need shell features, and never with untrusted input.
- If you must build a shell string, use `shlex.quote(value)` on each piece.
- Check input first. For example, a port number should be an integer from 1 to 65535 before you pass it anywhere.

### 5. Silent failures

A script that ignores failures keeps going and can do damage later. Always check the result: use `check=True` in Python, `set -e` or `if` tests in Bash.

### 6. Hanging commands

A command that waits for input or never ends will freeze your program. Use `timeout=` and avoid commands that ask questions.

### 7. Secrets and output

- Do not put passwords or tokens in command-line arguments. Other users on the machine can often see them. Use environment variables or files with strict permissions.
- Do not print or log secrets.

### 8. Test safely

- Print the command first (a "dry run") before you run it for real.
- Try destructive commands (`rm`, `mv`, `chmod`) on test folders first.
- Keep backups of anything you cannot recreate.

## Quick checklist

- [ ] Used a list with `subprocess.run`, not a shell string
- [ ] Set `check=True` and `timeout`
- [ ] Quoted every Bash variable: `"$var"`
- [ ] Added `set -euo pipefail` to Bash scripts
- [ ] Checked exit codes and handled errors
- [ ] Validated user input before using it
- [ ] Used `pathlib` for paths and `encoding="utf-8"` for text
## Mistake I fixed today
-

## Key takeaways
-

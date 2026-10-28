# Day 2: Loops, lists and functions
**Date:** 29 Oct 2026 · **Time:** 60 min

## Learn (20 min)
- `for` and `while` loops
- Lists and dictionaries
- Functions and parameters
- Return values
- Why reusable functions reduce repeated code

## Practice (30 min)
Create `port_reference.py` (starter: [scripts/day02_port_reference.py](../scripts/day02_port_reference.py)). Run it and **add three more common ports**.

## Notes (10 min)
## Notes: Loops, Lists, Dictionaries and Functions

### for loops
A `for` loop repeats a block **once for each item** in a collection. Use it when you know what you're looping over.

```python
ports = [22, 80, 443]

for port in ports:
    print("Checking port", port)
```

| Tool | Example | Meaning |
|---|---|---|
| `range(n)` | `for i in range(3)` | 0, 1, 2 |
| `range(a, b)` | `range(1, 1025)` | 1 up to **1024** (the end is excluded) |
| `range(a, b, step)` | `range(0, 100, 10)` | 0, 10, 20 ... 90 |
| `enumerate()` | `for i, p in enumerate(ports, start=1)` | Gives a counter and the item |
| `break` | | Leave the loop early |
| `continue` | | Skip to the next item |

```python
for number, port in enumerate(ports, start=1):
    print(f"{number}. port {port}")
```

### while loops
A `while` loop repeats **as long as a condition is true**. Use it when you don't know in advance how many times.

```python
attempts = 0
while attempts < 3:
    print("Attempt", attempts + 1)
    attempts += 1
```

A common pattern is validating input until it's acceptable:
```python
while True:
    choice = input("Enter windows or kali: ").strip().lower()
    if choice in ("windows", "kali"):
        break
    print("Invalid choice, try again.")
```

**Warning:** if the condition never becomes false, the loop runs forever (stop it with `Ctrl+C`). Make sure something inside the loop changes the condition.

| | `for` | `while` |
|---|---|---|
| Repeats | For each item / a set number of times | While a condition is true |
| Typical use | Go through ports, files, lines | Retry, wait, validate input |
| Risk | Low | Infinite loop |

### Lists
An **ordered, changeable** collection of items, written with `[ ]`. Items are accessed by **position** (index), starting at **0**.

```python
ports = [22, 80, 443]
print(ports[0])        # 22 (first)
print(ports[-1])       # 443 (last)
print(len(ports))      # 3
```

| Operation | Example | Result |
|---|---|---|
| Add to the end | `ports.append(3389)` | `[22, 80, 443, 3389]` |
| Insert at a position | `ports.insert(0, 21)` | |
| Remove a value | `ports.remove(80)` | |
| Remove by position | `ports.pop()` | Removes and returns the last |
| Check membership | `443 in ports` | `True` |
| Sort | `ports.sort()` | In place, ascending |
| Slice | `ports[0:2]` | First two items |

Lists can hold mixed types, and you can build one from a loop:
```python
open_ports = []
for port in ports:
    if port > 100:
        open_ports.append(port)
```
**List comprehension** (shorter form): `big = [p for p in ports if p > 100]`.

A **tuple** `(22, 80)` is like a list but **cannot be changed**, which suits fixed values. A **set** `{22, 80}` holds unique items only.

### Dictionaries
A collection of **key → value pairs**, written with `{ }`. You look things up by **key**, not by position.

```python
ports = {
    22: "SSH",
    53: "DNS",
    80: "HTTP",
}

print(ports[22])                   # SSH
print(ports.get(8080, "Unknown"))  # Unknown (safe lookup)
```

| Operation | Example |
|---|---|
| Add or update | `ports[3306] = "MySQL"` |
| Delete | `del ports[53]` |
| Check a key | `80 in ports` |
| Keys / values / pairs | `ports.keys()`, `ports.values()`, `ports.items()` |
| Loop over pairs | `for port, name in ports.items():` |

**`ports[9999]` raises a `KeyError`** if the key doesn't exist, while `ports.get(9999, "Unknown")` returns a default instead. Use `.get()` for lookups where a missing key is possible.

Looping over a dictionary directly gives its **keys**:
```python
for port in ports:
    print(port, ports[port])
```

**List vs dictionary:**

| | List | Dictionary |
|---|---|---|
| Structure | Ordered items | Key → value pairs |
| Access by | Position (`ports[0]`) | Key (`ports[22]`) |
| Best for | A sequence: ports to scan, lines in a file | Lookups: port → service, host → status |
| Duplicates | Allowed | Keys must be unique |

Nesting is common in security data:
```python
results = {
    "127.0.0.1": {"open": [8000], "closed": [22, 80]},
}
print(results["127.0.0.1"]["open"])
```
(This shape is very close to JSON, which you'll meet in web and API testing.)

### Functions and parameters
A **function** is a named, reusable block of code. You define it once with `def` and **call** it as many times as you like.

```python
def greet(name):
    print("Hello", name)

greet("kali")
greet("windows")
```

| Term | Meaning |
|---|---|
| **Parameter** | The variable name in the definition (`name`) |
| **Argument** | The actual value you pass when calling (`"kali"`) |
| **Default value** | `def scan(host, timeout=1):` makes `timeout` optional |
| **Keyword argument** | `scan("127.0.0.1", timeout=2)` names the argument |

```python
def check(host, port, timeout=1):
    print(f"Checking {host}:{port} with timeout {timeout}s")

check("127.0.0.1", 80)
check("127.0.0.1", 443, timeout=3)
```

**Rules:**
- The `def` line ends with `:` and the body is **indented**.
- Define the function **before** you call it.
- Variables created inside a function are **local**: they don't exist outside it.
- Docstring (a description) goes on the first line inside: `"""Return the service name for a port."""`.

### Return values
`return` sends a **result back** to the caller and ends the function. Without `return`, a function gives back `None`.

```python
def describe_port(port):
    return ports.get(port, "Unknown service")

service = describe_port(22)     # "SSH"
print(service)
```

| `print` | `return` |
|---|---|
| Shows text on the screen | Hands a value back to the code that called it |
| The result can't be reused | The result can be stored, tested or passed on |

Return several values (as a tuple):
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([22, 80, 443])
```

Return a boolean when the question is yes/no (the style you'll use for scanners):
```python
def is_valid_port(port):
    return 1 <= port <= 65535
```

### Why reusable functions reduce repeated code
Without a function, the same logic is copied for every case, and a fix has to be made in every copy.

```python
# Repeated
print(22, ports.get(22, "Unknown service"))
print(80, ports.get(80, "Unknown service"))
print(443, ports.get(443, "Unknown service"))

# Reusable
def describe_port(port):
    return ports.get(port, "Unknown service")

for port in [22, 80, 443]:
    print(port, describe_port(port))
```

Benefits:
- **Write once, fix once:** a bug or change is handled in a single place.
- **Readable:** `check_port(host, port)` says what it does.
- **Testable:** you can test one small function on its own.
- **Reusable:** the same function works in a port checker, a report tool and a log parser.

**In a security tool:** a scanner is naturally split into small functions such as `validate_target()`, `check_port()` and `save_results()`. That's why `validate_target()` can be improved without touching the scanning code (the Day 6 structure).

### Today's practice, step by step
1. Create `port_reference.py` with the starter dictionary and `describe_port()`.
2. Run it and read the output.
3. Add three more common ports to the dictionary (for example 21 FTP, 25 SMTP, 3306 MySQL).
4. Try `describe_port(9999)` and check that it returns the default.
5. Stretch: write `describe_ports(port_list)` that returns a list of `"22: SSH"` strings, then loop and print them.

### Common mistakes

| Mistake | Fix |
|---|---|
| Off-by-one with `range(1, 1024)` | The end is excluded, so use `range(1, 1025)` to include 1024 |
| `ports[9999]` raises `KeyError` | Use `ports.get(9999, "Unknown")` |
| Forgot to **call** the function (`describe_port` with no parentheses) | Write `describe_port(22)` |
| Used `print` instead of `return` and got `None` | Return the value, print it outside |
| Changing a list while looping over it | Loop over a copy or build a new list |
| Infinite `while` loop | Make sure the condition can become false, and use `Ctrl+C` to stop |
| Mixed up the index of a list with a dictionary key | Lists use positions, dicts use keys |

### Quick self-check
1. What is the difference between a `for` loop and a `while` loop?
2. How is a dictionary different from a list?
3. What is the difference between a parameter and an argument?
4. What happens if a function has no `return`?
5. Why is `describe_port()` better than copying the `.get()` line everywhere?

*Answers: `for` goes through items or a set number of times, `while` repeats while a condition is true; a list is ordered and accessed by position, a dictionary maps keys to values and is accessed by key; a parameter is the name in the definition, an argument is the value passed in; it returns `None`; fixing or changing it happens in one place and the code is clearer.*
## Mistake I fixed today
-

## Key takeaways
-

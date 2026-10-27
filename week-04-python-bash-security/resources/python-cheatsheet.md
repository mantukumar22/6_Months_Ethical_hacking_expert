# Python cheat sheet

```python
# Types and input
name = input("Name: ")          # str
count = int("5")                # int
ok = count > 3                  # bool

# Conditions
if x == 1: ...
elif x == 2: ...
else: ...

# Loops, lists, dicts
for p in [22, 80]: print(p)
ports = {22: "SSH"}; ports.get(23, "Unknown")

# Functions
def describe(port): return ports.get(port, "Unknown")

# Files
from pathlib import Path
Path("f.txt").write_text("hi\n", encoding="utf-8")
text = Path("f.txt").read_text(encoding="utf-8")

# Errors
try: ...
except OSError as error: print(error)

# Subprocess (safe)
import subprocess
subprocess.run(["whoami"], capture_output=True, text=True, timeout=5)

# Sockets
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(1)
    code = s.connect_ex(("127.0.0.1", 80))   # 0 = connected

# Validate an IP
import ipaddress
ipaddress.ip_address("127.0.0.1").is_loopback
```

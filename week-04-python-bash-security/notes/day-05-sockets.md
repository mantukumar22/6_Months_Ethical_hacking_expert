# Day 5: Networking with Python sockets
**Date:** 1 Nov 2026 · **Time:** 60 min

This is where Python starts connecting to the VAPT goal.

## Learn (20 min)
- What a socket is
- TCP connections
- IP addresses and ports
- Connection timeouts
- Difference between a port being **open, closed or filtered**

## Practice (30 min)
Create `tcp_check.py` (starter: [scripts/day05_tcp_check.py](../scripts/day05_tcp_check.py)) and run it. It tests four TCP ports on **your own computer**. If nothing is listening, failed connections are expected.

> A failed connection alone cannot tell you whether a remote port is closed or filtered.

Try it with a listener so one port shows up:
```
python3 -m http.server 8000      # in a second terminal
python3 tcp_check.py             # target: 127.0.0.1
```

## Notes (10 min)
# Sockets and TCP basics

Simple notes on how programs talk over a network.

## Contents

1. [What a socket is](#1-what-a-socket-is)
2. [IP addresses and ports](#2-ip-addresses-and-ports)
3. [TCP connections](#3-tcp-connections)
4. [Connection timeouts](#4-connection-timeouts)
5. [Port states: open, closed, filtered](#5-port-states-open-closed-filtered)
6. [Common problems](#6-common-problems)
7. [Quick summary](#quick-summary)

---

## 1. What a socket is

A **socket** is one end of a conversation between two programs. Your program asks the operating system for a socket, then reads from it and writes to it, a bit like a file.

- A **client** socket connects out to someone else.
- A **server** socket waits (listens) for others to connect.
- Each side has its own socket. Together they form the connection.

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 + TCP
s.close()
```

`AF_INET` means IPv4. `SOCK_STREAM` means TCP. (`SOCK_DGRAM` means UDP.)

## 2. IP addresses and ports

An **IP address** says *which computer*. A **port** says *which program* on that computer. Think of the IP as a building's street address and the port as the apartment number.

| Thing | Example | Notes |
|---|---|---|
| IPv4 address | `192.168.1.10` | 4 numbers, 0 to 255 |
| IPv6 address | `2001:db8::1` | longer, for the future-proof internet |
| Localhost | `127.0.0.1` | "this computer", never leaves the machine |
| All interfaces | `0.0.0.0` | used by servers to listen everywhere |
| Private ranges | `10.x.x.x`, `192.168.x.x`, `172.16-31.x.x` | home and office networks |

**Ports** are numbers from 0 to 65535.

- **0 to 1023**: well-known, usually need admin rights to listen on (80 = HTTP, 443 = HTTPS, 22 = SSH).
- **1024 to 49151**: registered, free for your apps (e.g. 5432 = PostgreSQL, 8080 = dev web servers).
- **49152 to 65535**: dynamic. The OS picks one of these for the client side of a connection. (Linux uses roughly 32768 to 60999 by default.)
- Port 0 is special. If you bind to it, the OS picks a free port for you.

An address plus a port is written `192.168.1.10:8080`.

## 3. TCP connections

**TCP** is the protocol most programs use. It gives you:

- **Reliable** delivery: lost data is sent again.
- **Ordered** delivery: bytes arrive in the order they were sent.
- A **stream** of bytes: there are no message boundaries. Two `send()` calls might arrive as one `recv()`, or one big send might arrive in pieces. You must mark message ends yourself (newlines, length prefixes).

### Opening: the three-way handshake

```
Client  --SYN------->  Server    "I want to connect"
Client  <--SYN-ACK---  Server    "OK, I'm here"
Client  --ACK------->  Server    "Great, connected"
```

### Closing

Each side sends a `FIN` to say "I'm done sending". A `RST` (reset) means "stop, abort now".

### Minimal server and client

```python
# server.py
import socket

with socket.socket() as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 5000))
    srv.listen()
    conn, addr = srv.accept()          # waits for a client
    with conn:
        data = conn.recv(1024)
        conn.sendall(b"echo: " + data)
```

```python
# client.py
import socket

with socket.create_connection(("127.0.0.1", 5000), timeout=3) as c:
    c.sendall(b"hello")
    print(c.recv(1024))                # b'echo: hello'
```

Each connection is identified by four values: your IP, your port, their IP, their port. That is how one server port can handle thousands of clients at once.

## 4. Connection timeouts

A **timeout** is how long you wait before giving up. Without one, a program can hang for a very long time (the OS default for connecting is often around 2 minutes on Linux).

There are two kinds:

- **Connect timeout**: how long to wait for the handshake to finish.
- **Read timeout**: how long to wait for data once connected.

```python
import socket

try:
    with socket.create_connection(("example.com", 80), timeout=3) as s:
        s.settimeout(5)                # separate limit for reads
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        print(s.recv(200))
except socket.timeout:
    print("Timed out")
except ConnectionRefusedError:
    print("Refused")
except OSError as e:
    print("Other network error:", e)
```

Tips:

- **Always set a timeout** on network calls.
- Pick a sensible number: 2 to 5 seconds on a local network, longer for slow links.
- A timeout does not tell you *why* it failed. The server could be down, busy, or hidden behind a firewall.
- Retrying a few times with a short pause is common, but put a limit on the retries.

## 5. Port states: open, closed, filtered

When you try to connect to a port, three things can happen.

| State | What is happening | What you see |
|---|---|---|
| **Open** | A program is listening and accepts you | Handshake completes, connection works |
| **Closed** | The computer is reachable, but nothing is listening on that port | Instant "connection refused" (it answers with `RST`) |
| **Filtered** | A firewall is blocking or dropping your packets | No answer, so you wait until the **timeout** |

**The key difference between closed and filtered:**

- **Closed** = fast answer, "no". The machine replied.
- **Filtered** = silence. The packets disappear, so you only find out after the timeout.

This is why a timeout often points to a firewall, and "refused" often points to "the service isn't running".

(Some firewalls reject instead of drop, which looks like closed. Tools like `nmap` also report `open|filtered` when they can't tell.)

### A simple check in Python

```python
import socket

def check_port(host, port, timeout=2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return "open"
    except ConnectionRefusedError:
        return "closed"
    except socket.timeout:
        return "filtered (or host down)"
    except OSError as e:
        return f"error: {e}"

print(check_port("127.0.0.1", 5000))
```

### Handy command-line tools

```bash
nc -zv example.com 443         # quick open/closed test
ss -tlnp                       # what is listening on this machine (Linux)
nmap -p 22,80,443 host         # scan specific ports
```

> Only scan machines you own or have permission to test.

## 6. Common problems

1. **"Address already in use"**: another program (or your previous run) holds the port. Pick a different port or use `SO_REUSEADDR`.
2. **Server works locally but not from another computer**: it is bound to `127.0.0.1`. Bind to `0.0.0.0` instead, and check the firewall.
3. **`recv()` returns less than you expected**: TCP is a stream. Loop until you have the full message.
4. **`recv()` returns `b""`**: the other side closed the connection.
5. **Program freezes**: you forgot a timeout.

## Quick summary

| Topic | Remember this |
|---|---|
| Socket | One end of a connection |
| IP address | Which computer |
| Port | Which program (0 to 65535) |
| TCP | Reliable, ordered stream, starts with a handshake |
| Timeout | Always set one |
| Open | Someone is listening |
| Closed | Machine answers "no" right away |
| Filtered | No answer, firewall is likely dropping packets |
## Mistake I fixed today
-

## Key takeaways
-

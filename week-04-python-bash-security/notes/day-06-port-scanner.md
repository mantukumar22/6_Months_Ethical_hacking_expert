# Day 6: Build a Python port scanner
**Date:** 2 Nov 2026 · **Time:** 60 min

## Learn (15 min)
Review socket code, exception handling and loops. A scanner automates repeated connection checks. It does **not** automatically identify vulnerabilities.

## Practice (35 min)
Extend Day 5's script so it:
- [ ] Accepts a target IP
- [ ] Checks a small, predefined list of TCP ports
- [ ] Prints successful connections
- [ ] Handles connection errors and timeouts
- [ ] Saves results to `scan_results.txt`

Keep the target restricted to `127.0.0.1` or a lab machine I own or am explicitly authorized to test.

Write your own version first. A finished reference is in [scripts/day06_port_scanner.py](../scripts/day06_port_scanner.py), so compare after.

## Review (10 min)
Test against localhost. Explain what happens when a port has no service listening, and why the results are not a full vulnerability assessment.

# Closed ports and port checks

Short notes in simple words. One line per topic.

## When no service is listening

- **What it means:** The port is closed. No program is waiting on it.
- **What the computer does:** It sends back a `RST` (reset) packet.
- **What you see:** A fast "connection refused" error.
- **What it tells you:** The computer is on and reachable.
- **Closed vs filtered:** Closed answers fast. Filtered stays silent until the timeout.
- **UDP:** The computer usually sends an ICMP "port unreachable" message.

```python
import socket

try:
    socket.create_connection(("127.0.0.1", 9999), timeout=2)
except ConnectionRefusedError:
    print("Closed: nothing is listening")
```

## Why a port check is not a vulnerability assessment

- **It only checks the door.** It shows if a port answers, not if the service is safe.
- **No version info.** It does not tell you which software or version is running.
- **No bug checks.** It does not look for known flaws (CVEs).
- **No weak settings.** It does not find default passwords or bad configs.
- **No login tests.** It does not test who can sign in or what they can do.
- **No app testing.** It does not test the website or API logic behind the port.
- **Filtered is unclear.** A firewall hides what is behind it.
- **Only the ports you tried.** Other ports and UDP may be open.
- **Only this moment.** Things change after a new install or update.
- **Open does not mean unsafe.** Many open ports are normal and needed.
- **Closed does not mean secure.** The machine can still have other weak spots.

## What a real assessment adds

- **Full scans:** All ports, TCP and UDP, IPv4 and IPv6.
- **Service detection:** Finds what runs behind each port.
- **Vulnerability scan:** Matches versions against known flaws.
- **Patch check:** Finds missing updates.
- **Config review:** Finds weak settings and default accounts.
- **Manual testing:** A trained person tries real attacks safely.
- **Report:** Risks ranked, with fixes listed.

> Only test machines you own or have permission to test.

## Quick summary

| Topic | One line |
|---|---|
| Closed port | Nothing listening, instant refusal |
| Port check | Shows reachability only |
| Vulnerability assessment | Looks for real weaknesses |

## Mistake I fixed today
-

## Key takeaways
-

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

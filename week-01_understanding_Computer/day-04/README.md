# Day 04 — Operating Systems (key day)

## Learn: what an OS does
1. **Process management** — decides who gets the CPU.
2. **Memory management** — gives each program its own memory space.
3. **File management** — organizes data on disk.
4. **User management** — accounts, admin vs standard user.
5. **Hardware interaction** — via drivers.
6. **Networking** — connections and ports.
7. **Security/permissions** — who may do what.

Examples: Windows, Linux, macOS, Android, iOS.

## Resource
TryHackMe — Operating Systems Basics room (OS fundamentals, Windows, Linux CLI, Windows CLI, OS security).

## Practical (Command Prompt)
```
whoami        # which user am I?
hostname      # computer name
systeminfo    # OS version, patches, hardware
ipconfig      # network configuration
tasklist      # running processes
```
Then:
```
cd
dir
mkdir cyber
cd cyber
echo hello > test.txt
type test.txt
```
Write what each command tells you in `evidence/commands.md`.

## Cybersecurity perspective
These are exactly the first commands an attacker runs after getting in (**enumeration**: who am I, what machine, what network, what's running) and the first an analyst runs when investigating. `systeminfo` reveals patch level — missing patches = known exploits. Privilege (admin vs user) decides how much damage a compromise causes: **least privilege** is a core defense.

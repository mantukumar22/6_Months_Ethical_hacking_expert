# Day 1: Linux basics and filesystem navigation
**Date:** 23 Oct 2026 · **OS:** Kali Linux · **Time:** 60 min

## Learn (20 min)
- What Linux is: kernel + shell + utilities. Distros (Kali is Debian-based).
- The shell: `bash`, the prompt, `$` (normal user) vs `#` (root).
- Everything is a file. One tree starting at `/` (no drive letters).
- Key directories (Filesystem Hierarchy Standard):

| Path | Purpose |
|---|---|
| `/` | Root of the whole filesystem |
| `/home` | Users' personal folders (`~` is your home) |
| `/root` | The root user's home |
| `/etc` | System configuration files |
| `/var` | Variable data: logs (`/var/log`), caches |
| `/tmp` | Temporary files |
| `/bin`, `/usr/bin` | User commands |
| `/sbin`, `/usr/sbin` | Admin commands |
| `/dev` | Device files |
| `/proc` | Live info about processes and kernel |
| `/opt` | Optional third-party software |

- Absolute path (`/etc/passwd`) vs relative path (`../notes`). `.` = here, `..` = parent, `~` = home.

## Practice (30 min)
Lab: [lab-01-navigation](../labs/lab-01-navigation.md)

## Notes (10 min)
## Day 1 Glossary: Linux Basics and the Filesystem

### What is Linux?
Strictly, **Linux is the kernel**: the core program that controls hardware (CPU, memory, disks, network) and lets programs run. A usable operating system adds a **shell** and **utilities** on top.

| Part | Role | Example |
|---|---|---|
| Kernel | Talks to hardware, manages processes and memory | Linux kernel (`uname -r`) |
| Shell | Command interpreter you type into | `bash`, `zsh` |
| Utilities | Small programs that do one job | `ls`, `cp`, `grep`, `ps` |

### Distribution (distro)
A complete package of the Linux kernel + utilities + package manager + defaults. Examples: Ubuntu, Fedora, Arch, and **Kali**. **Kali Linux is Debian-based**, so it uses `apt` / `dpkg` for software and is built for security testing. Check yours with `cat /etc/os-release`.

### The shell and the prompt
The **shell** reads what you type, runs the command and prints the result. **Bash** is the classic one (recent Kali versions default to **zsh**, which works the same for these commands). Check with `echo $SHELL`.

The last character of the prompt tells you who you are:

| Prompt ends with | Meaning |
|---|---|
| `$` | Normal user, limited rights |
| `#` | **root**, the superuser with full control |

On Kali the prompt looks like this:
```
┌──(kali㉿kali)-[~]
└─$
```
That reads as `user@hostname` and the current folder (`~` is the home folder). Use `sudo` to run single commands as root instead of working as root all the time, because a typo as root can damage the system.

### "Everything is a file"
Linux represents almost everything as a file or something you read and write like one: documents, directories, devices (`/dev/sda`), running process info (`/proc`), even some network and system settings. This is why the same tools (`cat`, `grep`, `ls`) work on so many different things.

### One tree starting at `/`
Windows has separate drives (`C:\`, `D:\`). Linux has **one single tree** that starts at `/` (the **root directory**, not to be confused with the root *user*). Other disks and USB drives are **mounted** somewhere inside this tree, for example under `/mnt` or `/media`. Paths use forward slashes: `/home/kali/notes.txt`.

### Key directories (Filesystem Hierarchy Standard)

| Path | Purpose | Try it |
|---|---|---|
| `/` | Root of the whole filesystem | `ls /` |
| `/home` | Users' personal folders (`~` is your own home) | `ls /home` |
| `/root` | The **root user's** home (not under `/home`) | `sudo ls /root` |
| `/etc` | System-wide **configuration** files | `ls /etc` |
| `/var` | **Variable** data that changes: logs (`/var/log`), caches, mail | `ls /var/log` |
| `/tmp` | Temporary files, usually cleared on reboot | `ls /tmp` |
| `/bin`, `/usr/bin` | Everyday **user commands** (`ls`, `cat`) | `ls /usr/bin \| head` |
| `/sbin`, `/usr/sbin` | **Admin** commands (`ip`, `fdisk`), mostly for root | `ls /usr/sbin \| head` |
| `/dev` | **Device** files (disks, terminals, `/dev/null`) | `ls /dev` |
| `/proc` | **Live** info about processes and the kernel, generated on the fly | `cat /proc/cpuinfo` |
| `/opt` | **Optional** third-party software installed as one folder | `ls /opt` |

On modern distros `/bin` and `/sbin` are often just links to `/usr/bin` and `/usr/sbin`, so you may see them as the same place.

**Why these matter for security work:** `/etc` holds configs and account files (`/etc/passwd`), `/var/log` holds the evidence of what happened on a system, `/tmp` is a world-writable place attackers often use, and `/proc` shows what is running.

### Paths
| Type | Example | Meaning |
|---|---|---|
| Absolute | `/etc/passwd` | Starts at `/`. Works from anywhere |
| Relative | `../notes` | Depends on where you are now |
| `.` | | The current directory |
| `..` | | The parent directory |
| `~` | | Your home directory |

### Quick self-check
1. What is the difference between the kernel and a distro?
2. What does `#` at the end of a prompt tell you?
3. Where would you look for a system log? A config file? Your own files?
4. Why is there no `C:` drive on Linux?

## Key takeaways
-

## Still confusing / to revisit
-

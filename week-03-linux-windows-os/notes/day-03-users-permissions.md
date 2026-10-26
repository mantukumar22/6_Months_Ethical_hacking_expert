# Day 3: Users, groups and permissions
**Date:** 25 Oct 2026 · **OS:** Kali Linux · **Time:** 60 min

## Learn (20 min)
- Users and groups: `whoami`, `id`, `groups`. Files: `/etc/passwd` (accounts), `/etc/shadow` (password hashes, root only), `/etc/group`.
- **root** = UID 0, full control. `sudo` runs one command with root rights.
- Reading `ls -l`:

```
-rwxr-xr-- 1 kali devs 1200 Oct 23 10:00 script.sh
│└┬┘└┬┘└┬┘
│ │  │  └ others: r--
│ │  └─── group:  r-x
│ └────── owner:  rwx
└──────── type (- file, d directory, l link)
```

- Octal: r=4, w=2, x=1. `rwx`=7, `r-x`=5, `r--`=4. So `rwxr-xr--` = **754**.
- `chmod` (symbolic `u+x`, `g-w`, `o=r`; octal `640`), `chown user:group file`, `umask`.
- On a directory: `r` list, `w` create/delete inside, `x` enter.
- Special bits: **SUID** (run as the file's owner), SGID, sticky bit (`/tmp`). Why they matter for privilege escalation later.

## Practice (30 min)
Lab: [lab-03-permissions](../labs/lab-03-permissions.md)

## Notes (10 min)
## Day 3 Notes: Users, Groups and Permissions

### Users and groups

| Command | One-line explanation | Example output |
|---|---|---|
| `whoami` | Prints the username you are currently logged in as | `kali` |
| `id` | Shows your UID, primary GID and all groups | `uid=1000(kali) gid=1000(kali) groups=...,27(sudo)` |
| `groups` | Lists the groups you belong to | `kali sudo users` |

A **group** lets you give the same access to several users at once. Every user has one **primary group** plus optional extra groups.

### Account files

| File | Contains | Who can read it |
|---|---|---|
| `/etc/passwd` | Account list (name, UID, home, shell) | Everyone |
| `/etc/shadow` | Password **hashes** and password aging | **root only** |
| `/etc/group` | Group names and their members | Everyone |

**Format of a `/etc/passwd` line:**
```
kali:x:1000:1000:Kali,,,:/home/kali:/usr/bin/zsh
 |   |  |    |     |        |           |
 |   |  |    |     |        |           └ login shell
 |   |  |    |     |        └ home directory
 |   |  |    |     └ comment (full name)
 |   |  |    └ primary GID
 |   |  └ UID
 |   └ "x" = the password hash is stored in /etc/shadow
 └ username
```
Why `/etc/shadow` is root-only: password hashes can be attacked offline (cracked). If anyone could read them, every user's password would be at risk.

### root and sudo
- **root** is the superuser with **UID 0** and full control over the system. Permissions don't restrict it.
- **`sudo`** runs **one command** with root rights, after you authenticate and only if you're allowed (members of the `sudo` group on Kali). Example: `sudo cat /etc/shadow`.
- Best practice: work as a normal user and use `sudo` only when needed, because a typo as root can damage the system.

### Reading `ls -l`
```
-rwxr-xr-- 1 kali devs 1200 Oct 23 10:00 script.sh
│└┬┘└┬┘└┬┘
│ │  │  └ others: r--
│ │  └─── group:  r-x
│ └────── owner:  rwx
└──────── type (- file, d directory, l link)
```
After the permission string: link count, **owner** (`kali`), **group** (`devs`), size, date, name.

### Permission meanings

| Letter | On a file | On a directory |
|---|---|---|
| `r` read | View the contents | **List** the names inside (`ls`) |
| `w` write | Modify the contents | **Create, rename, delete** files inside |
| `x` execute | Run it as a program | **Enter** it (`cd`) and access items inside |

Tip: a directory needs `x` to be usable. With `r` but no `x`, you can see the names but not open anything.

### Octal permissions
Each permission has a value: **r = 4, w = 2, x = 1**. Add them per group of three (owner, group, others).

| Symbolic | Calculation | Octal |
|---|---|---|
| `rwx` | 4+2+1 | 7 |
| `rw-` | 4+2 | 6 |
| `r-x` | 4+1 | 5 |
| `r--` | 4 | 4 |
| `---` | 0 | 0 |

So `rwxr-xr--` = 7 (owner) + 5 (group) + 4 (others) = **754**.

Common values:

| Octal | Meaning | Typical use |
|---|---|---|
| `600` | Owner read/write, no one else | Private files, SSH keys |
| `644` | Owner read/write, others read | Normal files |
| `700` | Owner only, full | Private directories/scripts |
| `755` | Owner full, others read/execute | Programs, public directories |
| `777` | Everyone can do everything | **Avoid**, it's a security risk |

### chmod, chown, umask

**`chmod`**: changes permissions.

| Style | Example | Meaning |
|---|---|---|
| Symbolic | `chmod u+x script.sh` | Add execute for the **u**ser (owner) |
| | `chmod g-w file` | Remove write from the **g**roup |
| | `chmod o=r file` | Set others to read-only exactly |
| | `chmod a+r file` | Add read for **a**ll |
| Octal | `chmod 640 file` | Owner rw, group r, others none |

(`u` = owner, `g` = group, `o` = others, `a` = all. `+` add, `-` remove, `=` set exactly.)

**`chown`**: changes owner and group (needs root): `sudo chown kali:devs file`.

**`umask`**: the mask that removes permissions from **newly created** files and directories.
- New files start from `666`, new directories from `777`, then the umask is subtracted.
- Common umask `022` → files `644`, directories `755`.
- Check yours with `umask`.

### Special permission bits

| Bit | Octal | Shown as | Effect | Example |
|---|---|---|---|---|
| **SUID** | 4000 | `s` in the owner's `x` spot (`-rwsr-xr-x`) | Runs with the **file owner's** privileges, not the user's | `/usr/bin/passwd` (needs root to edit shadow) |
| **SGID** | 2000 | `s` in the group's `x` spot | Runs as the file's group. On a directory, new files inherit the directory's group | Shared project folders |
| **Sticky** | 1000 | `t` at the end (`drwxrwxrwt`) | Only a file's owner (or root) can delete it, even if others can write to the directory | `/tmp` |

**Why they matter for privilege escalation:** a SUID program owned by root runs as root. If it can be tricked into running commands or reading files (misconfigured or vulnerable), a normal user can gain root. Attackers and pentesters list SUID files early:
```
find / -perm -4000 -type f 2>/dev/null
```
Also worth checking: world-writable files (`777`), readable private keys, and sensitive files with wrong permissions. In this lab, only **look**, don't change special bits on system files.

### Quick self-check
1. What does `rw-r-----` equal in octal? What about `755` in symbolic form?
2. Why is `/etc/passwd` readable by everyone but `/etc/shadow` isn't?
3. What does `x` allow on a directory?
4. What is the difference between `su` and `sudo`? (`su` switches user, `sudo` runs one command with elevated rights.)
5. Why can a root-owned SUID binary be dangerous?

*Answers: 640; rwxr-xr-x; entering the directory and accessing what's inside; see above; it runs with root's rights whatever user starts it.*

## Key takeaways
-

## Still confusing / to revisit
-

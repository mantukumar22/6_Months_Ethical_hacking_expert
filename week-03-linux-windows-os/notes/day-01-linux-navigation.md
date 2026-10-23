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
Explain in your own words: absolute vs relative path, and what lives in `/etc`, `/var/log` and `/home`.

## Key takeaways
-

## Still confusing / to revisit
-

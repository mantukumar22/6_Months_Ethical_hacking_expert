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
Convert by hand: `rw-r-----` = ? and `755` = ? Why is `/etc/shadow` not world-readable?

## Key takeaways
-

## Still confusing / to revisit
-

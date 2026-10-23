# Week 3: Linux & Windows Operating Systems

**23–29 October 2026 · 7 days · 1 hour per day**

Goal: navigate Linux, manage files and permissions, inspect processes, understand users and groups, and use basic Windows administration commands. These are prerequisites for ethical hacking, VAPT, SOC analysis and red teaming.

**Setup:** use **Kali Linux** for the Linux command-line practice and the **Windows laptop** for Windows administration practice.

> **Safety rules**
> - Practice only on my own machines (or VMs I own).
> - Do destructive commands (`rm`, `chmod -R`, `chown -R`) only inside the sandbox folder `~/week3-lab` (Linux) or `C:\week3-lab` (Windows). Never run `rm -rf` with `sudo` or on `/`.
> - Don't paste commands I don't understand. Read first, then run.
> - Never commit unredacted output (usernames, hostnames, IPs, serial numbers) to a public repo.

## Schedule

| Day | Date | Topic | OS | Notes | Lab |
|---|---|---|---|---|---|
| 1 | 23 Oct | Linux basics and filesystem navigation | Kali | [day-01](notes/day-01-linux-navigation.md) | [lab-01](labs/lab-01-navigation.md) |
| 2 | 24 Oct | Files, text tools, pipes and redirection | Kali | [day-02](notes/day-02-files-text-pipes.md) | [lab-02](labs/lab-02-files-text.md) |
| 3 | 25 Oct | Users, groups and permissions | Kali | [day-03](notes/day-03-users-permissions.md) | [lab-03](labs/lab-03-permissions.md) |
| 4 | 26 Oct | Processes and services | Kali | [day-04](notes/day-04-processes-services.md) | [lab-04](labs/lab-04-processes.md) |
| 5 | 27 Oct | Windows administration basics | Windows | [day-05](notes/day-05-windows-admin.md) | [lab-05](labs/lab-05-windows-basics.md) |
| 6 | 28 Oct | Windows users, permissions and logs | Windows | [day-06](notes/day-06-windows-users-logs.md) | [lab-06](labs/lab-06-windows-users-logs.md) |
| 7 | 29 Oct | Revision and mini-project | Both | [day-07](notes/day-07-revision.md) | [project](project/system-profile-report.md) |

Each day: **Learn 20 min → Practice 30 min → Notes 10 min** (Day 7: 15 revision / 35 project / 10 review).

## Repo layout
```
notes/          daily notes (one file per day)
labs/           hands-on exercises with result tables
project/        Day 7 system profile report (redacted)
resources/      Linux, Windows and comparison cheat sheets, links
raw-private/    UNREDACTED output. git-ignored, never commit
checklist.md    weekly completion checklist
```

## Progress
See [checklist.md](checklist.md). **0/7** done.

## Standard before Week 4
Without notes, I can: navigate Linux and find a file, read and change permissions in octal, list and stop a process, create a user and add it to a group, and do the equivalent tasks on Windows (CMD or PowerShell).

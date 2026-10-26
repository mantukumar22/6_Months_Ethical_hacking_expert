# Day 4: Processes and services
**Date:** 26 Oct 2026 · **OS:** Kali Linux · **Time:** 60 min

## Learn (20 min)
- A **process** is a running program with a **PID** and a parent (**PPID**). `systemd` is PID 1.
- View: `ps aux`, `ps -ef`, `top`/`htop`, `pstree`, `/proc/<PID>`.
- Background and jobs: `cmd &`, `jobs`, `fg`, `bg`, `Ctrl+Z`, `Ctrl+C`.
- Signals: `kill <PID>` (SIGTERM, polite), `kill -9 <PID>` (SIGKILL, force), `pkill name`.
- **Services** (daemons) are managed by `systemd`: `systemctl status|start|stop|restart|enable|disable <name>`.
- Logs: `journalctl -u <service>`, `/var/log/`.
- Link to Week 2: `ss -tulpn` shows which process owns a listening port.

## Practice (30 min)
Lab: [lab-04-processes](../labs/lab-04-processes.md)

## Notes (10 min)
## Day 4 Notes: Processes and Services

### What is a process?
A **process** is a running instance of a program. The kernel gives each one:

| Field | Meaning |
|---|---|
| **PID** | Process ID, a unique number |
| **PPID** | Parent process ID, the process that started it |
| UID | The user it runs as, which decides its permissions |
| State | Running (R), sleeping (S), stopped (T), zombie (Z) |

Every process has a parent, which forms a tree. **`systemd` is PID 1**, the first process started at boot, and it is the ancestor of everything else. When you type a command, your shell starts it as a child process.

### Viewing processes

| Command | One-line explanation |
|---|---|
| `ps aux` | Snapshot of **all** processes with user, CPU and memory |
| `ps -ef` | Same idea in another format, and it shows the **PPID** |
| `top` | Live view sorted by CPU (`q` quits, `M` sorts by memory, `k` kills) |
| `htop` | A friendlier `top` with colors and scrolling (`sudo apt install htop`) |
| `pstree -p` | Shows the parent/child tree with PIDs |
| `/proc/<PID>` | Kernel-generated folder of info about one process |

**Reading `ps aux`:**
```
USER   PID %CPU %MEM    VSZ   RSS TTY   STAT START  TIME COMMAND
kali  1234  0.0  0.1  10200  3500 pts/0 Ss   10:00  0:00 -zsh
```

| Column | Meaning |
|---|---|
| USER | Owner of the process |
| PID | Process ID |
| %CPU / %MEM | Share of CPU and memory used |
| STAT | State (`S` sleeping, `R` running, `Z` zombie, `s` session leader) |
| COMMAND | The command that started it |

Useful `/proc/<PID>` items (try with your shell's PID from `echo $$`):
```
cat /proc/$$/cmdline | tr '\0' ' '    # the command line
ls -l /proc/$$/exe                    # the actual program file
cat /proc/$$/status | head            # name, state, PPID, UID
```

Finding one process:
```
ps aux | grep "[s]leep"     # the [s] trick stops grep matching itself
pgrep -a sleep              # simpler
```

### Foreground, background and jobs

| Action | Key / command | Effect |
|---|---|---|
| Run in background | `cmd &` | Starts it and returns the prompt |
| List jobs | `jobs` | Shows background/stopped jobs in this shell |
| Pause the foreground job | `Ctrl+Z` | Suspends it (SIGTSTP) |
| Resume in background | `bg` | Continues the stopped job in the background |
| Bring to foreground | `fg` | Brings the job back to the front (`fg %1` for job 1) |
| Interrupt | `Ctrl+C` | Stops the foreground job (SIGINT) |

Example:
```
sleep 300 &          # starts in background, prints [1] <PID>
jobs                 # [1]+ Running  sleep 300 &
fg                   # bring it to the front
Ctrl+Z               # pause it
bg                   # let it run in the background again
kill %1              # stop job 1
```

### Signals and killing processes
A **signal** is a message sent to a process. `kill` doesn't only kill, it sends any signal. The default is SIGTERM.

| Signal | Number | Meaning | How |
|---|---|---|---|
| **SIGTERM** | 15 | "Please stop." The program can clean up first | `kill <PID>` |
| **SIGKILL** | 9 | Forced stop by the kernel. Can't be caught, **no cleanup** | `kill -9 <PID>` |
| SIGINT | 2 | Interrupt from the keyboard | `Ctrl+C` |
| SIGSTOP / SIGCONT | 19 / 18 | Pause / resume | `kill -STOP <PID>` / `kill -CONT <PID>` |
| SIGHUP | 1 | Hang up. Many services reload their config | `kill -HUP <PID>` |

| Command | One-line explanation |
|---|---|
| `kill <PID>` | Sends SIGTERM (polite). Try this first |
| `kill -9 <PID>` | Sends SIGKILL (force). Last resort, can leave temp files or corrupted data |
| `pkill name` | Kills processes by **name** (be careful, it matches patterns) |
| `killall name` | Kills all processes with exactly that name |

You can only signal your own processes unless you use `sudo`. **Never kill a process you don't recognize**, and never kill PID 1.

### Services (daemons)
A **service** (daemon) is a process that runs in the background, usually started at boot, such as `ssh`, `cron` or `NetworkManager`. On Kali, **systemd** manages them with `systemctl`.

| Command | One-line explanation |
|---|---|
| `systemctl status ssh` | Shows if it's active, enabled, its PID and recent log lines |
| `sudo systemctl start ssh` | Starts it **now** (not at boot) |
| `sudo systemctl stop ssh` | Stops it **now** |
| `sudo systemctl restart ssh` | Stops then starts it |
| `sudo systemctl enable ssh` | Makes it start **automatically at boot** (doesn't start it now) |
| `sudo systemctl disable ssh` | Stops it starting at boot (doesn't stop it now) |
| `systemctl list-units --type=service --state=running` | Lists the running services |
| `systemctl is-enabled ssh` | Shows if it starts at boot |

**`start` vs `enable`:** `start` affects the current session only. `enable` affects the next boot. They're independent, and `enable --now` does both.

**Security note:** every running service that listens on a port is attack surface. Only run what you need, and don't leave SSH running on a machine on a shared network without a reason.

### Logs

| Command / location | One-line explanation |
|---|---|
| `journalctl -u ssh` | Logs for one service from the systemd journal |
| `journalctl -u ssh -f` | Follows new log lines live |
| `journalctl -n 20` | Last 20 entries |
| `journalctl -p err -b` | Errors since the current boot |
| `journalctl --since "1 hour ago"` | Time-filtered logs |
| `/var/log/` | Traditional log files (`syslog`, `auth.log`, `dpkg.log`) |

`/var/log/auth.log` records logins and `sudo` use, which is a key source for SOC analysis. On some newer systems it may not exist, and `journalctl` has the same events.

### Link to Week 2: which process owns a port
```
sudo ss -tulpn
```

| Flag | Meaning |
|---|---|
| `-t` | TCP sockets |
| `-u` | UDP sockets |
| `-l` | **Listening** sockets only |
| `-p` | Show the **process** (and PID) that owns each |
| `-n` | Numeric ports and addresses, no name lookups |

Example output:
```
Netid State  Local Address:Port  Process
tcp   LISTEN 0.0.0.0:22          users:(("sshd",pid=842,fd=3))
tcp   LISTEN 127.0.0.1:5432      users:(("postgres",pid=911,fd=5))
```
Read it as: `sshd` (PID 842) is listening on port 22 on all interfaces. `127.0.0.1` means local only (Week 2). This is the Linux equivalent of `netstat -ano` plus `tasklist` on Windows.

### Why it matters for security
- **Malware and persistence:** attackers hide as processes or services. You find them by spotting unusual names, odd paths (`ls -l /proc/<PID>/exe`), and unexpected parent/child relationships (for example a web server spawning a shell).
- **Privilege:** a process runs with its owner's rights, so a vulnerable service running as root is a path to full compromise.
- **Exposure:** listening ports (`ss -tulpn`) show what an attacker can reach.
- **Evidence:** logs (`journalctl`, `/var/log`) show what happened and when.

### Quick self-check
1. What are PID and PPID, and which process is PID 1?
2. What is the difference between `kill` and `kill -9`? Which should you try first?
3. What is the difference between `systemctl start` and `systemctl enable`?
4. How do you find which process owns port 22?
5. What do `Ctrl+Z`, `bg` and `fg` do together?

*Answers: process ID and parent's ID, systemd; SIGTERM allows cleanup and SIGKILL can't be caught, so try `kill` first; start = now, enable = at boot; `sudo ss -tulpn` and look at the Process column; pause a job, resume it in the background, bring it back to the foreground.*

## Key takeaways
-

## Still confusing / to revisit
-

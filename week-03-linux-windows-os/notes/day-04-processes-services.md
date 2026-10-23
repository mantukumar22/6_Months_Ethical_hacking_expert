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
Explain: process vs service, SIGTERM vs SIGKILL, and `start` vs `enable`.

## Key takeaways
-

## Still confusing / to revisit
-

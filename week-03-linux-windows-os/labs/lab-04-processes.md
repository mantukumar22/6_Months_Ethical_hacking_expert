# Lab 04: Processes and services (Kali)

**Tasks**
1. `ps aux | head` and `ps -ef | head`. Identify the columns USER, PID, %CPU, %MEM, COMMAND.
2. `top` (quit with `q`). Which process uses the most CPU/memory? Try `htop` if installed.
3. `pstree -p | head -20`. What is PID 1?
4. Start and stop a process:
```
sleep 300 &
jobs
ps aux | grep "[s]leep"
kill <PID>
```
   Then run `sleep 300` in the foreground, press `Ctrl+Z`, then `bg`, then `fg`, then `Ctrl+C`.
5. Compare signals: start `sleep 500 &`, stop it once with `kill <PID>` and (another time) with `kill -9 <PID>`. Which is the safe default?
6. Services:
   - `systemctl list-units --type=service --state=running | head`
   - `systemctl status ssh` (or another service). Is it active? enabled?
   - **Do not enable SSH to the network without a reason.** If you try it: `sudo systemctl start ssh` then `sudo systemctl stop ssh`.
7. Logs: `journalctl -n 20`, `journalctl -u ssh --no-pager | tail`.
8. Ports to processes (Week 2 link): `sudo ss -tulpn`. Find one listening port and the process that owns it.

**Results**

| Item | Answer |
|---|---|
| PID 1 | |
| Top CPU/memory process | |
| SIGTERM vs SIGKILL | |
| One running service | |
| One listening port + owning process | |

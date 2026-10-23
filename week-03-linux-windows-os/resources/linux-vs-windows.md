# Linux vs Windows: command equivalents

| Task | Linux (Kali) | Windows |
|---|---|---|
| Current user | `whoami` | `whoami` |
| Current folder | `pwd` | `cd` |
| List files | `ls -la` | `dir /a` |
| Read a file | `cat f` | `type f` |
| Search in files | `grep -r` | `findstr /s` |
| Find files | `find / -name x` | `dir /s x` |
| Copy / move / delete | `cp` / `mv` / `rm` | `copy` / `move` / `del` |
| List processes | `ps aux` | `tasklist` |
| Kill a process | `kill PID` | `taskkill /PID n` |
| Services | `systemctl status x` | `sc query x` |
| Users | `cat /etc/passwd` | `net user` |
| Add user | `sudo adduser u` | `net user u /add` |
| Groups | `groups`, `id` | `net localgroup`, `whoami /groups` |
| Permissions | `ls -l`, `chmod` | `icacls` |
| Listening ports | `sudo ss -tulpn` | `netstat -ano` |
| System info | `uname -a` | `systeminfo` |
| Logs | `/var/log`, `journalctl` | Event Viewer |
| Network config | `ip addr` | `ipconfig /all` |

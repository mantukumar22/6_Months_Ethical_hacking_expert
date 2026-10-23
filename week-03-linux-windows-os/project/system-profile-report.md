# System Profile Report: Kali Linux and Windows
**Date:** 29 Oct 2026

> **Redact before publishing:** usernames, hostnames, IP and MAC addresses, serial numbers, product keys, and any machine-identifying details. Use placeholders such as `user1`, `host-kali`, `192.168.x.x`. Keep raw output in `raw-private/`.

## 1. Kali Linux
| Item | Command | Result |
|---|---|---|
| Distro / version | `cat /etc/os-release` | |
| Kernel | `uname -r` | |
| Current user / groups | `id` | |
| Number of user accounts | `wc -l /etc/passwd` | |
| Top 3 processes by memory | `ps aux --sort=-%mem \| head -4` | |
| Listening services | `sudo ss -tulpn` | |
| Running services (count) | `systemctl list-units --type=service --state=running \| wc -l` | |
| Example permission analysis | `ls -l /etc/passwd /etc/shadow` | |

## 2. Windows
| Item | Command | Result |
|---|---|---|
| OS name / version | `systeminfo` | |
| Current user / groups | `whoami /groups` | |
| Local users | `net user` | |
| Administrators | `net localgroup Administrators` | |
| Top 3 processes | `Get-Process \| Sort-Object WS -Desc \| Select -First 3` | |
| Listening ports | `netstat -ano \| findstr LISTENING` | |
| Firewall state | `netsh advfirewall show allprofiles` | |
| Notable event (4624/4625) | Event Viewer → Security | |

## 3. Linux vs Windows comparison
| Concept | Linux | Windows |
|---|---|---|
| Admin account | root / sudo | Administrator / UAC elevation |
| Permissions model | rwx for owner/group/others | ACLs (`icacls`) |
| List processes | `ps`, `top` | `tasklist`, `Get-Process` |
| Services | `systemctl` | `sc`, `Get-Service` |
| User accounts | `/etc/passwd` | `net user`, `Get-LocalUser` |
| Logs | `/var/log`, `journalctl` | Event Viewer, `Get-WinEvent` |

## 4. Analysis
- What stood out as most different between the two systems?
- One thing I found that I should review for security (e.g. an unneeded listening service or an extra admin user):
- One command I want to master next:

## 5. Redaction checklist
- [ ] Usernames and hostnames replaced
- [ ] IPs and MAC addresses removed
- [ ] Serial numbers / product IDs removed
- [ ] Screenshots checked and cropped

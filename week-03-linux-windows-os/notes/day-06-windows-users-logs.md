# Day 6: Windows users, permissions and logs
**Date:** 28 Oct 2026 · **OS:** Windows · **Time:** 60 min

## Learn (20 min)
- Accounts: local users and groups. Built-in: **Administrator**, **Administrators** group, **Users**.
- Identity and privileges: `whoami /all`, `whoami /groups`, `whoami /priv`.
- **UAC** (User Account Control): admin rights need elevation.
- Permissions: **NTFS ACLs**. View/change with `icacls <path>`. Rights like Full (F), Modify (M), Read & Execute (RX), Read (R).
- Users and groups from the command line: `net user`, `net localgroup`, PowerShell `Get-LocalUser`, `Get-LocalGroupMember`.
- Logs: **Event Viewer** (`eventvwr`). Logs: Application, System, **Security**. Key events: 4624 (logon success), 4625 (logon failed), 4672 (special privileges), 4688 (process created, if auditing enabled).
- Defenses: Windows Defender status, Windows Firewall.

## Practice (30 min)
Lab: [lab-06-windows-users-logs](../labs/lab-06-windows-users-logs.md)

## Notes (10 min)
## Notes: Windows Users, Permissions and Logs

### Accounts, users and groups
Windows accounts are either **local** (stored on this PC) or **domain/Microsoft** accounts. Each account has a unique **SID** (security identifier), and Windows checks SIDs rather than names when deciding access.

**Built-in accounts and groups:**

| Name | Type | Notes |
|---|---|---|
| **Administrator** | Account | Built-in admin (SID ends in **-500**). Usually **disabled** on a home PC |
| **Guest** | Account | Built-in, disabled by default (SID ends in -501) |
| **Administrators** | Group | Full control of the machine. Whoever is a member can change anything |
| **Users** | Group | Standard users with limited rights |
| Others | Group | `Guests`, `Remote Desktop Users`, `Backup Operators` |

Your everyday account is probably a **member of the Administrators group**, which is not the same as being the built-in "Administrator" account.

**Linux comparison:** `Administrators` ≈ `sudo`/root, `Users` ≈ normal users, SID ≈ UID.

### Identity and privileges

| Command | One-line explanation |
|---|---|
| `whoami` | Current user (`PC\user`) |
| `whoami /all` | User, SID, groups and privileges together |
| `whoami /groups` | Groups the current token belongs to, plus the **integrity level** |
| `whoami /priv` | Privileges held and whether each is **Enabled** or **Disabled** |

**Integrity level** (in `whoami /groups`):

| Label | Meaning |
|---|---|
| `Medium Mandatory Level` | Normal, non-elevated |
| `High Mandatory Level` | **Elevated** (Run as administrator) |
| `System Mandatory Level` | System services |

Privileges are specific rights separate from permissions on files. Examples: `SeShutdownPrivilege` (shut down), `SeBackupPrivilege` (read any file for backup), `SeDebugPrivilege` (inspect any process). Powerful privileges are a target for attackers, and "Disabled" means held but not currently active.

### UAC (User Account Control)
When an administrator logs in, Windows gives them **two tokens**: a standard one for daily use and a full admin one. Programs run with the **standard token** until you approve an **elevation prompt** (the "Do you want to allow this app to make changes?" dialog).

- Compare `whoami /groups` in a normal window (Medium) and an Administrator window (High).
- Why it matters: malware that runs as you can't silently use admin rights. Attackers look for **UAC bypasses** and users who click "Yes" without reading.
- Linux comparison: `sudo` is similar (asks before using root).

### NTFS permissions and ACLs
Files and folders on NTFS have an **ACL** (access control list), a list of **ACEs** (entries) that say which user or group gets which rights. Unlike Linux's three owner/group/others sets, an ACL can name **any number** of users and groups.

**View with `icacls`:**
```
icacls C:\week3-lab\private
```
Example output:
```
C:\week3-lab\private  BUILTIN\Administrators:(I)(OI)(CI)(F)
                      NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
                      PC\me:(I)(OI)(CI)(M)
                      BUILTIN\Users:(I)(OI)(CI)(RX)
```

**Rights:**

| Code | Meaning | Allows |
|---|---|---|
| `F` | Full control | Everything, including changing permissions |
| `M` | Modify | Read, write, delete (not change permissions) |
| `RX` | Read & Execute | View and run |
| `R` | Read | View only |
| `W` | Write | Create/modify |

**Inheritance flags:** `(I)` inherited from the parent, `(OI)` applies to files inside, `(CI)` applies to subfolders.

**Changing permissions (practice folders only):**
```
icacls C:\week3-lab\private /grant "BUILTIN\Users:(R)"
icacls C:\week3-lab\private /remove "BUILTIN\Users"
icacls C:\week3-lab\private /inheritance:r      # cut inheritance (careful)
```
**Important rules:**
- An explicit **deny** overrides an allow.
- Don't change ACLs on `C:\Windows`, `System32` or `Program Files`, as that can break Windows.
- Right-click → Properties → **Security** shows the same ACL in the GUI.

| Concept | Linux | Windows |
|---|---|---|
| Model | owner/group/others with `rwx` | ACL with many entries |
| View | `ls -l` | `icacls` |
| Change | `chmod`, `chown` | `icacls /grant`, `/remove` |

### Users and groups from the command line

| CMD | PowerShell | One-line explanation |
|---|---|---|
| `net user` | `Get-LocalUser` | Lists local accounts |
| `net user <name>` | `Get-LocalUser <name> \| Format-List *` | Details for one account |
| `net localgroup` | `Get-LocalGroup` | Lists local groups |
| `net localgroup Administrators` | `Get-LocalGroupMember Administrators` | Lists members of the admin group |
| `net user <name> <pass> /add` | `New-LocalUser` | Creates an account (admin needed) |
| `net localgroup Administrators <name> /add` | `Add-LocalGroupMember` | Adds a user to a group |
| `net user <name> /delete` | `Remove-LocalUser` | Deletes an account |

Security check you'll repeat as a defender: **who is in Administrators?** An unexpected member is a red flag. Only create test accounts on your own machine and delete them straight away.

### Logs: Event Viewer
Open it with `eventvwr`. Under **Windows Logs**:

| Log | Contains |
|---|---|
| **Application** | Events from programs |
| **System** | Windows components, drivers, services (e.g. a service installed or crashed) |
| **Security** | Logons, privilege use and audit events (**needs admin to read**) |

Each event has a **Level** (Information, Warning, Error), a time, a **Source** and an **Event ID**.

**Key Security event IDs:**

| ID | Meaning | Why it matters |
|---|---|---|
| **4624** | Successful logon | Who logged in, when and how (see logon type) |
| **4625** | Failed logon | Many in a row can mean password guessing |
| **4672** | Special privileges assigned to a new logon | An administrator-level logon happened |
| **4688** | A new process was created | Records what ran, but **only if process-creation auditing is enabled** |
| 4720 | User account created | Possible persistence |
| 4732 | Member added to a local group | Possible privilege escalation |
| 1102 | Audit log cleared | Attackers hide traces. Investigate immediately |

**Logon types (inside 4624):** `2` interactive (at the keyboard), `3` network, `10` remote desktop (RDP).

**Filter in Event Viewer:** Security → **Filter Current Log** → enter an Event ID (e.g. `4625`).

**PowerShell (run as administrator):**
```
Get-WinEvent -LogName Security -MaxEvents 10
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5
```
Generate a 4624 yourself by locking the screen (`Win+L`) and signing back in. Linux comparison: `journalctl` and `/var/log/auth.log`.

Privacy: event details include usernames, machine names and IPs, so redact them before sharing and keep raw exports in `raw-private/`.

### Defenses

**Windows Defender (antivirus):**
```
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled
```
Or open the **Windows Security** app. Check that real-time protection is on, and that signatures are up to date.

**Windows Firewall:**
```
netsh advfirewall show allprofiles
Get-NetFirewallProfile | Select-Object Name, Enabled
```

| Profile | Used when |
|---|---|
| Domain | Joined to a company domain |
| Private | A trusted network (home) |
| Public | Untrusted network (cafe, airport), the strictest |

The firewall allows or blocks traffic by **port and program**, which links back to Week 2 (ports and `netstat -ano`). **Don't disable them** to "make something work". Only read the status in this lab.

### Linux vs Windows summary

| Task | Linux | Windows |
|---|---|---|
| Who am I / groups | `id` | `whoami /groups` |
| List users | `cat /etc/passwd` | `net user` / `Get-LocalUser` |
| Admin group | `sudo` group / root | `Administrators` |
| Elevation | `sudo` | UAC prompt |
| File permissions | `chmod`, `ls -l` | `icacls` |
| Logs | `journalctl`, `/var/log` | Event Viewer, `Get-WinEvent` |

### Quick self-check
1. What is the difference between the **Administrators group** and the built-in **Administrator account**?
2. How can you tell if your command window is elevated?
3. What do `(F)`, `(M)` and `(RX)` mean in `icacls`?
4. Which event ID means a failed logon? A successful one? Log cleared?
5. Why is the Security log useful for spotting attacks?

*Answers: a group any number of users can belong to vs one specific built-in account (often disabled); `whoami /groups` shows High Mandatory Level when elevated; full control, modify, read and execute; 4625, 4624, 1102; it records logons, privilege use and account changes that attackers leave traces in.*
## Key takeaways
-

## Still confusing / to revisit
-

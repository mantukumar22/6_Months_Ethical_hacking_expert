# Day 5: Windows administration basics
**Date:** 27 Oct 2026 · **OS:** Windows · **Time:** 60 min

## Learn (20 min)
- CMD vs **PowerShell** (object-based, `Verb-Noun` cmdlets). Run as Administrator when needed.
- Filesystem: drive letters, `C:\Windows`, `C:\Windows\System32`, `C:\Users`, `C:\Program Files`.
- System info: `systeminfo`, `hostname`, `ver`, `whoami`.
- Processes: `tasklist`, `taskkill /PID <PID> /F`; PowerShell `Get-Process`, `Stop-Process`.
- Services: `sc query`, `net start`; PowerShell `Get-Service`.
- Navigation and files: `dir`, `cd`, `mkdir`, `copy`, `move`, `del`, `type`, `findstr` (Windows `grep`).
- The **registry** (concept only): hives like `HKLM`, `HKCU`. View with `reg query`. Don't edit it yet.

## Practice (30 min)
Lab: [lab-05-windows-basics](../labs/lab-05-windows-basics.md)

## Notes (10 min)

### CMD vs PowerShell

| | CMD (Command Prompt) | PowerShell |
|---|---|---|
| Style | Older, text-based | Modern, **object-based** (commands pass structured objects, not just text) |
| Command names | Short (`dir`, `copy`, `tasklist`) | `Verb-Noun` **cmdlets** (`Get-Process`, `Stop-Service`) |
| Power | Basic tasks and legacy tools | Full scripting, system administration, automation |
| Pipes | Pass text | Pass objects, so you can filter by property |

PowerShell also accepts most CMD commands and short aliases (`dir`, `cd`, `ls`, `cat` all work), so you can mix them.

**Run as Administrator** when a command changes the system or reads protected data: search "cmd" or "PowerShell", right-click, **Run as administrator**. Check with `whoami /groups` or whether the title bar says "Administrator". Use normal rights for everything else.

**Discover commands in PowerShell:**
```
Get-Command *process*        # find cmdlets by name
Get-Help Get-Process         # help for one cmdlet
Get-Process | Get-Member     # see the properties of the objects returned
```
Example of object filtering:
```
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
Get-Service | Where-Object Status -eq Running
```

### Filesystem layout

| Path | Purpose |
|---|---|
| `C:\` | Root of the system drive. Windows uses **drive letters** (C:, D:), each with its own tree (Linux has one tree from `/`) |
| `C:\Windows` | The operating system itself |
| `C:\Windows\System32` | Core system programs and libraries (`cmd.exe`, `notepad.exe`, DLLs) |
| `C:\Users` | User profiles. Each user has `C:\Users\<name>` (Desktop, Documents, Downloads, `AppData`) |
| `C:\Program Files` | 64-bit installed applications |
| `C:\Program Files (x86)` | 32-bit applications on 64-bit Windows |
| `C:\ProgramData` | Application data shared by all users (hidden by default) |
| `%TEMP%` | Temporary files for the current user (`echo %TEMP%`) |

Windows paths use **backslashes** (`C:\Users\me\notes.txt`) and are **case-insensitive**. Environment variables: `%USERPROFILE%` (your home), `%SystemRoot%` (`C:\Windows`), `%PATH%`. In PowerShell they are `$env:USERPROFILE`.

**Why it matters for security:** `System32` is a prime place for attackers to hide or imitate files, `AppData` and `%TEMP%` are common malware drop locations, and standard users usually can't write to `C:\Windows` or `Program Files`.

### System information

| Command | One-line explanation |
|---|---|
| `systeminfo` | OS name and version, build, hardware, hotfixes, boot time (long output, so filter it) |
| `hostname` | Prints the computer's name |
| `ver` | Shows the Windows version number |
| `whoami` | Shows the current user (`DOMAIN\user` or `PC\user`) |

Filtering example:
```
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```
`systeminfo` also reveals sensitive details (hostname, install date, hotfix list). Redact before sharing, and keep the raw output in `raw-private/`.

### Processes

| CMD | PowerShell | One-line explanation |
|---|---|---|
| `tasklist` | `Get-Process` | Lists running processes with PID and memory |
| `tasklist \| findstr notepad` | `Get-Process notepad` | Finds a process by name |
| `taskkill /PID 1234 /F` | `Stop-Process -Id 1234 -Force` | Ends a process by PID (`/F` = force) |
| `taskkill /IM notepad.exe /F` | `Stop-Process -Name notepad` | Ends a process by name |
| `tasklist /svc` | | Shows which **services** run inside each process (useful for `svchost.exe`) |

Like Linux's `kill -9`, forced termination gives the program no chance to save work. Don't kill processes you don't recognize, and never kill `csrss.exe`, `wininit.exe` or `lsass.exe` (this crashes Windows). Link to Week 2: match a port's PID from `netstat -ano` to a name with `tasklist | findstr <PID>`.

### Services

| CMD | PowerShell | One-line explanation |
|---|---|---|
| `sc query` | `Get-Service` | Lists services and their state |
| `sc query wuauserv` | `Get-Service wuauserv` | Checks one service (Windows Update) |
| `net start` | | Lists running services |
| `net start <name>` / `net stop <name>` | `Start-Service` / `Stop-Service` | Starts or stops a service (needs admin) |
| | `Get-Service \| Where-Object Status -eq Running` | Only running services |

A service's **StartType** is Automatic, Manual or Disabled. This is the same idea as `enable` vs `start` on Linux. The management console is `services.msc`.

### Navigation and files

| CMD | PowerShell alias / cmdlet | One-line explanation | Linux equivalent |
|---|---|---|---|
| `dir` | `Get-ChildItem` (`ls`) | Lists files (`dir /a` includes hidden) | `ls -la` |
| `cd <path>` | `Set-Location` | Changes directory (`cd ..` goes up, `cd /d D:\` switches drive) | `cd` |
| `mkdir <name>` | `New-Item -ItemType Directory` | Creates a directory | `mkdir` |
| `copy a b` | `Copy-Item` | Copies a file | `cp` |
| `move a b` | `Move-Item` | Moves or renames | `mv` |
| `del file` | `Remove-Item` | Deletes a file (`rmdir /s` for folders) | `rm` |
| `type file` | `Get-Content` | Prints a file | `cat` |
| `findstr "text" file` | `Select-String "text" file` | Searches **inside** files for text | `grep` |

`findstr` options: `/i` ignore case, `/s` search subfolders, `/n` show line numbers. Example: `findstr /s /i "error" *.log`.

Redirection and pipes work like Linux: `dir > list.txt`, `dir >> list.txt`, `dir | findstr txt`.

**Caution:** `del` and `Remove-Item` have no recycle bin. Practice only in `C:\week3-lab`, and check the path before pressing Enter.

### The registry (concept only)
The **registry** is Windows' central database of configuration for the OS, drivers, applications and users.

| Hive | Short | Contains |
|---|---|---|
| `HKEY_LOCAL_MACHINE` | `HKLM` | Settings for the whole machine |
| `HKEY_CURRENT_USER` | `HKCU` | Settings for the logged-in user |
| `HKEY_CLASSES_ROOT` | `HKCR` | File associations and COM data |
| `HKEY_USERS` | `HKU` | Settings for all loaded user profiles |

Structure: **keys** (like folders) hold **values** (name, type, data).

**View (read only):**
```
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName
```
GUI: `regedit` (look, don't edit).

**Do not edit the registry yet.** A wrong change can break Windows or stop it booting. Know that attackers use it for **persistence** (for example the `Run` keys under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`), and defenders check those places.

### Windows vs Linux quick map

| Task | Linux | Windows |
|---|---|---|
| Current user | `whoami` | `whoami` |
| List processes | `ps aux` | `tasklist` / `Get-Process` |
| Kill process | `kill PID` | `taskkill /PID n` / `Stop-Process` |
| Services | `systemctl status x` | `sc query x` / `Get-Service` |
| Search in files | `grep` | `findstr` / `Select-String` |
| Read a file | `cat` | `type` / `Get-Content` |
| System info | `uname -a` | `systeminfo` |

### Quick self-check
1. What is the main difference between CMD and PowerShell?
2. Where is the operating system stored, and where do user files live?
3. How do you list processes, and how do you stop one?
4. What is the Windows equivalent of `grep`?
5. Name the registry hives `HKLM` and `HKCU`, and explain why you shouldn't edit the registry casually.

*Answers: PowerShell is object-based with Verb-Noun cmdlets; `C:\Windows` and `C:\Users`; `tasklist`/`Get-Process` and `taskkill`/`Stop-Process`; `findstr` or `Select-String`; HLKM = machine-wide, HKCU = current user, and mistakes can break the system.*
Write the Linux equivalent of each command you used (see [cheat sheet](../resources/linux-vs-windows.md)).

## Key takeaways
-

## Still confusing / to revisit
-

# Day 06 Notes (own words)
- Absolute vs relative path:
  Absolute Path gives the full location fro the top of the filesystem, so it works the same no matter where you are. A relative path gives the location stating from your current working directory, so its meaning changes depending on where you are.
  	          Windows	                            Linux
  Absolute	C:\Users\Sam\Documents\report.docx	/home/sam/Documents/report.txt
  Relative	Documents\report.docx	              Documents/report.txt

  Useful shortcuts for relative paths: . is the current directory, .. is the parent directory, and ~ (Linux) is your home directory.

  Security angle: relative paths cause problems when software trusts them. If a program runs tool.exe without a full path, it may launch whichever copy it finds first, which attackers abuse in DLL hijacking and search-order hijacking. Relative paths with ../ are also used in path traversal attacks to escape a folder.
  
- Windows vs Linux path differences:
  
## Windows vs Linux File System

| Feature                | Windows                                                    | Linux                                                                                                        |
| ---------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Path Separator**     | Backslash `\`                                              | Forward slash `/`                                                                                            |
| **Root**               | Drive letters (`C:\`, `D:\`), separate drive roots         | Single root `/`, with drives mounted inside it (e.g., `/mnt`, `/media`)                                      |
| **Case Sensitivity**   | Generally not case-sensitive (`File.txt` = `file.txt`)     | Case-sensitive (`File.txt` ≠ `file.txt`)                                                                     |
| **User Folders**       | `C:\Users\<name>`                                          | `/home/<name>`                                                                                               |
| **System Files**       | `C:\Windows`, `C:\Program Files`                           | `/etc`, `/bin`, `/usr`, `/var`                                                                               |
| **Hidden Files**       | Hidden file attribute                                      | Names usually start with a dot (e.g., `.bashrc`)                                                             |
| **Executables**        | Commonly identified by extensions (`.exe`, `.bat`, `.ps1`) | Determined primarily by execute permissions, not file extensions                                             |
| **Special Characters** | Cannot use `< > : " / \ \| ? *` in file names              | `/` and the null character are forbidden in file names; other characters may have special meanings in shells |


- Where would malware hide on a filesystem, and why?
  
  Windows

    C:\Users\<name>\AppData\Roaming and \Local: writable without admin rights, and full of unfamiliar folders, so one more doesn't stand out.
  
    %TEMP% (AppData\Local\Temp): disposable by nature, so files here seem normal.
  
    C:\ProgramData: shared and writable, and often skipped by users.
  
    Startup folder (...\Start Menu\Programs\Startup) and Run registry keys: the file runs at every login, giving persistence.
  
    C:\Windows\Temp and C:\Users\Public: writable by many accounts.

    Lookalike paths such as C:\Windows\System32 copies with altered names (svch0st.exe) to blend in with real system files.

    Alternate data streams on NTFS: data attached to a normal file that Explorer doesn't show.

  Linux

    /tmp and /var/tmp: world-writable, and code can run from there if not mounted noexec.
  
    /dev/shm: lives in memory, so nothing touches the disk.
  
    Hidden dot-files and dot-folders in home directories (~/.cache/.x), which a plain ls skips.
  
    ~/.ssh/authorized_keys, cron jobs (/etc/cron.*, crontab), systemd units, and ~/.bashrc: all give persistence.
  
    /usr/local/bin or early entries in $PATH, so a fake ls or sudo runs instead of the real one.

  Why these places: they need low privileges to write to, they give automatic execution on boot or login, and they blend in with normal clutter. Defender tip: treat executables running from Temp, AppData, /tmp, or /dev/shm as suspicious, and compare against your baseline.
  
- What does `ls -la` show that `ls` doesn't?

  Plain ls lists only the names of non-hidden items. ls -la combines two options:
    -a (all) includes hidden files, those starting with ., plus the . and .. entries.
    -l (long format) shows details for each entry.

  Example line:

  -rwxr-xr-- 1 sam staff 4096 Oct 09 10:15 script.sh

  Part	                Meaning
  - (first character)	  Type: - file, d directory, l symlink
  rwxr-xr--	            Permissions for owner / group / others (read, write, execute)
  1	                    Number of hard links
  sam	                  Owner
  staff	                Group
  4096	                Size in bytes
  Oct 09 10:15	        Last modified time
  script.sh	            Name

  Security angle: -a exposes hidden persistence files, while -l reveals suspicious ownership (a file in a user's home owned by root), unexpected execute bits on something that shouldn't run, and recent modification times that line up with an incident. SUID files (an s in the permissions, such as rwsr-xr-x) are especially worth checking, since they run with the owner's privileges.

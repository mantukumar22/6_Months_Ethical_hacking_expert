# Day 05 Notes (own words)
- Program vs process:
  A program is a passive file stored on disk: the instructions, such as notepad.exe sitting in C:\Windows\System32. A process is a running instance of that program in memory, with its own process ID (PID), allocated memory, threads, handles, and security token.

  One program can have many processes. If you open Chrome three times, you get three processes from one program file. A program does nothing until it is launched; once launched, the process is what uses CPU, RAM, and network, and it is what an attacker's code becomes when it runs.
  
- What is a parent process, and why does it matter in investigations?
  A parent process is the process that launched another one (the child). Every process except the first has a parent, recorded as the PPID (parent process ID). For example, when you double-click a program, explorer.exe is usually the parent.

  It matters because legitimate software has predictable parent-child relationships, and attackers break them. The process itself may look normal, but the lineage reveals how it got there.

  Parent → Child	= Meaning
  explorer.exe → chrome.exe	= Normal: user opened a browser
  services.exe → svchost.exe = Normal: Windows service host
  winword.exe → powershell.exe	= Suspicious: a Word document (likely a malicious macro) spawned a shell
  outlook.exe → cmd.exe	= Suspicious: email attachment or exploit
  w3wp.exe (IIS web server) → cmd.exe	= Highly suspicious: possible web shell
  svchost.exe with parent explorer.exe	= Suspicious: real svchost is started by services.exe, so this is likely a disguised malware
- List 4 signs that powershell.exe is suspicious:
  
  1. Suspicious parent process. Launched by Office apps (winword.exe, excel.exe), a browser, outlook.exe, a web server, or wmiprvse.exe, rather than by a user or admin tool. Running from a path other than C:\Windows\System32\WindowsPowerShell\v1.0\ is also a red flag.
  2. Encoded or obfuscated command line. Flags like -enc / -EncodedCommand with long Base64 strings, plus -w hidden (hidden window), -NoProfile, -ExecutionPolicy Bypass, or heavy string concatenation and character-code tricks to hide the real command.
  3. Download-and-execute behavior. Commands using Invoke-WebRequest, DownloadString, Net.WebClient, or IEX (Invoke-Expression) to pull code from the internet and run it directly in memory, often with no file written to disk (fileless malware).
  4. Unusual network or system activity. Outbound connections to unfamiliar IPs or domains, sustained high CPU (such as cryptomining), disabling of Defender (Set-MpPreference -DisableRealtimeMonitoring), creation of scheduled tasks or registry Run keys for persistence, or running on a machine and at a time where PowerShell isn't normally used.

Key point: PowerShell itself is a legitimate, essential admin tool. Defenders judge it by context: who launched it, what it was told to do, where it connected, and whether that fits the baseline. Enabling Script Block Logging (Event ID 4104) and command-line logging makes these signs visible.

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
Write the Linux equivalent of each command you used (see [cheat sheet](../resources/linux-vs-windows.md)).

## Key takeaways
-

## Still confusing / to revisit
-

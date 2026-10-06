# Day 05 — Processes & Programs

## Learn
**Program ≠ Process.** `chrome.exe` on disk is a *program*. When launched, it becomes a *process* in memory.
- **PID**: unique process ID.
- **Parent / child process**: who started whom (explorer.exe → chrome.exe).
- **Services**: background programs, often starting at boot.
- **Background processes**, **executables** (.exe).

## Practical
1. Task Manager → Details. Find `explorer.exe`, `svchost.exe`, `RuntimeBroker.exe`. Record PID, CPU, Memory.
2. `tasklist` — find them again; try `tasklist | findstr explorer`.

## Cybersecurity perspective
`powershell.exe` running is **not** automatically malicious. It becomes suspicious through context:
- **Unusual parent** (e.g., Word spawning PowerShell)
- **Odd command line** (encoded/long commands)
- **Network connection** to unknown hosts
- **Execution context** (unexpected user, odd location like Temp)

Many attackers hide as look-alikes (`svch0st.exe`, `svchost.exe` in the wrong folder). This is the foundation of SOC triage, malware analysis and incident response.

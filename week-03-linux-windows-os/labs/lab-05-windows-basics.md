# Lab 05: Windows administration basics

Use **CMD or PowerShell**. Open as Administrator when a command asks for it. Work in a sandbox folder: `mkdir C:\week3-lab`.

**Tasks**
1. `hostname`, `whoami`, `ver`.
2. `systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"` → record (don't publish serial/product data).
3. Processes:
   - `tasklist | more`
   - PowerShell: `Get-Process | Sort-Object CPU -Descending | Select-Object -First 5`
   - Start `notepad`, find it with `tasklist | findstr notepad`, then close it with `taskkill /IM notepad.exe /F`.
4. Services:
   - `sc query | more` or PowerShell `Get-Service | Where-Object Status -eq Running | Select-Object -First 10`
   - `sc query wuauserv` → what state is Windows Update in?
5. Files:
```
cd C:\week3-lab
mkdir docs
echo hello windows > docs\a.txt
type docs\a.txt
copy docs\a.txt docs\b.txt
findstr /s /i "hello" *.txt
dir /a
```
6. Ports to processes (Week 2 link): `netstat -ano | findstr LISTENING` then `tasklist | findstr <PID>`.
7. Registry (read only): `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName`.

**Results**

| Item | Answer |
|---|---|
| OS name / version | |
| Top CPU process | |
| Windows Update service state | |
| Linux equivalent of `findstr` | |
| Linux equivalent of `tasklist` | |

# Windows cheat sheet (CMD / PowerShell)

## System
`hostname` · `whoami` · `ver` · `systeminfo` · `set` (environment)

## Files
`dir /a` · `cd` · `mkdir` · `copy` · `move` · `del` · `type f` · `findstr /s /i "text" *.txt`
PowerShell: `Get-ChildItem` · `Get-Content f` · `Select-String "text" f`

## Processes / services
`tasklist` · `taskkill /PID n /F` · `sc query` · `net start`
PowerShell: `Get-Process` · `Stop-Process -Id n` · `Get-Service`

## Users / permissions
`whoami /all` · `whoami /groups` · `whoami /priv`
`net user` · `net user name /add` · `net user name /delete` · `net localgroup Administrators`
`icacls path`
PowerShell: `Get-LocalUser` · `Get-LocalGroupMember Administrators`

## Logs / security
`eventvwr` · `Get-WinEvent -LogName Security -MaxEvents 10`
Key event IDs: 4624 logon OK · 4625 logon failed · 4672 special privileges · 4688 process created
`netsh advfirewall show allprofiles` · `Get-MpComputerStatus`

## Network (Week 2)
`ipconfig /all` · `netstat -ano` · `arp -a` · `nslookup` · `ping` · `tracert`

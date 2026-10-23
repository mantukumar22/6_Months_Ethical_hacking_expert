# Lab 06: Windows users, permissions and logs

**Part A: identity and privileges**
```
whoami
whoami /groups
whoami /priv
```
Are you in the **Administrators** group? Is your token elevated (look for "Mandatory Label\High")? Compare in a normal and an Administrator window.

**Part B: users and groups**
```
net user
net localgroup
net localgroup Administrators
```
PowerShell: `Get-LocalUser` and `Get-LocalGroupMember Administrators`.

Sandbox user (own machine only), then clean up:
```
net user labtest P@ssw0rd-Lab1 /add
net localgroup Users
net user labtest /delete
```
(Use a throwaway password and delete the account straight away.)

**Part C: NTFS permissions (ACLs)**
```
mkdir C:\week3-lab\private
icacls C:\week3-lab\private
```
Read the output: which accounts have (F) Full, (M) Modify, (RX) Read & Execute? Then try `icacls C:\Windows\System32\config` (administrator) and compare. **Do not change ACLs on system folders.**

**Part D: logs**
1. Open Event Viewer (`eventvwr`) → Windows Logs → **Security**.
2. Filter for event ID **4624** (successful logon) and **4625** (failed logon). Lock the screen and log back in to generate a 4624.
3. PowerShell (administrator): `Get-WinEvent -LogName Security -MaxEvents 10`
4. Look at **System** and **Application** logs. Find one warning or error and explain it.

**Part E: defenses**
```
netsh advfirewall show allprofiles
```
PowerShell: `Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled`

**Results**

| Item | Answer |
|---|---|
| Am I an administrator? | |
| Members of Administrators | |
| Permissions on my sandbox folder | |
| Event 4624 found? time | |
| Firewall state (Domain/Private/Public) | |
| Defender real-time protection | |

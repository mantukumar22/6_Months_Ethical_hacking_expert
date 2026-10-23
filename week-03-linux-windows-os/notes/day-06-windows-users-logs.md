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
Compare Linux and Windows: user/group commands, permission model (rwx vs ACLs), and log locations.

## Key takeaways
-

## Still confusing / to revisit
-

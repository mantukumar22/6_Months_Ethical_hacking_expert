# Day 04 Notes (own words)
| Command | What it tells me | Why an attacker/defender cares |
|---------|------------------|--------------------------------|
| whoami | The current user account (DOMAIN\user). Add /priv for the privileges held, /groups for group memberships. | Attacker: shows what access they landed with: a standard user, an admin, or SYSTEM, which decides whether they need privilege escalation. Defender: confirms which account is running a suspicious process or session, and whether a compromised account has excessive rights. |
| hostname |The computer's name. | Attacker: identifies the machine and, from naming conventions like SRV-DB01 or LAPTOP-HR, its likely role. Defender: ties logs, alerts, and incident notes to the right asset. |
| systeminfo |OS name and version, build, install date, last boot time, domain, installed hotfixes/patches, hardware summary, and network adapters. |Attacker: a missing-patch list reveals which known vulnerabilities might work, and the domain membership shows whether lateral movement is possible. Defender: a quick patch-level and configuration audit, and a way to confirm whether the system is up to date. |
| ipconfig |IP address, subnet mask, default gateway, and DNS servers. ipconfig /all adds MAC address, DHCP details, and domain name. |Attacker: maps the network the machine sits in, showing which subnet to explore next and which DNS/domain controllers exist. Defender: verifies the host's network identity, spots unexpected adapters (rogue VPN or tunnel), and correlates activity to an IP in logs. |
| tasklist |All running processes with name, PID, session, and memory use. /svc adds the services inside each process, and /v adds the user and window title. |Attacker: finds security tools (antivirus, EDR) to evade, and processes to inject into or blend with. Defender: spots unknown or disguised processes (like a cryptominer or a fake svch0st.exe) and compares against a known-good baseline. |

- Why least privilege matters:
  
  Together these answer the attacker's basic questions: Who am I? Where am I? What is this system? What network am I on? What is running here? None of them are exploits, and they're normal admin tools. That makes them hard to block, so defenders detect them by context and pattern instead. A user running all five within seconds from a command prompt, especially launched by Word, a browser, or a script, is a classic suspicious sequence.

  Defender tips
  Enable command-line logging (Sysmon Event ID 1, or Windows Event 4688 with command line auditing) so you can see these commands run.
  Alert on bursts of discovery commands, not single uses.
  Watch the parent process: cmd.exe spawned by winword.exe or powershell.exe is far more suspicious than one opened by a person at the desktop.
  Compare to your baseline: admins run these commands often, so build exceptions for known admin accounts and hosts.

# Day 5: Security Controls
**Date:** 18 · **Time:** 60 min
**Video:** Types of Security Controls: <paste URL>

## Learn (20 min)
A **security control** is a safeguard that reduces risk. Controls are grouped by **when they act**:

| Type | Purpose | Timing | Examples |
|---|---|---|---|
| **Preventive** | Stop the incident from happening | Before | Firewall, MFA, access control, patching, encryption, input validation |
| **Detective** | Discover that something happened or is happening | During or after | Logs, IDS/IPS alerts, SIEM, antivirus alerts, CCTV, file integrity monitoring |
| **Corrective** | Fix and recover after an incident | After | Backups and restore, incident response, patch deployment, reimaging a system |

Other types you'll see:
- **Deterrent:** discourage attackers (warning banners, visible cameras).
- **Compensating:** an alternative when the main control isn't possible.
- **Directive:** policies and rules.

### By implementation
| Category | Examples |
|---|---|
| **Technical** | Firewalls, encryption, MFA, antivirus |
| **Administrative** | Policies, training, background checks |
| **Physical** | Locks, badges, cameras, server-room access |

### The four required examples

| Control | What it does | Type | CIA principle |
|---|---|---|---|
| **Firewall** | Allows or blocks traffic by rules (port, program, address). Link: Windows Firewall, Day 6 of Week 3 | Preventive | Confidentiality, Integrity |
| **Antivirus / EDR** | Detects and blocks known and suspicious malware | Preventive and detective | All three |
| **MFA** | Requires two or more proofs of identity (something you know, have, are) | Preventive | Confidentiality |
| **Backups** | Keep copies of data so it can be restored | Corrective | Availability, Integrity |

Notes:
- A single control can be **more than one type**. Antivirus blocks (preventive) and alerts (detective).
- Backups must be **tested**, kept **offline or immutable**, and follow the **3-2-1 rule** (3 copies, 2 media types, 1 off-site).
- **Defense in depth:** use **layers** of controls so one failure doesn't mean total failure.
- **Least privilege:** give only the access that's needed.

### Mapping controls to attacks (Day 4)
| Attack | Controls that help |
|---|---|
| Phishing | Email filtering, training (preventive), report button and alerts (detective) |
| Brute force | MFA, lockout (preventive), failed-login alerts (detective) |
| SQL injection | Parameterized queries (preventive), WAF logs (detective) |
| XSS | Output encoding, CSP (preventive) |
| DoS | Rate limiting, CDN (preventive), traffic monitoring (detective) |
| Ransomware | Backups (corrective), EDR (preventive and detective) |

## Practice (30 min)
### 1. Classify (preventive / detective / corrective)
| Control | Type |
|---|---|
| Security camera recording a door | Detective |
| Password policy requiring 14 characters | Preventive |
| SIEM alert for 50 failed logins | Detective |
| Restoring files from last night's backup | Corrective |
| Patching a vulnerable server | Corrective |
| Incident response plan | Corrective |
| Antivirus quarantining a file | Detective|
| Disabling a compromised account | Corrective |

### 2. Layers for a small business
Name one control for each layer:
| Layer | Control |
|---|---|
| Perimeter (network) | firewall |
| Endpoint (devices) | Antivires |
| Application | MFA & Traffic Logs |
| Data | Backups |
| People | phising awearness |
| Physical | Cameras & server room security |

### 3. Check your own machine (read only)
- Windows: Firewall and Defender status (see Week 3, Lab 06).
- Kali: is a firewall (`ufw`) active? Do you have backups of your lab notes? yes
- Is MFA on for my email, GitHub and main accounts? yes

## Notes (10 min)
- Difference between preventive and detective controls:
  Preventive works like protect apps before attack & Detective is like detect attacks when thats happens.
- Why corrective controls matter even with strong prevention: Because no prevention is perfect, corrective controls limit the damag
  Because 

## Self-check
1. Why is a firewall preventive but a SIEM alert detective? Because Firewall stop the attack & SIEM alert detect the attack.
2. What does MFA protect against? What does it not protect against? MFA protects against account takeover from stolen or guessed passwords, since an attacker still needs a second factor to get in. & MFA doesn’t protect against attacks that bypass or hijack the login itself: session/cookie theft and adversary-in-the-middle phishing.
3. What is defense in depth? Defense in depth is a security strategy that layers multiple, independent controls (people, process, and technology) so that if one fails or is bypassed, others still stand in the way of an attacker.

## Mistake I fixed / still confusing
-

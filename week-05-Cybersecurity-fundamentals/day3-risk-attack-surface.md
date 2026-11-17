# Day 3: Risk and Attack Surface
**Date:** 17 Nov · **Time:** 60 min
**Video:** Risk and Attack Surface: <paste URL>

## Learn (20 min)

### Cybersecurity risk
**Risk** is the potential for loss or damage when a threat exploits a vulnerability in an asset.

**Basic model:**
```
Risk = Likelihood x Impact
```
- **Likelihood:** how probable is it that this happens?
- **Impact:** how bad is it if it does (money, data, safety, reputation, legal)?

Simple 1 to 5 scoring:

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost certain | Severe |

| Risk score | Level | Typical response |
|---|---|---|
| 1-4 | Low | Accept or monitor |
| 5-9 | Medium | Plan to reduce |
| 10-16 | High | Prioritize and fix soon |
| 17-25 | Critical | Fix immediately |

### Handling risk (4 options)
| Option | Meaning | Example |
|---|---|---|
| **Mitigate** | Reduce likelihood or impact | Patch, add MFA |
| **Accept** | Live with it knowingly | Low-value test server |
| **Transfer** | Shift the cost | Cyber insurance, outsourcing |
| **Avoid** | Stop the risky activity | Decommission a legacy service |

**Residual risk** is what remains after controls are applied.

### Attack surface
The **attack surface** is the **total set of points** where an attacker could try to enter, interact with or extract data from a system. A smaller surface means fewer chances for attackers.

| Type | Examples |
|---|---|
| **Digital / network** | Open ports, exposed services, APIs, web apps, cloud storage, remote access (RDP, SSH) |
| **Software** | Unpatched apps, third-party libraries, default configs |
| **Physical** | USB ports, unattended workstations, server rooms |
| **Human / social** | Staff who can be phished, helpdesk impersonation |

Link to earlier weeks: every **listening port** (`netstat -ano`, `ss -tulpn`) and every running service is part of the attack surface.

**Reducing it:** close unused ports, remove unneeded services and accounts, patch, apply least privilege, segment networks, remove unused code and endpoints.

### Attack vector
An **attack vector** is the **path or method** an attacker uses to reach the surface and gain access.

| Vector | Example |
|---|---|
| Email | Phishing link or attachment |
| Web | Injection or XSS in a web form |
| Network | Exposed RDP or SSH with weak credentials |
| Removable media | Infected USB drive |
| Supply chain | A compromised software update or library |
| Insider | A person with legitimate access |
| Wireless | Rogue access point, weak Wi-Fi |

**Surface vs vector:** the surface is *where* you can be attacked, and the vector is *how* the attack arrives.

## Practice (30 min)
### 1. Score the risks
| Risk | Likelihood (1-5) | Impact (1-5) | Score | Level |
|---|---|---|---|---|
| Staff clicking a phishing link | 4 | 5 | 20 | Critical |
| Server room flood | 2 | 5 | 25 | Critical |
| Unpatched internet-facing web server | 4 | 5 | 9 | Medium |
| Lost unencrypted laptop with customer data | 3 | 5 | 20 | Critical |

### 2. Map the attack surface of a small web app
(Login page, public API, admin panel, database, file upload, third-party scripts, a staff Wi-Fi network.)

| Component | Possible attack vector | One way to reduce it |
|---|---|---|
| | | |
|---|---|---|
| | | |
|---|---|---|
| | | |
|---|---|---|
| | | |

### 3. Your own PC (Week 2 and 3 link)
List what your Kali or Windows machine exposes: run `ss -tulpn` or `netstat -ano | findstr LISTENING`.
- Listening ports found:
- Any I can close or restrict?

## Notes (10 min)
- Risk in one sentence:
- Attack surface in one sentence:
- Attack vector in one sentence:

## Self-check
1. Why is risk not the same as vulnerability?
2. If likelihood is 5 and impact is 2, what is the score and level?
3. Name three ways to reduce an attack surface.

## Mistake I fixed / still confusing
-

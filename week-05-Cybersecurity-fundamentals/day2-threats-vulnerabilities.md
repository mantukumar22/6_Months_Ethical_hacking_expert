# Day 2: Threats, Vulnerabilities and Exploits
**Date:** ____ · **Time:** 60 min
**Video:** Threat vs Vulnerability vs Exploit: <paste URL>

## Learn (20 min)

| Term | Definition | Example |
|---|---|---|
| **Threat** | Anything that could cause harm to an asset: a person, group, event or malware | A criminal group, ransomware, a flood, a careless insider |
| **Vulnerability** | A **weakness** in a system, process or person that a threat could use | Unpatched software, weak password, missing input validation, no staff training |
| **Exploit** | The **method or code** that takes advantage of a vulnerability | A script that abuses an SQL injection flaw |
| **Asset** | Something valuable that needs protection | Customer database, servers, reputation |
| **Threat actor** | The one carrying out the threat | Cybercriminal, hacktivist, insider, nation state |

### How they connect
```
Threat actor  --uses-->  Exploit  --targets-->  Vulnerability  --in-->  Asset
```
A threat does nothing harmful unless there is a vulnerability to reach an asset. A vulnerability alone isn't an incident until something exploits it.

### The key differences
| | Threat | Vulnerability | Exploit |
|---|---|---|---|
| What it is | The danger or who or what could do harm | A weakness | A way to use the weakness |
| Where it lives | Outside (the environment) | Inside (the system) | In between: a technique or tool |
| Can you remove it? | Rarely | **Yes** (patch, fix, configure) | Reduce by fixing the vulnerability |
| Example | Ransomware gang | Unpatched server | Public exploit for that bug |

### Related terms
- **Zero-day:** a vulnerability unknown to the vendor, with no patch yet.
- **CVE:** a public ID for a known vulnerability (e.g. `CVE-YYYY-NNNN`).
- **CVSS:** a 0 to 10 score for vulnerability severity.
- **Payload:** what runs after a successful exploit.
- **Patch:** a fix from the vendor.

## Practice (30 min)
### Scenario analysis
A company runs an old web server. A new bug for that version is published, and a public tool uses it. A criminal group scans the internet for servers like this.

| Item | Answer |
|---|---|
| Threat | |
| Vulnerability | |
| Exploit | |
| Asset | |
| Which CIA principle is at risk? | |

### Classify each (Threat / Vulnerability / Exploit)
| Item | Type |
|---|---|
| Employee who reuses the same weak password everywhere | |
| A phishing email campaign | |
| Missing security patch on a VPN appliance | |
| A script that sends crafted input to bypass a login | |
| A disgruntled employee with admin access | |
| Default admin password left unchanged | |

### Write your own
One threat, one vulnerability and one exploit for a **home Wi-Fi router**:
- Threat:
- Vulnerability:
- Exploit:

## Notes (10 min)
In my own words, the difference between the three, in one sentence each:
- Threat:
- Vulnerability:
- Exploit:

## Self-check
1. Can a vulnerability exist without a threat? Can a threat succeed without a vulnerability?
2. Why can we fix vulnerabilities but not eliminate threats?
3. What is a zero-day?

## Mistake I fixed / still confusing
-

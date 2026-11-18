# Day 4: Types of Cyberattacks
**Date:** 18 · **Time:** 60 min
**Video:** Common Cyberattacks: <paste URL>

Learn how each attack works at a **conceptual** level, what it harms, and how to defend against it. Practice attacks only in the Day 6 lab environments.

## Learn (20 min)

### 1. Phishing
- **What:** a fake message (email, SMS, call, site) that tricks someone into giving credentials, money or running malware. A form of **social engineering**.
- **Variants:** spear phishing (targeted), whaling (executives), smishing (SMS), vishing (voice), business email compromise.
- **Red flags:** urgency, spelling errors, mismatched sender or link, unexpected attachments, requests for passwords or payments.
- **CIA impact:** mainly **Confidentiality** (stolen credentials), then often Integrity and Availability (malware, ransomware).
- **Defenses:** user training, email filtering, MFA, check links before clicking, report suspicious mail.

### 2. Brute-force attacks
- **What:** trying many passwords or keys until one works. Variants: **credential stuffing** (reusing leaked passwords), **password spraying** (one common password across many accounts), dictionary attacks.
- **CIA impact:** **Confidentiality** (account takeover).
- **Defenses:** long unique passwords, **MFA**, account lockout and rate limiting, monitoring failed logins (Windows Event 4625), breached-password checks.

### 3. SQL Injection (SQLi)
- **What:** an application builds a database query from user input without handling it safely, so an attacker's input changes the query's meaning.
- **Idea:** the app expects a username, but receives input containing SQL syntax, and the database runs it as part of the query.
- **Impact:** read data (Confidentiality), modify or delete it (Integrity), sometimes bypass login or crash things (Availability).
- **Defenses:** **parameterized queries / prepared statements**, input validation, least-privilege database accounts, error messages that don't leak details, a web application firewall (WAF) as an extra layer.

### 4. Cross-Site Scripting (XSS)
- **What:** an application includes untrusted input in a page without proper handling, so an attacker's **script runs in another user's browser**.
- **Types:** **Reflected** (in a crafted link), **Stored** (saved on the server, hits every visitor), **DOM-based** (client-side code).
- **Impact:** steal session cookies, act as the victim, alter the page, redirect. Mainly **Confidentiality** and **Integrity** of the user's session.
- **Defenses:** **output encoding**, input validation, Content Security Policy (CSP), `HttpOnly` and `Secure` cookie flags.

### 5. Denial of Service (DoS / DDoS)
- **What:** overwhelming a system with traffic or requests so legitimate users can't use it. **DDoS** comes from many machines (a botnet).
- **Types:** volumetric (flood of traffic), protocol (e.g. SYN flood, link to the TCP handshake in Week 2), application-layer (many expensive requests).
- **CIA impact:** **Availability**.
- **Defenses:** rate limiting, CDN or DDoS protection, load balancing, scalable infrastructure, upstream filtering.

### Summary table
| Attack | Target | Main CIA impact | Key defense |
|---|---|---|---|
| Phishing | People | Confidentiality | Training, MFA, email filtering |
| Brute force | Accounts | Confidentiality | MFA, lockout, strong passwords |
| SQL injection | Database via web app | C, I (and A) | Parameterized queries |
| XSS | Users' browsers | C and I | Output encoding, CSP |
| DoS / DDoS | Service | Availability | Rate limiting, CDN, redundancy |

## Practice (30 min)
### 1. Classify (attack and CIA principle)
| Situation | Attack | CIA |
|---|---|---|
| An email says "Your account is locked, click here" | | |
| A script tries 10,000 passwords on a login page | | |
| A comment box saves text that runs in every visitor's browser | | |
| A search box lets someone read the whole users table | | |
| A shop site goes down under millions of fake requests | | |

### 2. Pick a defense
For each attack, write one **preventive** and one **detective** control:
| Attack | Preventive | Detective |
|---|---|---|
| Phishing | | |
| Brute force | | |
| SQL injection | | |
| XSS | | |
| DoS | | |

### 3. Spot a phishing email
Find a sample phishing email (from your spam folder or an awareness site). List three red flags. **Do not click anything.**
- 1.
- 2.
- 3.

## Notes (10 min)
One sentence per attack, in my own words:
- Phishing:
- Brute force:
- SQL injection:
- XSS:
- DoS:

## Self-check
1. What is the root cause of SQL injection and XSS? (Think untrusted input.)
2. Which defense best stops SQL injection? Which stops brute force?
3. How is DDoS different from DoS?

## Mistake I fixed / still confusing
-

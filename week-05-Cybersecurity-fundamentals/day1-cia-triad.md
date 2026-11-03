# Day 1: CIA Triad
**Date:** ____ · **Time:** 60 min
**Video:** CIA Triad explained: <paste URL>

## Learn (20 min)
The **CIA Triad** is a fundamental information security model. Every security decision can be checked against it: *which of the three am I protecting?*

| Principle | Meaning | Example control |
|---|---|---|
| **Confidentiality** | Only authorized people can access data | Passwords, encryption, access control |
| **Integrity** | Data stays accurate and unchanged without authorization | File hashing, digital signatures, change logs |
| **Availability** | Systems and data are accessible when needed | Backups, redundancy, DDoS protection |

### Real-world examples
| Principle | Attack that breaks it | Defense |
|---|---|---|
| Confidentiality | Data breach, stolen password, sniffed traffic | Encryption, MFA, least privilege |
| Integrity | Tampered file, altered database record, man-in-the-middle edit | Hashes, signatures, input validation, audit logs |
| Availability | Ransomware, DoS, power failure, deleted data | Backups, failover, rate limiting |

Notes:
- The principles can **conflict**. Strong access controls (confidentiality) can slow people down (availability).
- Extensions you'll hear about: **authentication**, **authorization**, **non-repudiation** (can't deny an action), and **accountability** (logging).

## Practice (30 min): online banking exercise
Imagine an online banking application.

1. Someone steals a customer's password. **Which CIA principle is affected?**
   - My answer:
2. Someone changes the account balance without permission. **Which principle is affected?**
   - My answer:
3. The banking server goes offline. **Which principle is affected?**
   - My answer:

Stretch: for each answer, name one control that would reduce the problem.
- Control for 1:
- Control for 2:
- Control for 3:

### More scenarios (classify each)
| Scenario | Principle |
|---|---|
| A laptop with patient records is stolen, unencrypted | |
| An attacker edits a log file to hide their tracks | |
| A ransomware attack locks all hospital files | |
| An employee emails a salary spreadsheet to the wrong person | |
| A website defacement changes the home page text | |
| A shop's checkout is down on Black Friday | |

## Notes (10 min)
One real-world example I can remember for each principle:
- Confidentiality:
- Integrity:
- Availability:

## Self-check
1. What does each letter of CIA stand for?
2. Which principle does hashing support? Which does a backup support?
3. Can one incident affect more than one principle?

## Mistake I fixed / still confusing
-

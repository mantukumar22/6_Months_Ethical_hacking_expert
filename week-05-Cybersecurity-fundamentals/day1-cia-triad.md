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
   - My answer: Here Confidentiality breaks because it's a type of data leak problem.
2. Someone changes the account balance without permission. **Which principle is affected?**
   - My answer: Here Integrity breaks because it's a data change attack.
3. The banking server goes offline. **Which principle is affected?**
   - My answer: Here availblity breaks beacuse it's a Dos attack . here service not avalible .

Stretch: for each answer, name one control that would reduce the problem.
- Control for 1: We need to add Multi Factor Authentiction and password hasing to defence in this problem.
- Control for 2: here we need to add access control and signatures to protect the data.
- Control for 3: here we need to add backups, failover.

### More scenarios (classify each)
| Scenario | Principle |
|---|---|
| A laptop with patient records is stolen, unencrypted | Confidentiality |
| An attacker edits a log file to hide their tracks | Integrity |
| A ransomware attack locks all hospital files | Availblity |
| An employee emails a salary spreadsheet to the wrong person | Confidentiality |
| A website defacement changes the home page text | Integrity |
| A shop's checkout is down on Black Friday | Availblity|

## Notes (10 min)
One real-world example I can remember for each principle:
- Confidentiality: Someone Get my laptop password and viewd my all photos.
- Integrity: Someone sended my all laptop photo on his whatsapp. and deleted from my laptop.
- Availability: Someone crash my laptop by running some os cmd 's .

## Self-check
1. What does each letter of CIA stand for? Confidentiality, Integrity, Availblity
2. Which principle does hashing support? Which does a backup support? Integrity, Availblity
3. Can one incident affect more than one principle? Yes because if Someone gets password he do anything data change data delete .

## Mistake I fixed / still confusing
-

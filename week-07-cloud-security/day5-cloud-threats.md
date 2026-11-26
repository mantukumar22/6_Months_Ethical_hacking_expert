# Day 5: Cloud Threats and Misconfigurations
**Date:** 26 · **Time:** 60 min
**Video:** Cloud security misconfigurations: <paste title/URL>

## Learn (20 min)
Most cloud incidents are **misconfigurations and stolen credentials**, not clever zero-days. For each threat: what it is, how attackers use it, impact (CIA), and the fix.

### 1. Exposed cloud credentials
- **What:** access keys, secret keys, tokens or passwords exposed in public Git repos, code, screenshots, Docker images, CI logs, mobile or web apps, config files or pasted chats.
- **Attack:** automated bots scan public sources constantly. A leaked key can be abused within minutes, for example to launch crypto-mining instances, steal data or create new admin users.
- **Impact:** account takeover (Confidentiality, Integrity, Availability), surprise bills.
- **Fix:** never hardcode secrets, use **roles** and a secrets manager (AWS Secrets Manager), **rotate or delete exposed keys immediately**, add secret scanning (e.g. gitleaks, git hooks, GitHub secret scanning), and watch CloudTrail.

### 2. Public storage buckets
- **What:** S3 buckets (or snapshots, AMIs) readable or writable by anyone (Day 4).
- **Attack:** discovery by guessing predictable names or scanning, then downloading data. Write access allows planting or replacing files.
- **Impact:** data breach (Confidentiality), tampering (Integrity), ransom or deletion (Availability).
- **Fix:** Block Public Access, least-privilege bucket policies, encryption, access logging, Macie for sensitive data.

### 3. Over-permissive IAM policies
- **What:** `*` permissions, `iam:PassRole` or `iam:*` for low-trust identities, wide trust policies (Day 3).
- **Attack:** an attacker with a small foothold uses the extra permissions to **escalate privileges** to administrator, or moves **laterally** into other accounts.
- **Impact:** full account compromise.
- **Fix:** least privilege, permission boundaries, SCPs, Access Analyzer, regular reviews.

### 4. Insecure APIs
- **What:** APIs (API Gateway, Lambda URLs, internal and mobile APIs) with no authentication, weak authorization or excessive data exposure.
- **Attack:** broken object-level authorization (changing an ID to read someone else's data), missing rate limiting, injection, **SSRF** that makes a server request the cloud metadata service.
- **Impact:** data exposure and abuse.
- **Fix:** authentication and authorization on every endpoint, input validation, rate limiting, WAF, IMDSv2, API gateway authorizers.

### 5. Misconfigured Security Groups
- **What:** `0.0.0.0/0` open to SSH (22), RDP (3389), databases (3306, 5432, 1433, 6379, 27017), Elasticsearch (9200) or *all ports* (Day 2 and Day 4).
- **Attack:** internet scanners find open ports in minutes, then brute-force logins (Week 5) or exploit unpatched services.
- **Impact:** server compromise (all three CIA).
- **Fix:** restrict sources to known IPs or other Security Groups, private subnets, Session Manager instead of public SSH, patching.

### 6. Data breaches and account compromise
The result of the above. Typical **cloud attack chain:**
```
Exposed key / SSRF / phishing
   -> valid cloud credentials
   -> enumerate permissions (what can I do?)
   -> privilege escalation (IAM misconfiguration)
   -> data access / persistence (new keys, backdoor roles)
   -> exfiltration, crypto-mining, ransomware, or deletion
```
**Well-known pattern (the 2019 Capital One breach, widely documented):** a web application weakness allowed server-side requests to the instance metadata service, which returned role credentials, and an over-permissive role let the attacker copy data from S3. Lessons: IMDSv2, least privilege, and monitoring. (Read a public write-up, and note the lesson in your own words.)

### Other common issues
| Issue | Why it matters |
|---|---|
| No logging (CloudTrail off, no alerts) | Attacks go unnoticed |
| Unencrypted storage or databases | Greater impact if data is exposed |
| Unpatched EC2 instances (customer's job in IaaS) | Known exploits (Week 5) |
| Public snapshots, AMIs, RDS instances | Hidden data leaks |
| Unused regions and old resources | Forgotten and unmonitored |
| Default or shared credentials | No accountability |

### Detection and response (defender view)
| Service | What it gives you |
|---|---|
| **CloudTrail** | Record of every API call (who did what, when, from where) |
| **GuardDuty** | Threat detection from logs, DNS and network activity |
| **AWS Config** | Tracks configuration and flags non-compliance |
| **IAM Access Analyzer** | Finds resources shared outside the account |
| **Security Hub** | Central view of findings |
| **CloudWatch alarms and Budgets** | Alerts on unusual events and spend |

**If a key is leaked:** disable or delete it **first**, review CloudTrail for what it did, rotate other secrets, check for new users, roles and keys, and review all regions.

### MITRE ATT&CK for cloud
Tactics from the MITRE ATT&CK matrix (cloud) map to the same story: initial access, persistence, privilege escalation, defense evasion, credential access, discovery, exfiltration, impact. Use it later to name your findings.

## Practice (30 min)

### 1. Map each threat
| Misconfiguration | CIA impact | Control that prevents it | Control that detects it |
|---|---|---|---|
| Access key in a public GitHub repo | | | |
| Public S3 bucket | | | |
| `Action: "*"` policy on a developer role | | | |
| SSH open to `0.0.0.0/0` | | | |
| CloudTrail disabled | | | |
| Unauthenticated API endpoint | | | |

### 2. Hunt for secrets in your own repos (own code only)
Install a secret scanner such as **gitleaks** and run it on your learning repo, including its history:
```
gitleaks detect --source . -v
```
(If you find a real secret, treat it as compromised: revoke it, don't just delete the file.)

### 3. Attack path write-up
Choose one scenario and write 5 to 8 steps, from the attacker's first foothold to impact, then list where **three different controls** would have stopped it.

### 4. Run the sample checkers again
```
python3 scripts/iam_policy_checker.py samples/bad-policy.json
python3 scripts/sg_checker.py samples/sg-sample.json
```
Which findings belong to which threat above?

## Ethics and legal
Finding a public bucket or leaked key on the internet does **not** give you permission to access, download or use it. Without written authorization, stop at identifying that it exists and report it through the owner's disclosure channel. Practise only on your own accounts and training environments (Day 6).

## Notes (10 min)
- The three misconfigurations I think are most common, and why:
- How a leaked key becomes a full compromise:

## Self-check
1. Name four cloud misconfigurations.
2. Why is a leaked access key so dangerous?
3. What is SSRF and why does it matter for cloud metadata?
4. What is the first thing to do when a key is leaked?
5. Which AWS service records API calls?

## Mistake I fixed / still confusing
-

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

## 1. Map each threat

| Misconfiguration | CIA impact | Control that prevents it | Control that detects it |
|---|---|---|---|
| Access key in a public GitHub repo | All | Use roles & a Secret Manager instead of hardcoded keys | Watch CloudTrail for unexpected API activity from that key |
| Public S3 bucket | All | S3 Block Public Access | Access logging / S3 bucket access logs |
| `Action: "*"` policy on a developer role | All | Apply least privilege — scope the policy to specific required actions/resources | IAM Access Analyzer; CloudTrail for unusual API calls made with that role |
| SSH open to `0.0.0.0/0` | All | Restrict security group sources to known IPs / use a bastion host or SSM Session Manager | Patching, VPC Flow Logs, GuardDuty alerts for brute-force attempts |
| CloudTrail disabled | All (mainly Integrity/Accountability) | Enforce CloudTrail via Service Control Policies (SCPs) or AWS Config rules | AWS Config rule detecting CloudTrail is disabled; CloudWatch alarm on `StopLogging` event |
| Unauthenticated API endpoint | Confidentiality, Integrity | Require authentication/authorization (API keys, IAM auth, Cognito) on all API Gateway routes | API Gateway access logs; WAF logs showing anonymous requests; CloudTrail for API Gateway config changes |

## 2. Hunt for secrets in your own repos

```bash
gitleaks detect --source . -v
```

If this turns up a real secret: **treat it as compromised immediately** — revoke/rotate the credential in the provider's console, don't just delete it from the file or commit history (old commits may still be cached, forked, or already scraped by a bot).

## 3. Attack path write-up

**Scenario: Leaked AWS access key on GitHub → full account compromise**

1. A developer accidentally commits an AWS access key (`AKIA...`) to a public GitHub repo.
2. An automated bot scanning GitHub for leaked credentials finds and extracts the key within minutes.
3. The attacker uses the key with the AWS CLI to run `aws sts get-caller-identity`, confirming the key is valid and checking what account/role it belongs to.
4. The attacker enumerates permissions attached to the compromised identity (e.g., via `iam:ListAttachedUserPolicies` or by brute-force testing common actions).
5. The key turns out to have an overly broad `Action: "*"` policy attached, so the attacker pivots to create a new IAM user with admin access as a persistence backdoor.
6. The attacker spins up EC2 instances in multiple regions for cryptomining, or accesses S3 buckets to exfiltrate sensitive data.
7. Billing alerts or CloudTrail anomalies finally alert the account owner days later, by which point data has been exfiltrated and resources abused.
8. **Impact:** financial loss from resource abuse, potential data breach, and loss of trust/compliance violations if customer data was exposed.

**Where three controls would have stopped it:**
- **gitleaks / pre-commit secret scanning** — would have caught the key before it was ever pushed to GitHub (prevents step 1–2).
- **Least privilege IAM policy** (no `Action: "*"`) — even if the key leaked, the attacker's actions would have been tightly limited, preventing privilege escalation (stops step 5).
- **CloudTrail + GuardDuty/CloudWatch alarms** — would have detected the anomalous API activity (new region usage, unusual IAM calls) within minutes instead of days, enabling fast key revocation (stops step 6–7 from escalating further).

## 4. Run the sample checkers again

```bash
python3 scripts/iam_policy_checker.py samples/bad-policy.json
python3 scripts/sg_checker.py samples/sg-sample.json
```

Expected mapping of findings to the table above:
- `iam_policy_checker.py` findings (e.g., wildcard actions/resources, missing conditions) → maps to **"`Action: "*"` policy on a developer role"** and potentially **"Access key in a public GitHub repo"** if the checked policy belongs to a key-bearing user.
- `sg_checker.py` findings (e.g., port 22 or 3389 open to `0.0.0.0/0`) → maps directly to **"SSH open to `0.0.0.0/0`"**.

(Run both and compare their actual output against your sample files to confirm exact matches — paste the output if you want help interpreting specific findings.)

## Ethics and legal
Finding a public bucket or leaked key on the internet does **not** grant permission to access, download, or use it. Without written authorization, the correct action is to stop at identifying that it exists and report it through the owner's responsible disclosure channel. Practice only on your own accounts and dedicated training environments.

## Notes (10 min)

**The three misconfigurations I think are most common, and why:**
1. **Overly permissive IAM policies** (`Action: "*"` or `Resource: "*"`) — because it's the path of least resistance during development; it's faster to grant broad access than to scope permissions correctly, and it often never gets tightened later.
2. **Public S3 buckets** — because default settings have historically been easy to misconfigure, and a single checkbox or policy line can expose an entire bucket without any obvious warning signs during normal use.
3. **Leaked access keys in source code** — because developers often hardcode credentials for convenience during testing and forget to remove them before committing, especially in fast-moving or less security-mature teams.

**How a leaked key becomes a full compromise:**
A leaked key starts as just a credential, but its real danger comes from what it's *attached to*. Automated scanners find leaked keys on GitHub within minutes, after which an attacker checks the key's identity and enumerates its permissions. If that key belongs to an overly privileged role or user (e.g., with `iam:PassRole`, `iam:CreateUser`, or broad `*` permissions), the attacker can escalate to full administrative access, create backdoor users, access all data, or spin up expensive resources — turning one small leaked secret into complete account takeover.

---

## Self-check

**1. Name four cloud misconfigurations.**
Publicly accessible S3 buckets, overly permissive IAM policies (wildcard actions/resources), security groups with SSH/RDP open to `0.0.0.0/0`, and CloudTrail logging disabled.

**2. Why is a leaked access key so dangerous?**
A leaked access key gives an attacker direct, authenticated API access to AWS as if they were the legitimate user or application — there's no password prompt or MFA step to bypass. The actual damage depends entirely on what permissions that key has, but keys are often over-privileged, so a single leaked key can lead to data theft, resource abuse, or full account takeover within minutes of being discovered by automated scanners.

**3. What is SSRF and why does it matter for cloud metadata?**
SSRF (Server-Side Request Forgery) is a vulnerability where an attacker tricks a server into making HTTP requests on their behalf, often to internal resources the attacker couldn't normally reach directly. In cloud environments, this matters because instances often have a metadata service (e.g., `169.254.169.254` on AWS) that serves temporary IAM credentials for that instance — if an attacker can get the vulnerable application to request that internal URL, they can steal the instance's role credentials and use them to access AWS resources as that role.

**4. What is the first thing to do when a key is leaked?**
Immediately **revoke/deactivate the leaked key** in the IAM console (or via CLI), rather than just deleting it from the code or commit history — the key remains valid and usable until it's explicitly revoked, regardless of whether the file still exists.

**5. Which AWS service records API calls?**
**CloudTrail** records API calls made within an AWS account, logging details like who made the call, what action was performed, when, and from where — making it the primary tool for auditing activity and investigating suspicious behavior.

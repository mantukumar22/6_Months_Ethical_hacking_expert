# Day 6: Practical Cloud Security Lab
**Date:** 26 Nov · **Time:** 60 min
**Video:** Prowler AWS security audit: <paste title/URL>

## Goal
Explore the AWS Free Tier or a local or training cloud-security lab, **inspect IAM permissions, review storage access settings, inspect network exposure, and use Prowler or ScoutSuite in an authorized environment.** Then document the findings.

> **Authorization and safety**
> - Only use **my own AWS account** or a **deliberately vulnerable training environment** built for this purpose.
> - Never scan or test cloud resources that belong to someone else without written authorization.
> - Use **read-only** credentials for assessment tools.
> - Set a **billing alert** before starting. **Delete everything** afterwards.
> - Never commit keys, tool output (account IDs, ARNs) or screenshots with secrets.

## Choose a lab environment

| Option | What it is | Cost / risk | Best for |
|---|---|---|---|
| **A. My own AWS account** (Free Tier) | A real but small and clean account | Low, if you set a budget and clean up | Inspecting real IAM, S3 and network settings, and running Prowler or ScoutSuite |
| **B. CloudGoat** (Rhino Security Labs) | Intentionally vulnerable AWS scenarios that **deploy real resources into my account** | Uses my AWS account, so use a dedicated sandbox account and `destroy` afterwards | Practising attack paths (privilege escalation) |
| **C. flaws.cloud / flaws2.cloud** | Free public AWS security CTF built to be attacked | No setup, no cost | Learning S3 and IAM mistakes safely |
| **D. TryHackMe / vendor labs** | Guided cloud rooms with a prepared environment | Account only | Beginners who want a guided path |

Option A (assessment) is the core of today. Add B, C or D if time allows. For B, follow the CloudGoat README for installation and scenario names, and check which services a Free plan account allows.

## Part 1: Create a read-only audit identity (Option A)
In my own account, create an IAM user or role for assessment only:
- Attach AWS managed policies **`SecurityAudit`** and **`ViewOnlyAccess`** (read-only).
- Enable MFA. Create access keys only if needed, and delete them afterwards.
- Configure a named profile:
```
aws configure --profile audit
aws sts get-caller-identity --profile audit        # confirm who I am
```

## Part 2: Manual inspection (20 min)
Do these in the console or with the CLI (see [resources/aws-cli-readonly.md](resources/aws-cli-readonly.md)).

### IAM permissions
- [ ] Root MFA enabled? Root access keys absent?
- [ ] Credential report: users without MFA, old or unused keys
- [ ] Policies with `Action: "*"` or `iam:*`
- [ ] Roles with a broad trust policy
- [ ] Run `scripts/iam_policy_checker.py` on exported policies

### Storage access settings
- [ ] Account-level Block Public Access on?
- [ ] Per bucket: public access block, policy, ACLs, encryption, versioning, logging
- [ ] Any public snapshots or AMIs?

### Network exposure
- [ ] Security Groups with `0.0.0.0/0` (`scripts/sg_checker.py`)
- [ ] Instances with public IPs. Do they need them?
- [ ] Default VPC and default Security Group in use?
- [ ] VPC Flow Logs enabled?

### Logging and detection
- [ ] CloudTrail enabled in all regions?
- [ ] GuardDuty and Config enabled? (note costs)

## Part 3: Run Prowler (authorized, read-only)
Prowler is an open-source security assessment tool. Follow its documentation for the current install method.
```
python3 -m venv .venv && source .venv/bin/activate
pip install prowler
prowler aws --profile audit
```
Useful ideas: filter by severity (`--severity critical high`), choose one region, and review the HTML or JSON report it writes to its output folder (git-ignored here).

**ScoutSuite (alternative):**
```
pip install scoutsuite
scout aws --profile audit
```
It produces an HTML report. Open it locally.

Both read configuration and don't modify anything, but run them only against **my own account**. Findings from a brand-new clean account may be few, so also review the "informational" and "low" items and explain them.

## Part 4: Document findings (aim for at least 3)

### Finding 1
| Field | Details |
|---|---|
| Title | |
| Service and resource (redacted) | |
| What I observed | |
| Why it's a risk (threat and impact) | |
| CIA impact | |
| Severity (Low / Medium / High / Critical) | |
| Likelihood x Impact (Week 5) | |
| How I found it | Manual / Prowler / ScoutSuite / checker script |
| Evidence | `evidence/finding1.png` (redacted) |
| Recommended fix | |

### Finding 2
| Field | Details |
|---|---|
| Title | |
| Service and resource | |
| What I observed | |
| Why it's a risk | |
| CIA impact | |
| Severity | |
| Evidence | `evidence/finding2.png` |
| Recommended fix | |

### Finding 3
| Field | Details |
|---|---|
| Title | |
| Service and resource | |
| What I observed | |
| Why it's a risk | |
| CIA impact | |
| Severity | |
| Evidence | `evidence/finding3.png` |
| Recommended fix | |

## Findings summary
| # | Finding | Service | Severity | Fixed? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Cleanup checklist (important)
- [ ] Terminated EC2 instances, released Elastic IPs
- [ ] Emptied and deleted test S3 buckets
- [ ] Deleted test IAM users, roles and **access keys**
- [ ] `cloudgoat destroy` run if CloudGoat was used (check its README)
- [ ] Checked the **Billing dashboard** the next day
- [ ] Nothing sensitive in `git status`

## What I learned
-

## Reflection
- Which finding would an attacker find first, and why?
- How does this lab help with interview question 12 (a basic AWS security assessment)?

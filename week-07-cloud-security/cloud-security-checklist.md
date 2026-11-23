# Cloud Security Checklist (Day 7)
A basic AWS review checklist. Use it on **my own account** or an authorized environment, and record the result for each item.

Legend: ✅ pass · ❌ fail · ➖ not applicable · ❓ not checked

## 1. Account and identity
| Check | Result | Notes |
|---|---|---|
| Root user has MFA | | |
| No root access keys | | |
| Root user not used for daily work | | |
| MFA for all human users | | |
| No long-lived keys where roles could be used | | |
| Access keys rotated, unused keys removed | | |
| No wildcard (`*`) admin policies on regular users | | |
| Privilege-escalation permissions (`iam:PassRole`, `iam:*`) reviewed | | |
| Role trust policies limited to known principals | | |
| Billing alerts and budgets set | | |

## 2. Storage and data
| Check | Result | Notes |
|---|---|---|
| Account-level S3 Block Public Access on | | |
| No unintended public buckets | | |
| Bucket policies avoid `Principal: "*"` | | |
| ACLs disabled (bucket owner enforced) | | |
| Default encryption on (S3, EBS, RDS) | | |
| TLS enforced (`aws:SecureTransport`) | | |
| Versioning on for important data | | |
| No public snapshots or AMIs | | |

## 3. Network
| Check | Result | Notes |
|---|---|---|
| No `0.0.0.0/0` on SSH, RDP or database ports | | |
| Databases in private subnets | | |
| Unneeded public IPs removed | | |
| Default Security Group restricted | | |
| NACLs reviewed | | |
| VPC Flow Logs enabled | | |
| WAF in front of public web apps | | |

## 4. Compute
| Check | Result | Notes |
|---|---|---|
| IMDSv2 required on EC2 | | |
| OS patched | | |
| Instance roles instead of stored keys | | |
| No secrets in user data or environment files | | |
| Unused instances and regions cleaned up | | |

## 5. Logging, monitoring and response
| Check | Result | Notes |
|---|---|---|
| CloudTrail on in all regions | | |
| Log storage protected | | |
| GuardDuty enabled | | |
| AWS Config or Security Hub enabled | | |
| Alerts for root login, IAM changes and unusual spend | | |
| Incident response steps known (revoke keys, review CloudTrail) | | |

## Findings log (document findings)
| # | Finding | Area | Severity | Evidence | Fix | Status |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

## Revision (from memory)
| Concept | One-line definition |
|---|---|
| IaaS / PaaS / SaaS | |
| Shared Responsibility Model | |
| Region / AZ | |
| VPC / subnet | |
| Security Group vs NACL | |
| IAM user / group / role / policy | |
| Least privilege | |
| Block Public Access | |
| Encryption at rest vs in transit | |
| CloudTrail | |

## GitHub upload checklist
- [ ] All seven plan files committed
- [ ] Evidence redacted (account IDs, ARNs, bucket names, IPs)
- [ ] **No access keys, secret keys, tokens, `.pem` files or tool output committed** (`git status`, and `gitleaks` if installed)
- [ ] Cloud resources deleted and billing checked

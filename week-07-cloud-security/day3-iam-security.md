# Day 3: Cloud Identity and Access Management (IAM)
**Date:** ____ · **Time:** 60 min
**Video:** AWS IAM explained: <paste title/URL>

## Learn (20 min)

### What is IAM?
**AWS Identity and Access Management (IAM)** controls **who** (authentication) can do **what** (authorization) on **which resources**. It is the security backbone of AWS. Weak IAM is the most common root cause of serious cloud compromises, because identities are the new perimeter.

(Week 5 and Week 6 link: authentication vs authorization, MFA and least privilege.)

### Core building blocks
| Concept | Meaning |
|---|---|
| **Root user** | The account owner, with unlimited power. Lock it away: strong password, **MFA**, no access keys, use only for the few tasks that require it |
| **User** | A person or application identity with its own credentials |
| **Group** | A collection of users that share permissions (attach policies to groups, not individuals) |
| **Role** | An identity with permissions that is **assumed** temporarily, by users, AWS services (EC2, Lambda) or other accounts. **Uses temporary credentials, no long-term keys** |
| **Policy** | A JSON document that **allows or denies** actions |

### Policy types
| Type | Attached to | Purpose |
|---|---|---|
| Identity-based | Users, groups, roles | What this identity can do |
| Resource-based | The resource (S3 bucket policy, role trust policy) | Who can access this resource |
| Permissions boundary | A user or role | Maximum permissions allowed |
| Service control policy (SCP) | AWS Organization accounts | Guardrails over whole accounts |
| Session policy | A temporary session | Narrows permissions further |

### Anatomy of a policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::example-reports-bucket",
        "arn:aws:s3:::example-reports-bucket/*"
      ],
      "Condition": { "Bool": { "aws:MultiFactorAuthPresent": "true" } }
    }
  ]
}
```
| Element | Meaning |
|---|---|
| `Effect` | `Allow` or `Deny` |
| `Action` | The API calls permitted (`s3:GetObject`) |
| `Resource` | The ARNs affected |
| `Principal` | Who (only in resource-based and trust policies) |
| `Condition` | Extra requirements: MFA, source IP, TLS, time |

**Evaluation logic:** everything is **denied by default** (implicit deny). An explicit **Allow** grants access. An explicit **Deny always wins**.

### Credentials
| Type | Looks like | Notes |
|---|---|---|
| **Access key ID** | `AKIA...` (long-term), `ASIA...` (temporary) | Identifies the caller, like a username |
| **Secret access key** | Long random string | Like a password. Shown **once**. Must be kept secret |
| **Session token** | Long string | Needed with `ASIA` temporary keys (roles, STS) |
| **Console password** | | For the web console |

Whoever holds an access key and secret key **is that identity** from anywhere in the world. Prefer **roles and temporary credentials** (STS) over long-lived keys, and rotate or delete unused keys.

### MFA
Add a second factor (virtual authenticator app, or a hardware key such as FIDO2) for:
- The **root user** (mandatory in practice)
- All human users with console access
- Sensitive actions via policy conditions (`aws:MultiFactorAuthPresent`)

### Least privilege
Grant only the permissions needed, on only the resources needed, for only as long as needed. Start with nothing and add. Use **IAM Access Analyzer** and "last accessed" data to remove unused permissions.

| Too broad | Better |
|---|---|
| `"Action": "*", "Resource": "*"` | Specific actions on specific ARNs |
| `s3:*` on all buckets | `s3:GetObject` on one bucket prefix |
| `AdministratorAccess` for developers | Task-specific policy or a role for the job |

### IAM misconfigurations (what attackers and auditors look for)
| Misconfiguration | Why it's dangerous |
|---|---|
| **Wildcard permissions** (`Action: "*"`, `Resource: "*"`) | Full admin by accident |
| `iam:*` or **privilege-escalation permissions** (`iam:PassRole` on `*`, `iam:CreatePolicyVersion`, `iam:AttachUserPolicy`, `iam:CreateAccessKey`) | A low-privilege identity can make itself admin |
| **Root account in use** or root access keys | Unlimited, unrestricted power |
| **No MFA** | One stolen password means compromise |
| **Long-lived access keys** never rotated or unused | Leaked keys stay valid for years |
| **Keys in code, GitHub, containers or client apps** | Public exposure (Day 5) |
| **Overly broad trust policy** (`Principal: "*"` or an unknown account) | Anyone can assume the role |
| **Shared accounts and credentials** | No accountability in logs |
| **Unused users, roles and permissions** | Needless attack surface |

## Practice (30 min)

### 1. Read and explain
Use the AWS console (IAM → Policies) to open `ReadOnlyAccess`, `AdministratorAccess` and one S3 policy. For each: what do `Action` and `Resource` look like?

### 2. Build least privilege (own account)
- [ ] Create group `s3-readers` with a policy allowing only `s3:GetObject` and `s3:ListBucket` on **one** bucket.
- [ ] Create a test user, add them to the group, enable MFA.
- [ ] Use the **IAM Policy Simulator** to test: can the user read the bucket? Delete from it? Read another bucket?
- [ ] Clean up: delete the test user and group.

### 3. Run the offline policy checker (no AWS access needed)
```
python3 scripts/iam_policy_checker.py samples/bad-policy.json
python3 scripts/iam_policy_checker.py samples/good-policy.json
python3 scripts/iam_policy_checker.py samples/bad-bucket-policy.json
```
Note each finding, severity and the fix. Then write **your own** bad policy and see whether it's caught.

### 4. Read-only commands against your own account
```
aws iam get-account-summary
aws iam list-users
aws iam list-access-keys --user-name <user>
aws iam generate-credential-report && aws iam get-credential-report
```
In the credential report, look at: `mfa_active`, `access_key_1_last_used_date`, and `password_last_used`. Find users without MFA and keys that are never used.

### Record
| Check | Result |
|---|---|
| Root MFA enabled? | |
| Root access keys exist? | |
| Users without MFA | |
| Unused or old access keys | |
| Policies with `*` actions | |

## Notes (10 min)
- User vs role:
- Why explicit deny wins:
- Three IAM misconfigurations I can now recognize:

## Self-check
1. What is the difference between a user, a group and a role?
2. Why prefer roles over access keys?
3. What does `AKIA` vs `ASIA` indicate?
4. Why is `iam:PassRole` on `*` risky?
5. State the least privilege principle with an example.

## Mistake I fixed / still confusing
-

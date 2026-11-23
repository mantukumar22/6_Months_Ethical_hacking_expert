# Week 7: Cloud Security

**7 days · 1 hour/day**

Goal: understand cloud computing, cloud infrastructure, common cloud vulnerabilities, identity and access management (IAM), and cloud security testing. For the VAPT path, the focus is **AWS fundamentals, IAM misconfigurations, storage security, network security and cloud penetration-testing basics**.

> **Safety rules**
> - Use **only my own cloud account** or **deliberately vulnerable training environments**. Never test cloud resources that belong to other organizations without written authorization.
> - Never commit access keys, secret keys, session tokens, `.pem` files or AWS config files. `.gitignore` blocks the common ones, but check `git status` before every commit.
> - Redact 12-digit **AWS account IDs**, ARNs, bucket names and IPs in screenshots and reports.
> - Run assessment tools (Prowler, ScoutSuite) with a **read-only** identity in an account I own.
> - Cloud resources can cost money. Set a billing alert first and delete everything after each lab.

## Roadmap

| Day | Topic | File |
|---|---|---|
| 1 | Cloud Computing Fundamentals | [day1-cloud-fundamentals.md](day1-cloud-fundamentals.md) |
| 2 | AWS Fundamentals | [day2-aws-fundamentals.md](day2-aws-fundamentals.md) |
| 3 | Cloud Identity and Access Management | [day3-iam-security.md](day3-iam-security.md) |
| 4 | Cloud Storage and Network Security | [day4-storage-network-security.md](day4-storage-network-security.md) |
| 5 | Cloud Threats and Misconfigurations | [day5-cloud-threats.md](day5-cloud-threats.md) |
| 6 | Practical Cloud Security Lab | [day6-cloud-security-lab.md](day6-cloud-security-lab.md) |
| 7 | Revision and Assessment | [week7-interview-questions.md](week7-interview-questions.md), [cloud-security-checklist.md](cloud-security-checklist.md) |

Each day: **20 min** learn → **30 min** practice → **10 min** notes.

## Tools for the week

| Tool | Purpose |
|---|---|
| AWS IAM | Identity and access management |
| AWS CLI | Manage AWS resources from the terminal |
| Prowler | Cloud security assessments (open source) |
| ScoutSuite | Multi-cloud security auditing |
| CloudGoat | Intentionally vulnerable AWS lab scenarios (deploys real resources in my account) |
| `scripts/` (this repo) | Offline checkers for IAM policies and Security Groups, no AWS access needed |

## Offline practice scripts
```
python3 scripts/iam_policy_checker.py samples/bad-policy.json
python3 scripts/iam_policy_checker.py samples/good-policy.json
python3 scripts/iam_policy_checker.py samples/bad-bucket-policy.json
python3 scripts/sg_checker.py samples/sg-sample.json
```
They use only the Python standard library and never contact AWS. Later, point them at my own exported policies and `aws ec2 describe-security-groups` output.

## Resources
See [resources/links.md](resources/links.md) and [resources/aws-cli-readonly.md](resources/aws-cli-readonly.md).

## Folder layout
```
week7/
├── README.md
├── checklist.md
├── day1-cloud-fundamentals.md
├── day2-aws-fundamentals.md
├── day3-iam-security.md
├── day4-storage-network-security.md
├── day5-cloud-threats.md
├── day6-cloud-security-lab.md
├── week7-interview-questions.md
├── cloud-security-checklist.md     Day 7 checklist and findings log
├── scripts/                        offline policy and Security Group checkers
├── samples/                        intentionally bad example configs
├── resources/                      links and read-only AWS CLI cheat sheet
└── evidence/                       lab screenshots (redacted)
```
The seven files named in the plan are included. The rest are extras. Drop the whole `week7/` folder into the cybersecurity learning repo.

## Progress
See [checklist.md](checklist.md). **0/7** done.

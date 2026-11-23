# Week 7: Interview Questions
Answer each in **your own words, out loud first**, then write 3 to 5 sentences with an example. The hints show what to cover, not the answers.

## 1. What is cloud computing?
*Cover:* on-demand resources over the internet, pay-as-you-go, key characteristics, why it changes security (APIs and identities).

**My answer:**

## 2. What is the difference between IaaS, PaaS and SaaS?
*Cover:* what the provider gives vs what you manage, one example each (EC2, App Engine, Gmail).

**My answer:**

## 3. What is AWS?
*Cover:* Amazon's cloud platform, services, console/CLI/API, every action is an API call checked by IAM.

**My answer:**

## 4. What is an EC2 instance?
*Cover:* a virtual server (IaaS), AMI, instance type, key pair, Security Group, what you must secure (OS, patches, SSH), IMDSv2.

**My answer:**

## 5. What is an S3 bucket?
*Cover:* object storage, buckets and objects, globally unique name, access controls, why it's often misconfigured.

**My answer:**

## 6. What is IAM?
*Cover:* who can do what on which resource, users, groups, roles, policies, MFA, temporary credentials.

**My answer:**

## 7. What is the Shared Responsibility Model?
*Cover:* security of the cloud (provider) vs security in the cloud (customer), how it shifts across IaaS/PaaS/SaaS, what always stays with the customer.

**My answer:**

## 8. What is a public S3 bucket?
*Cover:* readable (or writable) by anyone, how it happens (policy, ACL, Block Public Access off), risks (data leak, tampering, cost), the fix.

**My answer:**

## 9. What is the principle of least privilege?
*Cover:* minimum access for the minimum time, an AWS example (specific actions and resources), tools (Access Analyzer, permission boundaries).

**My answer:**

## 10. What are cloud security misconfigurations?
*Cover:* examples (public buckets, `*` IAM policies, open Security Groups, exposed keys, no logging), why they're the top cause of cloud breaches, how to detect them (Prowler, Config, Security Hub).

**My answer:**

## 11. What is the difference between Security Groups and Network ACLs?
*Cover:* instance vs subnet level, stateful vs stateless, allow-only vs allow and deny, rule evaluation.

**My answer:**

## 12. How would you conduct a basic AWS security assessment?
*Cover (a sensible order):*
1. **Authorization and scope** in writing: accounts, regions, allowed activities, read-only vs active testing, contacts and timing.
2. **Get read-only access** (SecurityAudit and ViewOnlyAccess) and confirm the identity (`sts get-caller-identity`).
3. **Inventory** the environment: regions, services, resources, accounts.
4. **IAM review:** root, MFA, credential report, wildcard policies, privilege-escalation paths, trust policies, old keys.
5. **Storage:** Block Public Access, bucket policies, encryption, public snapshots.
6. **Network:** Security Groups, public IPs, subnets, NACLs, flow logs.
7. **Logging and detection:** CloudTrail, GuardDuty, Config, alerts.
8. **Automated scan:** Prowler or ScoutSuite, then validate findings manually (remove false positives).
9. **Rate findings** by likelihood x impact, **report with evidence and fixes**, and help retest.

**My answer:**

---
## Self-assessment
| Questions | Confident (Y/N) | Needs review |
|---|---|---|
| 1-3 | | |
| 4-6 | | |
| 7-9 | | |
| 10-12 | | |

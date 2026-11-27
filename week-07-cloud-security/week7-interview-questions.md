# Week 7: Interview Questions

## 1. What is cloud computing?

**My answer:** Cloud computing means renting computing resources (servers, storage, databases, networking) on demand over the internet instead of buying and running your own hardware. You pay as you go, can scale up or down in minutes, and share the underlying hardware with other customers (multi-tenancy). Key characteristics are on-demand self-service, broad network access, resource pooling, rapid elasticity and measured usage. For security, it shifts the focus from physical perimeters to **APIs and identities**, because everything is created and controlled through API calls. For example, a company can launch 50 web servers for a sale and delete them afterwards, but one leaked access key could let an attacker do the same.

## 2. What is the difference between IaaS, PaaS and SaaS?

**My answer:** The difference is how much the provider manages and how much you manage. **IaaS** gives you raw infrastructure (virtual machines, storage, networks) and you manage the OS, patches, apps and data, for example AWS EC2. **PaaS** gives you a platform to run code, where the provider handles the OS and runtime and you manage your application and data, for example Google App Engine or AWS Elastic Beanstalk. **SaaS** is a finished application you simply use and configure, for example Gmail or Microsoft 365. As you move from IaaS to SaaS you manage less, but you always remain responsible for your data, user access and configuration.

## 3. What is AWS?

**My answer:** AWS (Amazon Web Services) is Amazon's cloud platform, offering over 200 services such as compute (EC2, Lambda), storage (S3), databases (RDS), networking (VPC) and security (IAM). You use it through the web console, the CLI or SDKs and APIs, and they all end up doing the same thing. **Every action is an API call that IAM checks** to decide whether the caller is allowed. For example, running `aws s3 ls` sends a signed API request, and IAM allows or denies it based on the caller's policies. This is why identity and permissions are central to AWS security.

## 4. What is an EC2 instance?

**My answer:** An EC2 instance is a virtual server in AWS, a classic example of IaaS. You create it from an **AMI** (the OS image), choose an **instance type** (CPU and memory size), attach a **key pair** for SSH access, and control traffic with a **Security Group**. AWS secures the hardware and hypervisor, but you must secure the OS, apply patches, harden SSH and manage the software you run. You should also enforce **IMDSv2** on the instance metadata service, because IMDSv1 can be abused through SSRF to steal the instance role's credentials (this is how the 2019 Capital One breach worked). For example, a web server with port 22 open to `0.0.0.0/0` and an unpatched OS is an easy target.

## 5. What is an S3 bucket?

**My answer:** S3 (Simple Storage Service) is AWS's object storage. Data is stored as **objects** (a file plus metadata) inside **buckets**, and each bucket name is globally unique across all of AWS. Access is controlled by IAM policies, bucket policies, ACLs and the Block Public Access setting. It is often misconfigured because it has several overlapping permission mechanisms, and one wrong policy or ACL can expose everything. For example, a bucket used for website assets may be made public for convenience, and later someone uploads database backups into it.

## 6. What is IAM?

**My answer:** IAM (Identity and Access Management) controls **who can do what on which resource** in AWS. It has **users** (people or apps), **groups** (sets of users), **roles** (identities that are assumed temporarily, for example by an EC2 instance or Lambda) and **policies** (JSON documents that allow or deny actions). Best practice is to protect the root account with MFA, enable MFA for users, and prefer roles with **temporary credentials** over long-lived access keys. For example, an EC2 instance that reads from S3 should use an instance role with a read-only S3 policy, not an access key saved in a config file.

## 7. What is the Shared Responsibility Model?

**My answer:** The model splits security duties between AWS and the customer. AWS is responsible for **security *of* the cloud** (data centers, hardware, hypervisor, managed service internals), while the customer is responsible for **security *in* the cloud** (data, IAM, configuration, OS, network rules). The split shifts by service type: with EC2 (IaaS) you patch the OS, with RDS (PaaS-like) AWS patches the database engine, and with SaaS the provider manages almost everything. Some things **always stay with the customer**: your data, identities and access, and how you configure the service. For example, AWS keeps S3 itself secure, but if you make a bucket public, that is your responsibility.

## 8. What is a public S3 bucket?

**My answer:** A public S3 bucket is one whose objects can be read (or even written) by anyone on the internet without authentication. It usually happens through a bucket policy with `"Principal": "*"`, a public ACL, or **Block Public Access** being turned off. The risks include data leaks (customer records, backups, secrets), tampering or malware hosting if writes are allowed, and unexpected costs from abuse. For example, many breaches have come from buckets containing database backups that were reachable by a simple URL. The fix is to enable account-level Block Public Access, remove public policies and ACLs, grant access through IAM roles or pre-signed URLs, enable encryption, and turn on logging.

## 9. What is the principle of least privilege?

**My answer:** Least privilege means giving an identity only the minimum permissions it needs, for only as long as it needs them. This limits the damage if the identity is compromised or misused. In AWS that means allowing specific actions on specific resources instead of `"Action": "*", "Resource": "*"`. For example, a backup job should get `s3:PutObject` on `arn:aws:s3:::backup-bucket/*` only, not full S3 or admin access. Tools that help are **IAM Access Analyzer** (finds unused or overly broad access and generates policies from activity), **permission boundaries**, service control policies, and using temporary role sessions.

## 10. What are cloud security misconfigurations?

**My answer:** Misconfigurations are insecure settings in cloud resources, caused by human error, defaults or complexity rather than by a software flaw. Common examples are public S3 buckets, IAM policies with `*`, Security Groups open to `0.0.0.0/0` on SSH or RDP, access keys exposed in GitHub, unencrypted storage and logging turned off. They are the **top cause of cloud breaches** because the cloud is easy to change quickly and attackers constantly scan for these mistakes. They can be detected with tools like **Prowler**, **AWS Config**, **Security Hub** and ScoutSuite, and prevented with infrastructure-as-code reviews and guardrails. For example, a scan might flag an RDS database that is publicly accessible with no encryption.

## 11. What is the difference between Security Groups and Network ACLs?

**My answer:** A **Security Group** works at the **instance (network interface) level**, is **stateful** (return traffic is automatically allowed), supports **allow rules only**, and evaluates all rules together. A **Network ACL** works at the **subnet level**, is **stateless** (you must allow return traffic explicitly), supports **both allow and deny** rules, and evaluates rules **in numbered order**, stopping at the first match. Security Groups are the main day-to-day control, and NACLs add a coarse extra layer. For example, to block one malicious IP across a whole subnet you would add a NACL deny rule, since a Security Group cannot deny.

## 12. How would you conduct a basic AWS security assessment?

**My answer:** I would start with **written authorization and scope** (accounts, regions, allowed activities, read-only vs active testing, contacts and timing). Then I would get **read-only access** (SecurityAudit and ViewOnlyAccess) and confirm my identity with `aws sts get-caller-identity`, and **inventory** the regions, services and resources. Next I would review **IAM** (root account and MFA, credential report, wildcard policies, privilege-escalation paths, trust policies, old keys), **storage** (Block Public Access, bucket policies, encryption, public snapshots), **network** (Security Groups, public IPs, subnets, NACLs, flow logs) and **logging and detection** (CloudTrail, GuardDuty, Config, alerts). I would run an automated scan such as **Prowler** or ScoutSuite and **validate findings manually** to remove false positives. Finally I would rate each finding by likelihood x impact and write a report with evidence and fixes, then help retest. For example, a finding of "S3 bucket with public read, contains backups" would be rated high, with a screenshot or CLI output as evidence and "enable Block Public Access" as the fix.

---
## Self-assessment
| Questions | Confident (Y/N) | Needs review |
|---|---|---|
| 1-3 | | |
| 4-6 | | |
| 7-9 | | |
| 10-12 | | |

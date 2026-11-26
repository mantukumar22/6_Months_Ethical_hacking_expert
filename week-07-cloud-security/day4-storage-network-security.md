# Day 4: Cloud Storage and Network Security
**Date:** 26 · **Time:** 60 min
**Video:** AWS S3 and VPC security: <paste title/URL>

## Learn (20 min)

## Part A: Storage security (S3)

### Who can access an S3 object?
Access is the combination of several layers. **Any one of them being too open can expose data.**

| Layer | Meaning |
|---|---|
| **IAM policies** | What an identity is allowed to do |
| **Bucket policy** | Resource-based JSON policy on the bucket (can allow other accounts or `Principal: "*"`) |
| **ACLs (access control lists)** | Older per-bucket and per-object permissions. Modern guidance is to **disable ACLs** (Object Ownership: *Bucket owner enforced*) |
| **Block Public Access** | Account-level and bucket-level switches that **override** public policies and ACLs |
| **Pre-signed URLs** | Time-limited links that give temporary access to one object |

### Public vs private buckets
| | Private (default) | Public |
|---|---|---|
| Who can read | Only allowed identities | **Anyone on the internet**, no login needed |
| Risk | Low if IAM is tight | Data leak, scraping, data tampering, big egress bills |
| Legit use | Almost everything | Intentional static website or public assets, ideally via CloudFront |

**Best practice:** turn **Block Public Access ON at the account level** and make exceptions deliberately.

Dangerous bucket policy:
```json
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-bucket/*"
}
```
`Principal: "*"` with no condition means **anyone**. `s3:PutObject`, `s3:DeleteObject` or `s3:*` for everyone is even worse.

### Encryption
| | At rest | In transit |
|---|---|---|
| Protects | Stored data (disks, buckets, snapshots) | Data moving across the network |
| How | **SSE-S3** (AWS-managed keys), **SSE-KMS** (AWS KMS keys, audit trail and control), SSE-C (your own key), client-side encryption | **TLS / HTTPS** |
| Enforce | Default encryption on buckets, **EBS and RDS encryption** | Bucket policy denying requests where `aws:SecureTransport` is `false` |

Week 6 link: AES for the data, asymmetric crypto and certificates for TLS. **AWS KMS** manages the keys: control who can use them and log every use.

### Other storage protections
- **Versioning** (undo overwrites and deletes) and **MFA Delete**
- **Object Lock** (immutable, ransomware defense)
- **Logging:** S3 server access logs and **CloudTrail data events**
- **Macie** to find sensitive data in S3
- Snapshots and AMIs can be accidentally **shared publicly**, so check these too

## Part B: Network security

### VPC security building blocks
- Put databases and internal services in **private subnets**.
- Allow inbound traffic only on the ports you need.
- Use **VPC endpoints** to reach S3 and other services privately.
- Turn on **VPC Flow Logs** to record accepted and rejected traffic (evidence for detection, like Week 2 packet analysis).
- Use **bastion hosts or Session Manager** instead of exposing SSH to the world.

### Security Groups vs Network ACLs

| | **Security Group** | **Network ACL (NACL)** |
|---|---|---|
| Applies to | Instance (network interface) | **Subnet** |
| Stateful? | **Stateful** (replies are allowed automatically) | **Stateless** (must allow return traffic explicitly) |
| Rule types | **Allow only** | **Allow and Deny** |
| Rule evaluation | All rules evaluated together | **Numbered order**, first match wins |
| Default | Deny all inbound, allow all outbound | Default NACL allows all |
| Typical use | Main per-instance control | Extra subnet-level layer, blocking specific IPs |

Traffic must pass **both** the NACL (at the subnet boundary) and the Security Group (at the instance).

### Cloud firewalls
| Service | Role |
|---|---|
| **Security Groups / NACLs** | Basic network filtering (Layer 3 and 4, Week 2) |
| **AWS WAF** | Web application firewall (Layer 7): blocks SQL injection, XSS and bots (Week 5) |
| **AWS Network Firewall** | Managed firewall and intrusion prevention for the VPC |
| **AWS Shield** | DDoS protection |
| **Azure NSG, GCP firewall rules** | Equivalents on other clouds |

## Practice (30 min)

### 1. Check S3 exposure in your own account (read only)
Console: **S3 → Block Public Access settings for this account**. Or CLI (replace placeholders, redact outputs):
```
aws s3api get-public-access-block --bucket <my-bucket>
aws s3api get-bucket-policy --bucket <my-bucket>
aws s3api get-bucket-encryption --bucket <my-bucket>
aws s3api get-bucket-versioning --bucket <my-bucket>
aws s3control get-public-access-block --account-id <my-account-id>
```
"No policy" or "no encryption configuration" errors are results too, so write them down.

### 2. Review Security Groups offline
```
aws ec2 describe-security-groups > sg.json          # your own account only
python3 scripts/sg_checker.py sg.json
python3 scripts/sg_checker.py samples/sg-sample.json   # practice file
```
For each finding, say what an attacker could try from the internet and how to fix it.

### 3. Compare
Fill in the table from memory, then check it.

| Question | Security Group | NACL |
|---|---|---|
| Level | | |
| Stateful? | | |
| Can it deny? | | |

### 4. Fix it on paper
For the bad bucket policy in `samples/bad-bucket-policy.json`, write a corrected version (restrict the principal, add `aws:SecureTransport` or a source condition) and rerun the checker on it.

## Notes (10 min)

**Public bucket risk in two sentences:**
A publicly accessible S3 bucket means anyone on the internet can potentially read (or even write to) its contents without any authentication, which has led to numerous real-world breaches exposing sensitive data like credentials, customer PII, and backups. This often happens accidentally through misconfigured bucket policies or ACLs rather than intentional design, making it one of the most common and damaging cloud misconfigurations.

**Encryption at rest vs in transit:**
Encryption at rest protects data while it's stored on disk (e.g., in an S3 bucket, EBS volume, or database), ensuring that if the physical storage or a backup is accessed without authorization, the data remains unreadable. Encryption in transit protects data while it's moving across a network (e.g., HTTPS/TLS between a client and a server), ensuring that anyone intercepting the traffic can't read or tamper with it — both are needed since each protects against a different point of exposure.

**Security Group vs NACL, one-line difference:**
A Security Group is a stateful firewall attached to individual resources (like an EC2 instance) that only needs rules for one direction since return traffic is automatically allowed, while a Network ACL (NACL) is a stateless firewall attached at the subnet level that requires explicit inbound *and* outbound rules for traffic to flow in both directions.

---

## Self-check

**1. What does S3 Block Public Access do?**
It's an account- or bucket-level setting that overrides any individual bucket policies or ACLs that would otherwise grant public access, acting as a safety net to prevent accidental public exposure. Even if someone misconfigures a bucket policy to allow public access, Block Public Access will enforce the restriction anyway unless it's explicitly disabled, making it one of the most effective guardrails against accidental data leaks.

**2. Why is `Principal: "*"` dangerous?**
`"Principal": "*"` in a resource policy means the policy applies to **anyone** — any AWS account, any anonymous user, with no identity restriction at all. Combined with an `Allow` effect on an action like `s3:GetObject`, this effectively makes the resource public to the entire internet, which is almost never the intent and is one of the most common causes of accidental data exposure.

**3. Which is stateless, a Security Group or a NACL?**
A **NACL (Network ACL)** is stateless — it evaluates every packet independently in both directions, so you must explicitly allow both inbound and outbound traffic even for a single request/response pair. A Security Group, by contrast, is stateful, automatically allowing return traffic for any connection that was permitted.

**4. How do you enforce encryption in transit for S3?**
You add a bucket policy that denies any request where `aws:SecureTransport` is `false`, which blocks all non-HTTPS (plain HTTP) requests to the bucket. This ensures that even if someone attempts to access objects over an unencrypted connection, the request is explicitly denied regardless of their other permissions.

**5. Where should a database live in a VPC?**
A database should live in a **private subnet** with no direct route to an internet gateway, meaning it has no public IP and cannot be reached directly from the internet. Access should only be possible from specific resources within the VPC (like application servers in a separate subnet) via tightly scoped security group rules, often combined with a NAT gateway (for the private subnet's own outbound-only internet access, e.g. for patching) rather than any inbound exposure.

## Mistake I fixed / still confusing
-

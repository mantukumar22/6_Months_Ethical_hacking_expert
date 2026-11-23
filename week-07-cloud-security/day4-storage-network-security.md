# Day 4: Cloud Storage and Network Security
**Date:** ____ · **Time:** 60 min
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
- Public bucket risk in two sentences:
- Encryption at rest vs in transit:
- Security Group vs NACL, one-line difference:

## Self-check
1. What does S3 Block Public Access do?
2. Why is `Principal: "*"` dangerous?
3. Which is stateless, a Security Group or a NACL?
4. How do you enforce encryption in transit for S3?
5. Where should a database live in a VPC?

## Mistake I fixed / still confusing
-

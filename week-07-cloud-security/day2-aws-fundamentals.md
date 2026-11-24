# Day 2: AWS Fundamentals
**Date:** 24 · **Time:** 60 min
**Video:** AWS fundamentals for beginners: <paste title/URL>

## Learn (20 min)

### What is AWS?
**Amazon Web Services (AWS)** is Amazon's cloud platform, with 200+ services. You use it through the **web console**, the **AWS CLI** and **APIs/SDKs** (for example Python's `boto3`). Every action is an **API call**, and every API call is checked against **IAM permissions** and recorded by **CloudTrail**.

### Regions and Availability Zones
| Term | Meaning |
|---|---|
| **Region** | A geographic area (e.g. `us-east-1`, `ap-southeast-1` Singapore). Resources live in a region and data stays there unless you move it |
| **Availability Zone (AZ)** | One or more separate data centers inside a region (e.g. `ap-southeast-1a`). Spreading across AZs gives resilience (the **Availability** in CIA) |
| **Edge location** | CDN and DNS points of presence (CloudFront, Route 53) |

Security note: **resources in regions you don't use are easy to forget.** Attackers who steal credentials often start instances in unused regions. Check all regions during assessments.

### EC2 (virtual servers)
An **EC2 instance** is a virtual machine you rent (IaaS).
| Term | Meaning |
|---|---|
| **AMI** | The image the instance starts from (OS and software) |
| **Instance type** | CPU and memory size (e.g. `t3.micro`) |
| **Key pair** | SSH key: AWS stores the public key, you keep the private `.pem` (Week 6, asymmetric crypto, and `chmod 400`) |
| **EBS** | Block storage disk attached to the instance (can be encrypted) |
| **User data** | A startup script (don't put secrets in it) |
| **Instance profile / IAM role** | Gives the instance AWS permissions without stored keys |
| **IMDS** (instance metadata service) | `169.254.169.254` serves info and **role credentials** to the instance. Prefer **IMDSv2** (session tokens), because IMDSv1 is abused through SSRF |

Your responsibilities (IaaS): OS patches, software, SSH hardening, Security Group rules.

### S3 (object storage)
**S3** stores **objects** (files) in **buckets**.
| Term | Meaning |
|---|---|
| **Bucket** | Container with a **globally unique name** |
| **Object** | A file plus metadata, addressed by a **key** (`reports/2026/file.pdf`) |
| **Storage classes** | Standard, Infrequent Access, Glacier (cost vs access speed) |
| **Versioning** | Keeps old versions, which protects against deletion and overwrite |
| **Access control** | IAM policies, bucket policies, ACLs, Block Public Access (Day 4) |

S3 is the most commonly misconfigured service. **Bucket names are public information** and URLs follow predictable patterns, so a public bucket can be found by anyone.

### VPC (virtual network)
A **VPC (Virtual Private Cloud)** is your own isolated virtual network in AWS. Think back to Week 2: IP ranges, subnets, gateways, routing and ports.

| Component | Meaning |
|---|---|
| **CIDR block** | The VPC's IP range, e.g. `10.0.0.0/16` |
| **Subnet** | A slice of the range inside one AZ |
| **Public subnet** | Has a route to an **Internet Gateway (IGW)**, so instances can be reached from the internet |
| **Private subnet** | No direct internet route. Outbound access through a **NAT Gateway** |
| **Route table** | Rules for where traffic goes |
| **Internet Gateway** | Connects the VPC to the internet |
| **NAT Gateway** | Lets private instances reach out without being reachable in |
| **VPC endpoint** | Private path to AWS services (e.g. S3) without the internet |

Good design: web tier in a public subnet (or behind a load balancer), **databases and internal servers in private subnets**.

### Security Groups
A **Security Group (SG)** is a **virtual firewall attached to an instance** (its network interface).
- Rules are **allow only**. There is no explicit deny.
- **Stateful:** if inbound traffic is allowed, the reply is allowed automatically.
- **Default:** all inbound **denied**, all outbound **allowed**.
- Source can be an IP/CIDR (`203.0.113.10/32`), or **another Security Group**.
- **Red flag:** `0.0.0.0/0` (the whole internet) on SSH (22), RDP (3389) or database ports.

Example rule set for a web server:
| Type | Protocol | Port | Source | OK? |
|---|---|---|---|---|
| HTTPS | TCP | 443 | 0.0.0.0/0 | Yes, public site |
| SSH | TCP | 22 | My IP /32 | Yes, restricted |
| SSH | TCP | 22 | 0.0.0.0/0 | **No** |

### Link to earlier weeks
| Earlier week | Where it shows up in AWS |
|---|---|
| Week 2: ports, ARP, routing, CIDR | VPC, subnets, route tables, Security Groups |
| Week 3: users, permissions | IAM users and policies, `chmod 400` on `.pem` keys |
| Week 5: CIA, attack surface | Public IPs, open ports, public buckets |
| Week 6: keys, TLS, certificates | SSH key pairs, encryption at rest, HTTPS everywhere |

## Practice (30 min)

### 1. Set up a safe AWS account (own account only)
Check the current terms on `aws.amazon.com/free` before signing up, since they change. As of this repo's creation:
- New customers can choose a **Free plan** or a **Paid plan** and receive **$100 in credits**, with up to **$100 more** for completing activities.
- The Free plan runs up to **6 months or until the credits are used up**, whichever comes first, and the account then closes. Previously existing accounts are not eligible. A payment method is still required.
- Joining an AWS Organization converts a Free plan account to a Paid plan.

Then do these **security basics first**:
- [ ] **Enable MFA on the root user.** Don't use root for daily work, and don't create root access keys.
- [ ] Create a **billing budget and alert** (AWS Budgets).
- [ ] Create an **IAM admin identity for daily use** (IAM Identity Center or an IAM user with MFA), then log out of root.
- [ ] Pick one **region** to work in.

### 2. Console tour (15 min)
Open **IAM, S3, EC2, VPC, CloudTrail** and **Billing**. Write one sentence on what each shows.

### 3. Small build, then delete (optional, mind the costs)
- Create an **S3 bucket** with Block Public Access **on**, and upload a text file.
- Launch **one small EC2 instance** if it's covered by your plan. Security Group: SSH from **My IP only**. Require **IMDSv2** in advanced settings. Connect with the `.pem` key, then **terminate the instance**.
- Delete the bucket contents and the bucket.

### 4. AWS CLI (read only)
```
aws --version
aws configure                       # use an IAM user's keys, never root keys
aws sts get-caller-identity         # who am I? (account ID, user ARN)
aws s3 ls
aws ec2 describe-regions --query "Regions[].RegionName" --output text
```
Redact the account ID when you record output.

## Notes (10 min)
- Region vs AZ:
- Public vs private subnet:
- Why IMDSv2 matters:

## Self-check
1. What is an EC2 instance? What is an S3 bucket?
2. What does a Security Group do, and is it stateful?
3. What makes a subnet "public"?
4. Why shouldn't you use the root user for daily work?

## Mistake I fixed / still confusing
-

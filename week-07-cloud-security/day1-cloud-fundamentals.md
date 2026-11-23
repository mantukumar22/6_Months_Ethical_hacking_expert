# Day 1: Cloud Computing Fundamentals
**Date:** ____ · **Time:** 60 min
**Video:** Cloud computing fundamentals: <paste title/URL>

## Learn (20 min)

### What is cloud computing?
**Cloud computing** is renting computing resources (servers, storage, databases, networking, software) over the internet from a provider, on demand, and paying for what you use, instead of buying and running your own hardware.

**Core characteristics:**
| Characteristic | Meaning |
|---|---|
| On-demand self-service | Create resources yourself in minutes (console, CLI, API) |
| Broad network access | Reached over the internet or private links |
| Resource pooling | Providers share hardware between many customers (multi-tenancy) |
| Rapid elasticity | Scale up and down quickly |
| Measured service | Pay per use, usage is metered |

**Why it matters for security:** everything is controlled by **APIs and identities**. One wrong permission or one exposed key can expose a whole environment from anywhere on the internet. There is no "inside the building" to hide behind.

### IaaS, PaaS, SaaS

| Model | Provider gives you | You manage | Example |
|---|---|---|---|
| **IaaS** (Infrastructure as a Service) | Virtual machines, storage, networks | OS, applications, configurations, data, network rules | **AWS EC2**, Azure VMs, Google Compute Engine |
| **PaaS** (Platform as a Service) | A platform to run code | Your application and data | Google App Engine, AWS Elastic Beanstalk, Azure App Service |
| **SaaS** (Software as a Service) | A finished application | Mainly your data, users and settings | Gmail, Microsoft 365, Salesforce |

```
You manage more  <------------------------------------>  Provider manages more
   On-premises        IaaS             PaaS            SaaS
```
Also: **FaaS / serverless** (AWS Lambda): you provide only functions, and the provider runs everything else. **Containers** (Docker, Kubernetes) sit between IaaS and PaaS.

### Deployment models
| Model | Description | Example |
|---|---|---|
| **Public cloud** | Shared infrastructure owned by a provider | AWS, Azure, GCP |
| **Private cloud** | Cloud infrastructure used by one organization (own or hosted) | A company's own OpenStack or VMware cloud |
| **Hybrid cloud** | Public and private connected together | On-premises systems linked to AWS |
| **Multi-cloud** | Using more than one provider | AWS and Azure together |

### The big three providers
| Concept | AWS | Azure | Google Cloud |
|---|---|---|---|
| Virtual server | EC2 | Virtual Machines | Compute Engine |
| Object storage | S3 | Blob Storage | Cloud Storage |
| Identity and access | IAM | Microsoft Entra ID + Azure RBAC | Cloud IAM |
| Virtual network | VPC | Virtual Network (VNet) | VPC |
| Instance firewall | Security Group | Network Security Group (NSG) | VPC firewall rules |
| Serverless functions | Lambda | Functions | Cloud Functions |
| Audit logging | CloudTrail | Activity Log | Cloud Audit Logs |

AWS is the market's largest provider and the focus of this week, and most concepts carry across.

### Shared Responsibility Model
The provider and the customer each secure different parts.

- **The provider is responsible for security OF the cloud:** physical data centers, hardware, networking, the virtualization layer.
- **The customer is responsible for security IN the cloud:** data, identities and access, configuration, OS and applications (depending on the model), network rules, encryption choices.

| Layer | On-premises | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Data and classification | You | You | You | You |
| Identity and access (users, permissions, MFA) | You | You | You | You |
| Applications | You | You | You | Provider |
| Operating system and patching | You | You | Provider | Provider |
| Network controls and firewall rules | You | You | Shared | Provider |
| Virtualization and hardware | You | Provider | Provider | Provider |
| Physical data center | You | Provider | Provider | Provider |

**Key idea:** the customer **always** keeps responsibility for **data and access**. Most cloud breaches come from **customer-side misconfiguration**, not from the provider being hacked.

## Practice (30 min)
### Your first assignment: answer in your own words
1. What is the difference between IaaS, PaaS and SaaS?
   - My answer:
2. What is the Shared Responsibility Model?
   - My answer:
3. If an AWS S3 bucket accidentally allows public access, what security risk does this create?
   - My answer:

### Who is responsible? (Provider / Customer)
| Scenario | Responsible |
|---|---|
| A fire at the data center destroys servers | |
| An EC2 instance runs an unpatched operating system | |
| An S3 bucket is set to public by mistake | |
| An employee's access key is posted on GitHub | |
| A hypervisor vulnerability in the provider's platform | |
| A SaaS provider's staff accidentally delete the service | |
| A user in Microsoft 365 has no MFA | |

### Classify (IaaS / PaaS / SaaS)
| Service | Model |
|---|---|
| AWS EC2 | |
| Gmail | |
| Heroku or Google App Engine | |
| Dropbox | |
| A virtual machine in Azure | |

## Notes (10 min)
- Cloud computing in one sentence:
- Which parts of security always stay my job:

## Self-check
1. Which model gives you the most control, and which the least?
2. Who patches the OS on an EC2 instance? On a SaaS product?
3. Why is "the cloud provider got hacked" usually not the cause of cloud breaches?

## Mistake I fixed / still confusing
-

# Day 2: Firewalls and Network Filtering
**Date:** 28 · **Time:** 60 min
**Video:** Firewall explained: <paste title/URL>

## Learn (20 min)

### What is a firewall?
A **firewall** is a security control that **filters network traffic according to rules**. It can **allow, block or restrict** connections based on addresses, ports, protocols, connection state and sometimes application content. It sits between networks (for example internet and LAN) or on a single host.

### Firewall types
| Type | How it filters | Examples |
|---|---|---|
| **Packet filtering (stateless)** | Checks each packet alone: source/destination IP, port, protocol | Basic router ACLs |
| **Stateful inspection** | Tracks connection state, so replies to allowed outbound traffic are accepted | Most modern firewalls, Windows Firewall, `iptables`/`nftables` with conntrack, AWS Security Groups |
| **Application / proxy** | Understands app-layer protocols and content | Proxy firewalls, web gateways |
| **Next-generation firewall (NGFW)** | Stateful + deep packet inspection, application awareness, IPS, user identity | Palo Alto, Fortinet |
| **Web Application Firewall (WAF)** | Protects web apps from SQL injection, XSS, etc. (Week 5 and 7 link) | AWS WAF, ModSecurity |
| **Host-based** | Runs on one device | Windows Defender Firewall, UFW |
| **Network-based** | Protects a whole network at the edge or between zones | Perimeter and internal firewalls |

### Stateful vs stateless firewalls

| | **Stateless** | **Stateful** |
|---|---|---|
| Decision based on | The single packet only | The packet **and** the connection state |
| Remembers connections? | No | Yes (a state table) |
| Return traffic | Must be allowed by an explicit rule | Allowed automatically if it belongs to an established connection |
| Performance | Very fast, simple | Slightly heavier, smarter |
| Security | Weaker, easier to trick with crafted packets | Stronger |
| Example | AWS **Network ACL**, basic router ACL | AWS **Security Group**, Windows Firewall, UFW |

Example: you browse a website. A **stateful** firewall sees the outbound request, records the connection and lets the reply back in. A **stateless** firewall needs an inbound rule for the reply ports too.

### Inbound vs outbound traffic
| Direction | Meaning | Typical default |
|---|---|---|
| **Inbound (ingress)** | Traffic coming **into** the host or network | **Deny** unless allowed |
| **Outbound (egress)** | Traffic going **out** | Often allow, but restrict in high-security setups (limits malware calling home and data exfiltration) |

### Firewall rules
**Anatomy of a rule:**
```
ACTION   DIRECTION  PROTOCOL  SOURCE            DEST PORT   (LOG?)
allow    in         tcp       203.0.113.10/32   22
allow    in         tcp       any               443
deny     in         any       any               any
```
| Field | Meaning |
|---|---|
| Action | Allow, deny (silently drop) or reject (drop and tell the sender) |
| Direction | Inbound or outbound |
| Protocol | TCP, UDP, ICMP |
| Source / destination | IP, subnet (CIDR), or any |
| Port | One port or range |

**Principles:**
- **Default deny:** block everything, then allow only what is needed.
- **Rule order matters:** many firewalls apply the **first matching rule**, so specific rules go before general ones.
- **Least privilege:** open the narrowest source and port.
- **Log** denied traffic and important allowed traffic.
- **Review regularly:** remove old rules.
- Document each rule's purpose.

| Mistake | Result |
|---|---|
| `allow any any` | No protection |
| SSH or RDP open to the whole internet | Brute-force target |
| Forgetting outbound rules | Malware can freely call out |
| Wrong rule order | Intended rule never matches |
| Enabling a default-deny rule before allowing SSH | **Locked out of a remote machine** |

### Windows Firewall basics (Week 3 link)
- Profiles: **Domain, Private, Public**.
- Check status:
```
netsh advfirewall show allprofiles
```
```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled
Get-NetFirewallRule -Enabled True -Direction Inbound | Select-Object -First 10 DisplayName, Action
```
- GUI: `wf.msc`. Don't turn it off to fix a problem. Add a narrow rule instead.

### Linux firewall basics
Linux filtering happens in the kernel (**netfilter**), managed by tools:
| Tool | Role |
|---|---|
| **UFW** (Uncomplicated Firewall) | Simple front end, common on Ubuntu, available on Kali |
| **iptables** | Classic rule tool (chains: INPUT, OUTPUT, FORWARD) |
| **nftables** (`nft`) | Modern replacement for iptables |
| **firewalld** | Zone-based manager (RHEL, Fedora) |

**UFW essentials (read-only first):**
```
sudo ufw status verbose            # state, default policies, rules
sudo ufw status numbered           # rules with numbers
```
Typical rules, **practise in a VM, not your main system**:
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp                                   # allow SSH FIRST
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
sudo ufw allow 443/tcp
sudo ufw logging on
sudo ufw enable                                         # activate
sudo ufw delete <rule-number>                           # remove a rule
sudo ufw disable
```
**Warning:** if you are connected over SSH, allow SSH **before** you enable UFW with a default-deny policy, or you'll lock yourself out.

**Inspect the underlying rules (read only):**
```
sudo iptables -L -n -v
sudo nft list ruleset
```
Kali often ships with no firewall active, so `Status: inactive` is normal there.

### Cloud link (Week 7)
Security Groups are **stateful** and allow-only. Network ACLs are **stateless**, with allow and deny in numbered order. The principles here are identical.

## Practice (30 min)

### 1. Check firewall status (Lab 2)
```
sudo ufw status verbose
```
(If UFW isn't installed: `sudo apt install ufw`. If it's inactive, just record that. Don't change anything on your main system without understanding it.)

On Windows: `netsh advfirewall show allprofiles`.

| Item | Result |
|---|---|
| UFW status (active/inactive) | |
| Default incoming policy | |
| Default outgoing policy | |
| Rules listed | |
| Windows Firewall profiles on/off | |

### 2. Design a ruleset on paper
A small office has a web server (HTTPS public), an admin who needs SSH from one fixed IP, and a database that only the web server may reach (port 5432). Write the firewall rules (allow rules + default deny) for the web server and the database.

# Firewall ruleset design (on paper)

## Assumptions

- Web server = `WEB_IP` (e.g. 10.0.1.10), database = `DB_IP` (e.g. 10.0.1.20), admin's fixed public IP = `ADMIN_IP` (e.g. 203.0.113.5).
- The firewalls are **stateful** (like UFW and Security Groups), so replies to allowed connections are automatically allowed.
- Principle: **default deny incoming**, then allow only what is needed (least privilege).

## Web server

| # | Action | Direction | Protocol | Source | Port | Purpose |
|---|---|---|---|---|---|---|
| 1 | ALLOW | Inbound | TCP | Any (0.0.0.0/0) | 443 | Public HTTPS |
| 2 | ALLOW | Inbound | TCP | `ADMIN_IP`/32 | 22 | Admin SSH from one fixed IP only |
| 3 | ALLOW | Inbound | TCP | Any (0.0.0.0/0) | 80 | *Optional:* HTTP, only to redirect to HTTPS |
| 4 | ALLOW | Outbound | TCP | `DB_IP`/32 (destination) | 5432 | Web app queries the database |
| 5 | ALLOW | Outbound | TCP/UDP | DNS resolver (destination) | 53 | Name resolution |
| 6 | ALLOW | Outbound | TCP | Any (destination) | 80, 443 | OS updates and external APIs (tighten if possible) |
| 7 | **DENY** | Inbound | All | Any | Any | **Default deny incoming** (everything else) |

## Database server

| # | Action | Direction | Protocol | Source | Port | Purpose |
|---|---|---|---|---|---|---|
| 1 | ALLOW | Inbound | TCP | `WEB_IP`/32 | 5432 | Only the web server may reach PostgreSQL |
| 2 | ALLOW | Inbound | TCP | `ADMIN_IP`/32 | 22 | Admin SSH (or remove and use the web server as a jump host) |
| 3 | ALLOW | Outbound | TCP/UDP | DNS resolver (destination) | 53 | Name resolution |
| 4 | ALLOW | Outbound | TCP | Update mirrors (destination) | 80, 443 | OS patches (or use a proxy/mirror) |
| 5 | **DENY** | Inbound | All | Any | Any | **Default deny incoming** (everything else, including the internet) |

## Why these rules

- **Port 5432 is never open to "Any".** A database exposed to the internet is a classic breach cause. Restricting the source to the web server's IP means an attacker must compromise the web server first.
- **SSH is limited to one IP** (`/32`), which removes most brute-force and scanning noise.
- **Default deny** means a forgotten service stays unreachable instead of accidentally exposed.
- **The database has no inbound rule from the internet** at all.
- **Return traffic** needs no rule because of stateful tracking.


### 3. Optional: try UFW in a VM
In a VM you own, set UFW to default deny incoming, allow SSH and one web port, then check with `sudo ufw status verbose`. Loopback (`127.0.0.1`) traffic is normally allowed by UFW, so to see the firewall's effect, test from **another machine you own** (for example from your host to the VM). Disable it afterwards with `sudo ufw disable`.

### 4. Explain with an example
Describe in your own words how a stateful firewall handles a reply packet.

## Notes (10 min)

**Firewall in one sentence:**
A firewall is a security control that monitors and filters network traffic based on a defined set of rules, allowing or blocking connections based on criteria like source/destination IP, port, and protocol.

**Stateful vs stateless, one-line difference:**
A stateful firewall tracks the state of active connections and automatically allows return traffic, while a stateless firewall evaluates every packet independently with no memory of prior traffic, requiring explicit rules for both directions.

**Why "default deny"?**
Default deny ensures that any traffic not explicitly permitted is blocked by default, so a missing or forgotten rule results in a safe failure (access denied) rather than accidentally leaving a port open or exposing a service to unintended traffic.

---

## Self-check

**1. What does a stateful firewall remember that a stateless one doesn't?**
A stateful firewall remembers the **connection state** — it tracks active sessions (e.g., an outbound request that was allowed) and automatically permits the corresponding return traffic without needing a separate explicit rule. A stateless firewall has no memory of previous packets, so it must evaluate every single packet against the rule set independently, requiring matching inbound and outbound rules to allow two-way communication.

**2. What is the difference between inbound and outbound rules?**
Inbound rules control traffic **coming into** a resource (e.g., allowing SSH connections from a specific IP to reach a server), while outbound rules control traffic **leaving** a resource (e.g., allowing a server to make outbound HTTPS requests to update software). Both directions need to be considered separately, especially in stateless firewalls like NACLs, where allowing inbound traffic doesn't automatically allow the matching outbound response.

**3. Why does rule order matter?**
In many firewall implementations (like NACLs), rules are evaluated **in order, from lowest number to highest**, and the first matching rule is applied — any rules after a match are ignored. This means a broad "allow" rule placed before a more specific "deny" rule can accidentally override the intended restriction, so rules must be carefully ordered from most specific to least specific (or vice versa, depending on the system's logic) to achieve the intended security outcome.

**4. What's the risk of enabling a default-deny policy over SSH before allowing SSH?**
If you enable default-deny before adding an explicit rule to allow your own SSH access, you can **immediately lock yourself out** of the server, since the default-deny rule blocks all traffic — including your own legitimate connection — until the allow rule is added. This is a common and costly real-world mistake, especially on remote/cloud servers with no physical console access, potentially requiring a provider's emergency console or a full server rebuild to regain access.

**5. Is an AWS Security Group stateful or stateless?**
An AWS Security Group is **stateful**. If you allow inbound traffic on a port, the corresponding outbound return traffic is automatically permitted without needing a matching outbound rule, and vice versa for traffic initiated from within the instance.

## Mistake I fixed / still confusing
-

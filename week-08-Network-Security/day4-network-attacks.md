# Day 4: Network Attacks and Defenses
**Date:** ____ · **Time:** 60 min
**Video:** Common network attacks: <paste title/URL>

> **Scope:** this day is **conceptual**. Learn how the attacks work, what they harm, and how to **detect and prevent** them. Don't run spoofing, MitM or DoS tools against any network except an isolated lab you fully own. Doing so on real networks is illegal.

## Learn (20 min)

### Why these attacks exist
Many core protocols were designed when networks were trusted. **ARP, DNS and DHCP have no built-in authentication**, so a device on the same network can often lie to others. Encryption (TLS, SSH) and network controls are what limit the damage.

### 1. ARP spoofing (ARP poisoning)
**Recap (Week 2):** ARP maps an IPv4 address to a MAC address on the local network. Hosts accept ARP replies, even ones they didn't ask for, and cache them.

**How it works (concept):** an attacker on the **same LAN** sends **forged ARP replies**, claiming "the gateway's IP is at *my* MAC". Victims update their ARP cache, send their traffic to the attacker, and the attacker can read it, change it, or drop it.
```
Normal:   Victim ----> Gateway ----> Internet
Spoofed:  Victim ----> Attacker ----> Gateway ----> Internet
```
- **Needs:** local network access (same broadcast domain). It doesn't work across routers.
- **Impact:** eavesdropping, session hijacking, MitM, DoS (traffic dropped). Mainly Confidentiality and Integrity.

**Detection**
- Run `arp -a` / `ip neigh` regularly: the gateway's MAC suddenly changing, or **two IPs sharing one MAC**, is a warning sign. (Use `scripts/arp_table_check.py`.)
- Wireshark filter `arp`: look for floods of unsolicited replies (gratuitous ARP) and warnings like "duplicate IP address detected".
- Tools: ARP monitoring (arpwatch), IDS rules.

**Defense**
- **Dynamic ARP Inspection (DAI)** with DHCP snooping on managed switches
- **Port security** and network segmentation (VLANs)
- Static ARP entries for critical hosts such as the gateway
- **Encryption everywhere** (HTTPS, SSH, VPN) so intercepted traffic is unreadable
- Don't use untrusted public Wi-Fi without a VPN

### 2. DNS spoofing (DNS cache poisoning)
**Recap (Week 2):** DNS turns names into IPs, and plain DNS answers aren't authenticated.

**How it works (concept):** an attacker gets a **forged DNS answer** accepted, so a victim's resolver or device maps a real domain (like a bank) to the **attacker's IP**. The victim types the right name but lands on a fake site. This can happen by poisoning a resolver's cache, by intercepting DNS on the local network (often combined with ARP spoofing), by tampering with a router's DNS settings, or via malware editing the `hosts` file.

- **Impact:** phishing at scale, credential theft, malware delivery. Confidentiality and Integrity.

**Detection**
- Same domain resolving to **different or unexpected IPs** (`nslookup`/`dig` against different resolvers)
- **Certificate warnings** (the fake site can't present a valid certificate for the real domain)
- Unexpected changes in router DNS settings or the `hosts` file
- DNS monitoring and logs, Wireshark filter `dns`

**Defense**
- **HTTPS with certificate validation** (and HSTS) so a fake server is detected
- **DNSSEC** (proves DNS answers are authentic), **DoT / DoH** (encrypts DNS)
- Randomized source ports and query IDs, patched resolvers
- Secure router admin access and firmware, trusted resolvers only

### 3. Man-in-the-Middle (MitM)
**What it is:** an attacker **secretly positions between two parties**, relaying and possibly altering their communication, while both believe they are talking directly.

**Common ways to get in the middle (concept):** ARP spoofing on a LAN, DNS spoofing, **rogue / evil-twin Wi-Fi access points**, a compromised router, rogue DHCP server, malicious proxies, SSL stripping (downgrading HTTPS to HTTP).

**Impact:** stolen credentials and sessions, altered data, injected content.

**Detection:** certificate warnings, unexpected certificate issuers, duplicate MACs, unknown access points, unusual latency or routes (`tracert`/`traceroute`).

**Defense**
- **TLS/HTTPS with proper certificate validation**, HSTS, certificate pinning where used
- **Never click through certificate warnings**
- Use SSH and VPNs, mutual authentication
- Secure Wi-Fi (WPA3/WPA2-Enterprise), network access control
- The same switch features as for ARP (DAI, DHCP snooping, port security)

### 4. DoS and DDoS
**DoS** (Denial of Service): making a service unavailable by overwhelming or crashing it. **DDoS:** the same, from **many sources** (often a botnet). Target: **Availability**.

| Type | Idea | Example |
|---|---|---|
| **Volumetric** | Flood the target with huge traffic | UDP floods, **reflection/amplification** (spoofed requests to DNS/NTP servers) |
| **Protocol** | Exhaust connection tables or devices | **SYN flood** (Day 1 and Week 2: the TCP handshake) |
| **Application layer** | Many expensive requests | HTTP request floods |

**Detection:** sudden traffic spikes, many half-open connections (`ss -s`, `netstat`), a single IP or many IPs sending many requests, service slowness, monitoring graphs and IDS alerts.

**Defense**
- **Rate limiting** and connection limits, SYN cookies
- **DDoS protection services** (CDN, scrubbing, cloud shields like AWS Shield)
- **Anti-spoofing filters** (ingress/egress filtering), disable open resolvers and unneeded UDP services
- Load balancing, redundancy and autoscaling
- An incident plan and an upstream ISP contact

### Summary table
| Attack | Layer | Needs | Main CIA impact | Best defenses |
|---|---|---|---|---|
| ARP spoofing | 2 | Same LAN | C, I (A) | DAI, port security, segmentation, encryption |
| DNS spoofing | 7 (DNS) | Resolver or LAN position | C, I | DNSSEC, DoH/DoT, HTTPS and HSTS |
| MitM | Various | A position in the path | C, I | TLS, VPN, secure Wi-Fi, validation |
| DoS / DDoS | 3 to 7 | Resources or a botnet | A | Rate limiting, CDN/scrubbing, redundancy |

## Practice (30 min)
Everything here **observes**. Nothing attacks.

### 1. Baseline your ARP table
```
ip neigh            # Linux   (or: arp -a)
arp -a              # Windows
```
Note the gateway IP and its MAC (redact in your notes). Run it again later and compare. Then test the checker:
```
python3 scripts/arp_table_check.py samples/arp-sample.txt
```
It flags **two IPs with the same MAC**. Explain one innocent reason and one malicious reason for that.

### 2. Watch normal ARP in Wireshark
Capture on your interface with the filter `arp`. Run `ping <gateway>` after clearing the entry if you can (`sudo ip neigh flush all`, which is safe on your own machine). Find a request ("Who has...?") and a reply ("... is at ...").

### 3. Compare DNS answers
```
nslookup example.com
nslookup example.com 1.1.1.1
nslookup example.com 8.8.8.8
```
Do they agree? (Large sites can legitimately return different IPs, so differences alone don't prove spoofing.)

### 4. Check SYN-state connections (defender view)
```
ss -s
ss -tan state syn-recv
```
What would a SYN flood look like here?

### 5. Write defenses
| Attack | Two preventive controls | One way to detect |
|---|---|---|
| ARP spoofing | | |
| DNS spoofing | | |
| MitM | | |
| DDoS | | |

## Notes (10 min)
- ARP spoofing in my own words:
- Why HTTPS limits the damage of MitM:
- DoS vs DDoS:

## Self-check
1. Why does ARP spoofing only work on the same local network?
2. What does DNSSEC protect, and what doesn't it protect? (Hint: authenticity, not privacy)
3. Name two ways an attacker can become a man in the middle.
4. Which CIA principle does DDoS attack?
5. Why should you never click through a certificate warning?

## Mistake I fixed / still confusing
-

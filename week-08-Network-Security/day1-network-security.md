# Day 1: Network Security Fundamentals
**Date:** 27 · **Time:** 60 min
**Video:** Network security basics: <paste title/URL>

**Today's plan:** learn network security basics (20 min) · ports, protocols and threats (15 min) · practise commands in Kali (15 min) · notes and questions (10 min)

## Learn (20 min)

### What is network security?
**Network security** is the set of policies, tools and practices that protect a network and the data crossing it from unauthorized access, misuse, modification and disruption. It covers devices (routers, switches, servers), connections (cables, Wi-Fi, VPNs), traffic and the people who use them.

### Network security goals
| Goal | Meaning | Network example |
|---|---|---|
| **Confidentiality** | Only the right people can read the data | TLS, VPN, encrypted Wi-Fi |
| **Integrity** | Data isn't altered in transit | TLS integrity checks, signatures |
| **Availability** | The network and services stay reachable | Redundancy, DDoS protection |
| **Authentication** | Know who or what is connecting | Passwords, MFA, certificates |
| **Authorization / access control** | Allow only what's permitted | Firewall rules, ACLs, segmentation |
| **Accountability** | Record who did what | Logs, monitoring |

(Weeks 5 and 6 link: CIA Triad, authentication and authorization.)

### Defense in depth
Use **layers** of controls so one failure doesn't mean compromise:
```
Policies and training
  Perimeter firewall / VPN
    Network segmentation (VLANs, subnets)
      Host firewall and hardening
        Encryption (TLS, SSH)
          Monitoring (IDS/IPS, logs)
            Backups and incident response
```

### Network segmentation (key idea)
Splitting a network into zones (for example guest Wi-Fi, staff, servers, IoT, management) with controlled traffic between them. **Why:** an attacker who compromises one device can't freely reach everything else, which limits lateral movement and reduces the blast radius.

### TCP vs UDP: security implications

| | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (three-way handshake) | Connectionless |
| Reliability | Guaranteed, ordered delivery | Best effort |
| Speed / overhead | Slower | Faster, lighter |
| Typical use | Web, SSH, email, file transfer | DNS, VoIP, streaming, gaming, NTP, DHCP |

**Security implications:**
- **TCP:** the handshake lets firewalls track connections (stateful filtering). Attackers abuse it with **SYN floods** (many half-open connections exhaust the server). Open TCP ports are easy to probe, because a reply (SYN-ACK, or RST for closed) reveals the state.
- **UDP:** no handshake, so the **source address is easy to spoof**. That enables **reflection and amplification** DDoS attacks (a small spoofed request to a DNS or NTP server produces a large reply sent to the victim). It's also harder to filter statefully and to scan, because "no reply" is ambiguous (open, or filtered).
- Both need rate limiting, and both can be encrypted at higher layers (TLS over TCP, DTLS or QUIC over UDP).

### Common ports and protocols

| Port | Protocol | Transport | Secure? | Secure alternative |
|---|---|---|---|---|
| 20/21 | FTP | TCP | **No** (clear text) | SFTP (22), FTPS |
| 22 | SSH | TCP | Yes (encrypted) | |
| 23 | Telnet | TCP | **No** (clear text) | SSH |
| 25 | SMTP | TCP | Often unencrypted | SMTP over TLS (587/465) |
| 53 | DNS | UDP/TCP | Unauthenticated by default | DNSSEC, DoT, DoH |
| 67/68 | DHCP | UDP | Trusts any server on the LAN | DHCP snooping |
| 69 | TFTP | UDP | **No** | SFTP |
| 80 | HTTP | TCP | **No** | HTTPS |
| 110 / 143 | POP3 / IMAP | TCP | **No** | 995 / 993 (TLS) |
| 123 | NTP | UDP | Abusable for amplification | Restrict and update |
| 137-139, 445 | NetBIOS / SMB | TCP/UDP | Frequent attack target | Restrict, patch, never expose |
| 161 | SNMP | UDP | v1/v2c use clear-text community strings | SNMPv3 |
| 389 | LDAP | TCP | Clear text | LDAPS (636) |
| 443 | HTTPS | TCP | Yes (TLS) | |
| 1433 / 3306 / 5432 | MS SQL / MySQL / PostgreSQL | TCP | Should not be public | Private network + TLS |
| 3389 | RDP | TCP | Common brute-force target | VPN + MFA |

(Link: Week 2 ports and Week 7 Security Group rules.)

### Network attack surface
The **attack surface** is every place an attacker can try to reach or abuse the network: open ports and listening services, exposed management interfaces, Wi-Fi, VPN gateways, remote access (SSH, RDP), cloud-exposed resources, misconfigured devices with default credentials, unpatched systems, and users.

To **reduce it:** close unused ports, remove unneeded services, segment, use least privilege, patch, disable defaults, and monitor.

Link (Week 5): attack surface vs attack vector. The surface is *where* you can be attacked, the vector is *how*.

### Types of threats on a network
| Category | Examples |
|---|---|
| Eavesdropping / sniffing | Reading clear-text traffic (HTTP, FTP, Telnet) |
| Spoofing | ARP, DNS, IP and MAC spoofing |
| Interception / modification | Man-in-the-Middle |
| Denial of service | SYN floods, volumetric DDoS |
| Unauthorized access | Brute force, weak credentials, exposed services |
| Malware and lateral movement | Spreading across a flat network |
| Rogue devices | Unknown access points or devices on the LAN |

## Practice (30 min): commands in Kali

### Lab 1: Check listening ports
```
ss -tulnp
```
| Flag | Meaning |
|---|---|
| `-t` | TCP |
| `-u` | UDP |
| `-l` | Listening sockets |
| `-n` | Numeric addresses and ports (no name lookups) |
| `-p` | Show the associated process (where permitted; use `sudo` to see more) |

Read the output (Week 2 and Week 3 link):
- `0.0.0.0:PORT` or `[::]:PORT`: listens on **all** interfaces (reachable from the network)
- `127.0.0.1:PORT`: listens on **loopback only**
- The process column shows which program owns the port

Offline practice with the sample file, then your own machine:
```
python3 scripts/ss_report.py samples/ss-sample.txt
python3 scripts/ss_report.py --run
```

### Record
| Local address:port | Proto | Process | Exposure (all / local only) | Needed? |
|---|---|---|---|---|
| | | | | |

Questions:
1. Which ports are reachable from the network?
2. Are any services listening that you don't recognize or need?
3. Any insecure protocols (FTP, Telnet, TFTP)?

### Also
- `ip addr` and `ip route` (your interfaces and gateway)
- `sudo ufw status verbose` (read only. Day 2 covers firewalls)

# Network Security Assignment

## Today's assignment: answer without searching first

### 1. What is network security?

**My answer:** Network security is the policies, tools and practices that protect a network and the data crossing it from unauthorized access, misuse, modification and disruption. It covers devices, connections and the people who use them.

*(Your answer was already good. I only fixed spelling: "Netwoork", "polices", "accses", "conections". It could also name the three goals, **confidentiality, integrity and availability (CIA)**, and give an example such as a firewall blocking unwanted traffic.)*

### 2. What is the difference between TCP and UDP?

**My answer:** Both are transport-layer protocols, but they trade reliability for speed differently. **TCP** is connection-oriented: it does a three-way handshake (SYN, SYN-ACK, ACK), numbers packets, retransmits lost ones and keeps them in order. It is reliable but has more overhead, and it is used for web (HTTP/HTTPS), SSH and email. **UDP** is connectionless: it just sends packets with no handshake, no delivery guarantee and no ordering. It is faster and lighter, and it is used for DNS, video calls, streaming and gaming. For example, a file download uses TCP because every byte must arrive, while a live video call uses UDP because a late packet is worse than a lost one.

### 3. What is the purpose of a firewall?

**My answer:** A firewall controls which network traffic is allowed or blocked, based on rules such as source and destination IP, port and protocol. Its purpose is to reduce the attack surface by allowing only the traffic that is needed and blocking the rest, usually with a default-deny policy for incoming traffic. Firewalls can be network-based (at the perimeter) or host-based (like `ufw` on Linux). For example, a server's firewall may allow only port 443 from anywhere and port 22 from the admin's IP. Next-generation firewalls also inspect applications, but a firewall alone doesn't stop attacks that come through allowed traffic.

### 4. What is the difference between IDS and IPS?

**My answer:** An **IDS** (Intrusion Detection System) **monitors and alerts**: it watches traffic or logs for suspicious patterns and tells you, but doesn't stop anything. An **IPS** (Intrusion Prevention System) sits **inline** in the traffic path and can **block or drop** malicious traffic automatically. IDS is passive and has no impact on traffic flow, while IPS is active, so a false positive can block legitimate traffic. For example, Snort or Suricata can run in either mode: as an IDS it logs a port scan, as an IPS it drops the scanner's packets.

### 5. Why is HTTPS more secure than HTTP?

**My answer:** HTTP sends everything in plain text, so anyone on the path (Wi-Fi, ISP, attacker) can read or modify it. HTTPS is HTTP over **TLS**, which gives three things: **confidentiality** (traffic is encrypted), **integrity** (tampering is detected) and **authentication** (the server's certificate, signed by a trusted CA, proves it is the real site). For example, on public Wi-Fi, a login over HTTP exposes the password to a sniffer, but over HTTPS the attacker sees only encrypted data. HTTPS protects data in transit only. It does not make a website itself safe from phishing or vulnerabilities.

## Notes (10 min)

- **Network security in one sentence:** Network security is the set of policies, tools and practices that protect a network and its data from unauthorized access, misuse, modification and disruption.
- **Two TCP risks and two UDP risks:**
  - **TCP:** (1) **SYN flood**, a DoS attack that fills the server's half-open connection table; (2) **session hijacking / TCP reset injection**, where an attacker predicts sequence numbers to take over or kill a connection. (Port scanning with SYN scans is another.)
  - **UDP:** (1) **IP spoofing and amplification/reflection DDoS** (DNS, NTP, memcached), because there is no handshake to verify the source; (2) **UDP flood**, which overwhelms a host with packets it must process, and also easy-to-miss scanning because closed ports give no reply.
- **Three services on my machine that listen on all interfaces:** Run this to find your own answer:

  ```bash
  sudo ss -tulpn | grep -E '0.0.0.0|\[::\]'
  ```

  Pick three lines and write them down, for example:
  - `sshd` on `0.0.0.0:22` (if SSH is enabled)
  - `cupsd` or `avahi-daemon` (printing / mDNS, common on desktops)
  - `systemd-resolved` is usually on `127.0.0.53` only, so it does *not* count

  On a default Kali VM you may see few or none, because services are off until started. If so, start one (`sudo systemctl start ssh`), re-run the command, and note it. Then stop it again.

## Self-check

### 1. Why is UDP easier to spoof than TCP?

UDP has **no handshake and no connection state**. A sender can put any source IP in a single packet and the receiver processes it, so the attacker never needs to see a reply. To spoof TCP you must complete the three-way handshake, which requires receiving the server's SYN-ACK (sent to the fake address) and guessing the correct sequence numbers. That is why UDP services are favored for **reflection and amplification attacks**.

### 2. What does `0.0.0.0:22` mean in `ss` output?

A service (here SSH on port 22) is **listening on all IPv4 interfaces**, so it accepts connections on every IP the machine has: Wi-Fi, Ethernet, VPN and so on. Compare:

| Output | Meaning |
|---|---|
| `0.0.0.0:22` | Reachable from any IPv4 network the host is on |
| `[::]:22` | Same, for IPv6 |
| `127.0.0.1:22` | Reachable only from the machine itself |
| `192.168.1.5:22` | Only on that one interface |

It matters for security because every service listening on all interfaces is **exposed attack surface**. If it doesn't need to be reachable remotely, bind it to `127.0.0.1` or block it with a firewall.

### 3. Why is network segmentation useful?

Segmentation splits a network into separate zones (VLANs, subnets, DMZ) with firewall rules between them.

- **Limits lateral movement:** if one device is compromised, the attacker can't freely reach everything else.
- **Reduces attack surface and blast radius:** the guest Wi-Fi, IoT devices, servers and workstations are isolated from one another.
- **Protects sensitive systems:** databases or payment systems can be reachable only from specific hosts.
- **Easier monitoring and compliance:** traffic between zones is controlled and logged (e.g. PCI DSS).

Example: a smart camera on an IoT VLAN is hacked, but it cannot reach the file server on the server VLAN. In AWS, this is the same idea as separate subnets with Security Groups and NACLs.

## Mistake I fixed / still confusing
-

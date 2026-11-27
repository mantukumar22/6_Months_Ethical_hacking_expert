# Day 1: Network Security Fundamentals
**Date:** ____ · **Time:** 60 min
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

## Today's assignment: answer without searching first
1. What is network security?
   - My answer:
2. What is the difference between TCP and UDP?
   - My answer:
3. What is the purpose of a firewall?
   - My answer:
4. What is the difference between IDS and IPS?
   - My answer:
5. Why is HTTPS more secure than HTTP?
   - My answer:

## Notes (10 min)
- Network security in one sentence:
- Two TCP risks and two UDP risks:
- Three services on my machine that listen on all interfaces:

## Self-check
1. Why is UDP easier to spoof than TCP?
2. What does `0.0.0.0:22` mean in `ss` output?
3. Why is network segmentation useful?

## Mistake I fixed / still confusing
-

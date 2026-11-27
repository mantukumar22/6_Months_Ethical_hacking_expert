# Network Security Checklist (Day 7)
A basic review checklist for a small network or a single host. Use it only on **my own** systems or an authorized environment.

Legend: ✅ pass · ❌ fail · ➖ not applicable · ❓ not checked

## 1. Attack surface and services
| Check | Result | Notes |
|---|---|---|
| Listening ports reviewed (`ss -tulnp`) | | |
| Unneeded services stopped or disabled | | |
| No insecure protocols exposed (Telnet, FTP, TFTP, HTTP only, SNMPv1/2c) | | |
| Admin interfaces (SSH, RDP, router) not exposed to the internet | | |
| Default credentials changed | | |

## 2. Firewall and segmentation
| Check | Result | Notes |
|---|---|---|
| Host firewall enabled (UFW / Windows Firewall) | | |
| Default deny on inbound | | |
| Rules are least-privilege and documented | | |
| Egress (outbound) filtering considered | | |
| Network segmented (guest, staff, servers, IoT) | | |

## 3. Encryption and protocols
| Check | Result | Notes |
|---|---|---|
| HTTPS with valid certificates, TLS 1.2 or 1.3 | | |
| SSH uses keys, root login disabled | | |
| VPN with MFA for remote access | | |
| Wi-Fi uses WPA3 or WPA2-AES, strong passphrase | | |
| DNS: trusted resolvers, DoH/DoT or DNSSEC considered | | |

## 4. Monitoring and detection
| Check | Result | Notes |
|---|---|---|
| Logs enabled (auth, firewall, DNS) | | |
| Failed-login monitoring in place (`failed_logins.py` or fail2ban) | | |
| IDS/IPS or equivalent monitoring | | |
| ARP table and gateway MAC baseline recorded | | |
| Clocks synchronized (NTP) | | |

## 5. Maintenance and response
| Check | Result | Notes |
|---|---|---|
| Systems and firmware patched | | |
| Backups tested | | |
| Incident response steps known | | |
| Regular authorized scans or reviews scheduled | | |

## Findings log (document findings)
| # | Finding | Area | Severity | Evidence | Fix | Status |
|---|---|---|---|---|---|---|
| 1 | | | | `screenshots/` | | |
| 2 | | | | | | |
| 3 | | | | | | |

## Revision (from memory)
| Concept | One-line definition |
|---|---|
| Network security | |
| Stateful vs stateless firewall | |
| IDS vs IPS | |
| Signature vs anomaly detection | |
| ARP spoofing | |
| DNS spoofing | |
| MitM | |
| DoS vs DDoS | |
| VPN | |
| TLS / HTTPS | |
| Network segmentation | |
| Port states: open, closed, filtered | |

## GitHub upload checklist
- [ ] All files named in the plan committed
- [ ] `screenshots/` redacted (IPs, MACs, hostnames, usernames)
- [ ] **No `.pcap` or raw logs committed** (`git status`)
- [ ] Lab reports follow the format: objective, tool, commands, screenshots, observations, implications, learning

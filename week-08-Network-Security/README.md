# Week 8: Network Security

**7 days · 1 hour/day**

Goal: learn how networks are secured, how network attacks work at a **conceptual** level, how to monitor network traffic, and how to identify security weaknesses during **authorized** assessments. This week builds on networking fundamentals (Week 2), Linux commands (Week 3), Python sockets (Week 4), cryptography (Week 6) and cloud security (Week 7).

> **Safety and legal rules**
> - Capture packets **only on my own machine and network**. Captures hold private data (domains, cookies, sometimes credentials), so `.pcap`/`.pcapng` files are git-ignored and never committed.
> - Scan **only systems I own or have written authorization to test**: `127.0.0.1`, my own VM or my own lab. Never scan public IPs, other people's networks or my college, office or ISP.
> - Attacks (ARP spoofing, DNS spoofing, MitM, DoS) are studied **conceptually**, with detection and defense. Don't run them against any network except an isolated lab I fully own.
> - Don't change firewall rules on my main machine without understanding the effect (lockouts happen). Practise changes in a VM.
> - Redact public IPs, MAC addresses, hostnames and usernames in screenshots and reports.

## Roadmap

| Day | Topic | File |
|---|---|---|
| 1 | Network Security Fundamentals | [day1-network-security.md](day1-network-security.md) |
| 2 | Firewalls and Network Filtering | [day2-firewalls.md](day2-firewalls.md) |
| 3 | IDS, IPS and Network Monitoring | [day3-ids-ips.md](day3-ids-ips.md) |
| 4 | Network Attacks and Defenses | [day4-network-attacks.md](day4-network-attacks.md) |
| 5 | Network Security Protocols | [day5-secure-protocols.md](day5-secure-protocols.md) |
| 6 | Practical Network Security Lab | [day6-network-security-lab.md](day6-network-security-lab.md) |
| 7 | Revision and Assessment | [week8-interview-questions.md](week8-interview-questions.md), [network-security-checklist.md](network-security-checklist.md) |

Each day: **20 min** learn → **30 min** practice → **10 min** notes.

## Tools to practise
| Tool | Purpose |
|---|---|
| Wireshark | Packet capture and analysis |
| Nmap | Network discovery and security auditing (authorized targets only) |
| UFW (and `iptables`/`nft`) | Linux firewall management |
| Snort / Suricata | Network intrusion detection and prevention |
| `ss` | Listening sockets and connections on Linux |

## Offline practice scripts (standard library only)
```
python3 scripts/ss_report.py samples/ss-sample.txt            # classify listening ports
python3 scripts/ss_report.py --run                            # run `ss -tulnp` on this machine
python3 scripts/failed_logins.py samples/auth.log.sample      # spot SSH brute-force patterns
python3 scripts/arp_table_check.py samples/arp-sample.txt     # spot duplicate MACs in an ARP table
```
They read files (or local `ss` output) and never contact the network.

## Lab report format (from the plan)
Each lab records: **Objective · Tool used · Commands executed · Screenshots · Observations · Security implications · What I learned**. Use [lab-report-template.md](lab-report-template.md).

## Folder layout
```
week8/
├── README.md
├── checklist.md
├── lab-report-template.md
├── day1-network-security.md
├── day2-firewalls.md
├── day3-ids-ips.md
├── day4-network-attacks.md
├── day5-secure-protocols.md
├── day6-network-security-lab.md
├── week8-interview-questions.md
├── network-security-checklist.md    Day 7 checklist and findings log
├── screenshots/                     lab screenshots (redacted)
├── scripts/                         ss, auth-log and ARP checkers
├── samples/                         sample inputs for the scripts
└── resources/                       links and command cheat sheet
```
The files named in the plan are included. The rest are extras. Drop the whole `week8/` folder into the cybersecurity learning repo.

## Progress
See [checklist.md](checklist.md). **0/7** done.

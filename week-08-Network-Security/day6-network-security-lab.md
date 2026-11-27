# Day 6: Practical Network Security Lab
**Date:** ____ · **Time:** 60 min
**Video:** Wireshark beginner tutorial: <paste title/URL>

## Goal
Capture traffic with Wireshark, identify **TCP, UDP and DNS** traffic, inspect **TLS** connections, review **local listening ports**, check the **firewall configuration**, and practise **basic authorized scanning**. Document every lab in the format below.

> **Authorization and scope**
> - Capture only **my own traffic**. Scan only `127.0.0.1` or machines I own.
> - Don't commit `.pcap` files. Redact IPs, MACs, hostnames and usernames in screenshots.
> - Don't change firewall settings on my main system without understanding them.

## Report format (each lab)
Objective · Tool used · Commands executed · Screenshots · Observations · Security implications · What I learned. Template: [lab-report-template.md](lab-report-template.md).

---
## Lab 1: Check listening ports
**Objective:** see what services accept connections on my Kali machine.
**Tool:** `ss`
**Commands:**
```
ss -tulnp
sudo ss -tulnp
python3 scripts/ss_report.py --run
```
| Flag | Meaning |
|---|---|
| `-t` / `-u` | TCP / UDP |
| `-l` | Listening sockets |
| `-n` | Numeric (no name lookup) |
| `-p` | Show the owning process |

**Screenshot:** `screenshots/lab1-ss.png`

**Results**
| Port | Proto | Process | Listens on (all / local only) | Needed? | Action |
|---|---|---|---|---|---|
| | | | | | |

**Observations:**
**Security implications:** (every listening service is attack surface. `0.0.0.0` = reachable from the network)
**What I learned:**

---
## Lab 2: Check firewall status
**Objective:** find out whether a host firewall is active and what it allows.
**Tool:** UFW (Linux), Windows Defender Firewall
**Commands:**
```
sudo ufw status verbose
sudo iptables -L -n -v          # read only
```
Windows:
```
netsh advfirewall show allprofiles
```
> If UFW is installed, this shows its status and rules. **Don't change firewall settings on your main system without understanding the impact.** `Status: inactive` is common on Kali.

**Screenshot:** `screenshots/lab2-firewall.png`

| Item | Result |
|---|---|
| UFW status | |
| Default incoming / outgoing | |
| Number of rules | |
| Windows profiles on/off | |

**Observations:**
**Security implications:** (an inactive firewall plus listening services means they are exposed to the LAN)
**What I learned:**

---
## Lab 3: Capture network traffic
**Objective:** identify TCP, UDP, DNS, TLS and ICMP in my own traffic.
**Tool:** Wireshark
**Setup:** open Wireshark, choose the interface with activity (`eth0`, `wlan0`...), start the capture, then in another window:
```
nslookup example.com
ping -c 4 1.1.1.1
curl -I https://example.com
```
Stop the capture and try the display filters:

| Filter | Shows | What to look for |
|---|---|---|
| `dns` | DNS queries and replies | The query for `example.com` and its answer (UDP 53) |
| `tcp` | All TCP | The **three-way handshake**: SYN → SYN-ACK → ACK |
| `udp` | All UDP | DNS, QUIC, mDNS, DHCP |
| `tls` | TLS traffic | **ClientHello** (look for the SNI field) and **ServerHello** |
| `icmp` | Ping | Echo request and reply |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | New connection attempts | |
| `ip.addr == <my-ip>` | Traffic to or from me | |

Useful actions: **Statistics → Protocol Hierarchy**, **Statistics → Conversations**, right-click a packet → **Follow → TCP Stream**.

**Screenshots:** `screenshots/lab3-dns.png`, `lab3-tcp-handshake.png`, `lab3-tls.png`

**Results**
| Observation | Packet / filter used | Notes |
|---|---|---|
| DNS query and response found | `dns` | |
| TCP handshake found | `tcp` | |
| UDP traffic seen (what protocol?) | `udp` | |
| TLS ClientHello and SNI | `tls` | |
| ICMP echo pair | `icmp` | |

**Inspect TLS:** open a ClientHello and expand it: TLS version, cipher suites offered, **server_name (SNI)**. Open a ServerHello: chosen version and cipher. In **TLS 1.2** you can see the server certificate in the capture. In **TLS 1.3** the certificate is encrypted, so you won't see it.

**Observations:**
**Security implications:** (what an eavesdropper sees even with HTTPS: IPs, SNI, DNS)
**What I learned:**

---
## Lab 4: Localhost port scan (authorized)
**Objective:** see what an attacker could learn from the network about my own machine.
**Tool:** Nmap
**Commands (own machine only):**
```
nmap -sT -sV 127.0.0.1
```
- `-sT`: TCP connect scan (completes the handshake, no special privileges needed)
- `-sV`: try to identify services and versions
- `127.0.0.1`: loopback, my own machine

Compare the Nmap result with Lab 1 (`ss`). They should agree for TCP.

**Optional (still my own machine):**
```
nmap -sT -p 22,80,443,8000 127.0.0.1
nmap -sU --top-ports 20 127.0.0.1        # UDP scan needs sudo and is slower
```
Start a test service so there is something to find: `python3 -m http.server 8000` (then stop it).

**Screenshot:** `screenshots/lab4-nmap.png`

| Port | State | Service / version | Matches `ss`? |
|---|---|---|---|
| | | | |

**Port states:** `open` (a service accepts connections), `closed` (reachable, nothing listening), `filtered` (no response, likely a firewall).

**Scanning rules:**
- Only scan targets you own or have **written permission** to test.
- Scanning is not harmless on other people's networks. It can be illegal and can trigger alerts.
- Keep scope small and note the date, target and purpose in the report.

**Observations:**
**Security implications:** (version info helps attackers match known vulnerabilities, so close or patch what you don't need)
**What I learned:**

---
## Bonus labs (if time allows)
**Bonus A: spot clear text vs encryption**
On loopback, run `python3 -m http.server 8000`, capture `lo`, filter `http`, then `curl http://127.0.0.1:8000/`. Compare it with the `tls` capture in Lab 3.

**Bonus B: ARP in Wireshark**
Filter `arp`, flush your neighbor table (`sudo ip neigh flush all`), `ping` your gateway and find the request and reply. Run `scripts/arp_table_check.py` on your `ip neigh` output.

**Bonus C: brute-force detection**
Run `scripts/failed_logins.py` on the sample log and on your own `/var/log/auth.log`.

---
## Summary of findings (document findings)
| # | Finding | Lab | Severity | Recommended fix |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Cleanup
- [ ] Stopped `http.server` and any test services
- [ ] Re-enabled or confirmed the firewall state I started with
- [ ] No `.pcap` files committed (they're git-ignored)
- [ ] Screenshots redacted

## Reflection
- Which lab showed me the most about my machine's exposure?
- How does this prepare me for interview question 15 (securing a network)?

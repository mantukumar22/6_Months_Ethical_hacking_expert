# Day 3: IDS, IPS and Network Monitoring
**Date:** ____ · **Time:** 60 min
**Video:** IDS vs IPS: <paste title/URL>

## Learn (20 min)

### IDS: Intrusion Detection System
An **IDS** **monitors** traffic or activity and **detects suspicious behavior**, then **alerts** people or systems. It **does not block** traffic by itself. It is *detective* (Week 5 controls).

### IPS: Intrusion Prevention System
An **IPS** does what an IDS does but sits **inline** in the traffic path and can **actively block or drop** malicious traffic. It is *preventive and detective*.

### IDS vs IPS

| | **IDS** | **IPS** |
|---|---|---|
| Action | Detects and alerts | Detects **and blocks** |
| Placement | **Out of band** (a copy of traffic from a SPAN/mirror port or TAP) | **Inline** (traffic flows through it) |
| Effect on traffic | None | Can drop packets, reset connections |
| Risk | May miss reaction time (humans must respond) | A false positive can **block legitimate traffic**, and a failure can disrupt the network |
| Control type | Detective | Preventive + detective |
| Examples | Snort / Suricata in IDS mode, Zeek | Snort / Suricata in inline IPS mode, NGFW IPS |

### Types by location
| Type | Watches | Example |
|---|---|---|
| **NIDS / NIPS** (network) | Traffic on a network segment | Snort, Suricata, Zeek |
| **HIDS / HIPS** (host) | One machine: logs, file changes, processes | Wazuh, OSSEC, AIDE, Windows Defender |

### Detection methods
| Method | How it works | Strength | Weakness |
|---|---|---|---|
| **Signature-based** | Matches traffic against known attack patterns (rules) | Accurate for known attacks, few false positives | **Misses new or modified attacks** (zero-days), needs constant updates |
| **Anomaly-based** | Learns a normal baseline, flags deviations | Can catch unknown attacks | **More false positives**, needs tuning and a good baseline |
| **Stateful protocol analysis** | Checks traffic against expected protocol behavior | Finds protocol abuse | Resource intensive |
| **Hybrid** | Combines methods | Balanced | More complex |

### Alerts: the four outcomes
| | Real attack | No attack |
|---|---|---|
| **Alert** | **True positive** (good) | **False positive** (noise, wasted time) |
| **No alert** | **False negative** (dangerous, missed attack) | **True negative** (good) |

**Tuning** reduces false positives without creating false negatives. Too many false positives leads to **alert fatigue**, where real alerts get ignored.

### Snort rule anatomy (concept)
Snort and Suricata use similar rule syntax:
```
alert tcp any any -> $HOME_NET 22 (msg:"SSH connection attempt"; flags:S; sid:1000001; rev:1;)
```
| Part | Meaning |
|---|---|
| `alert` | Action (log or alert, `drop` in IPS mode) |
| `tcp` | Protocol |
| `any any` | Source IP and port |
| `->` | Direction |
| `$HOME_NET 22` | Destination network and port |
| `msg` | Text shown in the alert |
| `flags:S` | Match TCP SYN packets |
| `sid`, `rev` | Rule ID and revision (local rules use ids 1000000+) |

Snort is available as a free tool. Follow the official documentation for installation and for the version you use. A first goal is to **read** rules and alerts, not to write complex ones.

### Network traffic monitoring
| Method | What it gives you |
|---|---|
| **Packet capture** (Wireshark, `tcpdump`) | Full detail, great for investigating, heavy to store |
| **Flow data** (NetFlow, IPFIX) | Who talked to whom, when and how much, with no content |
| **Logs** (firewall, DNS, proxy, auth, server logs) | Events and decisions |
| **IDS/IPS alerts** | Pre-analysed suspicious events |
| **SIEM** | Collects and correlates all of the above (Splunk, Elastic, Wazuh) |

**Things monitoring looks for:**
- Port scans (many connection attempts to many ports)
- Repeated failed logins (brute force)
- Connections to unusual countries or known bad IPs
- Large or unusual data transfers (possible exfiltration)
- Regular, timed "beaconing" to one address (malware calling home)
- Spikes in DNS queries or odd domains
- Clear-text protocols and new, unknown devices

### Security alerts and logs
**Where to look**
| Source | Location or command |
|---|---|
| SSH logins on Linux | `/var/log/auth.log`, `journalctl -u ssh` |
| UFW firewall logs | `/var/log/ufw.log` or `journalctl -k` (when logging is on) |
| System journal | `journalctl -p warning -b` |
| Windows logons | Event Viewer, Security log: **4624** success, **4625** fail |
| Windows firewall | Event Viewer, firewall logs |
| IDS alerts | Snort/Suricata alert files (e.g. `fast.log`, `eve.json`) |

**Triage questions for an alert:** What happened? When? Which source and destination? Which asset and how important? Is it a true positive? What's the severity? What should happen next (contain, investigate, ignore, tune)?

**Good logging practice:** synchronized clocks (NTP), centralized storage, protected from tampering, retention policy, and never log secrets. Attackers try to delete or edit logs.

(Week 3 link: Windows Event IDs, Linux `journalctl` and logs.)

## Practice (30 min)

### 1. Detect brute force from a log (no network needed)
```
python3 scripts/failed_logins.py samples/auth.log.sample
python3 scripts/failed_logins.py samples/auth.log.sample --threshold 3
```
The script groups failed SSH logins by source IP, lists the usernames tried, and flags an IP that **succeeded after many failures**. Record what you find.

| Question | Answer |
|---|---|
| Which IP has the most failures? | |
| Which usernames were tried? | |
| Did any IP succeed after failing? Why is that serious? | |
| What control would stop it (give two)? | |

### 2. Look at your own logs (read only)
```
sudo tail -n 20 /var/log/auth.log
journalctl -p warning -b --no-pager | tail -n 20
```
(If `auth.log` doesn't exist, use `journalctl`.)

### 3. Classify
For each, say IDS or IPS behavior, and signature or anomaly:
| Situation | IDS / IPS | Signature / anomaly |
|---|---|---|
| A rule matches a known exploit string and the packet is dropped | | |
| A tool emails an alert that traffic volume is 10x normal | | |
| A device flags a known malware domain in DNS and only logs it | | |

### 4. Optional
Read the official Snort documentation or its rules on the Snort website, and write two rules in plain English (don't deploy them on a network you don't own).

## Notes (10 min)
- IDS vs IPS in two sentences:
- Why anomaly detection has more false positives:
- Three things I'd monitor on a small network:

## Self-check
1. Why can't an IDS stop an attack on its own?
2. What is a false positive vs a false negative, and which is more dangerous?
3. Which detection method misses zero-day attacks?
4. Where is an IPS placed in a network compared to an IDS?
5. Which Windows event ID means a failed logon?

## Mistake I fixed / still confusing
-

# Day 3: IDS, IPS and Network Monitoring
**Date:** 28 · **Time:** 60 min
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
| Which IP has the most failures? | 203.0.113.5 |
| Which usernames were tried? | admin, kali, oracle, root, test, ubuntu |
| Did any IP succeed after failing? Why is that serious? | 203.0.113.5: logged in as 'kali' via password after 8 failures |
| What control would stop it (give two)? | rate limiting & MFA |

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
| A rule matches a known exploit string and the packet is dropped | IPS | Signature-based |
| A tool emails an alert that traffic volume is 10x normal | IDS | Anomaly-based |
| A device flags a known malware domain in DNS and only logs it | IDS | Signature-based |

### 4. Optional
Read the official Snort documentation or its rules on the Snort website, and write two rules in plain English (don't deploy them on a network you don't own).

```
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (
    msg:"LAB HTTP request for /admin from external network";
    flow:to_server,established;
    http_uri;
    content:"/admin",nocase;
    service:http;
    classtype:web-application-activity;
    sid:1000002;
    rev:1;
)
```

# IDS / IPS Notes

## Notes (10 min)

- **IDS vs IPS in two sentences:** An IDS (Intrusion Detection System) passively monitors traffic or logs and raises alerts about suspicious activity, but it does not stop anything. An IPS (Intrusion Prevention System) sits inline in the traffic path and can automatically block or drop malicious traffic, so a false positive can also block legitimate users.

- **Why anomaly detection has more false positives:** Anomaly detection learns a baseline of "normal" behavior and flags anything that deviates, but unusual is not the same as malicious. A new backup job, a software update, a busy sale day or an admin working at night can all look abnormal. Signature detection only fires on known bad patterns, so it is more precise, though it misses new attacks. Baselines are also hard to get right and drift over time, which adds more noise.

- **Three things I'd monitor on a small network:**
  1. **Authentication logs:** failed and successful logins, especially repeated failures (brute force) and logins at odd hours (SSH, Windows Event IDs 4625/4624).
  2. **Firewall and network traffic:** blocked connections, port scans, and unusual outbound traffic to unknown IPs (possible malware or data exfiltration).
  3. **Critical servers and changes:** new user accounts, privilege changes, new listening ports or services, and file integrity changes on the web and database servers. Also DNS queries and system health (CPU spikes can reveal cryptominers).

## Self-check

### 1. Why can't an IDS stop an attack on its own?

An IDS is **passive**. It usually receives a copy of the traffic (from a SPAN/mirror port or TAP) and is not in the path of the real traffic, so it cannot drop packets. It can only log and alert, and a person or another system (firewall, SOAR, IPS) must respond. By the time someone reads the alert, the attack may have already succeeded. Some IDS products can send a TCP reset or ask a firewall to block, but that is a limited, slower reaction, not true prevention.

### 2. What is a false positive vs a false negative, and which is more dangerous?

| | Meaning | Example | Impact |
|---|---|---|---|
| **False positive** | An alert for harmless activity | Alert on a legitimate admin scan | Wasted time, alert fatigue, blocked users (with an IPS) |
| **False negative** | A real attack that raised no alert | A stealthy intrusion goes unnoticed | Undetected breach |

**The false negative is more dangerous**, because the attacker gets in and nobody knows. False positives are costly, but too many of them cause **alert fatigue**, which leads analysts to ignore alerts and creates false negatives in practice. Good tuning balances both.

### 3. Which detection method misses zero-day attacks?

**Signature-based detection** (also called rule- or pattern-based). It only matches known patterns, and a zero-day has no signature yet. **Anomaly-based (behavioral) detection** has a better chance of catching zero-days because it notices unusual behavior, at the cost of more false positives.

### 4. Where is an IPS placed in a network compared to an IDS?

| | Placement | Why |
|---|---|---|
| **IPS** | **Inline**, directly in the traffic path (e.g. behind the perimeter firewall, between networks) | It must see traffic first so it can drop it |
| **IDS** | **Out of band**, on a mirror/SPAN port or network TAP, off to the side | It only needs a copy of the traffic and must not disrupt flow |

An inline IPS is a potential **single point of failure** and a latency source, so it is often deployed with fail-open or high-availability options. An IDS failing does not break network connectivity.

### 5. Which Windows event ID means a failed logon?

**Event ID 4625** (Security log): "An account failed to log on." Many 4625 events from one source in a short time suggest brute force or password spraying.

Related IDs worth remembering:

| Event ID | Meaning |
|---|---|
| 4624 | Successful logon |
| 4625 | **Failed logon** |
| 4634 / 4647 | Logoff |
| 4720 | User account created |
| 4672 | Special privileges assigned (admin logon) |

View them in **Event Viewer > Windows Logs > Security**, or with PowerShell: `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625}`.

## Mistake I fixed / still confusing
-

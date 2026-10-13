# Week 2: Networking Fundamentals

**13–19 October 2026 · 7 days · 1 hour per day**

Goal: understand how devices communicate, how traffic travels, and how to inspect my own network. This is the base for future VAPT, web pentesting and red-team work.

> **Safety rule:** run these commands only on my own device and network. Never scan or intercept anyone else's systems without authorization.

## Main video
*Complete Networking for Cybersecurity Beginners (2026)*, about 59 min. Do **not** binge it in one sitting. Follow the daily topics and do the labs.

## Schedule

| Day | Date | Topic | Notes | Lab |
|---|---|---|---|---|
| 1 | 13 Oct | Network basics and OSI model | [day-01](notes/day-01-osi-model.md) | Draw OSI model |
| 2 | 14 Oct | IP and MAC addresses | [day-02](notes/day-02-ip-mac.md) | [lab-02](labs/lab-02-ipconfig.md) |
| 3 | 15 Oct | TCP, UDP and ports | [day-03](notes/day-03-tcp-udp-ports.md) | [lab-03](labs/lab-03-netstat.md) |
| 4 | 16 Oct | DNS, DHCP and ARP | [day-04](notes/day-04-dns-dhcp-arp.md) | [lab-04](labs/lab-04-dns-arp.md) |
| 5 | 17 Oct | HTTP, HTTPS and web traffic | [day-05](notes/day-05-http-https.md) | [lab-05](labs/lab-05-devtools.md) |
| 6 | 18 Oct | Troubleshooting and packet analysis | [day-06](notes/day-06-troubleshooting.md) | [lab-06](labs/lab-06-ping-tracert-wireshark.md) |
| 7 | 19 Oct | Revision and mini-project | [day-07](notes/day-07-revision.md) | [project](project/network-profile-report.md) |

Each day: **Learn 20 min → Practice 30 min → Notes 10 min** (Day 6: 15/35/10. Day 7: 15 revision / 35 project / 10 review).

## Repo layout
```
notes/          daily notes (one file per day)
labs/           command exercises with output sections
project/        Day 7 network profile report (redacted)
resources/      commands cheat sheet, links
raw-private/    UNREDACTED output. git-ignored, never commit
checklist.md    weekly completion checklist
```

## Progress
See [checklist.md](checklist.md). **0/7** done.

## Standard before Week 3
I can explain, without notes, what happens when I type a URL into a browser: DNS resolution → network connection (TCP/TLS) → HTTP response.

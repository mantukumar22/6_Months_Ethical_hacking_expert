# Day 6: Network troubleshooting and packet analysis
**Date:** 18 Oct 2026 · **Time:** 60 min

## Learn (20 min)
Latency, packet loss, DNS failures, routing. (15 min)

### What is Network Troubleshooting?

**Network troubleshooting** is the process of identifying, diagnosing and fixing problems that stop devices from communicating properly. Instead of guessing, you test step by step to narrow down *where* the fault is and *what* is causing it.

**Typical symptoms:** no internet, slow connections, websites not loading, dropped video calls, a device that can't reach a printer or server.

**The basic method:**
1. **Identify the problem:** what exactly is failing, for whom, and since when?
2. **Gather information:** run tools such as `ipconfig`, `ping`, `tracert` and `nslookup`.
3. **Form a theory:** for example, "DNS is failing" or "the gateway is unreachable".
4. **Test the theory:** run a targeted check to confirm or rule it out.
5. **Fix it:** restart, reconfigure or replace the faulty part.
6. **Verify and document:** confirm it works and note what you found.

**Common approach: use the OSI model.** Work from the bottom up (physical connection, then IP configuration, then routing, then DNS, then the application), or top down, to isolate which layer is failing. This is why Day 1 matters.

**Why it matters for security:** the same tools and thinking are used in VAPT and red-team work. Understanding how traffic normally flows is what lets you spot abnormal behavior, and tools like `ping`, `tracert` and Wireshark are also used for network reconnaissance and analysis. Use them only on your own devices and networks, or ones you're authorized to test.

### Core concepts

| Concept | Meaning | Typical cause when bad |
|---|---|---|
| **Latency** | Time for a packet to travel to a destination and back (round trip), measured in ms | Distance, congestion, weak Wi-Fi, overloaded devices |
| **Packet loss** | Percentage of packets that never arrive | Congestion, poor Wi-Fi signal, faulty cable, a firewall dropping traffic |
| **Jitter** | Variation in latency between packets | Unstable connection. Hurts calls and gaming |
| **DNS failure** | A name can't be resolved to an IP | Wrong or unreachable DNS server, typo, domain doesn't exist |
| **Routing problem** | Packets can't find a path to the destination | Wrong gateway, a router down along the path, bad route |

**Troubleshooting order (bottom-up, like the OSI model):**
1. Is my device connected? (cable/Wi-Fi, Layer 1–2)
2. Do I have a valid IP and gateway? (`ipconfig /all`)
3. Can I reach the gateway? (`ping <gateway>`)
4. Can I reach the internet by IP? (`ping 1.1.1.1`)
5. Can I resolve names? (`nslookup example.com`)
6. Is it only one site or service? (application issue)

**Key trick:** if `ping 1.1.1.1` works but `ping example.com` fails, the network is fine and **DNS is the problem**.

### Commands (Windows CMD, own device only)

```
ping 1.1.1.1
tracert example.com
nslookup example.com
```

**Reading `ping`:**
```
Reply from 1.1.1.1: bytes=32 time=18ms TTL=57
...
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
Approximate round trip times: Minimum = 17ms, Maximum = 21ms, Average = 18ms
```
- `time` is latency. `Lost` is packet loss.
- `TTL` (time to live) drops by one at each router and prevents endless loops.
- `Request timed out` means no reply came back. It could be loss, or the target is blocking ping.
- `Destination host unreachable` means no route was found.

**Reading `tracert`:**
```
  1    <1 ms    <1 ms    <1 ms  192.168.1.1
  2     8 ms     9 ms     8 ms  10.20.x.x
  3     *        *        *     Request timed out.
  4    19 ms    18 ms    20 ms  93.184.x.x
```
- Each line is one **hop** (router). The three times are three probes.
- A big latency jump between hops shows where delay starts.
- `* * *` in the middle isn't necessarily a failure. Many routers don't answer these probes but still forward traffic. It's only a problem if every hop after it also fails.

**Reading `nslookup`:** shows which DNS server answered and what IP(s) it returned. See Day 4 / Lab 04.

### What each command tells me, and one limitation

| Command | Tells me | Limitation |
|---|---|---|
| `ping` | Whether a host is reachable, the round-trip latency, and the percentage of packet loss | Many hosts and firewalls block ICMP, so no reply doesn't prove the host is down. It also doesn't show *where* a problem is, and it says nothing about whether a specific service or port works |
| `tracert` | The path packets take, each router hop, and where latency increases | Some routers don't respond (`* * *`), and the path can differ from run to run or from the return path, so results are a snapshot rather than the full picture |
| `nslookup` | Which DNS server is used and what IP address a name resolves to | It queries the DNS server directly and can show a different result than what the OS or browser actually uses (cache, hosts file, DNS-over-HTTPS). It also doesn't confirm the site itself is reachable |

### Optional: Wireshark (own traffic only)

Wireshark captures and shows the packets crossing your network interface.

**Steps:**
1. Install Wireshark (use the official site) and open it.
2. Pick your active interface (Wi-Fi or Ethernet, the one with a moving graph) and start capturing.
3. In your browser, visit `example.com`, then stop the capture.
4. Apply a **display filter** in the bar at the top.

| Filter | Shows |
|---|---|
| `dns` | DNS queries and responses |
| `tcp` | All TCP traffic |
| `icmp` | Ping traffic (run a `ping` while capturing) |
| `tcp.flags.syn == 1` | Connection start packets (SYN) |
| `ip.addr == <your-ip>` | Only traffic to or from your machine |

**What to find:**
- A **DNS query** for `example.com` and its response containing the IP.
- A **TCP three-way handshake**: SYN → SYN-ACK → ACK (Day 3).
- **ICMP echo request/reply** pairs from your `ping`.

Why HTTP/TLS traffic looks unreadable: on HTTPS sites the content is encrypted (Day 5), so you'll see the handshake and encrypted data rather than page content.

### Safety and privacy
- Capture **only on your own device and network**. Never capture on someone else's network without authorization.
- Captures can contain sensitive data (domains visited, cookies, unencrypted credentials). Save `.pcapng` files only in `raw-private/` (git-ignored) and **never commit them**.
- Redact public IPs and MAC addresses from anything you publish.

### My results

| Test | Result |
|---|---|
| `ping 1.1.1.1`: avg latency / loss | |
| `tracert example.com`: number of hops | |
| `tracert`: any `* * *` lines? | |
| `nslookup example.com`: IP returned | |
| Wireshark: DNS query found? | |
| Wireshark: TCP handshake found? | |

### Reflection
Why can `ping 1.1.1.1` succeed while `ping example.com` fails?

## Practice (30 min)
Lab: [lab-06](../labs/lab-06-ping-tracert-wireshark.md). `ping 1.1.1.1`, `tracert example.com`, `nslookup example.com`, optional Wireshark (35 min).

## Key takeaways
-

## Still confusing / to revisit
-

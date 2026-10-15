# Lab 04: DNS, DHCP and ARP
Commands: `nslookup example.com`, `ipconfig /all`, `arp -a`

## Lab 04: DNS, DHCP and ARP

**Commands:** `nslookup example.com`, `ipconfig /all`, `arp -a`

> Run on my own device only. Redact MAC addresses and any public IP before committing.

### Results

| Question | Where to find it | My result |
|---|---|---|
| DNS server used | `nslookup example.com`, the `Server` / `Address` lines at the top | `<192.168.x.x or 1.1.1.1>` |
| IP(s) returned for example.com | `nslookup`, below `Non-authoritative answer:` | `<IPv4 / IPv6 addresses>` |
| DHCP server | `ipconfig /all`, the `DHCP Server` line on the active adapter | `<192.168.x.x>` |
| Lease obtained / expires | `ipconfig /all`, the `Lease Obtained` and `Lease Expires` lines | `<date/time>` / `<date/time>` |
| Gateway's ARP entry | `arp -a`, find the default gateway's IP under the correct `Interface:` | `192.168.x.x -> XX-XX-XX-XX-XX-XX` (dynamic) |

### How to read the output

- **Non-authoritative answer:** the reply came from a resolver's cache, not directly from the domain's own name server.
- **DHCP Enabled: Yes** means the router assigns the IP address automatically. The **lease** is how long I may keep it before renewing.
- **`arp -a` shows one table per interface.** Use the one whose `Interface:` IP matches my adapter's IPv4 address.

### Dynamic vs static ARP entry

| | Dynamic | Static |
|---|---|---|
| How created | Learned automatically via ARP request/reply | Added manually (`arp -s`) or built in by the system |
| Lifetime | Temporary, removed after a timeout | Stays until deleted or reboot |
| Typical examples | Gateway, other devices on the LAN | Broadcast `ff-ff-ff-ff-ff-ff`, multicast addresses |
| Security | Can be overwritten by a fake ARP reply (ARP spoofing) | Resistant to spoofing, but must be maintained by hand |

### What I learned
- DNS turns the name into an IP, using the resolver shown in `nslookup`.
- DHCP gave my device its IP, gateway and DNS settings.
- ARP maps IPs to MAC addresses, and I reach the internet through the **gateway's** MAC, not the website's.

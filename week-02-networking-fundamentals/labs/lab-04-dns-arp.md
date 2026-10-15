# Lab 04: DNS, DHCP and ARP
Commands: `nslookup example.com`, `ipconfig /all`, `arp -a`
## Lab 04: DNS, DHCP and ARP

**Commands (Windows CMD, own device only):**
```
nslookup example.com
ipconfig /all
arp -a
```

### 1. DNS server used
Run `nslookup example.com`. The first two lines show which DNS server answered:
```
Server:  router.local
Address: 192.168.1.1
```
Record the **Address**. It should match "DNS Servers" in `ipconfig /all`.
- Private address (`192.168.x.x`): your router is the resolver and forwards queries to your ISP.
- Public address (`1.1.1.1`, `8.8.8.8`): you're using a public resolver.

### 2. IP(s) returned for example.com
Read below `Non-authoritative answer:` in the same output. "Non-authoritative" means the answer came from a cache rather than the domain's own server. Record all addresses, including IPv6 ones (long, with colons).

### 3. DHCP server / lease info
In `ipconfig /all`, find the **active adapter** (the Wi-Fi or Ethernet one with an IPv4 address):

| Field | Meaning |
|---|---|
| DHCP Enabled | `Yes` means the address is assigned automatically |
| DHCP Server | Who gave you the address, usually your router |
| Lease Obtained | When you got the address |
| Lease Expires | When it must be renewed |

### 4. Gateway's entry in `arp -a`
1. Find "Default Gateway" in `ipconfig /all` (e.g. `192.168.1.1`).
2. In `arp -a`, find the section headed `Interface: <your IP>`.
3. Find the gateway's IP in that list and note the MAC next to it, **redacted** (`AA-BB-CC-XX-XX-XX`).

### 5. Dynamic vs static ARP entry

| | Dynamic | Static |
|---|---|---|
| How created | Learned automatically via ARP request/reply | Added manually (`arp -s`) or by the system |
| Lifetime | Temporary, removed after a timeout | Fixed, does not expire |
| Examples | Your router, other LAN devices | Broadcast `ff-ff-ff-ff-ff-ff`, multicast entries |
| Security | Can be overwritten by a fake ARP reply (spoofing) | Resists spoofing, used for critical devices |

### My results

| Item | Value (redacted) |
|---|---|
| DNS server used | `192.168.x.x` |
| IP(s) returned for example.com | |
| DHCP server | `192.168.x.x` |
| Lease obtained / expires | |
| Gateway IP → MAC (from `arp -a`) | `192.168.x.x` → `XX-XX-XX-XX-XX-XX` |

> Redact public IPs, MAC addresses and hostnames before committing. Keep raw output in `raw-private/`.

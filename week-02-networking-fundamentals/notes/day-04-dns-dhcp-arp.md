# Day 4: DNS, DHCP and ARP
**Date:** 16 Oct 2026 · **Time:** 60 min

## Learn (20 min)
DNS: DNS Domain Name System (Server) is used to translate a fully qualifed Domain Name into a  ip address & a Ip address to fully qualifed Domain Name.

DHCP: Dynamic Host Configuration Protocol server is used to assign automatic ip address into client Computer systems.

ARP: (Address Resolution Protocol) A protocol that finds the **MAC address** that belongs to a known **IPv4 address** on the local network. It connects Layer 3 (IP) to Layer 2.

WINS: Window Internet Name Service is used to resolve NetBIOS name into IP address.

## Practice (30 min)
Lab: [lab-04-dns-arp](../labs/lab-04-dns-arp.md). Run `nslookup example.com`, `ipconfig /all`, `arp -a`.

## Notes (10 min)
Draw the steps from typing a website name to finding its IP address:

### From website name to IP address (3 steps)

```
 You type: www.example.com
      |
      v
 STEP 1: Check local memory
 [Browser cache] -> [OS DNS cache + hosts file]
      |  found? -> done, use that IP
      | not found
      v
 STEP 2: Ask the DNS resolver (UDP port 53)
 [Your PC] -----> [Resolver: router / ISP / 1.1.1.1]
      |  has it cached? -> returns IP, done
      | not cached
      v
 STEP 3: Resolver walks the DNS hierarchy
 [Root server]  "ask .com"
      -> [.com TLD server]  "ask example.com's name server"
      -> [Authoritative server]  "www.example.com = 93.184.x.x"
      |
      v
 Answer returns to your PC (and is cached)
 -> Browser connects to the IP
```

1. **Check local caches.** The browser, then the operating system (and the `hosts` file), look for a saved answer. If one exists, no network request is needed.
2. **Ask the DNS resolver.** Your PC sends a query to the DNS server set in `ipconfig /all`, usually your router, ISP or a public one like 1.1.1.1. If the resolver has the answer cached, it replies immediately.
3. **Resolver finds the answer.** If not cached, the resolver asks the root server, then the `.com` TLD server, then the domain's authoritative server, which gives the IP. The resolver caches it and returns it to your PC, and the browser connects to that IP.

## Key takeaways
-

## Still confusing / to revisit
-

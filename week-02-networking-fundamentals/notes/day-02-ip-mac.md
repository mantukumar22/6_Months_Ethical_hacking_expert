# Day 2: IP and MAC addresses
**Date:** 14 Oct 2026 · **Time:** 60 min

## Learn (20 min)
IPv4, IPv6, private vs public IP, MAC addresses, subnet masks, default gateways.

## Practice (30 min)
Lab: [lab-02-ipconfig](../labs/lab-02-ipconfig.md). Run `ipconfig /all`.

## Notes (10 min)
## Day 2 Glossary: IP and MAC Addresses

### IPv4
A 32-bit logical address written as four decimal numbers (0–255) separated by dots, e.g. `192.168.1.10`. It allows about 4.3 billion addresses, which is not enough for every device, so IPv4 addresses are shared and reused through NAT. Operates at **Layer 3 (Network)**.

### IPv6
The successor to IPv4. A 128-bit address written as eight groups of hexadecimal separated by colons, e.g. `2001:db8::1` (`::` shortens a run of zeros). It provides a practically unlimited address space and was designed to remove the need for NAT. Both versions currently run side by side.

### Public IP
An address that is unique and routable on the internet. It is assigned by your ISP and identifies your network to the outside world. Anyone you connect to can see it, so treat it as identifying information (redact it in reports).

### Private IP
An address used only inside a local network. It is not routable on the internet, so many networks can reuse the same ranges. The reserved IPv4 private ranges are:

| Range | Typical use |
|---|---|
| `10.0.0.0` – `10.255.255.255` | Large networks |
| `172.16.0.0` – `172.31.255.255` | Mid-size networks |
| `192.168.0.0` – `192.168.255.255` | Home and small office |

A router uses **NAT** to translate private addresses to its one public address when traffic leaves the network.

Also worth knowing: `127.0.0.1` is **loopback** (your own machine), and `169.254.x.x` means the device failed to get an address from DHCP.

### MAC Address
A 48-bit hardware address burned into a network interface (NIC), written as six hex pairs, e.g. `AA:BB:CC:DD:EE:FF`. The first half identifies the manufacturer (OUI) and the second half is unique to the device. It is used for delivery **within one local network**. Operates at **Layer 2 (Data Link)**. Windows calls it the "Physical Address" in `ipconfig /all`.

### Subnet Mask
A 32-bit value that splits an IP address into a **network part** and a **host part**, telling a device which addresses are local and which must go through the gateway. Example: `255.255.255.0` (also written `/24`) means the first three numbers identify the network and the last identifies the device. So `192.168.1.10` and `192.168.1.20` are on the same network, but `192.168.2.10` is not.

### Default Gateway
The router address a device sends traffic to when the destination is **outside its own network**. It is your exit door to other networks and the internet, usually something like `192.168.1.1`.

### IP vs MAC at a glance

| | IP address | MAC address |
|---|---|---|
| Layer | 3 (Network) | 2 (Data Link) |
| Size | 32-bit (v4) / 128-bit (v6) | 48-bit |
| Scope | Across networks (routing) | Within one local network |
| Assigned by | DHCP or manually | Manufacturer (hardware) |
| Changes? | Yes, depending on the network | Normally fixed, though it can be randomized by the OS |
| Used by | Routers | Switches |

**Why they are not interchangeable:** the IP address gets a packet to the right *network*, and the MAC address gets the frame to the right *device on that network*. At each hop the MAC addresses change while the IP addresses stay the same.
Why are an IP address and a MAC address not interchangeable?


## Key takeaways
-

## Still confusing / to revisit
-

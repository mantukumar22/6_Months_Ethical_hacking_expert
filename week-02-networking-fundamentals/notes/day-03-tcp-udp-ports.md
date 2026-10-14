# Day 3: TCP, UDP and ports
**Date:** 15 Oct 2026 · **Time:** 60 min

## Learn (20 min)
TCP three-way handshake, UDP, ports, sockets.

## Day 3 Glossary: TCP, UDP and Ports

### TCP (Transmission Control Protocol)
A **connection-oriented, reliable** Layer 4 protocol. It sets up a connection first, numbers the data, confirms delivery, resends anything lost, and delivers it in order. That makes it slower but dependable. Used for web pages, file transfers, email and remote login.

### UDP (User Datagram Protocol)
A **connectionless, best-effort** Layer 4 protocol. It just sends datagrams, with no handshake, no delivery confirmation and no ordering. That makes it fast and lightweight, but the application must cope with lost data. Used for DNS lookups, live video and voice calls, and online games.

| | TCP | UDP |
|---|---|---|
| Connection | Yes (handshake first) | No |
| Reliability | Guaranteed, with retransmission | Not guaranteed |
| Ordering | In order | No ordering |
| Speed / overhead | Slower, higher | Faster, lower |
| Typical use | Web, SSH, file transfer, email | DNS, streaming, VoIP, gaming |

### Port
A 16-bit number (0–65535) that identifies a specific **application or service** on a device. The IP address finds the machine, and the port finds the program on it. TCP and UDP each have their own set of ports, so TCP 53 and UDP 53 are different.

| Range | Name | Use |
|---|---|---|
| 0 – 1023 | Well-known ports | Standard services (HTTP, SSH, DNS) |
| 1024 – 49151 | Registered ports | Specific applications |
| 49152 – 65535 | Dynamic / ephemeral | Temporary client-side ports |

When your browser connects to a website, it uses a random ephemeral port on your side and port 443 on the server's side.

### Socket
One endpoint of a network conversation: an **IP address + port number + protocol**, e.g. `192.168.1.10:51234` over TCP. A connection is uniquely identified by the pair of sockets (source IP, source port, destination IP, destination port, protocol). This is why one server on port 443 can serve thousands of clients at once.

### TCP Three-Way Handshake
How a TCP connection is established before any data is sent:

```
Client                         Server
  |  ---- SYN (seq=x) ------>    |   1. "I want to connect"
  |  <--- SYN-ACK (seq=y,        |   2. "OK, I'm ready too"
  |        ack=x+1) ---------    |
  |  ---- ACK (ack=y+1) ---->    |   3. "Confirmed"
  |                              |
  |  ====== data flows ======    |
```

1. **SYN:** the client asks to start a connection and sends its initial sequence number.
2. **SYN-ACK:** the server acknowledges and sends its own sequence number.
3. **ACK:** the client acknowledges, and the connection is **established**.

A connection is closed with **FIN** and **ACK** packets (or abruptly with **RST**).

### Common Ports to Memorize

| Port | Service | Protocol | What it does |
|---|---|---|---|
| 22 | SSH | TCP | Encrypted remote command-line access |
| 53 | DNS | UDP (and TCP) | Resolves domain names to IPs. TCP is used for large responses and zone transfers |
| 80 | HTTP | TCP | Unencrypted web traffic |
| 443 | HTTPS | TCP (and UDP for HTTP/3) | Encrypted web traffic (HTTP over TLS) |
| 3389 | RDP | TCP | Remote Desktop access to Windows machines |

Security note: SSH (22) and RDP (3389) are among the most commonly attacked services when exposed to the internet, and open ports in general are the starting point of any security assessment.

### Reading `netstat -ano` (Windows)

| Column | Meaning |
|---|---|
| Proto | TCP or UDP |
| Local Address | Your IP and port |
| Foreign Address | The remote IP and port |
| State | `LISTENING` (waiting for connections), `ESTABLISHED` (active), `TIME_WAIT` (closing) |
| PID | Process ID. Match it to a program with `tasklist` |

A port in `LISTENING` state means a program on your machine is accepting connections on it.

## Practice (30 min)
Lab: [lab-03-netstat](../labs/lab-03-netstat.md). Run `netstat -ano` and `tasklist`.

## Notes (10 min)
Memorize:

| Port | Service |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3389 | RDP |

Draw the 3-way handshake: SYN → SYN-ACK → ACK.

## Key takeaways
-

## Still confusing / to revisit
-

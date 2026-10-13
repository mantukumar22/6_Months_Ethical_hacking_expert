# Lab 06: Troubleshooting and packet analysis
Commands: `ping 1.1.1.1`, `tracert example.com`, `nslookup example.com`

- Average latency / packet loss:
- Number of hops in tracert; any `* * *` timeouts? What might they mean?
- Why can `ping 1.1.1.1` work while `ping example.com` fails? (Think DNS.)

## Optional: Wireshark (own traffic only)
Capture on my own interface. Display filters: `dns`, `tcp`.

- Found the DNS query for:
- Found a TCP handshake (SYN, SYN-ACK, ACK)?

Save `.pcapng` files only in `raw-private/`. They are git-ignored.

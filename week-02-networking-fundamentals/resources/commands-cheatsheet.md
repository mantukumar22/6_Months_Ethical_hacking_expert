# Commands (Windows CMD, own device only)

| Command | Purpose |
|---|---|
| `ipconfig /all` | IP, mask, gateway, MAC, DHCP, DNS |
| `netstat -ano` | Connections, listening ports, owning PID |
| `tasklist` | Map PID → process |
| `nslookup example.com` | DNS lookup |
| `arp -a` | IP → MAC table for the local network |
| `ping 1.1.1.1` | Reachability and latency |
| `tracert example.com` | Path and per-hop latency |

## Wireshark display filters
`dns` · `tcp` · `ip.addr == <your-ip>` · `tcp.flags.syn == 1`

## Common ports
22 SSH · 53 DNS · 80 HTTP · 443 HTTPS · 3389 RDP

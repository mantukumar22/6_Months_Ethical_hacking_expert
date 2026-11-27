# Network security commands (own systems only)

## Listening ports and connections
```
ss -tulnp                  # listening TCP/UDP with process (sudo for more)
ss -tan                    # all TCP connections, numeric
ss -s                      # socket summary
ss -tan state syn-recv     # half-open connections
```
## Firewall (read only first)
```
sudo ufw status verbose
sudo ufw status numbered
sudo iptables -L -n -v
sudo nft list ruleset
netsh advfirewall show allprofiles          # Windows
```
## ARP and neighbours
```
ip neigh            arp -a
sudo ip neigh flush all        # own machine, safe
```
## DNS
```
nslookup example.com           dig example.com
nslookup example.com 1.1.1.1
```
## Wireshark display filters
`dns` · `tcp` · `udp` · `tls` · `icmp` · `arp` · `http` · `ip.addr == x.x.x.x` · `tcp.port == 443` · `tcp.flags.syn == 1 && tcp.flags.ack == 0`

## Nmap (authorized targets only, start with 127.0.0.1)
```
nmap -sT -sV 127.0.0.1         # TCP connect + version detection
nmap -sT -p 22,80,443 127.0.0.1
sudo nmap -sU --top-ports 20 127.0.0.1
```
States: open · closed · filtered

## Logs
```
sudo tail -n 50 /var/log/auth.log
journalctl -u ssh --no-pager | tail
journalctl -p warning -b
```

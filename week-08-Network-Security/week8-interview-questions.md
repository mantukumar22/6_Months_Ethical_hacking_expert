# Week 8: Interview Questions
Answer each in **your own words, out loud first**, then write 3 to 5 sentences with an example. The hints show what to cover, not the answers.

## 1. What is network security?
*Cover:* protecting networks and data from unauthorized access, misuse, modification and disruption, the goals (CIA, authentication, accountability), layered defense.

**My answer:**

## 2. What is the difference between TCP and UDP?
*Cover:* connection-oriented and reliable vs connectionless and fast, handshake, examples, one security implication each (SYN flood, spoofing and amplification).

**My answer:**

## 3. What is a firewall?
*Cover:* filters traffic by rules (IP, port, protocol, state), allow/deny, host vs network, default deny.

**My answer:**

## 4. What is the difference between a stateful and a stateless firewall?
*Cover:* connection tracking vs single-packet decisions, return traffic, examples (Security Group vs Network ACL).

**My answer:**

## 5. What are IDS and IPS?
*Cover:* intrusion detection (alerts) and intrusion prevention (blocks inline), network vs host-based, tools (Snort, Suricata).

**My answer:**

## 6. What is the difference between IDS and IPS?
*Cover:* detect vs prevent, placement (out of band vs inline), risk of false positives blocking real traffic, detective vs preventive control.

**My answer:**

## 7. What is a VPN?
*Cover:* an encrypted tunnel, remote-access vs site-to-site, protocols (IPsec, OpenVPN, WireGuard), what it does and does not protect.

**My answer:**

## 8. What is a Man-in-the-Middle attack?
*Cover:* attacker secretly relays or alters traffic, how they get in the path (ARP/DNS spoofing, rogue Wi-Fi), impact, defenses (TLS, certificate validation, VPN).

**My answer:**

## 9. What is ARP spoofing?
*Cover:* forged ARP replies to poison the cache, same-LAN requirement, impact, detection (duplicate MACs, changing gateway MAC), defenses (DAI, port security, encryption).

**My answer:**

## 10. What is DNS spoofing?
*Cover:* forged or poisoned DNS answers sending users to the wrong IP, impact, detection, defenses (DNSSEC, DoH/DoT, HTTPS and HSTS).

**My answer:**

## 11. What is network segmentation?
*Cover:* splitting a network into zones (VLANs, subnets) with controlled traffic, limits lateral movement, examples (guest, servers, IoT), link to cloud VPC subnets.

**My answer:**

## 12. What is Wireshark used for?
*Cover:* capturing and analysing packets, display filters, protocol analysis and troubleshooting, security investigation, the legal and privacy caution.

**My answer:**

## 13. What does `ss -tulnp` show?
*Cover:* TCP and UDP **listening** sockets with numeric addresses and the owning process, what `0.0.0.0` vs `127.0.0.1` means, why it matters for attack surface.

**My answer:**

## 14. What is the difference between HTTP and HTTPS?
*Cover:* clear text vs TLS-encrypted, certificates and authentication, integrity, port 80 vs 443, what is still visible (IP, domain).

**My answer:**

## 15. How would you secure a network?
*Cover (a sensible layered answer):*
1. **Inventory and risk:** know the assets, data and threats.
2. **Segmentation:** separate guest, staff, servers, IoT and management networks.
3. **Firewalls:** default deny, least privilege rules, egress filtering.
4. **Secure access:** VPN with MFA, SSH keys, no exposed RDP or admin interfaces.
5. **Encrypt:** TLS everywhere, WPA3 or WPA2-Enterprise Wi-Fi, disable clear-text protocols.
6. **Harden and patch:** close unused ports, change default credentials, update devices.
7. **Monitor:** logs, IDS/IPS, SIEM, alerting.
8. **Prepare:** backups, an incident response plan, staff training, regular tests (authorized scans and assessments).

**My answer:**

---
## Self-assessment
| Questions | Confident (Y/N) | Needs review |
|---|---|---|
| 1-3 | | |
| 4-6 | | |
| 7-9 | | |
| 10-12 | | |
| 13-15 | | |

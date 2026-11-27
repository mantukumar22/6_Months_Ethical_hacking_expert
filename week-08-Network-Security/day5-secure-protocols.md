# Day 5: Network Security Protocols
**Date:** ____ · **Time:** 60 min
**Video:** SSH, TLS, VPN explained: <paste title/URL>

## Learn (20 min)

### HTTPS and TLS (Week 6 and Week 2 recap)
- **HTTPS = HTTP over TLS**, on port 443.
- TLS provides **confidentiality** (encryption), **integrity** (tamper detection) and **authentication** (the server proves its identity with a certificate signed by a trusted CA).
- Handshake in short: negotiate version and cipher → server certificate → key exchange (ECDHE) → symmetric session key (AES-GCM/ChaCha20) → encrypted data.
- Use **TLS 1.2 or 1.3**. SSL and TLS 1.0/1.1 are deprecated.
- **What an observer still sees:** IP addresses, the domain name (DNS and the SNI field in the handshake), packet sizes and timing.
- Extra protections: **HSTS** (force HTTPS), valid certificates, strong cipher suites.

### SSH (Secure Shell)
- Encrypted remote login and file transfer, TCP **port 22** (replaces Telnet, FTP and rsh).
- **Authentication:** password or **public-key** (preferred). Week 6 link: your private key stays on your machine, the public key goes on the server (`~/.ssh/authorized_keys`).
- **Host keys:** on the first connection you verify the server's fingerprint. A changed host key warning can mean a MitM, so don't ignore it.
- Other uses: SCP/SFTP, **port forwarding / tunnelling** (also a way attackers pivot, so monitor it).

**SSH hardening (settings in `/etc/ssh/sshd_config`: read only for now)**
| Setting | Safer value |
|---|---|
| `PermitRootLogin` | `no` |
| `PasswordAuthentication` | `no` (use keys) |
| `PubkeyAuthentication` | `yes` |
| `MaxAuthTries` | low (3-4) |
| `AllowUsers` / `AllowGroups` | only the users who need it |
| Network exposure | Limit by firewall to known IPs or use a VPN |
Other defenses: **fail2ban** (bans IPs after repeated failures), MFA, patching, logging. Changing the SSH port reduces log noise but is **obscurity, not security**.

### VPN (Virtual Private Network)
A VPN creates an **encrypted tunnel** between endpoints or networks, so traffic crosses an untrusted network (like the internet or café Wi-Fi) protected.

| Type | Use |
|---|---|
| **Remote-access VPN** | One user or device connects to a company network |
| **Site-to-site VPN** | Joins two office networks |
| Protocols | **IPsec**, **OpenVPN**, **WireGuard** (modern, simple), SSL VPNs |

| Concept | Meaning |
|---|---|
| **Full tunnel** | All traffic goes through the VPN |
| **Split tunnel** | Only some traffic goes through the VPN |

**What a VPN does:** encrypts traffic between you and the VPN endpoint, hides your traffic from the local network (helps against sniffing and MitM on public Wi-Fi), and can give access to private resources.
**What a VPN does not do:** make you anonymous (the VPN provider sees your traffic), protect you from malware or phishing, secure the destination site, or fix a compromised device. A VPN **gateway itself is an attack surface**, so keep it patched with MFA.

### DNS security concepts
| Concept | Meaning |
|---|---|
| **Problem** | Classic DNS is unencrypted and unauthenticated (spoofing, snooping, tampering) |
| **DNSSEC** | Signs DNS records so resolvers can verify they're **authentic and unmodified**. Doesn't encrypt |
| **DoT (DNS over TLS) / DoH (DNS over HTTPS)** | **Encrypt** the DNS queries between client and resolver |
| **Resolver hygiene** | Don't run open resolvers (amplification), restrict recursion |
| **Monitoring** | DNS logs show malware domains, tunnelling and data exfiltration |
| **Filtering** | Block known malicious domains (DNS firewalls) |

### Secure vs insecure protocols

| Insecure | Why | Secure replacement |
|---|---|---|
| **HTTP** (80) | Clear text, anyone on the path can read or modify | **HTTPS** (443) |
| **FTP** (21) | Credentials and files in clear text | **SFTP** (SSH) or **FTPS** |
| **Telnet** (23) | Clear-text login | **SSH** (22) |
| **TFTP** (69) | No authentication or encryption | SFTP |
| **SMTP/POP3/IMAP** (25/110/143) | Often unencrypted | TLS versions (587/465, 995, 993) |
| **SNMP v1/v2c** (161) | Clear-text community strings | **SNMPv3** |
| **LDAP** (389) | Clear text | **LDAPS** (636) or StartTLS |
| **Plain DNS** (53) | Spoofable and visible | DNSSEC, DoT/DoH |
| **WEP / WPA (old Wi-Fi)** | Broken | **WPA3** (or WPA2-AES at minimum) |
| **SMBv1** | Old and vulnerable | SMBv3 (and restrict access) |

**Why it matters (Week 2 link):** on an open network, clear-text protocols show passwords in Wireshark in plain view. That is why the **"identify insecure protocols"** step is part of every network assessment.

## Practice (30 min)

### 1. See clear text vs TLS in Wireshark (own traffic only)
Capture while you visit **an HTTP-only practice site you're allowed to use** (or use your own local test server) and then an HTTPS site. Use filters `http` and `tls`. Compare: can you read the request in each case?

Quick local clear-text test (no internet, your machine only):
```
python3 -m http.server 8000     # in one terminal
curl http://127.0.0.1:8000/     # in another
```
Capture on the **loopback** interface (`lo`) and filter `http`. Note what is visible. Stop the server afterwards.

### 2. Inspect an HTTPS connection
```
python3 ../week6/scripts/day5_cert_inspect.py example.com    # the Week 6 script, if it's next to this folder
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```
Record the TLS version, issuer and expiry.

### 3. Review SSH settings (read only)
```
ssh -V
grep -Ei '^(PermitRootLogin|PasswordAuthentication|PubkeyAuthentication|MaxAuthTries)' /etc/ssh/sshd_config
sudo systemctl status ssh
```
(If SSH isn't installed, note that. **No SSH server running is the most secure setting if you don't need it.**) Compare each value with the hardened table above.

### 4. Find insecure ports on your machine
```
python3 scripts/ss_report.py --run
```
Does anything listen on 21, 23, 69, 80, 110, 143 or 161?

### 5. Table to complete
| Protocol | Secure or insecure? | Why | Replacement |
|---|---|---|---|
| FTP | | | |
| Telnet | | | |
| HTTP | | | |
| SSH | | | |
| DNS | | | |

## Notes (10 min)
- What TLS protects and what it doesn't hide:
- Why SSH keys beat passwords:
- What a VPN does and doesn't do:

## Self-check
1. Name three services that send credentials in clear text.
2. What does DNSSEC protect, and what does DoH protect?
3. Why is changing the SSH port not real security?
4. What's the difference between a full tunnel and a split tunnel?
5. What does a "host key changed" SSH warning mean?

## Mistake I fixed / still confusing
-

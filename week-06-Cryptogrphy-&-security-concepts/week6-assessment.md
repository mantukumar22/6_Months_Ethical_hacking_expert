# Week 6: Practical Lab and Assessment
**Date:** 23 · **Time:** 60 min

## Practical lab checklist
Save outputs (redacted) in `evidence/`.

| # | Task | How | Done |
|---|---|---|---|
| 1 | Hash a file using SHA-256 | `python3 day4-hashing.py` (or `sha256sum test.txt`) | [ Y ] |
| 2 | Change the file, hash again, compare | Edit `test.txt`, re-run | [ Y ] |
| 3 | Generate encryption keys | `python3 scripts/day3_keypair.py` and the AES demo | [ Y ] |
| 4 | Inspect a website's TLS certificate | `python3 scripts/day5_cert_inspect.py <site>` | [ Y ] |
| 5 | Test password hashing concepts | `python3 scripts/day7_password_hashing.py` | [ Y ] |

### Lab results
| Check | Result |
|---|---|
| SHA-256 of `test.txt` (original) | 01f3b04fa8d66d9c95855a0564b1ef9eb0bf7ed2195a38f76efb84965208eb23 |
| SHA-256 after my change | 2b0c70133653567ae1c34e6feb64b048b0820a507509aa48035f712256a2ae1d |
| Do they match? Why? | No |
| Key pair generated (type and size) | RSA, 2048 bits |
| Signature verified? After tampering? | Valid on the original message. Invalid after tampering — the signature correctly detected the change. |
| Site inspected, issuer, expiry date | youtube.com, 3 Nov, 26 Jan 27|
| TLS version and cipher | TLSv1.3, TLS_AES_256_GCM_SHA384 |
| Same password hashed twice with **no salt**: same digest? | Yes |
| Same password with **salt**: same digest? | No |
| MD5 vs SHA-256 vs PBKDF2 timing | SHA-256 hashes : 0.097s, PBKDF2 : 0.178s |

### Observations
- What surprised me:
- What I'd improve in my scripts:

## Interview questions
Answer each in your own words, out loud first, then write 3 to 5 sentences. Hints show what to cover.

## Interview questions

### 1. What is cryptography?
Cryptography is the practice of protecting information using mathematical techniques so that it can only be accessed, read, or modified by authorized parties. Its core goals are confidentiality (keeping data secret), integrity (detecting tampering), authentication (proving identity), and non-repudiation (proving an action can't be denied after the fact). For example, when you log into online banking over HTTPS, cryptography encrypts your session so an attacker on the same network can't read your password or account data in transit.

### 2. What is the difference between encryption and hashing?
Encryption is a two-way process: data is scrambled using a key and can be reversed back to its original form using the same or a related key. Hashing is one-way: it produces a fixed-size digest from input data, and there's no key, no way to reverse it back to the original input. Encryption is used for secrecy (e.g., encrypting a file so only someone with the key can read it), while hashing is used for integrity checks (e.g., verifying a downloaded file hasn't been corrupted or altered) and for storing passwords without keeping the plaintext.

### 3. What is the difference between AES and RSA?
AES is a symmetric algorithm, meaning the same key is used to both encrypt and decrypt data, and it's very fast, making it ideal for encrypting large amounts of data like files or network traffic. RSA is asymmetric, using a mathematically linked key pair — a public key to encrypt or verify, and a private key to decrypt or sign — but it's much slower and typically limited to small amounts of data like a symmetric key or a signature. TLS combines both: RSA (or another asymmetric algorithm) is used during the handshake to securely exchange a symmetric session key, and then AES is used to encrypt the actual bulk data for the rest of the connection.

### 4. What is a public key?
A public key is the shareable half of an asymmetric key pair, and it's designed to be given out freely — to anyone, over any channel. It's used to encrypt data so that only the matching private key can decrypt it, or to verify a signature that was created with the private key. Sharing it is safe because the mathematical relationship between the two keys makes it computationally infeasible to derive the private key from the public key alone.

### 5. What is a private key?
A private key is the secret half of an asymmetric key pair, and it must never be shared or exposed to anyone else. It's used to decrypt data that was encrypted with the matching public key, or to create digital signatures that others can verify using the public key. It should be protected with strict file permissions (e.g., 600, owner read/write only), encrypted with a strong passphrase, and never committed to source control or shared over insecure channels.

### 6. What is SHA-256?
SHA-256 is a cryptographic hash function that takes an input of any size and produces a fixed 256-bit (32-byte) output, called a digest or hash. It's deterministic (the same input always produces the same output) and one-way (you can't reverse the hash back to the original input). It exhibits the avalanche effect, meaning even a tiny change to the input completely changes the output, and it's designed to be collision-resistant, meaning it's computationally infeasible to find two different inputs that produce the same hash. It's commonly used for verifying file integrity, in digital signatures, and in blockchain systems.

### 7. Why is MD5 considered insecure?
MD5 is considered broken because researchers have demonstrated practical collision attacks, meaning two different inputs can be crafted to produce the same hash — this undermines its ability to prove integrity against a deliberate attacker who wants to swap in malicious data without changing the hash. It's also extremely fast to compute, which is bad specifically for password hashing because it makes brute-force and dictionary attacks cheap to run at scale. MD5 is still acceptable for non-security purposes, like quickly checking if a file was accidentally corrupted during a transfer, but it should never be used for passwords, signatures, or anything security-critical.

### 8. What is salting in password hashing?
A salt is a random value generated uniquely per user (or per password) that gets added to the password before it's hashed. This means that even if two users have the identical password, their stored hashes will look completely different, which defeats precomputed rainbow table attacks and prevents an attacker from cracking many accounts at once using a single shared hash lookup. Salting is typically paired with a slow, purpose-built password hashing algorithm like PBKDF2, bcrypt, scrypt, or Argon2 rather than a fast general-purpose hash like SHA-256. Importantly, the salt itself isn't secret — it's usually stored right alongside the hash — its purpose is uniqueness, not secrecy.

### 9. What is the difference between Base64 and encryption?
Base64 is an encoding scheme, not an encryption scheme — it converts binary data into ASCII text for safe transport, but it provides zero confidentiality. There's no key involved, and it's trivially reversible by anyone using a single line of code or even an online tool, with no secret knowledge required. Base64 commonly appears in contexts like JWT headers/payloads and HTTP Basic Authentication headers, and in both cases it's easy to mistake it for "encrypted" when it's really just obscured, readable data.

### 10. What is a digital certificate?
A digital certificate binds a public key to a verified identity (like a domain name or organization), and it's digitally signed by a trusted Certificate Authority (CA) to vouch for that binding. Key fields typically include the subject, issuer, public key, validity dates, and the CA's signature. Trust is established through a chain of trust, where the certificate is signed by an intermediate CA, which is in turn signed by a root CA that's already trusted by your browser or operating system. If a certificate is invalid — expired, self-signed, issued for the wrong domain, or revoked — browsers will show a warning or block the connection entirely, since the identity of the server can no longer be reliably verified.

### 11. What is TLS?
TLS (Transport Layer Security) is a protocol that secures data in transit over a network, and it's the modern successor to the now-deprecated SSL protocol. It provides authentication (verifying the server's identity via its certificate), key exchange (securely agreeing on a shared session key), encryption (protecting data confidentiality), and integrity (detecting if data was tampered with in transit). HTTPS is simply HTTP running over TLS, and the two most relevant versions in use today are TLS 1.2 and TLS 1.3, with 1.3 being faster and more secure due to a simplified handshake and the removal of outdated cryptographic options.

### 12. What is the difference between authentication and authorization?
Authentication verifies who you are, while authorization determines what you're allowed to do once your identity has been confirmed. Authentication always happens first, since a system can't decide your permissions before it knows who it's dealing with. For example, logging in with a username and password is authentication, while being allowed (or denied) access to an admin panel afterward is authorization. This distinction also maps to HTTP status codes: a 401 Unauthorized response means authentication failed or is missing, while a 403 Forbidden response means you were authenticated but aren't permitted to access that specific resource — and a common real-world vulnerability called broken access control occurs when authorization checks are missing or flawed even though authentication works correctly.

**My answer:**

---
## Self-assessment
| Questions | Confident (Y/N) | Needs review |
|---|---|---|
| 1-3 | | |
| 4-6 | | |
| 7-9 | | |
| 10-12 | | |

## Concept summary (from memory)
| Concept | One-line definition | Example |
|---|---|---|
| Encryption | | |
| Hashing | | |
| Encoding | | |
| Digital signature | | |
| Certificate | | |
| TLS | | |
| Authentication | | |
| Least privilege | | |

## GitHub upload checklist
- [ ] All seven plan files committed
- [ ] Evidence added and redacted
- [ ] **No private keys, passphrases, tokens or real passwords committed** (check with `git status` before committing)

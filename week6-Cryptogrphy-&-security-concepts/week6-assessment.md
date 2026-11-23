# Week 6: Practical Lab and Assessment
**Date:** 23 · **Time:** 60 min

## Practical lab checklist
Save outputs (redacted) in `evidence/`.

| # | Task | How | Done |
|---|---|---|---|
| 1 | Hash a file using SHA-256 | `python3 day4-hashing.py` (or `sha256sum test.txt`) | [ Y ] |
| 2 | Change the file, hash again, compare | Edit `test.txt`, re-run | [ Y ] |
| 3 | Generate encryption keys | `python3 scripts/day3_keypair.py` and the AES demo | [ ] |
| 4 | Inspect a website's TLS certificate | `python3 scripts/day5_cert_inspect.py <site>` | [ ] |
| 5 | Test password hashing concepts | `python3 scripts/day7_password_hashing.py` | [ ] |

### Lab results
| Check | Result |
|---|---|
| SHA-256 of `test.txt` (original) | 01f3b04fa8d66d9c95855a0564b1ef9eb0bf7ed2195a38f76efb84965208eb23 |
| SHA-256 after my change | 2b0c70133653567ae1c34e6feb64b048b0820a507509aa48035f712256a2ae1d |
| Do they match? Why? | No |
| Key pair generated (type and size) | RSA, 2048 bits |
| Signature verified? After tampering? | |
| Site inspected, issuer, expiry date | |
| TLS version and cipher | |
| Same password hashed twice with **no salt**: same digest? | |
| Same password with **salt**: same digest? | |
| MD5 vs SHA-256 vs PBKDF2 timing | |

### Observations
- What surprised me:
- What I'd improve in my scripts:

## Interview questions
Answer each in your own words, out loud first, then write 3 to 5 sentences. Hints show what to cover.

### 1. What is cryptography?
*Cover:* protecting information with math, goals (confidentiality, integrity, authentication, non-repudiation), a real example.

**My answer:**

### 2. What is the difference between encryption and hashing?
*Cover:* two-way vs one-way, key vs no key, purposes (secrecy vs integrity), examples.

**My answer:**

### 3. What is the difference between AES and RSA?
*Cover:* symmetric vs asymmetric, one key vs a pair, speed, use cases, how TLS combines them.

**My answer:**

### 4. What is a public key?
*Cover:* shareable half of the pair, what it does (encrypt to the owner, verify signatures), why sharing it is safe.

**My answer:**

### 5. What is a private key?
*Cover:* the secret half, what it does (decrypt, sign), how to protect it (permissions, passphrase, never commit).

**My answer:**

### 6. What is SHA-256?
*Cover:* a hash function, 256-bit fixed output, deterministic, one-way, avalanche effect, collision resistance, uses.

**My answer:**

### 7. Why is MD5 considered insecure?
*Cover:* collisions can be created, so it can't prove integrity against an attacker, and it's fast, so password guessing is cheap. Still OK for non-security checksums.

**My answer:**

### 8. What is salting in password hashing?
*Cover:* a random per-user value added before hashing, same password gives a different hash, defeats rainbow tables and shared-hash cracking, pair with a slow hash (PBKDF2, bcrypt, scrypt, Argon2). The salt isn't secret.

**My answer:**

### 9. What is the difference between Base64 and encryption?
*Cover:* encoding vs secrecy, no key, trivially reversible, where Base64 appears (JWT, Basic auth).

**My answer:**

### 10. What is a digital certificate?
*Cover:* binds a public key to an identity, signed by a CA, key fields, chain of trust, what happens when it's invalid.

**My answer:**

### 11. What is TLS?
*Cover:* protocol that secures data in transit, replaced SSL, authentication, key exchange, encryption, integrity, HTTPS = HTTP over TLS, versions 1.2 and 1.3.

**My answer:**

### 12. What is the difference between authentication and authorization?
*Cover:* who you are vs what you can do, order, examples, 401 vs 403, broken access control.

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

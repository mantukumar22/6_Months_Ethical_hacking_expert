# Week 6: Cryptography & Security Concepts

**7 days · 1 hour/day**

Goal: understand how cryptography protects information, how authentication works, and how security mechanisms are used in real-world systems. By the end of the week I understand **encryption, hashing, encoding, digital signatures, certificates, TLS/HTTPS and authentication**.

> **Safety rules**
> - Use well-tested libraries. **Never invent my own cryptography.**
> - Never commit private keys, passphrases, tokens or real passwords. `keys/` and `*.pem` are git-ignored.
> - Only hash, test or crack things I own (my own test files and sample passwords).
> - Inspect certificates by making a normal TLS connection to a site. Don't attack or scan servers.

## Setup
```
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt    # installs the "cryptography" library
```
Hashing (Day 4) uses only the standard library.

## Roadmap

| Day | Topic | File |
|---|---|---|
| 1 | Introduction to Cryptography | [day1-cryptography.md](day1-cryptography.md) |
| 2 | Symmetric Encryption (AES) | [day2-symmetric-encryption.md](day2-symmetric-encryption.md), `scripts/day2_aes_demo.py` |
| 3 | Asymmetric Encryption (RSA) | [day3-asymmetric-encryption.md](day3-asymmetric-encryption.md), `scripts/day3_keypair.py` |
| 4 | Hashing | [day4-hashing.py](day4-hashing.py), `scripts/day7_password_hashing.py` |
| 5 | Encoding, Certificates and TLS | [day5-tls-certificates.md](day5-tls-certificates.md), `scripts/day5_cert_inspect.py` |
| 6 | Authentication and Security Concepts | [day6-authentication.md](day6-authentication.md) |
| 7 | Practical Lab and Assessment | [week6-assessment.md](week6-assessment.md) |

Each day: **20 min** learn → **30 min** practice → **10 min** notes.

## Video resources (YouTube searches)

| Day | Search |
|---|---|
| 1 | [Cryptography fundamentals](https://www.youtube.com/results?search_query=cryptography+fundamentals+cybersecurity) |
| 2 | [AES encryption explained](https://www.youtube.com/results?search_query=AES+encryption+explained) |
| 3 | [RSA encryption explained](https://www.youtube.com/results?search_query=RSA+public+private+key+explained) |
| 4 | [Hashing and SHA-256](https://www.youtube.com/results?search_query=hashing+SHA256+cybersecurity) |
| 5 | [SSL TLS HTTPS explained](https://www.youtube.com/results?search_query=SSL+TLS+HTTPS+handshake+explained) |
| 6 | [Authentication and authorization](https://www.youtube.com/results?search_query=authentication+authorization+MFA+cybersecurity) |
| 7 | [Cryptography practical Python](https://www.youtube.com/results?search_query=Python+cryptography+hands+on+tutorial) |

Pick one good video per day and note its title in that day's file.

## Folder layout
```
week6/
├── README.md
├── checklist.md
├── requirements.txt
├── test.txt                      sample file for the hashing exercises
├── day1-cryptography.md
├── day2-symmetric-encryption.md
├── day3-asymmetric-encryption.md
├── day4-hashing.py
├── day5-tls-certificates.md
├── day6-authentication.md
├── week6-assessment.md
├── scripts/                      AES, RSA, certificate and password-hashing demos
├── evidence/                     lab screenshots and outputs (redacted)
└── keys/                         generated keys (git-ignored)
```
The seven files named in the plan are included. The rest are extras. Drop the whole `week6/` folder into the cybersecurity learning repo.

## Progress
See [checklist.md](checklist.md). **0/7** done.

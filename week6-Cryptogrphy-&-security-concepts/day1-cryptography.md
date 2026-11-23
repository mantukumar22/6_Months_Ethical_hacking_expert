# Day 1: Introduction to Cryptography
**Date:** 19 · **Time:** 60 min
**Video:** Cryptography fundamentals: <paste title/URL>

## Learn (20 min)

### What is cryptography?
**Cryptography** is the practice of protecting information using mathematics, so that only the intended people can read it, and so that changes or fakes can be detected. It supports the **CIA Triad** from Week 5.

| Goal | Meaning | Tool |
|---|---|---|
| **Confidentiality** | Only authorized people can read the data | Encryption |
| **Integrity** | The data hasn't been altered | Hashing, MACs, signatures |
| **Authentication** | You are talking to who you think | Certificates, signatures, passwords |
| **Non-repudiation** | The sender can't deny sending it | Digital signatures |

### The four terms to remember

| Term | Meaning |
|---|---|
| **Plaintext** | Original readable data |
| **Ciphertext** | Encrypted, unreadable data |
| **Encryption** | Converts plaintext into ciphertext |
| **Decryption** | Converts ciphertext back into plaintext |

```
Plaintext --[encrypt + key]--> Ciphertext --[decrypt + key]--> Plaintext
```

### Algorithm (cipher) and key
- The **algorithm** is the method (e.g. AES). It is **public**.
- The **key** is the secret value that controls it. **Security depends on the key, not on hiding the algorithm** (Kerckhoffs's principle).
- Longer keys mean more possible keys, so brute-forcing gets infeasible (AES-256 has 2^256 keys).
- Weak or reused keys, and keys stored badly, are the usual real-world failures.

### The three families (the plan for the week)

| Family | Keys | Example | Used for | Day |
|---|---|---|---|---|
| **Symmetric encryption** | One shared secret key | AES | Encrypting data fast | 2 |
| **Asymmetric encryption** | Public + private key pair | RSA | Key exchange, signatures | 3 |
| **Hashing** | No key | SHA-256 | Integrity, password storage | 4 |

**Encoding is not cryptography.** Base64 and URL-encoding just change the format and anyone can reverse them (Day 5).

### Data in different states
| State | Example | Protection |
|---|---|---|
| At rest | Files on a disk, database | Disk or file encryption |
| In transit | Browser to server | TLS / HTTPS |
| In use | Data being processed in memory | Harder, access control |

### Real-world examples
| Where | What cryptography does |
|---|---|
| HTTPS (padlock) | Encrypts traffic, proves the site's identity |
| WhatsApp / Signal | End-to-end encryption of messages |
| Password storage | Stores a hash, not the password |
| Software updates | Digital signatures prove the update is genuine |
| Wi-Fi (WPA2/WPA3) | Encrypts wireless traffic |
| Disk encryption (BitLocker, LUKS) | Protects data if a laptop is stolen |
| Banking cards and payments | Encryption and signatures protect transactions |

### Classic example (history)
The **Caesar cipher** shifts each letter by a fixed number (key = 3: `A→D`). It is trivially broken because there are only 25 keys. Modern ciphers like AES exist because attackers have computers.

### Golden rules
1. **Never invent your own cryptography.** Use vetted libraries.
2. Keep keys secret, and never hardcode them in code or commit them to Git.
3. Use modern, current algorithms. Old ones (DES, RC4, MD5, SHA-1) are broken for security uses.

## Practice (30 min)
### Your first task: answer from your own understanding
# Cryptography Basics: Q&A

## 1. What is the difference between encryption and hashing?

**My answer:**

Encryption and hashing both transform data, but they serve different purposes.

| | Encryption | Hashing |
|---|---|---|
| **Purpose** | Keep data confidential | Verify data integrity |
| **Reversible?** | Yes, with the correct key (decryption) | No, it is a one-way function |
| **Uses a key?** | Yes | No (except keyed variants such as HMAC) |
| **Output size** | Varies with input size | Fixed length (e.g. 256 bits for SHA-256) |
| **Examples** | AES, RSA, ChaCha20 | SHA-256, SHA-3, bcrypt, Argon2 |

- **Encryption** turns plaintext into ciphertext so that only someone with the right key can recover the original. Use it when you need to read the data again later (e.g. HTTPS traffic, encrypted files).
- **Hashing** turns any input into a fixed-size digest. The same input always gives the same output, and the original cannot feasibly be recovered from it. Use it for password storage, file integrity checks, and digital signatures.

---

## 2. Why do we use cryptographic keys?

**My answer:**

A cryptographic key is the secret (or public/private pair) that controls how an algorithm encrypts, decrypts, signs, or verifies data.

- **Security depends on the key, not the algorithm.** Algorithms such as AES are public and heavily reviewed. If security relied on hiding the algorithm, it would break once the algorithm leaked (Kerckhoffs's principle).
- **Reusable algorithms.** The same algorithm can protect many users and messages, each with a different key.
- **Access control.** Only holders of the right key can decrypt or sign. Compromising one key does not compromise others.
- **Enables key-based features:**
  - *Confidentiality*: encrypting and decrypting data.
  - *Authentication*: proving who you are (e.g. private key in SSH or TLS).
  - *Integrity and non-repudiation*: digital signatures and MACs.
- **Two kinds of keys:**
  - *Symmetric*: one shared secret key (AES).
  - *Asymmetric*: a public/private key pair (RSA, ECC), which allows secure communication without sharing a secret in advance.

---

## 3. Is Base64 encryption? Explain why.

**My answer:**

**No. Base64 is encoding, not encryption.**

- **No key and no secret.** Anyone can decode Base64 instantly using a standard, publicly known algorithm.
- **Purpose is data representation.** It converts binary data into plain ASCII text (using `A-Z`, `a-z`, `0-9`, `+`, `/`) so it can travel safely through text-only systems such as email (MIME), JSON, URLs, and HTML.
- **Provides no confidentiality.** It only makes data look scrambled. It also increases size by about 33%.

Example:

```
Plain text : hello
Base64     : aGVsbG8=
```

Decoding `aGVsbG8=` returns `hello` with no key needed.

> **Never use Base64 to protect sensitive data** such as passwords or tokens. Use proper encryption (e.g. AES) for confidentiality and a proper password hash (e.g. bcrypt or Argon2) for passwords.

### Classify
| Situation | Which tool? (encryption / hashing / encoding / signature) |
|---|---|
| Storing a user's password in a database | Encryption |
| Sending a credit card number to a shop | Encryption |
| Embedding an image inside an HTML email | Encoding |
| Proving that a downloaded installer is genuine | Signature |
| Checking that a file wasn't corrupted | hashing |

### Try the Caesar cipher (5 lines of Python, for fun only)
```python
def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

print(caesar("Hello", 3))      # Khoor
print(caesar("Khoor", -3))     # Hello
```
Then brute-force it: loop shifts 1 to 25 and read the results. This shows why small key spaces are insecure.

# Cryptography Notes (10 min)

## In my own words: what is cryptography for?

Cryptography is the toolbox for protecting information when you can't trust the channel or the people who might see it. It lets me keep data **secret** (encryption), check that it hasn't been **changed** (hashing, MACs), and prove **who** it came from (digital signatures), even over an untrusted network like the internet.

## Three real-world places I used cryptography today without noticing

1. **HTTPS (the padlock in the browser):** TLS encrypts everything between my browser and the website, including logins and payments.
2. **Messaging apps (e.g. WhatsApp, Signal):** end-to-end encryption means only my device and the recipient's device can read the messages.
3. **Phone unlock and app logins:** the passcode or fingerprint is checked against a stored hash or protected by device encryption, and the password is never stored in plain text.

*(Other common ones: Wi-Fi WPA2/WPA3, UPI or card payments, software updates verified by digital signatures.)*

---

## Self-check

### 1. What is the difference between plaintext and ciphertext?

- **Plaintext** is the original, readable data (a message, a file, a card number).
- **Ciphertext** is the scrambled output after encryption, which looks like random data and is unreadable without the key.
- Encryption turns plaintext into ciphertext. Decryption (with the correct key) turns it back.

### 2. Why is the algorithm public but the key secret?

- **Kerckhoffs's principle:** a system should stay secure even if everything about it, except the key, is public.
- Public algorithms (AES, RSA) are reviewed by thousands of experts, so weaknesses get found and fixed. Secret, home-made algorithms tend to hide flaws.
- Secrets are hard to keep. It is far easier to protect and replace a short key than to keep a whole algorithm hidden or to replace it after a leak.
- Many people can use the same algorithm safely, each with their own key.

### 3. Which of C, I and A does encryption mainly protect?

**C: Confidentiality.**

- **C**onfidentiality: only authorized people can read the data. **Encryption mainly protects this.**
- **I**ntegrity: the data hasn't been altered. This is protected mainly by hashes, MACs, and signatures.
- **A**vailability: the data and systems are accessible when needed. This is protected by backups, redundancy, and DDoS protection.

> Encryption alone does not guarantee integrity. Modern schemes (e.g. AES-GCM) combine encryption with an authentication tag to cover both.

## Mistake I fixed / still confusing
-

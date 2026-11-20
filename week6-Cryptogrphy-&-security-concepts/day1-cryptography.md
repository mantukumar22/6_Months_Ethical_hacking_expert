# Day 1: Introduction to Cryptography
**Date:** ____ · **Time:** 60 min
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
1. What is the difference between encryption and hashing?
   - My answer:
2. Why do we use cryptographic keys?
   - My answer:
3. Is Base64 encryption? Explain why.
   - My answer:

### Classify
| Situation | Which tool? (encryption / hashing / encoding / signature) |
|---|---|
| Storing a user's password in a database | |
| Sending a credit card number to a shop | |
| Embedding an image inside an HTML email | |
| Proving that a downloaded installer is genuine | |
| Checking that a file wasn't corrupted | |

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

## Notes (10 min)
- In my own words: what is cryptography for?
- Three real-world places I used cryptography today without noticing:

## Self-check
1. What is the difference between plaintext and ciphertext?
2. Why is the algorithm public but the key secret?
3. Which of C, I and A does encryption mainly protect?

## Mistake I fixed / still confusing
-

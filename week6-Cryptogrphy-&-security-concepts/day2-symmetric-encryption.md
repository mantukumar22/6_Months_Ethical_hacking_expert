# Day 2: Symmetric Encryption
**Date:** 20 · **Time:** 60 min
**Video:** AES encryption explained: <paste title/URL>

## Learn (20 min)

### How it works
**Symmetric encryption** uses the **same secret key** to encrypt and decrypt.

```
Plaintext --[AES + key K]--> Ciphertext --[AES + key K]--> Plaintext
```
Both sides must already share the key, and keeping it secret is the whole problem. That is the **key distribution problem**, and asymmetric cryptography (Day 3) helps solve it.

### AES (Advanced Encryption Standard)
- The current standard symmetric cipher, a **block cipher** working on 128-bit blocks.
- Key sizes: **128, 192 or 256 bits**. AES-128 is already considered strong, and AES-256 is common for high-security needs.
- Fast, and often built into CPU hardware.
- Replaced **DES** (56-bit key, brute-forced) and **3DES** (deprecated).

### Modes of operation
A block cipher alone only handles one block, so a **mode** defines how to handle more data.

| Mode | Notes |
|---|---|
| **ECB** | Same plaintext block gives the same ciphertext block, which leaks patterns (the famous "ECB penguin"). **Never use.** |
| **CBC** | Chains blocks with an **IV** (random starting value). No built-in integrity, so it can be tampered with unless a MAC is added |
| **CTR** | Turns AES into a stream cipher, no integrity either |
| **GCM** | **Authenticated encryption (AEAD):** gives confidentiality **and** integrity. **Use this by default** |

### Key terms
| Term | Meaning |
|---|---|
| **IV / nonce** | A value that must be **unique** (random for CBC, never reused for GCM) for every encryption with the same key. It's not secret and is stored with the ciphertext |
| **Authentication tag** | Check value in GCM. If ciphertext is changed, decryption **fails** |
| **Padding** | Fills the last block to full size (CBC) |
| **Key derivation (KDF)** | Turns a password into a key properly (PBKDF2, scrypt, Argon2). Never use a raw password as a key |
| **AEAD** | Authenticated Encryption with Associated Data |

**Critical mistake:** reusing a nonce with the same key in GCM can destroy its security.

### Advantages and limitations
| Advantages | Limitations |
|---|---|
| Very fast, good for large data | **Key distribution:** how do both sides get the key safely? |
| Strong with modern algorithms (AES) | Many users means many keys (n people need n(n-1)/2 pairs) |
| Hardware support | Doesn't prove **who** sent a message (shared key) |

### Where it is used
Disk and file encryption, VPNs, Wi-Fi (WPA2/3), the bulk data encryption inside TLS, encrypted backups, database encryption.

## Practice (30 min): Python AES demo
Setup (once):
```
python3 -m venv .venv && source .venv/bin/activate
pip install cryptography
```
Run [scripts/day2_aes_demo.py](scripts/day2_aes_demo.py):
```
python3 scripts/day2_aes_demo.py
```
It encrypts with AES-256-GCM, decrypts, then **tampers with the ciphertext** to show decryption failing.

### Experiments
1. Run it twice. Is the ciphertext the same? Why not? (random nonce)
2. Decrypt with a **wrong key**. What happens?
3. Flip one byte of the ciphertext. What happens, and what does that prove?
4. Why must the nonce be stored with the ciphertext?

| Observation | Explanation |
|---|---|
| Ciphertext differs on each run | |
| Wrong key result | |
| Tampered ciphertext result | |

## Notes (10 min)
- Symmetric encryption in one sentence:
- Why GCM over ECB:
- The main weakness of symmetric encryption:

## Self-check
1. What does "symmetric" mean here?
2. What are AES's key sizes?
3. Why is ECB mode unsafe?
4. What is the key distribution problem?

## Mistake I fixed / still confusing
-

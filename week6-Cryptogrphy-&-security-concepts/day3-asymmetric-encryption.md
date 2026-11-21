# Day 3: Asymmetric Encryption
**Date:** 21 · **Time:** 60 min
**Video:** RSA encryption explained: <paste title/URL>

## Learn (20 min)

### Public key and private key
**Asymmetric (public-key) cryptography** uses a **mathematically linked key pair**:

| Key | Who has it | Used for |
|---|---|---|
| **Public key** | Anyone, share freely | Encrypt data to the owner, verify the owner's signatures |
| **Private key** | Only the owner, **never shared** | Decrypt data, create signatures |

```
Encryption:   sender --[recipient's PUBLIC key]--> ciphertext --[recipient's PRIVATE key]--> plaintext
Signature:    signer --[signer's PRIVATE key]--> signature --[signer's PUBLIC key]--> valid / invalid
```
You can't work out the private key from the public key in practice. That removes the key distribution problem of symmetric encryption.

### RSA
- Based on the difficulty of **factoring a product of two large primes**.
- Key sizes: **2048 bits minimum** today (3072+ for longer-term). 1024 is broken.
- **Slow**, so it's used for small data: keys, signatures, not bulk files.
- Use proper padding: **OAEP** for encryption and **PSS** for signatures. "Textbook RSA" is insecure.
- Other asymmetric algorithms: **ECC** (ECDSA, Ed25519, ECDH) gives the same security with smaller keys, and **Diffie-Hellman** is for key exchange.

### Key exchange concept
Asymmetric crypto is slow and symmetric is fast, so real systems combine them (**hybrid encryption**):
1. Use asymmetric crypto (or Diffie-Hellman) to agree on a **session key**.
2. Use that key with AES to encrypt the actual data.

This is exactly what **TLS** does (Day 5). With **Diffie-Hellman**, two parties each combine their private value with the other's public value and arrive at the **same shared secret**, even though an eavesdropper sees only the public values. **Ephemeral** versions (ECDHE) give **forward secrecy**: stealing a server's long-term key later doesn't decrypt past traffic.

### Digital signatures
A **digital signature** proves **who** created a message (authenticity), that it **wasn't changed** (integrity), and that the signer **can't deny it** (non-repudiation).

1. Hash the message (SHA-256).
2. Sign the hash with the **private key**.
3. The receiver verifies the signature with the **public key** and compares it to their own hash of the message.

| Encryption | Signing |
|---|---|
| Uses recipient's **public** key to encrypt | Uses signer's **private** key to sign |
| Goal: confidentiality | Goal: authenticity, integrity |

Real uses: software and code signing, TLS certificates, signed emails, Git commit signing, SSH keys.

### Symmetric vs asymmetric

| | Symmetric (AES) | Asymmetric (RSA) |
|---|---|---|
| Keys | One shared | Public + private |
| Speed | Fast | Slow |
| Best for | Bulk data | Key exchange, signatures |
| Main problem | Sharing the key | Speed, trusting that a public key is really the owner's (solved by certificates) |

## Practice (30 min): generate a key pair
Run [scripts/day3_keypair.py](scripts/day3_keypair.py):
```
python3 scripts/day3_keypair.py
```
It creates an RSA-2048 pair in `keys/` (git-ignored), signs a message, verifies it, tampers with it to show verification failing, and encrypts and decrypts a short message with OAEP.

### With OpenSSL (same idea from the command line)
```
openssl genrsa -out keys/private.pem 2048
openssl rsa -in keys/private.pem -pubout -out keys/public.pem
openssl rsa -in keys/private.pem -text -noout | head
```
Open both PEM files. Note which header says `PRIVATE KEY` and which says `PUBLIC KEY`.

**SSH link (Week 2):** `ssh-keygen -t ed25519` creates the same kind of pair. The `.pub` file is shared, and the private file must stay at `chmod 600`.

### Questions
1. Which key encrypts and which decrypts when sending a secret to Alice? Public key encrypts nd private key decrypts.
2. Which key signs and which verifies? Private Key signs & Pubic key verifies .
3. What happens if you change one character of the signed message? Verification **fails** with `InvalidSignature`.
4. Why is the private key file permission important? (Week 3, `chmod 600`) The private key is the **only secret** in public-key crypto. Whoever has a copy can
decrypt messages sent to you and sign as you, and nothing in the math can tell them
apart from the real owner.

# Day 3 Notes: Public-Key Cryptography

## Notes (10 min)

- **Public key in one sentence:** The public key is the shareable half of a key pair, used to encrypt data *to* the key's owner or to verify signatures made by them.
- **Private key in one sentence:** The private key is the secret half of the pair, used to decrypt data sent to its owner or to create digital signatures, and it must never be shared.
- **Why TLS uses both asymmetric and symmetric crypto:** Asymmetric crypto (RSA, ECDHE) solves the key-distribution problem, letting two strangers agree on a secret and authenticate each other over an open network, but it is slow and limited to small data. Symmetric crypto (AES-GCM) is fast and handles bulk data, but both sides need the same key first. TLS uses asymmetric crypto for the handshake to establish a shared session key, then switches to symmetric crypto for the actual traffic.

## Self-check

### 1. Why can the public key be shared openly?

Deriving the private key from the public key is computationally infeasible (for RSA, it would require factoring a huge number). The public key can only *encrypt* and *verify*; it cannot decrypt or sign. Anyone holding it gains no ability to read your messages or forge your signatures. (What does matter is that it is **authentic**, i.e. really belongs to who you think, which is why certificates exist.)

### 2. What is a digital signature for?

A digital signature provides:

- **Authenticity:** proves the message came from the holder of the private key.
- **Integrity:** any change to the message makes verification fail (e.g. "Pay 100" vs "Pay 900").
- **Non-repudiation:** the signer can't plausibly deny having signed it.

It does **not** hide the message; it only proves who wrote it and that it is unaltered.

### 3. Why is RSA not used to encrypt large files?

- **Size limit:** RSA can only encrypt data smaller than its key size minus padding overhead (about 190 bytes for RSA-2048 with OAEP/SHA-256).
- **Speed:** RSA is orders of magnitude slower than AES.

The standard solution is **hybrid encryption**: encrypt the file with a random AES key, then encrypt only that small AES key with RSA.

### 4. What is forward secrecy?

Forward secrecy (also called *perfect forward secrecy*, PFS) means that **compromising a long-term private key later does not expose past sessions.**

- Each session uses a fresh, temporary (**ephemeral**) key pair, typically via ECDHE or DHE key exchange.
- The session key is derived from these ephemeral values and discarded after the session. The long-term key is used only to *authenticate* the handshake, not to encrypt the session key.
- **Without PFS** (e.g. old RSA key exchange): an attacker who records traffic today and steals the server's private key next year can decrypt everything recorded.
- **With PFS:** the stolen key reveals nothing about past sessions, because the ephemeral keys no longer exist.

TLS 1.3 mandates forward secrecy; static RSA key exchange was removed.

## Quick reference

| Concept | Asymmetric (RSA/ECC) | Symmetric (AES) |
|---|---|---|
| Keys | Pair (public + private) | One shared key |
| Speed | Slow | Fast |
| Data size | Small only | Any size |
| Role in TLS | Handshake, authentication, key agreement | Bulk data encryption |

## Mistake I fixed / still confusing
-

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
1. Which key encrypts and which decrypts when sending a secret to Alice?
2. Which key signs and which verifies?
3. What happens if you change one character of the signed message?
4. Why is the private key file permission important? (Week 3, `chmod 600`)

## Notes (10 min)
- Public key in one sentence:
- Private key in one sentence:
- Why TLS uses both asymmetric and symmetric crypto:

## Self-check
1. Why can the public key be shared openly?
2. What is a digital signature for?
3. Why is RSA not used to encrypt large files?
4. What is forward secrecy?

## Mistake I fixed / still confusing
-

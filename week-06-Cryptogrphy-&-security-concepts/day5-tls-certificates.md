# Day 5: Encoding, Certificates and TLS
**Date:** 22 · **Time:** 60 min
**Video:** SSL TLS HTTPS explained: <paste title/URL>

## Learn (20 min)

### Encoding
Encoding converts data from one format to another using a public, reversible scheme so it can be stored, transmitted, or displayed correctly. There is no key and no secret: anyone who knows the scheme can reverse it.

### Base64 Encoding
Base64 turns binary data into plain text using only 64 safe characters: A-Z, a-z, 0-9, +, /, with = used as padding. This lets binary data travel through systems built for text (email, JSON, URLs, HTTP headers).

### Base64 encoding vs encryption
| | Encoding | Encryption |
|---|---|---|
| Purpose | Change the **format** so data can be carried or stored | Keep data **secret** |
| Key needed? | **No** | **Yes** |
| Reversible by anyone? | **Yes** | Only with the key |
| Example | Base64, URL-encoding, hex | AES, RSA |

**Base64** turns binary data into 64 printable characters (A-Z, a-z, 0-9, `+`, `/`, with `=` padding). It is used in emails, data URLs, JWT tokens, HTTP Basic auth headers and PEM files.

```
echo -n "admin:password" | base64        # YWRtaW46cGFzc3dvcmQ=
echo "YWRtaW46cGFzc3dvcmQ=" | base64 -d  # admin:password
```
```python
import base64
base64.b64encode(b"admin:password")     # b'YWRtaW46cGFzc3dvcmQ='
base64.b64decode(b"YWRtaW46cGFzc3dvcmQ=")
```
**Base64 is not encryption.** Anything "protected" only by Base64 is effectively plain text (a common finding in web and API testing).

### Digital certificates
A **digital certificate** (X.509) binds a **public key to an identity** (such as a domain name), signed by a trusted party. It answers: *"Is this public key really example.com's?"*

| Field | Meaning |
|---|---|
| **Subject** | Who the certificate is for (domain or organization) |
| **Subject Alternative Names (SAN)** | All the domain names it covers |
| **Issuer** | The CA that signed it |
| **Validity (Not Before / Not After)** | The dates it's valid |
| **Public key** | The server's public key (RSA or ECC) |
| **Serial number** | Unique ID from the CA |
| **Signature algorithm** | How the CA signed it (e.g. SHA-256 with RSA) |

### Certificate Authority (CA)
A **CA** is a trusted organization that verifies identity and **signs certificates**. Examples: Let's Encrypt, DigiCert, Sectigo.

**Chain of trust:**
```
Root CA (pre-installed in your OS/browser)
   └── Intermediate CA
          └── Server certificate (example.com)
```
Your browser trusts the server certificate because a chain of valid signatures leads to a root CA it already trusts.

**Certificate warnings** happen when: it's expired, the name doesn't match the domain, it's self-signed, the chain doesn't reach a trusted root, or it was revoked. Never click through warnings on sites you don't control.

Types by validation: **DV** (domain only), **OV** (organization checked), **EV** (extended). The padlock never means the site is *trustworthy*, only that the connection is encrypted to that domain.

### SSL vs TLS
| | SSL | TLS |
|---|---|---|
| Status | **Deprecated** (SSL 2.0 and 3.0 are broken) | **Current** standard |
| Versions | SSL 2.0, 3.0 | TLS 1.0, 1.1 (deprecated), **1.2**, **1.3** |

People still say "SSL certificate", but modern HTTPS uses **TLS 1.2 or 1.3**. **HTTPS = HTTP over TLS**, on port 443 (Week 2).

### HTTPS handshake fundamentals (simplified)
```
Client                                          Server
  | -- ClientHello (TLS versions, ciphers) -->  |
  | <-- ServerHello + Certificate ------------  |
  |  [client checks: trusted CA? name match?    |
  |   dates valid? signature valid?]            |
  | -- key exchange (ECDHE) ------------------> |
  | <==== both derive the same session key ==== |
  | ======= AES-encrypted HTTP traffic ======== |
```
1. **Negotiate** the TLS version and cipher suite.
2. **Authenticate** the server through its certificate.
3. **Exchange keys** (asymmetric / Diffie-Hellman), and derive a **symmetric session key**.
4. **Encrypt** the data with that key (AES-GCM or ChaCha20).

TLS 1.3 is faster and removes weak options. It combines everything from this week: asymmetric crypto (key exchange and signatures), hashing (integrity), and symmetric crypto (bulk data).

**What HTTPS protects and doesn't hide:** content, URL path and headers are encrypted. The domain (via DNS and SNI), IP address and traffic volume are still visible (Week 2, Day 5).

## Practice (30 min): inspect an HTTPS certificate

### 1. In the browser
Click the **padlock / site-info icon** → connection is secure → certificate. Record: Issued to, Issued by, valid from/to, and look at the chain.

### 2. With Python
Run [scripts/day5_cert_inspect.py](scripts/day5_cert_inspect.py):
```
python3 scripts/day5_cert_inspect.py example.com
```

### 3. With OpenSSL
```
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -text | head -40
```

### Record (use any public site you normally visit)
| Field | Value |
|---|---|
| Site | |
| Subject / CN | |
| SANs | |
| Issuer (CA) | |
| Valid from / to | |
| Days until expiry | |
| TLS version / cipher | |
| Key type and size | |

### Base64 task
Encode `admin:password`, decode it back, then explain in one line why this is not security.

# Day 5 Notes: Encoding, Certificates and TLS

## Notes (10 min)

- **Base64 vs encryption:** Base64 is a public, keyless encoding that only changes the *format* of data (binary to text) so it can travel safely; anyone can reverse it. Encryption uses a secret key to make data unreadable to everyone *without* that key. Base64 gives no confidentiality; encryption does.
- **What a certificate proves:** A certificate (X.509) binds a **public key to an identity** (e.g. `example.com`), and it is **signed by a Certificate Authority**. It proves that the server presenting it is the legitimate owner of that domain's key, so the client isn't talking to an impostor (a man-in-the-middle).
- **Steps of the TLS handshake, in my own words (TLS 1.3):**
  1. **ClientHello:** the browser says "I want to talk securely." It sends its supported cipher suites and an ephemeral key share (its half of ECDHE).
  2. **ServerHello:** the server picks a cipher suite and sends its own ephemeral key share. Both sides can now compute the same shared secret and derive session keys. Everything after this is encrypted.
  3. **Certificate:** the server sends its certificate (and the chain to a CA).
  4. **CertificateVerify + Finished:** the server **signs** the handshake with its private key, proving it owns the certificate's key, and sends a Finished message to confirm nothing was tampered with.
  5. **Client verifies:** the client checks the CA signature, the domain name, the expiry date and revocation status, then sends its own Finished.
  6. **Secure data:** both sides now exchange traffic encrypted with the fast symmetric session key (AES-GCM or ChaCha20-Poly1305).

## Self-check

### 1. Why can anyone decode Base64?

Because Base64 is a **public, fixed algorithm with no key and no secret**. Decoding is just reversing the mapping of 6-bit groups to characters, and any tool (`base64 -d`, Python, online decoders) does it instantly. It exists for compatibility, not security.

### 2. What is a CA and why do we trust it?

A **Certificate Authority** is an organization (e.g. Let's Encrypt, DigiCert) that verifies a site's identity or domain control and then **signs its certificate** with the CA's private key.

We trust it because of the **chain of trust**:

- Operating systems and browsers ship with a built-in **trust store** of root CA certificates.
- A server's certificate is signed by an intermediate CA, which is signed by a root CA in the trust store.
- The client verifies each signature up the chain. If it reaches a trusted root, the certificate is accepted.
- CAs are audited, must follow strict industry rules, and are publicly logged (Certificate Transparency). A CA that misbehaves gets removed from trust stores.

### 3. What is the difference between SSL and TLS?

**TLS is the successor to SSL.** SSL (Netscape, SSL 2.0/3.0) was found to be insecure (e.g. the POODLE attack), and it was replaced by TLS (1.0, 1.1, 1.2, 1.3). All SSL versions and TLS 1.0/1.1 are deprecated. Only **TLS 1.2 and 1.3** should be used, preferably 1.3. People still say "SSL certificate" out of habit, but the protocol in use today is TLS.

### 4. Which keys does TLS use for the key exchange, and which for the bulk data?

| Purpose | Keys | Type |
|---|---|---|
| **Key exchange** | Ephemeral Diffie-Hellman key pairs (ECDHE/DHE), one per session | Asymmetric |
| **Authentication** | Server's long-term key (RSA or ECDSA) signs the handshake | Asymmetric |
| **Bulk data** | Session keys derived from the shared secret (AES-GCM or ChaCha20-Poly1305) | Symmetric |

Asymmetric crypto sets up trust and a shared secret; symmetric crypto then encrypts the actual traffic because it is much faster. Because the key exchange uses ephemeral keys, TLS gets **forward secrecy**. (In old TLS 1.2 RSA key exchange, the client encrypted the session key with the server's RSA public key instead, which had no forward secrecy and was removed in TLS 1.3.)

## Quick reference

| Concept | Role |
|---|---|
| Base64 | Format conversion, no security |
| Certificate | Binds a public key to an identity |
| CA | Trusted signer of certificates |
| Handshake | Agree on keys, authenticate the server |
| Session key | Fast symmetric encryption of the data |

## Mistake I fixed / still confusing
-

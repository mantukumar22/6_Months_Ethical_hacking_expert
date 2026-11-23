"""Day 3: RSA key pair, digital signature and OAEP encryption.

Requires:  pip install cryptography
Run:       python3 scripts/day3_keypair.py

Keys are written to ./keys/ (git-ignored). Lab keys only: never reuse them.
"""
import os
from getpass import getpass
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

KEYS_DIR = Path("keys")
KEYS_DIR.mkdir(exist_ok=True)

# 1. Generate the key pair (2048 bits minimum).
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 2. Save them. Protect the private key with a passphrase if you can.
passphrase = getpass("Passphrase for private key (blank = none, lab only): ")
if passphrase:
    encryption = serialization.BestAvailableEncryption(passphrase.encode())
else:
    print("WARNING: private key saved without a passphrase (lab only).")
    encryption = serialization.NoEncryption()

private_path = KEYS_DIR / "private.pem"
public_path = KEYS_DIR / "public.pem"
private_path.write_bytes(
    private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        encryption,
    )
)
os.chmod(private_path, 0o600)  # owner read/write only (Week 3)
public_path.write_bytes(
    public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
)
print(f"Saved {private_path} (PRIVATE, keep secret) and {public_path} (public).")
print("Key size:", private_key.key_size, "bits")

# 3. Sign a message with the PRIVATE key.
message = b"Pay 100 to Alice"
pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
signature = private_key.sign(message, pss, hashes.SHA256())
print("\nSignature (first 32 hex chars):", signature.hex()[:32], "...")

# 4. Verify with the PUBLIC key.
try:
    public_key.verify(signature, message, pss, hashes.SHA256())
    print("Original message : signature VALID")
except InvalidSignature:
    print("Original message : signature INVALID")

# 5. Tampered message -> verification fails.
try:
    public_key.verify(signature, b"Pay 900 to Alice", pss, hashes.SHA256())
    print("Tampered message : signature VALID (unexpected!)")
except InvalidSignature:
    print("Tampered message : signature INVALID (change detected)")

# 6. Encrypt with the PUBLIC key, decrypt with the PRIVATE key (OAEP).
oaep = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)
secret = b"session key: 0123456789abcdef"
encrypted = public_key.encrypt(secret, oaep)
print("\nEncrypted with public key (first 32 hex):", encrypted.hex()[:32], "...")
print("Decrypted with private key:", private_key.decrypt(encrypted, oaep).decode())
print("RSA can only encrypt SMALL data (a key, not a file): that's why TLS uses AES for bulk data.")

"""Day 2: AES-256-GCM encryption demo (symmetric, authenticated).

Requires:  pip install cryptography
Run:       python3 scripts/day2_aes_demo.py

Use a vetted library. Never write your own cipher.
"""
import os

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

plaintext = b"Confidential: server password is hunter2"

# 1. Key: 256 random bits. In real systems, protect it (key vault / KDF).
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# 2. Nonce: 12 random bytes, UNIQUE for every encryption with this key.
nonce = os.urandom(12)

# 3. Encrypt. The result includes the authentication tag.
ciphertext = aesgcm.encrypt(nonce, plaintext, None)

print("Plaintext :", plaintext.decode())
print("Key (hex) :", key.hex(), "(demo only: never print real keys)")
print("Nonce     :", nonce.hex())
print("Ciphertext:", ciphertext.hex())

# 4. Decrypt with the same key and nonce.
recovered = aesgcm.decrypt(nonce, ciphertext, None)
print("\nDecrypted :", recovered.decode())
assert recovered == plaintext

# 5. Wrong key -> fails.
try:
    AESGCM(AESGCM.generate_key(256)).decrypt(nonce, ciphertext, None)
except InvalidTag:
    print("Wrong key : decryption FAILED (as expected)")

# 6. Tampered ciphertext -> fails (integrity is protected).
tampered = bytearray(ciphertext)
tampered[0] ^= 1  # flip one bit
try:
    aesgcm.decrypt(nonce, bytes(tampered), None)
except InvalidTag:
    print("Tampered  : decryption FAILED, change detected (as expected)")

# 7. Encrypting the same text again gives different output (new nonce).
second = aesgcm.encrypt(os.urandom(12), plaintext, None)
print("\nSame plaintext, new nonce -> different ciphertext:", second != ciphertext)

"""Day 4/7: Password hashing concepts, with the standard library only.

Run: python3 scripts/day7_password_hashing.py
Uses sample passwords only. Never test real passwords or other people's data.
"""
import hashlib
import hmac
import os
import time

PASSWORD = "Summer2026!"        # sample password for the demo


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


print("== 1. Plain hashes are deterministic ==")
print("MD5    :", hashlib.md5(PASSWORD.encode()).hexdigest())
print("SHA-256:", sha256_hex(PASSWORD.encode()))
print("Same password -> same hash, for every user, everywhere.")
print("Attackers precompute these (rainbow tables / lookup tables).")

print("\n== 2. Two users, same password, NO salt ==")
alice = sha256_hex(PASSWORD.encode())
bob = sha256_hex(PASSWORD.encode())
print("Identical hashes?", alice == bob, "-> a leak reveals who shares passwords")

print("\n== 3. Add a random per-user SALT ==")
salt_a, salt_b = os.urandom(16), os.urandom(16)
alice = sha256_hex(salt_a + PASSWORD.encode())
bob = sha256_hex(salt_b + PASSWORD.encode())
print("Alice salt:", salt_a.hex())
print("Bob salt  :", salt_b.hex())
print("Identical hashes?", alice == bob, "-> precomputed tables no longer work")
print("(The salt is stored next to the hash. It isn't secret.)")

print("\n== 4. Fast vs slow hashing ==")
start = time.perf_counter()
for _ in range(100_000):
    hashlib.sha256(PASSWORD.encode()).digest()
fast = time.perf_counter() - start
print(f"100,000 SHA-256 hashes : {fast:.3f}s (an attacker can try millions/sec)")

start = time.perf_counter()
hashlib.pbkdf2_hmac("sha256", PASSWORD.encode(), salt_a, 600_000)
slow = time.perf_counter() - start
print(f"1 PBKDF2 (600k rounds) : {slow:.3f}s (deliberately slow)")
print("Password hashes should be SLOW + SALTED: PBKDF2, bcrypt, scrypt or Argon2.")


def hash_password(password: str):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)
    return salt, digest


def verify_password(password: str, salt: bytes, expected: bytes) -> bool:
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)
    return hmac.compare_digest(digest, expected)   # constant-time compare


print("\n== 5. Store and verify ==")
salt, stored = hash_password(PASSWORD)
print("Stored (salt, hash):", salt.hex()[:16] + "...", stored.hex()[:16] + "...")
print("Correct password :", verify_password(PASSWORD, salt, stored))
print("Wrong password   :", verify_password("summer2026", salt, stored))
print("\nNote: hashing is one-way. Login works by hashing the attempt and comparing.")

"""Week 6, Day 4: Hashing with Python's standard library.
Hashing is the process of running data of any size through a hash function to produce a fixed-length output called a hash (or digest), a kind of digital fingerprint of that data.
Run:  python3 day4-hashing.py
Uses test.txt from this folder (created if missing).

Learning goals
  - A hash turns any input into a fixed-length digest (SHA-256 = 256 bits).
  - Same input -> same hash. Tiny change -> completely different hash.
  - Hashing is one-way: you cannot "decrypt" it.
  - Use hashes to check file integrity.
  - For PASSWORDS, plain SHA-256/MD5 is not enough (see day7_password_hashing.py).
"""
import hashlib
from pathlib import Path


# ---------- Exercise 1: SHA-256 of a string ----------
def hash_text(message: str, algorithm: str = "sha256") -> str:
    digest = hashlib.new(algorithm, message.encode("utf-8"))
    return digest.hexdigest()


# ---------- Exercise 2: verify file integrity ----------
def hash_file(path: str, algorithm: str = "sha256") -> str:
    """Hash a file in chunks, so large files don't need to fit in memory."""
    digest = hashlib.new(algorithm)
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    # Exercise 1
    print("== Exercise 1: SHA-256 of a string ==")
    message = "Hello Cybersecurity"
    print("Message :", message)
    print("SHA-256 :", hash_text(message))

    # Properties of hashing
    print("\n== Properties ==")
    for text in ("Hello Cybersecurity", "Hello Cybersecurity!", "hello cybersecurity"):
        print(f"{text!r:28} -> {hash_text(text)[:32]}...")
    print("Note: a one-character change gives a completely different hash.")

    # Output sizes
    print("\n== Digest sizes (hex characters) ==")
    for algo in ("md5", "sha1", "sha256", "sha512"):
        print(f"{algo:7} {len(hash_text(message, algo)):4} hex chars"
              f" ({len(hash_text(message, algo)) * 4} bits)")
    print("MD5 and SHA-1 are broken for security use (collisions). Use SHA-256+.")

    # Exercise 2
    print("\n== Exercise 2: verify file integrity ==")
    path = Path("test.txt")
    if not path.exists():
        path.write_text("Hello Cybersecurity\n", encoding="utf-8")
    try:
        file_hash = hash_file(str(path))
    except OSError as error:
        raise SystemExit(f"Could not read {path}: {error}")
    print("SHA-256:", file_hash)

    # Exercise 3 (manual): change test.txt, run again, compare the hashes.
    saved = Path("test.txt.sha256")
    if saved.exists():
        previous = saved.read_text(encoding="utf-8").strip()
        if previous == file_hash:
            print("Integrity OK: file matches the saved hash.")
        else:
            print("WARNING: file CHANGED since the saved hash!")
            print("  saved  :", previous)
            print("  current:", file_hash)
    else:
        saved.write_text(file_hash + "\n", encoding="utf-8")
        print(f"Saved baseline hash to {saved}.")
        print("Now edit test.txt and run this script again (Exercise 3).")


if __name__ == "__main__":
    main()

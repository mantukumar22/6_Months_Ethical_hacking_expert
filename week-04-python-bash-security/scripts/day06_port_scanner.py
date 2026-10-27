#!/usr/bin/env python3
"""Day 6 reference: simple TCP connect checker.

For localhost or lab machines you own / are authorized to test ONLY.
It reports which TCP ports accept a connection. It is NOT a vulnerability
assessment. Write your own version first, then compare.
"""
import ipaddress
import socket
from datetime import datetime
from pathlib import Path

PORTS = [22, 80, 443, 8000, 8080]
TIMEOUT = 1  # seconds
OUTPUT = Path("scan_results.txt")


def validate_target(raw):
    """Allow loopback freely; private IPs only after an authorization check."""
    raw = raw.strip()
    if raw.lower() == "localhost":
        return "127.0.0.1"
    try:
        ip = ipaddress.ip_address(raw)
    except ValueError:
        raise SystemExit("Enter a valid IPv4 address or 'localhost'.")
    if ip.version != 4:
        raise SystemExit("IPv4 only in this exercise.")
    if ip.is_loopback:
        return str(ip)
    if ip.is_private:
        answer = input(
            f"{ip} is a private address. Do you own it or have written "
            "permission to test it? (yes/no): "
        )
        if answer.strip().lower() == "yes":
            return str(ip)
        raise SystemExit("Not authorized. Stopping.")
    raise SystemExit("Public addresses are not allowed in this exercise.")


def check_port(host, port):
    """Return 'open', 'closed' or 'filtered/no response', or an error text."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(TIMEOUT)
        try:
            sock.connect((host, port))
            return "open"
        except ConnectionRefusedError:
            return "closed"          # host answered with a reset
        except TimeoutError:
            return "filtered/no response"   # silence: firewall, or host down
        except OSError as error:
            return f"error: {error}"


def main():
    target = validate_target(input("Enter target (127.0.0.1 / localhost): "))
    started = datetime.now().isoformat(timespec="seconds")
    lines = [f"Scan of {target} at {started}"]
    open_count = 0

    for port in PORTS:
        state = check_port(target, port)
        if state == "open":
            open_count += 1
        line = f"{port}/tcp {state}"
        print(line)
        lines.append(line)

    lines.append(f"Summary: {open_count} open of {len(PORTS)} checked")
    print(lines[-1])

    try:
        OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Results saved to {OUTPUT}")
    except OSError as error:
        print("Could not save results:", error)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Classify listening sockets from `ss -tulnp` output.

Usage:
  python3 scripts/ss_report.py samples/ss-sample.txt     # read a saved file
  ss -tulnp | python3 scripts/ss_report.py -             # read from a pipe
  python3 scripts/ss_report.py --run                     # run `ss -tulnp` locally

Reads text only (or runs one fixed local command). It never scans a network.
"""
import re
import subprocess
import sys
from pathlib import Path

SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 67: "DHCP server",
    68: "DHCP client", 69: "TFTP", 80: "HTTP", 110: "POP3", 123: "NTP",
    143: "IMAP", 161: "SNMP", 389: "LDAP", 443: "HTTPS", 445: "SMB",
    631: "CUPS/IPP", 1433: "MS SQL", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 6379: "Redis", 8000: "HTTP-alt", 8080: "HTTP-alt",
    27017: "MongoDB",
}
CLEAR_TEXT = {
    21: "FTP sends credentials in clear text: use SFTP/FTPS",
    23: "Telnet is clear text: use SSH",
    69: "TFTP has no authentication or encryption",
    80: "HTTP is unencrypted: use HTTPS",
    110: "POP3 is clear text: use POP3S",
    143: "IMAP is clear text: use IMAPS",
    161: "SNMP v1/v2c uses clear-text community strings: use SNMPv3",
    389: "LDAP is clear text: use LDAPS",
}
DATABASES = {1433, 3306, 5432, 6379, 27017}


def exposure(address):
    host = address.split("%")[0]
    if host in ("0.0.0.0", "*", "::", "[::]"):
        return "ALL interfaces"
    if host.startswith("127.") or host in ("[::1]", "::1"):
        return "local only"
    return "specific IP"


def parse_line(line):
    parts = line.split()
    if len(parts) < 5 or parts[0] not in ("tcp", "udp"):
        return None
    local = parts[4]
    host, _, port = local.rpartition(":")
    if not port.isdigit():
        return None
    match = re.search(r'\(\("([^"]+)"', line)
    return {
        "proto": parts[0],
        "host": host,
        "port": int(port),
        "process": match.group(1) if match else "-",
    }


def run_ss():
    try:
        result = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SystemExit(f"Could not run ss: {error}")
    return result.stdout


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    if argv[0] == "--run":
        text = run_ss()
    elif argv[0] == "-":
        text = sys.stdin.read()
    else:
        try:
            text = Path(argv[0]).read_text(encoding="utf-8")
        except OSError as error:
            raise SystemExit(f"Could not read {argv[0]}: {error}")

    rows = [r for r in (parse_line(l) for l in text.splitlines()) if r]
    if not rows:
        raise SystemExit("No listening sockets found in the input.")

    print(f"{'PROTO':5} {'LOCAL':22} {'PORT':>5}  {'SERVICE':12} {'PROCESS':16} EXPOSURE")
    notes = []
    for r in sorted(rows, key=lambda x: (x["port"], x["proto"])):
        exp = exposure(r["host"])
        service = SERVICES.get(r["port"], "unknown")
        print(f"{r['proto']:5} {r['host']:22} {r['port']:>5}  {service:12} {r['process']:16} {exp}")
        label = f"{r['proto']}/{r['port']} ({r['process']})"
        if exp == "ALL interfaces":
            if r["port"] in CLEAR_TEXT:
                notes.append(f"HIGH   {label}: {CLEAR_TEXT[r['port']]}")
            if r["port"] in DATABASES:
                notes.append(f"HIGH   {label}: database listening on all interfaces, restrict to localhost or a private network")
            if r["port"] == 3389:
                notes.append(f"HIGH   {label}: RDP exposed, put it behind a VPN with MFA")
            if r["port"] == 22:
                notes.append(f"MEDIUM {label}: SSH reachable from the network, use keys and restrict sources")
            if service == "unknown" or r["port"] in (8000, 8080):
                notes.append(f"LOW    {label}: confirm this service is intended to be reachable")

    all_if = sum(1 for r in rows if exposure(r["host"]) == "ALL interfaces")
    print(f"\nSockets: {len(rows)} total, {all_if} on all interfaces")
    if notes:
        print("\nReview:")
        seen = set()
        for note in notes:
            if note not in seen:
                print("  " + note)
                seen.add(note)
    else:
        print("\nNothing obviously risky exposed on all interfaces.")


if __name__ == "__main__":
    main(sys.argv[1:])

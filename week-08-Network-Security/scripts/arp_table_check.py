#!/usr/bin/env python3
"""Check an ARP table for warning signs (offline).

Usage:  python3 scripts/arp_table_check.py samples/arp-sample.txt
Accepts `arp -a` (Linux or Windows) and `ip neigh` output. Reads a file only.

Warning sign: several IPs sharing one MAC. It can be benign (a router doing
proxy ARP, VMs, one device with several IPs) or a sign of ARP spoofing.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

IP = r"(\d{1,3}(?:\.\d{1,3}){3})"
MAC = r"((?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2})"
LINUX_ARP = re.compile(rf"\({IP}\) at {MAC}")          # ? (192.168.1.1) at aa:bb:..
WINDOWS_ARP = re.compile(rf"^\s*{IP}\s+{MAC}\s+(\w+)")  # 192.168.1.1  aa-bb-..  dynamic
IP_NEIGH = re.compile(rf"^{IP}\s+dev\s+\S+\s+lladdr\s+{MAC}")


def parse(text):
    table = []
    for line in text.splitlines():
        for pattern in (LINUX_ARP, WINDOWS_ARP, IP_NEIGH):
            m = pattern.search(line)
            if m:
                ip, mac = m.group(1), m.group(2).lower().replace("-", ":")
                if mac not in ("ff:ff:ff:ff:ff:ff",) and not mac.startswith(("01:00:5e", "33:33")):
                    table.append((ip, mac))
                break
    return table


def main(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError as error:
        raise SystemExit(f"Could not read {path}: {error}")

    table = parse(text)
    if not table:
        raise SystemExit("No ARP entries found.")

    by_mac = defaultdict(list)
    for ip, mac in table:
        by_mac[mac].append(ip)

    print(f"Entries parsed: {len(table)}\n")
    print(f"{'IP':16} MAC")
    for ip, mac in table:
        print(f"{ip:16} {mac}")

    duplicates = {mac: ips for mac, ips in by_mac.items() if len(ips) > 1}
    print()
    if duplicates:
        print("WARNING: one MAC address answers for several IPs:")
        for mac, ips in duplicates.items():
            print(f"  {mac} -> {', '.join(ips)}")
        print("Check: is it a router or VM host (benign), or an attacker claiming the gateway's IP?")
        print("Compare with a baseline taken when the network was known good.")
        return 1
    print("No duplicate MAC addresses found.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1]))

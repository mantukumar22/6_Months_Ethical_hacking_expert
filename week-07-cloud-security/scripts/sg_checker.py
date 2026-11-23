#!/usr/bin/env python3
"""Offline checker for `aws ec2 describe-security-groups` JSON output.

Usage:  python3 scripts/sg_checker.py sg.json
Reads a file only. It never contacts AWS or scans anything.
"""
import json
import sys
from pathlib import Path

WORLD = {"0.0.0.0/0", "::/0"}
SENSITIVE_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 445: "SMB", 1433: "MS SQL",
    2375: "Docker API", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    5900: "VNC", 6379: "Redis", 9200: "Elasticsearch", 27017: "MongoDB",
}
EXPECTED_PUBLIC = {80: "HTTP", 443: "HTTPS"}


def world_sources(permission):
    sources = [r.get("CidrIp") for r in permission.get("IpRanges", [])]
    sources += [r.get("CidrIpv6") for r in permission.get("Ipv6Ranges", [])]
    return [s for s in sources if s in WORLD]


def check_group(group):
    findings = []
    for perm in group.get("IpPermissions", []):
        exposed = world_sources(perm)
        if not exposed:
            continue
        proto = perm.get("IpProtocol")
        src = ", ".join(exposed)
        if proto == "-1":
            findings.append(("CRITICAL", f"ALL traffic, all ports, open to {src}"))
            continue
        low, high = perm.get("FromPort"), perm.get("ToPort")
        if low is None or high is None:
            continue
        hit = False
        for port, name in SENSITIVE_PORTS.items():
            if low <= port <= high:
                findings.append(("HIGH", f"{name} (port {port}/{proto}) open to {src}"))
                hit = True
        if not hit:
            if high - low > 1000:
                findings.append(("MEDIUM", f"Wide port range {low}-{high}/{proto} open to {src}"))
            elif low == high and low in EXPECTED_PUBLIC:
                findings.append(("INFO", f"{EXPECTED_PUBLIC[low]} (port {low}) open to {src}: expected for a public web server"))
            else:
                findings.append(("MEDIUM", f"Port {low}-{high}/{proto} open to {src}: confirm it needs to be public"))
    return findings


def main(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Could not read {path}: {error}")
    groups = data.get("SecurityGroups", []) if isinstance(data, dict) else data

    order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "INFO": 3}
    problems = 0
    print(f"Security Groups checked: {len(groups)}")
    for group in groups:
        findings = check_group(group)
        name = f"{group.get('GroupName', '?')} ({group.get('GroupId', '?')})"
        if not findings:
            print(f"\n{name}\n  OK: nothing open to the world")
            continue
        print(f"\n{name}")
        for severity, message in sorted(findings, key=lambda f: order[f[0]]):
            print(f"  {severity:8} {message}")
            if severity in ("CRITICAL", "HIGH"):
                problems += 1
    print(f"\nHigh/critical findings: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1]))

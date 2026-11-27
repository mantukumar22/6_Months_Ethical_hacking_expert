#!/usr/bin/env python3
"""Spot SSH brute-force patterns in an auth log (offline).

Usage:  python3 scripts/failed_logins.py samples/auth.log.sample [--threshold 5]
Works on /var/log/auth.log style lines (or journalctl output). Reads a file only.
"""
import argparse
import re
from collections import defaultdict
from pathlib import Path

FAILED = re.compile(r"Failed (?:password|publickey) for (?:invalid user )?(\S+) from (\S+) port \d+")
INVALID = re.compile(r"Invalid user (\S+) from (\S+)")
ACCEPTED = re.compile(r"Accepted (\S+) for (\S+) from (\S+) port \d+")


def analyse(lines):
    failures = defaultdict(list)       # ip -> [usernames]
    accepted = defaultdict(list)       # ip -> [(user, method)]
    order = []                         # events in order: (kind, ip)
    for line in lines:
        m = FAILED.search(line)
        if m:
            user, ip = m.groups()
            failures[ip].append(user)
            order.append(("fail", ip))
            continue
        m = ACCEPTED.search(line)
        if m:
            method, user, ip = m.groups()
            accepted[ip].append((user, method))
            order.append(("ok", ip))
    return failures, accepted, order


def main():
    parser = argparse.ArgumentParser(description="SSH failed-login analysis")
    parser.add_argument("logfile")
    parser.add_argument("--threshold", type=int, default=5,
                        help="failures from one IP that count as suspicious (default 5)")
    args = parser.parse_args()

    try:
        lines = Path(args.logfile).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as error:
        raise SystemExit(f"Could not read {args.logfile}: {error}")

    failures, accepted, order = analyse(lines)
    if not failures:
        print("No failed SSH logins found.")
        return

    print(f"Failed logins by source IP (threshold {args.threshold}):\n")
    print(f"{'IP':18} {'FAILS':>5}  {'DISTINCT USERS':>14}  USERNAMES TRIED")
    for ip, users in sorted(failures.items(), key=lambda kv: -len(kv[1])):
        flag = "  <-- SUSPICIOUS" if len(users) >= args.threshold else ""
        unique = sorted(set(users))
        print(f"{ip:18} {len(users):>5}  {len(unique):>14}  {', '.join(unique)}{flag}")

    print("\nSuccess AFTER many failures (possible compromise):")
    found = False
    for ip, users in failures.items():
        if len(users) < args.threshold:
            continue
        fails_before = 0
        for kind, who in order:
            if who != ip:
                continue
            if kind == "fail":
                fails_before += 1
            elif kind == "ok" and fails_before >= args.threshold:
                user, method = accepted[ip][0]
                print(f"  ALERT {ip}: logged in as '{user}' via {method} after {fails_before} failures. "
                      "Investigate, reset credentials, check what the session did.")
                found = True
                break
    if not found:
        print("  none")

    print("\nIdeas: key-only SSH, fail2ban or rate limiting, firewall the source, MFA, alert on this pattern.")


if __name__ == "__main__":
    main()

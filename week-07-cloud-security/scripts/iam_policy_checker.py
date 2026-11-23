#!/usr/bin/env python3
"""Offline checker for AWS IAM / bucket / trust policy JSON files.

Usage:  python3 scripts/iam_policy_checker.py policy.json [more.json ...]

Reads files only. It never contacts AWS. Findings are hints for review,
not a complete audit: always validate them manually.
"""
import json
import sys
from pathlib import Path

READ_PREFIXES = ("get", "list", "describe")

# Actions that commonly enable privilege escalation when granted broadly.
PRIVESC_ACTIONS = {
    "iam:passrole": "can pass a powerful role to a service the user controls",
    "iam:createaccesskey": "can create keys for other users",
    "iam:createloginprofile": "can set console passwords for other users",
    "iam:updateloginprofile": "can reset console passwords",
    "iam:attachuserpolicy": "can attach admin policies to users",
    "iam:attachrolepolicy": "can attach admin policies to roles",
    "iam:attachgrouppolicy": "can attach admin policies to groups",
    "iam:putuserpolicy": "can write inline admin policies",
    "iam:putrolepolicy": "can write inline admin policies",
    "iam:createpolicyversion": "can replace a policy with an admin version",
    "iam:setdefaultpolicyversion": "can activate an older, broader policy version",
    "iam:updateassumerolepolicy": "can change who may assume a role",
    "sts:assumerole": "can assume other roles if trust allows it",
    "lambda:updatefunctioncode": "can run code under the function's role",
}


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def principal_is_public(principal):
    if principal == "*":
        return True
    if isinstance(principal, dict):
        return any("*" in as_list(v) for v in principal.values())
    return False


def check_statement(stmt, index):
    """Return a list of (severity, message) for one policy statement."""
    findings = []
    if stmt.get("Effect") != "Allow":
        return findings

    label = stmt.get("Sid") or f"#{index}"
    actions = [str(a) for a in as_list(stmt.get("Action"))]
    resources = [str(r) for r in as_list(stmt.get("Resource"))]
    lowered = [a.lower() for a in actions]
    has_condition = bool(stmt.get("Condition"))

    if "*" in actions and "*" in resources:
        findings.append(("CRITICAL", f"[{label}] Action '*' on Resource '*': full administrator access"))
    elif "*" in actions:
        findings.append(("HIGH", f"[{label}] Action '*': every action allowed on {resources or 'unspecified resources'}"))

    for action in actions:
        if action.endswith(":*") and action != "*":
            service = action.split(":")[0]
            sev = "CRITICAL" if service.lower() == "iam" else "HIGH"
            findings.append((sev, f"[{label}] Service wildcard '{action}': all {service} actions"))

    if stmt.get("NotAction") is not None:
        findings.append(("HIGH", f"[{label}] Allow with NotAction: grants everything EXCEPT the listed actions"))

    for action, why in PRIVESC_ACTIONS.items():
        if action in lowered and "*" in resources:
            findings.append(("HIGH", f"[{label}] '{action}' on Resource '*': {why}"))

    if "*" in resources and "*" not in actions and not any(a.endswith(":*") for a in actions):
        non_read = [a for a in actions
                    if not a.split(":")[-1].lower().startswith(READ_PREFIXES)]
        if non_read and not any(a.lower() in PRIVESC_ACTIONS for a in non_read):
            findings.append(("MEDIUM", f"[{label}] Resource '*' with write-style actions {non_read}: scope to specific ARNs"))

    if principal_is_public(stmt.get("Principal")):
        sev = "LOW" if has_condition else "CRITICAL"
        extra = "has a Condition: verify it really restricts access" if has_condition \
            else "NO Condition: anyone on the internet may use this"
        findings.append((sev, f"[{label}] Principal is '*' ({extra})"))

    return findings


def check_policy(document):
    statements = as_list(document.get("Statement"))
    findings = []
    for index, stmt in enumerate(statements, start=1):
        if isinstance(stmt, dict):
            findings.extend(check_statement(stmt, index))
    return findings, len(statements)


def main(paths):
    order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    worst = 99
    for path in paths:
        print(f"\n=== {path} ===")
        try:
            document = json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            print(f"Could not read policy: {error}")
            worst = 0
            continue
        findings, count = check_policy(document)
        print(f"Statements checked: {count}")
        if not findings:
            print("No issues found by these checks (still review manually).")
            continue
        for severity, message in sorted(findings, key=lambda f: order[f[0]]):
            print(f"  {severity:8} {message}")
            worst = min(worst, order[severity])
    return 1 if worst <= 1 else 0   # exit 1 on CRITICAL/HIGH


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1:]))

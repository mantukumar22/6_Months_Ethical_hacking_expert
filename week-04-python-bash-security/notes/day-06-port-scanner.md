# Day 6: Build a Python port scanner
**Date:** 2 Nov 2026 · **Time:** 60 min

## Learn (15 min)
Review socket code, exception handling and loops. A scanner automates repeated connection checks. It does **not** automatically identify vulnerabilities.

## Practice (35 min)
Extend Day 5's script so it:
- [ ] Accepts a target IP
- [ ] Checks a small, predefined list of TCP ports
- [ ] Prints successful connections
- [ ] Handles connection errors and timeouts
- [ ] Saves results to `scan_results.txt`

Keep the target restricted to `127.0.0.1` or a lab machine I own or am explicitly authorized to test.

Write your own version first. A finished reference is in [scripts/day06_port_scanner.py](../scripts/day06_port_scanner.py), so compare after.

## Review (10 min)
Test against localhost. Explain what happens when a port has no service listening, and why the results are not a full vulnerability assessment.

## Mistake I fixed today
-

## Key takeaways
-

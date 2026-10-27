# Day 7 Mini-Project: My First Security Tool
**Date:** 3 Nov 2026

Polish the Day 6 scanner into a small, safe command-line tool. Redact any real IPs or hostnames before committing.

## Requirements
- [ ] Target validation: loopback, or a private IP after an authorization confirmation. Refuse public IPs
- [ ] Ports from a list (and optionally a `--ports 22,80,443` argument using `argparse`)
- [ ] Timeout handling and clear states: `open`, `closed`, `filtered/no response`
- [ ] Results saved to a file with a timestamp
- [ ] Errors handled with `try/except` (no tracebacks for normal failures)
- [ ] Optional: logging to a file, and a Bash wrapper that runs it and stores output with a date in the filename

## Report
| Item | Notes |
|---|---|
| What the tool does | |
| How I ran it (command) | |
| Example output (redacted) | |
| What an `open` result proves | A TCP connection was accepted on that port |
| What it does NOT prove | That the service is vulnerable, or what it is |
| What `closed` vs `filtered` suggests | Refused = host reachable, nothing listening. Silence = firewall or host down |
| One bug I fixed | |
| One improvement for next time | |

## Redaction checklist
- [ ] No real IPs or hostnames
- [ ] No result files with private data committed

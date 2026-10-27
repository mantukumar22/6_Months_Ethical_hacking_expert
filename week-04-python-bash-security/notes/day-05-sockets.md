# Day 5: Networking with Python sockets
**Date:** 1 Nov 2026 · **Time:** 60 min

This is where Python starts connecting to the VAPT goal.

## Learn (20 min)
- What a socket is
- TCP connections
- IP addresses and ports
- Connection timeouts
- Difference between a port being **open, closed or filtered**

## Practice (30 min)
Create `tcp_check.py` (starter: [scripts/day05_tcp_check.py](../scripts/day05_tcp_check.py)) and run it. It tests four TCP ports on **your own computer**. If nothing is listening, failed connections are expected.

> A failed connection alone cannot tell you whether a remote port is closed or filtered.

Try it with a listener so one port shows up:
```
python3 -m http.server 8000      # in a second terminal
python3 tcp_check.py             # target: 127.0.0.1
```

## Notes (10 min)
Explain what `socket()`, `settimeout()` and `connect_ex()` do.

## Mistake I fixed today
-

## Key takeaways
-

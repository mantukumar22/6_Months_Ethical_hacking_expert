# Sockets cheat sheet

| Item | Meaning |
|---|---|
| `AF_INET` | IPv4 addressing |
| `SOCK_STREAM` | TCP (use `SOCK_DGRAM` for UDP) |
| `settimeout(1)` | Give up after 1 second instead of waiting |
| `connect_ex((ip, port))` | Returns `0` on success, an error code on failure (no exception) |
| `connect(...)` | Raises `ConnectionRefusedError` or `TimeoutError` on failure |

| What you observe | Likely meaning |
|---|---|
| Connection succeeds | **Open**: a service accepted the connection |
| Connection refused (reset) | **Closed**: host reachable, nothing listening |
| Timeout / no reply | **Filtered** (firewall drops) or host down. Can't tell which |

A scan shows reachability only. It does not prove a service is vulnerable.

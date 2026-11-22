# Day 6: Authentication and Security Concepts
**Date:** 22 · **Time:** 60 min
**Video:** Authentication and authorization: <paste title/URL>

## Learn (20 min)

### Authentication vs authorization
| | Authentication (AuthN) | Authorization (AuthZ) |
|---|---|---|
| Question | **Who are you?** | **What are you allowed to do?** |
| Happens | First | After authentication |
| Example | Logging in with a password | A normal user can't open the admin panel |
| Failure code | HTTP **401** Unauthorized | HTTP **403** Forbidden |
| Linux/Windows link | Login | Permissions (`chmod`, `icacls`) |

**Accounting / auditing** is the third piece: logging who did what (Week 3 logs, Event IDs 4624 and 4625). Together: **AAA**.

Common web flaw: **broken access control** (authorization missing), e.g. changing `?id=5` to `?id=6` and seeing another user's data (IDOR).

### Authentication factors
| Factor | Meaning | Examples |
|---|---|---|
| **Something you know** | Secret | Password, PIN |
| **Something you have** | Device | Phone app, security key, smart card |
| **Something you are** | Biometrics | Fingerprint, face |

### MFA and 2FA
- **MFA** (multi-factor authentication) uses **two or more different factors**.
- **2FA** is MFA with exactly two.
- Two passwords is **not** MFA, because both are the same factor.

| Method | Strength |
|---|---|
| SMS codes | Better than nothing, but vulnerable to SIM-swapping |
| **TOTP** app (Google Authenticator, Authy) | Good. Time-based codes from a shared secret |
| Push approval | Good, but vulnerable to "MFA fatigue" |
| **Hardware key (FIDO2/WebAuthn)** | Strongest, resists phishing |

MFA blocks most credential-stuffing and brute-force attacks (Week 5, Day 4), but phishing can still beat weaker MFA.

### Password security
| Do | Don't |
|---|---|
| Use long passphrases (14+ characters) | Reuse passwords across sites |
| Use a **password manager** and unique passwords | Use predictable patterns (`Summer2026!`) |
| Check for breaches | Share passwords or write them in plain text files |
| Enable MFA | Rely on complexity rules alone |

**For developers:** store a **slow, salted hash**, not the password (Day 4). Rate-limit and lock out repeated failures. Don't tell attackers whether the username or password was wrong. Never log passwords.

### Session management
HTTP is **stateless** (Week 2, Day 5), so after login the server issues a **session ID** or token and the client sends it with every request. **Whoever holds it is treated as the user.**

```
1. POST /login (username + password)
2. Server verifies, creates a session  ->  Set-Cookie: session=abc123
3. Browser sends  Cookie: session=abc123  with each request
4. Logout / timeout  ->  server destroys the session
```
Good session practice:
- Session IDs must be **long, random and unguessable**. Use a secure generator, e.g. Python's `secrets` module.
- **Regenerate the ID after login** (prevents session fixation).
- Set **timeouts** and invalidate the session on logout.
- Use **HTTPS** everywhere.

### Cookies and tokens
| | Cookie | Token (e.g. JWT) |
|---|---|---|
| What | Small data the browser stores and sends automatically | A signed value the client sends, often in the `Authorization: Bearer` header |
| State | Usually a session ID (state on server) | Often self-contained (claims inside) |
| Risks | CSRF, theft via XSS | Theft, weak signing, long lifetimes |

**Cookie flags (check them in DevTools → Application/Storage, Week 2 Lab 05):**
| Flag | Purpose |
|---|---|
| `HttpOnly` | JavaScript can't read it (limits XSS theft) |
| `Secure` | Sent only over HTTPS |
| `SameSite` | Limits cross-site sending (helps stop CSRF) |
| `Expires` / `Max-Age` | Lifetime |

**JWT (JSON Web Token):** three Base64URL parts, `header.payload.signature`. The payload is **encoded, not encrypted**, so anyone can read it. Never put secrets inside. The signature (HMAC or RSA, Days 3 and 4) stops tampering. Common mistakes: accepting `alg: none`, weak signing secrets, no expiry.

### Least privilege principle
Give every user, program and service **only the access it needs, for only as long as it needs it**.

- A web server shouldn't run as root. A database account for an app shouldn't be able to drop tables.
- Regular users shouldn't be admins (Week 3: UAC, `sudo`).
- Limits damage from a compromise, mistakes and malware.
- Related ideas: **separation of duties**, **need to know**, **defense in depth**, **zero trust** ("never trust, always verify").

## Practice (30 min)
1. **Cookies:** open a site you use, DevTools → Application → Cookies. List 3 cookies and their `HttpOnly`, `Secure` and `SameSite` flags.
2. **Decode a JWT** (use an example, never a real token): split on `.` and Base64-decode the first two parts in Python. Explain why the payload isn't secret.
```python
import base64, json
def b64url_decode(part):
    return base64.urlsafe_b64decode(part + "=" * (-len(part) % 4))
# token = "<header>.<payload>.<signature>"
# header, payload, signature = token.split(".")
# print(json.loads(b64url_decode(payload)))
```
3. **Session IDs:** generate a good one: `python3 -c "import secrets; print(secrets.token_urlsafe(32))"`. Why is `random` or a counter a bad choice?
4. **MFA:** turn on MFA for one important account (email or GitHub) if not already done.
5. **Least privilege audit:** `id` on Kali and `whoami /groups` on Windows. Do you run daily as an admin? Could you use a standard account instead?

## Notes (10 min)
- Authentication vs authorization, with one example each:
- Why session IDs must be random:
- Least privilege in one sentence:

## Self-check
1. Which comes first, authentication or authorization?
2. Why is a password plus a security question not MFA?
3. What do `HttpOnly` and `Secure` do?
4. Why isn't a JWT payload confidential?
5. Give an example of least privilege on Linux.

## Mistake I fixed / still confusing
-

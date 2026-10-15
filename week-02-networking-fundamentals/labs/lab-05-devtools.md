# Lab 05: Browser DevTools
Open DevTools (F12) → **Network** tab, then load a site.

| Request | Method | Status | Type | Time | Notable headers |
|---|---|---|---|---|---|
| | | | | | |

Questions
### 1. Which status codes did I see, and what does each mean?

**How to find them:** read the **Status** column, or click the column header to sort by it. To trigger different codes safely:
- **200:** any normal page load.
- **301/302:** visit `http://` (not https) version of a site, which usually redirects to HTTPS.
- **304:** reload normally (Ctrl+R) on a site you've visited before. Cached files often return 304.
- **404:** add a nonsense path to a site you're allowed to browse, e.g. `https://example.com/doesnotexist`.

| Code | Name | Meaning |
|---|---|---|
| 200 | OK | Request succeeded and the content was returned |
| 301 | Moved Permanently | Resource has a new permanent URL (see the `Location` header) |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Your cached copy is still current, so no body was re-sent |
| 404 | Not Found | The server has no resource at that path |
| 403 | Forbidden | Server understood but refuses access |
| 500 | Internal Server Error | The server failed while handling the request |

**My results:**

| Request | Method | Status | What it means |
|---|---|---|---|
| | | | |

### 2. What do the `Host`, `User-Agent` and `Content-Type` headers do?

Click a request → **Headers** tab → **Request Headers** (and **Response Headers**).

| Header | Direction | Purpose |
|---|---|---|
| `Host` | Request | Names the website wanted, e.g. `example.com`. One server/IP can host many sites, and this header tells it which one to serve |
| `User-Agent` | Request | Identifies the client (browser, version, OS) so the server can adapt its response. It is easy to fake, so never trust it for security |
| `Content-Type` | Both | Says what format the body is in, e.g. `text/html`, `application/json`, `image/png`. In a request it describes data you send (like a POST), in a response it tells the browser how to handle what it received |

**Security note:** servers also reveal information in headers like `Server`, so reading headers is a basic information-gathering skill.

**My observed values:**
- `Host`:
- `User-Agent`:
- `Content-Type` (response):

### 3. Padlock: who issued the certificate, and when does it expire?

1. Click the **padlock / site-info icon** left of the address bar.
2. Choose **Connection is secure** → **Certificate is valid** (wording varies by browser).
3. Read the **Issued To**, **Issued By** and **Valid from / to** dates. The **Details** tab shows the certificate chain.

| Field | Meaning |
|---|---|
| Issued To | The domain the certificate covers |
| Issued By | The Certificate Authority (CA) that signed it, e.g. Let's Encrypt, DigiCert |
| Valid from / to | The window in which it is trusted. After the end date, browsers show a warning |

**My results:**

| Site | Issued by | Expires |
|---|---|---|
| | | |

Many certificates are short-lived (e.g. 90 days with Let's Encrypt) and renew automatically, so a near expiry date isn't unusual.

### Reflection
Why does a `Host` header matter if the IP address already identifies the server?

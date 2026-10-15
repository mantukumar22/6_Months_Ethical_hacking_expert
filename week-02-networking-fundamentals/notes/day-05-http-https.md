# Day 5: HTTP, HTTPS and web traffic
**Date:** 17 Oct 2026 · **Time:** 60 min

## Learn (20 min)
HTTP requests/responses, methods, status codes, TLS and certificates.
HTTP, HTTPS and Web Traffic

### HTTP (HyperText Transfer Protocol)
The **Layer 7 (Application)** protocol browsers and servers use to exchange web content. It follows a **request → response** model: the client asks, the server answers. HTTP is **stateless**, so each request is independent. Sites use cookies or tokens to remember who you are. It runs over TCP, on port **80** by default.

### HTTP Request
What the client sends:
```
GET /login HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session=abc123
```
1. **Request line:** method + path + HTTP version
2. **Headers:** extra information (key: value)
3. **Body** (optional): data being sent, e.g. a submitted form

### HTTP Response
What the server sends back:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
Set-Cookie: session=xyz789

<html>...page content...</html>
```
1. **Status line:** version + status code + reason
2. **Headers:** metadata about the response
3. **Body:** the actual content (HTML, JSON, image)

### HTTP Methods

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve a resource | Load a page |
| POST | Send data to create or process something | Submit a login form |
| PUT | Replace a resource | Update a whole record |
| PATCH | Partially modify a resource | Change one field |
| DELETE | Remove a resource | Delete an account |
| HEAD | Like GET, but headers only | Check if a page exists |
| OPTIONS | Ask which methods are allowed | CORS preflight |

Note: GET puts data in the URL (visible in logs and history), while POST puts it in the body. Neither is secure without HTTPS.

### Status Codes

| Range | Meaning | Common examples |
|---|---|---|
| 1xx | Informational | 101 Switching Protocols |
| 2xx | Success | **200** OK, 201 Created, 204 No Content |
| 3xx | Redirection | **301** Moved Permanently, **302** Found, 304 Not Modified |
| 4xx | Client error | **400** Bad Request, **401** Unauthorized, **403** Forbidden, **404** Not Found |
| 5xx | Server error | **500** Internal Server Error, **502** Bad Gateway, **503** Service Unavailable |

Memory aid: 2xx = it worked, 3xx = go elsewhere, 4xx = you made an error, 5xx = the server failed. For 401 vs 403: 401 means "not logged in / not authenticated", 403 means "logged in but not allowed".

### Important Headers

| Header | Direction | Purpose |
|---|---|---|
| Host | Request | Which website is wanted (many sites share one IP) |
| User-Agent | Request | Identifies the browser or client |
| Cookie | Request | Sends stored session data |
| Content-Type | Both | Format of the body (`text/html`, `application/json`) |
| Set-Cookie | Response | Tells the browser to store a cookie |
| Location | Response | Where to go on a 3xx redirect |
| Server | Response | Software the server runs (can leak information) |

### HTTPS
**HTTP over TLS.** The same HTTP messages, wrapped in an encrypted, authenticated channel. Runs on TCP port **443** by default. The padlock in the browser means the connection is encrypted and the server's certificate was validated. It does **not** mean the website itself is trustworthy.

### TLS (Transport Layer Security)
The protocol that provides three things:
1. **Confidentiality:** traffic is encrypted, so eavesdroppers can't read it.
2. **Integrity:** data can't be modified in transit without detection.
3. **Authentication:** you can verify you're talking to the real server.

**Simplified TLS handshake:**
```
Client                                Server
  | ---- ClientHello (versions, ciphers) --->  |
  | <--- ServerHello + Certificate ----------  |
  |  (client verifies certificate)             |
  | ---- key exchange ------------------------>|
  | <==== encrypted session keys agreed =====> |
  | ======== encrypted HTTP traffic ========== |
```
Asymmetric cryptography is used during the handshake to agree on keys, then fast symmetric encryption protects the data. Older versions (SSL, TLS 1.0 and 1.1) are deprecated, and TLS 1.2 and 1.3 are current.

### Digital Certificate
A document that binds a **domain name to a public key**, signed by a trusted **Certificate Authority (CA)**. It contains the domain name(s), the public key, the issuer, and the validity dates.

Your browser trusts certificates through a **chain of trust**: Server certificate → Intermediate CA → Root CA (pre-installed in your OS/browser). Certificate warnings appear when it is expired, issued for a different domain, self-signed, or not chained to a trusted root.

### What HTTPS protects and what it doesn't hide

| Protected (encrypted) | Still visible to observers |
|---|---|
| Page content and form data | The **IP address** you connect to |
| URL path and query string | The **domain name** (via DNS queries and the TLS SNI field, unless DNS-over-HTTPS or encrypted SNI are used) |
| Headers and cookies | Connection timing and amount of data transferred |

HTTPS also does not protect against malware on your device, a phishing site with a valid certificate, or a vulnerable web application. It secures the **connection**, not the **site or server**.

### Inspecting it yourself (Browser DevTools)
Press **F12 → Network** tab, then reload a site:

| Column | What it shows |
|---|---|
| Name | The requested resource |
| Status | The response status code |
| Method | GET, POST, etc. |
| Type | Document, script, image, etc. |
| Time | How long it took |

Click any request to see its **Headers**, **Payload** and **Response**. Click the padlock → certificate to see the issuer and expiry date.

## Practice (30 min)
Lab: [lab-05-devtools](../labs/lab-05-devtools.md). Browser DevTools → Network tab.

## Notes (10 min)
What does HTTPS protect, and what does it **not** hide?

- Protects:
- Does not hide:

## Key takeaways
-

## Still confusing / to revisit
-

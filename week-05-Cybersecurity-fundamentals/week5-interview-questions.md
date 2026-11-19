# Week 5: Cybersecurity Interview Questions

Answers to the ten Week 5 interview questions. Questions 1-7 are based on my own answers, tidied up and completed. Questions 8-10 are new.

---

## 1. What is the CIA Triad?

CIA stands for **Confidentiality, Integrity, Availability**. It is a core information security model, and every security decision can be checked against it by asking: *which of the three am I protecting?*

| Principle | What it protects | Example |
|---|---|---|
| Confidentiality | Data is seen only by authorized people | MFA protects user data. If an attacker bypasses login, confidentiality is broken. |
| Integrity | Data is accurate and unaltered | If an attacker edits the information in a user's account, integrity is broken. |
| Availability | Systems and data are usable when needed | A DoS attack that takes the app down breaks availability. |

The three can conflict. For example, very strict access controls improve confidentiality but can make data harder to reach, which hurts availability.

---

## 2. What is the difference between a threat and a vulnerability?

- **Threat:** anything or anyone that could cause harm to an asset (people, data, money, systems). *Example: a thief who could steal my gold chain.*
- **Vulnerability:** a weakness in a system, process or person that a threat can use. *Example: I cannot defend myself against the thief.*

You usually cannot control threats, but you **can fix vulnerabilities**. That is where security work focuses: patching, hardening and training.

---

## 3. What is an exploit?

An **exploit** is a method or piece of code that takes advantage of a vulnerability in a system, process or person. A successful exploit can deliver access, such as remote control of a computer, data theft or malware installation. Without a vulnerability there is nothing to exploit.

**Why patching matters:** if the owner patches the vulnerability before an attacker uses an exploit, the system stays safe. Patching removes the weakness the exploit depends on.

---

## 4. What is attack surface?

The **attack surface** is the total set of points where an attacker can try to enter a system, interact with it or extract data from it.

- **Examples:** open ports, app URLs, input fields, APIs, third-party components, people (staff who can be phished).
- **How to reduce it:**
  1. Run vulnerability assessments on apps, systems and people to find weak points.
  2. Patch what is vulnerable.
  3. Turn off unused services, ports and features.
  4. Train people.
  5. Keep monitoring.

---

## 5. What is an attack vector?

An **attack vector** is the path or method an attacker uses to exploit a system.

- **Examples:** email (phishing), a website input field (SQL injection, XSS), an exposed remote service, a malicious USB drive.

**Difference from attack surface:** the attack surface is *all the places* an attacker could get in. The attack vector is *the specific route* they actually take.

---

## 6. What is cybersecurity risk?

**Risk** is the potential for loss or damage when a threat exploits a vulnerability in an asset.

**Formula:** `Risk = Likelihood × Impact`

**Four ways to handle risk:**

1. **Mitigate:** reduce it with controls (for example, patching or MFA).
2. **Accept:** knowingly live with it when it is low or too costly to fix.
3. **Transfer:** shift it to another party (for example, cyber insurance or outsourcing).
4. **Avoid:** stop the risky activity altogether.

**Residual risk** is the risk that remains after controls are applied. It should be at a level the organization accepts.

---

## 7. What is the difference between preventive and detective controls?

Security controls come in three main types:

- **Preventive** controls act *before* an incident and stop it from happening. *Examples: firewall, MFA, input validation.*
- **Detective** controls discover that something is happening or has happened. *Examples: IDS/SIEM alerts, log monitoring, CCTV.*
- **Corrective** controls limit damage and restore normal operation *after* an incident. *Examples: restoring from backup, patching, incident response.*

You need all of them because no preventive control is perfect. Detection tells you when prevention failed, and correction gets you back to normal.

---

## 8. What is SQL Injection?

**SQL Injection (SQLi)** happens when an application puts untrusted user input directly into a database query, so the input changes the meaning of the query.

*Example:* a login form builds `SELECT * FROM users WHERE name='` + input + `'`. An attacker enters `' OR '1'='1` and the query returns every user, bypassing login.

- **What an attacker could gain:** read, modify or delete data, bypass authentication and sometimes run commands on the server.
- **Main defense:** **parameterized queries (prepared statements)**, which keep input as data and never as SQL code. Also use input validation, least-privilege database accounts and a WAF as extra layers.
- **CIA impact:** all three. Confidentiality (data leaked), Integrity (data changed) and Availability (data deleted or tables dropped).

---

## 9. What is XSS?

**Cross-Site Scripting (XSS)** happens when an application includes untrusted input in a page without proper handling, so it runs as script in *another user's browser*.

**Types:**

- **Reflected:** the malicious script comes from the request (for example, a crafted link) and is immediately echoed back in the response.
- **Stored:** the script is saved on the server (for example, in a comment) and runs for every visitor who views it.
- **DOM-based:** client-side JavaScript writes untrusted data into the page, so the flaw is in the browser code itself.

**Impact:** stealing session cookies and taking over accounts, performing actions as the victim, defacing pages and redirecting to phishing sites.

**Defenses:**

- **Output encoding** based on context (HTML, attribute, JavaScript).
- A **Content Security Policy (CSP)**.
- Input validation.
- `HttpOnly` cookies.
- Avoiding dangerous sinks such as `innerHTML`.

---

## 10. How would you begin assessing the security of a web application?

1. **Get authorization and scope in writing:** what is allowed, what is off limits, testing windows and contacts.
2. **Understand the app:** its purpose, users, roles, the data it handles and its technologies.
3. **Map the attack surface:** pages, forms, APIs, parameters, login, file upload and third-party components.
4. **Gather information** passively and actively, within scope: headers, technologies, certificates and DNS.
5. **Check against a framework:** the **OWASP Top 10**, such as injection, broken access control, authentication problems and misconfiguration.
6. **Test and validate** findings safely, then rate them by likelihood and impact.
7. **Document and report** with evidence, risk ratings and remediation advice.

The key point is that authorization and scope come first. Without them, testing is not legal.

---

## Self-assessment

| Question | Confident (Y/N) | Needs review |
|---|---|---|
| 1-3 | | |
| 4-6 | | |
| 7-9 | | |
| 10 | | |

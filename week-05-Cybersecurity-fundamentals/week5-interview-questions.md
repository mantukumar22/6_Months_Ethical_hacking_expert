# Week 5: Interview Questions
Answer each in **your own words, out loud first**, then write it below. Aim for 3 to 5 sentences with one example. The hints list points worth covering, not the answers.

## 1. What is the CIA Triad?
*Cover:* three principles, what each protects, one example each, and that they can conflict.
** CIA stands for Confidentiality, Integrity, Availability. The CIA Triad is a fundamental information security model . Every security decision checked against it: which of the three am I protecting.
Ex:- When i add MFA in a app its protecting User Data( Confidentiality ) and when attacker bypass login Confidentiality breaks. and when attacker edit the info in the user account integrity breaks & if the attacker doing DOS attack on app Availability breaks. ** 

## 2. What is the difference between a threat and a vulnerability?
*Cover:* threat = danger or actor, vulnerability = weakness, which one you can fix, one example pair.
****

## 3. What is an exploit?
*Cover:* how it relates to a vulnerability, what it can deliver, why patching matters.

**My answer:**

## 4. What is attack surface?
*Cover:* the sum of entry points, examples (ports, apps, people), how to reduce it.

**My answer:**

## 5. What is an attack vector?
*Cover:* the path or method used, examples, how it differs from the attack surface.

**My answer:**

## 6. What is cybersecurity risk?
*Cover:* likelihood and impact, the simple formula, the four ways to handle risk, residual risk.

**My answer:**

## 7. What is the difference between preventive and detective controls?
*Cover:* before vs during/after, two examples each, why you need both, corrective as a third kind.

**My answer:**

## 8. What is SQL Injection?
*Cover:* untrusted input changing a database query, what an attacker could gain, the main defense (parameterized queries), CIA impact.

**My answer:**

## 9. What is XSS?
*Cover:* untrusted input running as script in another user's browser, reflected vs stored vs DOM, impact, defenses (output encoding, CSP).

**My answer:**

## 10. How would you begin assessing the security of a web application?
*Cover (a sensible order):*
1. **Get authorization and scope** in writing: what is allowed, what's off limits, testing windows, contacts.
2. **Understand the app:** its purpose, users, roles, data it handles and technologies used.
3. **Map the attack surface:** pages, forms, APIs, parameters, login and file upload, third-party components.
4. **Gather information** passively and actively within scope (headers, technologies, certificates, DNS).
5. **Check against a framework:** the OWASP Top 10 (injection, broken access control, authentication problems, misconfiguration, and so on).
6. **Test and validate** findings safely, then rate them by likelihood and impact.
7. **Document and report** with evidence, risk ratings and remediation advice.

**My answer:**

---
## Self-assessment
| Question | Confident (Y/N) | Needs review |
|---|---|---|
| 1-3 | | |
| 4-6 | | |
| 7-9 | | |
| 10 | | |

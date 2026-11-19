# Day 6: Practical Lab
**Date:** 19 · **Time:** 60 min
**Video:** OWASP Juice Shop beginner lab: <paste URL>

## Goal
Explore **OWASP Juice Shop** or a **TryHackMe beginner room**, identify possible vulnerabilities, map them to the **CIA Triad**, and document the findings.

> **Scope and safety**
> - Juice Shop is an intentionally vulnerable app. Run it **only on my own machine** (localhost).
> - For TryHackMe, stay inside the room's machines and rules.
> - Do not test any real website. Do not publish passwords, tokens or personal data.

## Option A: OWASP Juice Shop (local)
**Run it with Docker** (Kali: `sudo apt install docker.io`, then start the service):
```
sudo systemctl start docker
sudo docker run -d --name juice-shop -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```
Then open `http://localhost:3000` in the browser. Binding to `127.0.0.1` keeps it off the network.

Stop and remove it afterwards:
```
sudo docker stop juice-shop && sudo docker rm juice-shop
```
(Without Docker, the project also offers other install options on the OWASP Juice Shop site.)

**Exploration steps (30 min)**
1. Browse the shop as a normal user. Note every feature: login, register, search, basket, reviews, feedback, file upload.
2. Open DevTools (F12) → **Network** (Week 2, Day 5). Watch requests, status codes and cookies as you use the site.
3. Find the **Score Board** page (it's hidden, so look for it) and pick **1-star challenges**.
4. Try a few beginner challenges, such as:
   - Finding the hidden Score Board
   - Reading the feedback form and testing how it handles input
   - Checking the login form and error messages
   - Looking at the basket and request parameters
   - Reviewing the page source and JavaScript for hints
5. For every issue you find, take a **screenshot** and write it up below.

## Option B: TryHackMe beginner rooms
Pick a free beginner path, such as an intro to cybersecurity, web fundamentals or OWASP Top 10 room. Complete the tasks, take screenshots of your progress (no flags or answers pasted publicly), and note what you learned.

## Findings (aim for at least 3)

### Finding 1
| Field | Details |
|---|---|
| Title | |
| Where (page / feature / URL) | |
| What I observed | |
| Possible vulnerability type | (e.g. injection, XSS, broken access control, sensitive data exposure, security misconfiguration) |
| **CIA impact** | Confidentiality / Integrity / Availability |
| Severity (Low / Medium / High) | |
| Likelihood x Impact (Day 3) | |
| Evidence | `evidence/finding1.png` |
| Suggested fix / control | |

### Finding 2
| Field | Details |
|---|---|
| Title | |
| Where | |
| What I observed | |
| Possible vulnerability type | |
| **CIA impact** | |
| Severity | |
| Evidence | `evidence/finding2.png` |
| Suggested fix / control | |

### Finding 3
| Field | Details |
|---|---|
| Title | |
| Where | |
| What I observed | |
| Possible vulnerability type | |
| **CIA impact** | |
| Severity | |
| Evidence | `evidence/finding3.png` |
| Suggested fix / control | |

## CIA mapping summary
| Finding | Confidentiality | Integrity | Availability |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Link back to the week
| Concept | Where I saw it in the lab |
|---|---|
| Threat | |
| Vulnerability | |
| Exploit (method used) | |
| Attack surface item | |
| Attack vector | |
| Control that would have helped | |

## What I learned
-

## Reflection
- What was easier or harder than expected?
- How does this lab help me answer interview question 10 (starting a web app assessment)?

## Evidence checklist
- [ ] Screenshots saved in `evidence/`
- [ ] Passwords, tokens, cookies and personal data redacted
- [ ] Findings written in my own words
- [ ] Docker container stopped and removed (if used)

# Guide: 7 separate repos (one per day, cybersecurity angle)

Use separate repos if you want 7 portfolio-visible projects. Suggested names and what each should showcase:

| Repo name | Day | Cybersecurity angle to show |
|-----------|-----|-----------------------------|
| `cyber-01-computer-architecture` | 1 | Attack surface map of the I-P-M-S-O chain |
| `cyber-02-resource-baseline` | 2 | Normal vs abnormal CPU/RAM/disk (cryptominer, ransomware signs) |
| `cyber-03-security-layers` | 3 | Vulnerability-per-layer table with real CVE examples |
| `cyber-04-os-enumeration` | 4 | Enumeration command cheat sheet (attacker vs defender view) |
| `cyber-05-process-analysis` | 5 | Process triage checklist (parent, path, cmdline, network) |
| `cyber-06-filesystem-security` | 6 | Permissions, hidden files, persistence locations |
| `cyber-07-system-baseline-report` | 7 | Final baseline report + quiz + learning log |

## Option A — automatic (script)
```bash
bash split_repos.sh
```
Creates `../cyber-repos/cyber-0X-...` folders, each with its own `git init` and commit.

## Option B — push to GitHub
For each folder:
```bash
cd ../cyber-repos/cyber-01-computer-architecture
git remote add origin https://github.com/<your-username>/cyber-01-computer-architecture.git
git branch -M main
git push -u origin main
```
Or with GitHub CLI: `gh repo create cyber-01-computer-architecture --public --source=. --push`

## Make each repo look professional
- README: goal, what you learned, screenshots from `evidence/`, a "Security takeaway" section.
- Add topics/tags: `cybersecurity`, `soc`, `blue-team`, `learning`.
- Never commit usernames, IPs, hostnames or personal paths you don't want public — redact screenshots.
- Commit messages like `Day 05: add process triage checklist`.
- Pin the best 4–6 repos on your GitHub profile and link them from your portfolio/resume.

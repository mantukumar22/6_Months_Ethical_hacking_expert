# Day 06 — Filesystems

## Learn
File, directory, path (absolute `C:\Users\Mantu\Documents\test.txt` vs relative `..\Documents`), file extension, executable, permissions, hidden files.
Linux example: `/home/user/Documents/test.txt`.

## Practical — Windows CMD
```
cd \
dir
mkdir cyber
cd cyber
mkdir week1
cd week1
echo Cybersecurity > notes.txt
type notes.txt
cd ..
dir
```
Also try `dir /a` (shows hidden files). Work out the exact absolute path of the file.

## Practical — Linux (Kali VM or TryHackMe Linux Fundamentals Part 1)
```
pwd
ls
ls -la
cd
mkdir
touch
cat
```

## Cybersecurity perspective
- **Permissions** decide who can read/write/execute — misconfigured ones are a top vulnerability.
- **Hidden files / odd locations** (Temp, AppData, `.ssh`) are common places for malware and persistence.
- **Extensions lie**: `invoice.pdf.exe` is an executable.
- Logs, config files and credentials live in the filesystem — investigators and attackers both go looking there.

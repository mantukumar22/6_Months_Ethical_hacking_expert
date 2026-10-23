# Lab 02: Files, text tools, pipes and redirection (Kali)

Work only inside `~/week3-lab`.

**Tasks**
1. Build a structure: `mkdir -p project/{docs,src,logs}` then `ls -R project`.
2. `touch project/docs/a.txt project/docs/b.txt`, then `echo "hello linux" > project/docs/a.txt` and `echo "second line" >> project/docs/a.txt`. Check with `cat`.
3. `cp project/docs/a.txt project/src/`, `mv project/docs/b.txt project/docs/notes.txt`, then `rm project/src/a.txt`.
4. `find ~/week3-lab -name "*.txt"` and `find ~/week3-lab -type d`.
5. Search inside files: `grep -r "linux" ~/week3-lab`, then `grep -ri "LINUX" ...` (what does `-i` do?).
6. Logs practice:
   - `head -n 5 /var/log/dpkg.log` (or any readable log), `tail -n 5 ...`
   - `wc -l /etc/passwd`
7. Pipes:
   - `cat /etc/passwd | cut -d: -f1 | sort | head`
   - `ls /etc | wc -l`
   - `ps aux | grep bash`
8. Redirect errors: `ls /nonexistent 2> errors.txt` then `cat errors.txt`.

**Results**

| Task | Command | Output / meaning |
|---|---|---|
| Lines in /etc/passwd | | |
| First 5 usernames | | |
| Files in /etc | | |
| `>` vs `>>` | | |

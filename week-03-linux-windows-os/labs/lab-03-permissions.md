# Lab 03: Users, groups and permissions (Kali)

Work inside `~/week3-lab`.

**Part A: identity**
1. `whoami`, `id`, `groups`. What are your UID, GID and groups?
2. `cat /etc/passwd | grep $USER`. Identify the fields (name:x:UID:GID:comment:home:shell).
3. `ls -l /etc/passwd /etc/shadow`. Why is shadow restricted? Try `cat /etc/shadow` (expected: permission denied).

**Part B: reading and changing permissions**
```
touch secret.txt script.sh
ls -l secret.txt script.sh
chmod 600 secret.txt        # owner read/write only
chmod 755 script.sh         # owner rwx, others r-x
chmod u+x,g-w,o-rwx script.sh
ls -l secret.txt script.sh
```
Questions: What are the symbolic equivalents of 600 and 755? Make `script.sh` print something (`echo 'echo hi' > script.sh`), try to run it without `x` (`./script.sh`), then add `x` and run again.

**Part C: ownership and groups (sandbox user)**
```
sudo adduser labtest         # follow prompts
sudo groupadd labgroup
sudo usermod -aG labgroup labtest
id labtest
sudo chown labtest:labgroup secret.txt
ls -l secret.txt
```
Then **clean up**:
```
sudo deluser --remove-home labtest
sudo groupdel labgroup
```

**Part D: directory permissions**
`mkdir d && chmod 000 d && ls d` → what happens? Then `chmod 755 d`. What does `x` on a directory allow?

**Part E: look at SUID (read only, don't change)**
`find / -perm -4000 -type f 2>/dev/null | head`. Note two entries. Why are SUID files interesting to attackers?

**Results**

| Item | Answer |
|---|---|
| My UID / GID / groups | |
| 600 in symbolic form | |
| 755 in symbolic form | |
| What `x` on a directory does | |
| Two SUID files found | |

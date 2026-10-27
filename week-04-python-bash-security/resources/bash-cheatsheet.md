# Bash cheat sheet

```bash
#!/usr/bin/env bash
name="kali"                    # no spaces around =
echo "Hello $name"
echo "Arg 1: $1"               # $# = number of args, "$@" = all args
for item in a b c; do echo "$item"; done
if [ -e "$1" ]; then echo exists; else echo missing; fi
ls /nonexistent; echo "exit code: $?"   # 0 = success
exit 1
```
- Always quote variables: `"$var"`.
- Make executable: `chmod +x script.sh`, run `./script.sh`.
- Don't build commands from untrusted input.

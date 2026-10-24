# Day 2: Files, text tools, pipes and redirection
**Date:** 24 Oct 2026 · **OS:** Kali Linux · **Time:** 60 min

## Learn (20 min)
- Create/copy/move/delete: `touch`, `mkdir -p`, `cp -r`, `mv`, `rm`, `rmdir`.
- Read files: `cat`, `less`, `head`, `tail` (`tail -f` follows a log), `wc`.
- Search: `find` (by name/type/size), `grep` (inside files), `locate`, `which`.
- Wildcards: `*` (any chars), `?` (one char), `[abc]`.
- Standard streams: stdin (0), stdout (1), stderr (2).
- Redirection: `>` overwrite, `>>` append, `2>` errors, `2>&1`.
- Pipes: `cmd1 | cmd2` sends the output of one command into the next.
- Useful pipe tools: `sort`, `uniq -c`, `cut`, `awk`, `tr`, `sed`.

## Practice (30 min)
Lab: [lab-02-files-text](../labs/lab-02-files-text.md)

## Notes (10 min)
## Day 2 Glossary: Files, Text Tools, Pipes and Redirection

### Create / copy / move / delete

| Command | One-line explanation | Example |
|---|---|---|
| `touch` | Creates an empty file, or updates the timestamp of an existing one | `touch a.txt` |
| `mkdir -p` | Creates a directory, including any missing parent directories | `mkdir -p project/src` |
| `cp -r` | Copies a file or, with `-r`, a whole directory and its contents | `cp -r src backup` |
| `mv` | Moves a file or directory, or renames it | `mv old.txt new.txt` |
| `rm` | Deletes a file permanently (no recycle bin); `-r` deletes directories | `rm a.txt` |
| `rmdir` | Deletes an **empty** directory only (safer than `rm -r`) | `rmdir emptydir` |

### Read files

| Command | One-line explanation | Example |
|---|---|---|
| `cat` | Prints a whole file to the screen | `cat /etc/hostname` |
| `less` | Opens a file in a scrollable viewer (`q` quits, `/word` searches) | `less /var/log/syslog` |
| `head` | Shows the first 10 lines of a file (`-n 5` for 5) | `head -n 5 f.txt` |
| `tail` | Shows the last 10 lines of a file | `tail -n 5 f.txt` |
| `tail -f` | Keeps showing new lines as they are added, ideal for watching a live log | `tail -f /var/log/auth.log` |
| `wc` | Counts lines, words and bytes (`-l` for lines only) | `wc -l /etc/passwd` |

### Search

| Command | One-line explanation | Example |
|---|---|---|
| `find` | Searches the filesystem for files by name, type or size | `find ~ -name "*.txt"` |
| `grep` | Searches **inside** files for lines matching text (`-r` recursive, `-i` ignore case) | `grep -ri "error" /var/log` |
| `locate` | Finds files by name instantly using a prebuilt index (refresh with `sudo updatedb`) | `locate passwd` |
| `which` | Shows the full path of a command that would run | `which python3` |

`find` looks for files by their **properties**, and `grep` looks for **text** inside them.

### Wildcards

| Symbol | One-line explanation | Example |
|---|---|---|
| `*` | Matches any number of characters | `ls *.txt` |
| `?` | Matches exactly one character | `ls file?.txt` |
| `[abc]` | Matches one character from the set (`[a-z]` for a range) | `ls file[12].txt` |

### Standard streams

| Stream | Number | One-line explanation |
|---|---|---|
| stdin | 0 | Input a program reads (keyboard or piped data) |
| stdout | 1 | Normal output a program prints |
| stderr | 2 | Error messages, kept separate from normal output |

### Redirection

| Operator | One-line explanation | Example |
|---|---|---|
| `>` | Sends output to a file, **overwriting** it | `ls > list.txt` |
| `>>` | Sends output to a file, **appending** to the end | `echo hi >> list.txt` |
| `2>` | Sends only error messages to a file | `ls /nope 2> err.txt` |
| `2>&1` | Sends errors to the same place as normal output | `cmd > all.txt 2>&1` |

Tip: `2>/dev/null` throws errors away, which is useful with `find / -name x 2>/dev/null`.

### Pipes

| Operator | One-line explanation | Example |
|---|---|---|
| `\|` | Feeds the output of one command into the input of the next | `ls /etc \| wc -l` |

### Useful pipe tools

| Command | One-line explanation | Example |
|---|---|---|
| `sort` | Sorts lines alphabetically (`-n` numerically, `-r` reversed) | `sort names.txt` |
| `uniq -c` | Collapses **adjacent** duplicate lines and counts them (sort first) | `sort f \| uniq -c` |
| `cut` | Extracts columns or fields from each line (`-d` delimiter, `-f` field) | `cut -d: -f1 /etc/passwd` |
| `awk` | Processes text by columns and patterns, like a mini programming language | `awk '{print $1}' f.txt` |
| `tr` | Translates or deletes characters | `echo hi \| tr a-z A-Z` |
| `sed` | Edits text in a stream, most often find-and-replace | `sed 's/old/new/' f.txt` |

**Example combining several:** count the most frequent login shells on the system:
```
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -nr
```
## Key takeaways
-

## Still confusing / to revisit
-

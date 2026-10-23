# Linux cheat sheet (Kali)

## Navigation
`pwd` · `ls -la` · `cd <dir>` · `cd ~` · `cd -` · `cd ..` · `tree`

## Files
`touch f` · `mkdir -p a/b` · `cp -r src dst` · `mv old new` · `rm f` · `rm -r dir` · `ln -s target link`

## Read / search
`cat f` · `less f` · `head -n 5 f` · `tail -f f` · `wc -l f` · `find / -name "x" 2>/dev/null` · `grep -rni "text" dir` · `which cmd` · `man cmd`

## Redirection / pipes
`>` overwrite · `>>` append · `2>` errors · `cmd1 | cmd2` · `sort | uniq -c | sort -nr`

## Users / permissions
`whoami` · `id` · `groups` · `sudo cmd` · `su - user`
`chmod 755 f` · `chmod u+x f` · `chown user:group f` · `umask`
`adduser u` · `deluser u` · `groupadd g` · `usermod -aG g u`
Octal: r=4 w=2 x=1 → 7=rwx, 6=rw-, 5=r-x, 4=r--

## Processes / services
`ps aux` · `top` · `htop` · `pstree -p` · `kill PID` · `kill -9 PID` · `pkill name`
`systemctl status|start|stop|restart|enable|disable svc` · `journalctl -u svc` · `sudo ss -tulpn`

## System info
`uname -a` · `cat /etc/os-release` · `df -h` · `free -h` · `uptime` · `lsblk`

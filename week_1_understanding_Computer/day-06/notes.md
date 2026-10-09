# Day 06 Notes (own words)
- Absolute vs relative path:
  Absolute Path gives the full location fro the top of the filesystem, so it works the same no matter where you are. A relative path gives the location stating from your current working directory, so its meaning changes depending on where you are.
  	          Windows	                            Linux
  Absolute	C:\Users\Sam\Documents\report.docx	/home/sam/Documents/report.txt
  Relative	Documents\report.docx	              Documents/report.txt

  Useful shortcuts for relative paths: . is the current directory, .. is the parent directory, and ~ (Linux) is your home directory.

  Security angle: relative paths cause problems when software trusts them. If a program runs tool.exe without a full path, it may launch whichever copy it finds first, which attackers abuse in DLL hijacking and search-order hijacking. Relative paths with ../ are also used in path traversal attacks to escape a folder.
  
- Windows vs Linux path differences:
|            |    Windows      	   |         Linux        |
|Separator	 |    Backslash \	     |           Forward slash /
|Root	       |  Drive letters (C:\, D:\), one tree per drive |	Single root /, with drives mounted inside it (/mnt, /media) |
|Case sensitivity	| Not case-sensitive (File.txt = file.txt)	| Case-sensitive (File.txt ≠ file.txt) |
|User folders |	C:\Users\<name>	    |/home/<name> |
|System files	| C:\Windows, C:\Program Files	| /etc, /bin, /usr, /var |
|Hidden files	| A file attribute (hidden flag)	| Name starts with a dot (.bashrc) |
|Executables	| Defined by extension (.exe, .bat, .ps1)	| Defined by the execute permission, not the extension |
|Special characters	| Cannot use `< > : " / \ `|`	? *` in names |

- Where would malware hide on a filesystem, and why?
- What does `ls -la` show that `ls` doesn't?

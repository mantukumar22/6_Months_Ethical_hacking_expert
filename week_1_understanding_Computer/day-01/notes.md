# Day 01 Notes (own words)
- CPU = The brain of the computer. It follows instructions one tiny step at a time, billions of times per second, doing calculations & decisions that make programs run.
- RAM = The computer's short-term workspace. that hold's the programs and data you are using right now so the cpu reach them quickly, and it is erased when the power goes off. 
- Storage = The long-term place where files, apps, and operating system are kept. Data stays there after the shoutdown(HDD, SSD or NVMe).
- Motherboard = The main circuit board that everything plugs into. It connects the CPU, RAM, storage and other parts so they can talk to each other.
- GPU = A processor built for graphics and many small calculations at once. It draws what you see on screen and also speeds up game, video and Ai work.
- Operating System = The manager software that sits between you, your programs & your hardware. it decides which program get the CPU & RAM, organizes files, and controls who can do what.
- Process = A program that is currently running. chrome.exe on disk is just a file, but once launched it becomes a process in memory with its own ID (PID) that uses CPU and RAM.

## Which part would an attacker target first, and why?
The operating system and the software running on it, meaning processes and user accounts. Here is why:

It is the easiest way in. Attackers rarely break into the CPU or motherboard. They go after software bugs, unpatched systems, weak passwords and tricked users, which are far easier.
The OS controls everything. Once an attacker has control of it, or of an admin account, they can reach files, memory, the network and other programs.
Their code has to run as a process. Malware becomes a process, so it uses CPU and RAM and often hides among normal-looking processes. That is why you learn to spot an unusual process.
Storage and RAM are what they want to steal or damage. Storage holds the valuable data (documents, passwords), which ransomware encrypts or attackers copy out. RAM can hold passwords and keys in plain form while a program is running.

The I-P-M-S-O chain goes from the easiest target to the hardest. The first target is usually the user and the software (input and processing), then the data (memory and storage). Hardware attacks exist but are rare and expensive.

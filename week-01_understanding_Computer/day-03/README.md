# Day 03 — Hardware vs Software

## Learn
- **Hardware**: physical parts — CPU, RAM, SSD, GPU, motherboard, network adapter, keyboard, mouse.
- **Software**: instructions — Windows, Linux, Chrome, VS Code, Python, Nmap, Burp Suite.
- **Layer model**: `Application → OS → Drivers → Hardware`
  - Application asks the OS; OS asks the driver; driver talks to hardware.
  - A **driver** is a translator between OS and a specific device.

## Practical
1. Settings → System → About: note Processor, RAM, System type (64-bit?).
2. Device Manager: expand Network adapters, Display adapters, Disk drives, Processors. List what you see in `evidence/devices.md`.

## Cybersecurity perspective
Vulnerabilities exist at **every layer**:
- Application: bugs, bad input handling (e.g., SQL injection, XSS)
- OS: unpatched flaws, weak permissions
- Driver: kernel-level code; a bad driver = full system control
- Hardware/firmware: e.g., CPU flaws like Spectre/Meltdown, malicious USB devices

You don't need to be a hardware engineer; you need to know **where** a problem can sit, so you know where to look and what to patch.

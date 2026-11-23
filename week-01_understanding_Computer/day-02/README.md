# Day 02 — CPU, RAM & Storage

## Learn
**CPU**
- *Cores*: independent workers. *Threads*: task lanes per core. *Clock speed*: steps per second (GHz). *Instructions*: the tiny commands the CPU runs.

**RAM**
- Volatile: contents vanish when power is lost.
- Holds running programs and their data.
- More RAM = more things open at once without slowing to a crawl (swapping to disk is slow).

**Storage**
- HDD: spinning platters, slow, cheap. SSD: flash, fast. NVMe: SSD over a faster PCIe connection, fastest.
- Persistent: survives reboot.

## Practical
1. Task Manager → Performance. Record in `machine-specs.md`: CPU, cores, logical processors, RAM, storage type, GPU.
2. Task Manager → Processes. Pick 5 apps; record CPU / Memory / Disk use.

## Cybersecurity perspective
Malware that runs becomes a **process** and uses CPU, RAM, disk and network. Cryptominers spike CPU; ransomware spikes disk; botnets show odd network use. You can only spot "abnormal" if you know **normal** — this is the idea of a *baseline*.

RAM matters forensically: passwords, keys and decrypted data can exist in memory only, which is why memory forensics exists.

# Day 07 Notes (own words)
- What I understood best:
- What is still confusing:
- Plan for next week:

# IPMSO Chain in Computers

The **IPMSO chain** describes the basic flow of how a computer works:

**Input → Processing → Memory → Storage → Output**

(Some books call it the IPO cycle, or IPOS when storage is included.)

## Flow Diagram

```
 Input  →  Processing  →  Memory  →  Storage  →  Output
```

## Stages

| Stage | Meaning | Examples |
|-------|---------|----------|
| **I – Input** | Data enters the computer | Keyboard, mouse, mic, scanner, camera |
| **P – Processing** | The CPU calculates, compares, and follows instructions | CPU (ALU + Control Unit) |
| **M – Memory** | Holds data and programs currently in use. Fast but temporary (cleared when power goes off) | RAM |
| **S – Storage** | Keeps data permanently, even after shutdown | Hard disk, SSD, pen drive |
| **O – Output** | Shows the results to the user | Monitor, printer, speakers |

## Example: Writing a Letter

1. **Input:** You type the letter on the keyboard.
2. **Processing:** The CPU handles the typing and formatting.
3. **Memory:** The open document sits in RAM while you work.
4. **Storage:** You press Save and the file goes to the SSD.
5. **Output:** You see it on the screen or print it.

## Key Difference: Memory vs Storage

| | Memory (RAM) | Storage (SSD/HDD) |
|---|---|---|
| Speed | Very fast | Slower |
| Data kept | Temporarily | Permanently |
| Used for | Running programs | Saving files |

---

# CPU, RAM and Storage Roles

| Component | Role |
|-----------|------|
| **CPU** | The brain. Runs instructions, calculates, and controls the other parts |
| **RAM** | Fast, temporary workspace for programs and data in use right now. Clears when power goes off |
| **Storage (SSD/HDD)** | Permanent and slower. Holds the OS, apps, and files |

Programs are loaded from storage into RAM before the CPU runs them.

# Layer Model of a Computer System

```
 5. User
 4. Applications        (browser, editor, games)
 3. System software     (drivers, utilities, shell)
 2. Operating system    (kernel)
 1. Hardware            (CPU, RAM, disk, devices)
```

Each layer talks only to the layer next to it. Apps never touch hardware directly; they ask the OS.

# What an Operating System Does

- **CPU management:** schedules which process runs and when
- **Memory management:** gives each process its own RAM space
- **File and storage management:** organizes files and folders
- **Device control:** talks to hardware through drivers
- **Security:** users, passwords, permissions
- **User interface:** GUI or command line

# Program vs Process

| | Program | Process |
|---|---|---|
| State | Passive file on disk | Running instance in RAM |
| Example | `chrome.exe` | Chrome open and running |
| Resources | None while stored | Has memory, CPU time, and a PID |

One program can have many processes (open Chrome twice, get two processes).

# Absolute vs Relative Path

| Type | Meaning | Windows example | Linux example |
|------|---------|-----------------|---------------|
| **Absolute** | Full path from the root, works from anywhere | `C:\Users\mantu\Documents\notes.txt` | `/home/mantu/Documents/notes.txt` |
| **Relative** | Path from the current folder | `Documents\notes.txt` | `Documents/notes.txt` |

Shortcuts: `.` is the current folder and `..` is the parent folder.

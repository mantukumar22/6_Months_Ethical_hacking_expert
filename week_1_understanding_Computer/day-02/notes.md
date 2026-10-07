# Day 02 Notes (own words)
- Core vs thread: A core is a physical processing unit on the CPU, with its own execution hardware. A thread is a stream of instructions that a core works on. Without multithreading, one core runs one thread at a time. With Hyper-Threading (Intel) or SMT (AMD), each core presents itself as two logical processors, so it can switch between two threads quickly and fill idle gaps in its pipeline.

The key difference: two threads on one core share that core's resources, so they don't give you double the performance, usually only about 20-30% more on heavy multithreaded work. Two real cores run truly in parallel.
- Why RAM is volatile: RAM (DRAM) stores each bit as an electrical charge in a tiny capacitor. Two things follow from this:

Charge leaks away. Even with power on, the capacitors must be refreshed thousands of times per second, or the data is lost.
No power means no refresh. When you shut down, the charge drains within a fraction of a second and the contents disappear.

This is a trade-off: DRAM is extremely fast and cheap per bit, but it can't hold data without power. That's why files must be saved to storage, and why unsaved work is lost in a crash or power cut.
- HDD vs SSD vs NVMe:
- What would a cryptominer look like in Task Manager?
Cryptominers use your hardware to compute hashes for cryptocurrency, so the signs are sustained, unexplained resource use:

 - Constant high CPU or GPU usage (often 80-100%) while you're idle, with nothing demanding open. Check the Performance tab, especially the GPU graphs, and look at the GPU "Compute" or "CUDA" engine rather than just "3D."
 - A single process using heavy resources with an unfamiliar or disguised name, such as one that imitates a system process (svch0st.exe, csrss in the wrong folder, or random letters).
 - High power use and heat: fans spinning loudly, the laptop hot, battery draining fast, even when idle.
Persistence: the process returns after you end it, or reappears after reboot (check the Startup tab).
 - Odd behavior: it may drop in usage when you open Task Manager, because some miners pause to hide.
Network activity to a mining pool, which appears as steady low-bandwidth traffic.

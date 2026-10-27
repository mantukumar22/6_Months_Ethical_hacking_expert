import os
import platform

print("OS:", platform.system())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("CPU count:", os.cpu_count())

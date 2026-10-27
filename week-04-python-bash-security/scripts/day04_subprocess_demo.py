"""Safe use of subprocess: a fixed command as an argument LIST, no shell."""
import subprocess

# Safe: fixed command, list of arguments, no shell involved.
result = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True,
    timeout=5,
)
print("Exit code:", result.returncode)
print("Output:", result.stdout.strip())

# UNSAFE pattern (do NOT do this with untrusted input):
#   user_input = input("Host: ")
#   subprocess.run("ping " + user_input, shell=True)
# An input like "8.8.8.8; rm -rf ~" would run a second command.
# If you must accept input, validate it strictly (e.g. ipaddress module)
# and still pass it as a list item: subprocess.run(["ping", "-c", "1", ip])

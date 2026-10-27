username = input("Enter your username: ")
system = input("Enter your operating system: ")

print("Username:", username)
print("Operating system:", system)

if system.lower() == "kali":
    print("Linux security lab detected.")
elif system.lower() == "windows":
    print("Windows environment detected.")
else:
    print("Other operating system.")

# TODO (Notes): accept three operating-system names and handle unexpected input.

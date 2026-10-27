import socket

target = input("Enter target IP (use 127.0.0.1): ")
ports = [22, 80, 443, 8000]

if target not in ("127.0.0.1", "localhost"):
    raise SystemExit("For this exercise, use localhost only.")

for port in ports:
    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        ) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{port}: TCP connection succeeded")
            else:
                print(f"{port}: No TCP connection")
    except OSError as error:
        print(f"{port}: Error - {error}")

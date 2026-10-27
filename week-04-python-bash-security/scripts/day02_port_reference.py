ports = {
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP",
    # TODO: add three more common ports
}


def describe_port(port):
    return ports.get(port, "Unknown service")


for port in ports:
    print(port, describe_port(port))

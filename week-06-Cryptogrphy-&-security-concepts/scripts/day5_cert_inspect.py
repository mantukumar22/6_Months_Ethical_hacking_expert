"""Day 5: Inspect a site's TLS certificate with Python's standard library.

Usage:  python3 scripts/day5_cert_inspect.py [host] [--port 443] [--cafile PATH]
Makes one normal TLS connection (like a browser). Does not scan or attack.
"""
import argparse
import socket
import ssl
import time


def get_cert(host, port, cafile=None):
    context = ssl.create_default_context(cafile=cafile)  # verifies chain + hostname
    with socket.create_connection((host, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=host) as tls:
            return tls.getpeercert(), tls.version(), tls.cipher()


def flatten(name_tuples):
    return ", ".join(f"{k}={v}" for rdn in name_tuples for k, v in rdn)


def main():
    parser = argparse.ArgumentParser(description="Show a site's TLS certificate")
    parser.add_argument("host", nargs="?", default="example.com")
    parser.add_argument("--port", type=int, default=443)
    parser.add_argument("--cafile", help="extra CA file (for local lab servers)")
    args = parser.parse_args()

    try:
        cert, version, cipher = get_cert(args.host, args.port, args.cafile)
    except ssl.SSLCertVerificationError as error:
        raise SystemExit(f"Certificate verification FAILED: {error.verify_message}")
    except (OSError, ssl.SSLError) as error:
        raise SystemExit(f"Connection failed: {error}")

    not_after = ssl.cert_time_to_seconds(cert["notAfter"])
    days_left = int((not_after - time.time()) // 86400)

    print(f"Host           : {args.host}:{args.port}")
    print(f"Subject        : {flatten(cert['subject'])}")
    print(f"Issuer         : {flatten(cert['issuer'])}")
    print(f"Valid from     : {cert['notBefore']}")
    print(f"Valid until    : {cert['notAfter']}  ({days_left} days left)")
    print(f"Serial number  : {cert.get('serialNumber')}")
    sans = [value for kind, value in cert.get("subjectAltName", ()) if kind == "DNS"]
    print(f"SAN (DNS)      : {', '.join(sans) if sans else '-'}")
    print(f"TLS version    : {version}")
    print(f"Cipher suite   : {cipher[0]} ({cipher[2]}-bit)")
    print("Chain/hostname : verified OK (trusted CA, name matches)")
    if days_left < 14:
        print("WARNING: certificate expires soon.")


if __name__ == "__main__":
    main()

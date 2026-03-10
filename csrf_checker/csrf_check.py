import requests
from bs4 import BeautifulSoup
import sys

print("""
========================================
      ETHICAL CYBER LAB - CSRF CHECKER
========================================
Educational CSRF protection analyzer
Author: Divine Sunday OFUOWOICHO
========================================
""")

if len(sys.argv) != 2:
    print("Usage: python3 csrf_check.py <target_url>")
    print("Example: python3 csrf_check.py http://example.com/login")
    sys.exit()

url = sys.argv[1]

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.RequestException:
    print("[-] Could not connect to the target")
    sys.exit()

soup = BeautifulSoup(response.text, "html.parser")

forms = soup.find_all("form")

if not forms:
    print("[!] No forms found on the page.")
    sys.exit()

print(f"\n[+] Found {len(forms)} form(s) on the page\n")

for i, form in enumerate(forms, start=1):

    print(f"--- Form {i} ---")

    inputs = form.find_all("input")

    csrf_token_found = False

    for input_tag in inputs:

        name = input_tag.get("name")

        if name:
            lower_name = name.lower()

            if "csrf" in lower_name or "token" in lower_name:
                csrf_token_found = True

    if csrf_token_found:
        print("[+] CSRF token detected (good protection)")
    else:
        print("[!] Possible missing CSRF protection")

    print()

print("CSRF analysis complete.")

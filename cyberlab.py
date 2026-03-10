import sys
import subprocess

print("""
========================================
        ETHICAL CYBER LAB
========================================
Institutional Cybersecurity Toolkit
Author: Divine Sunday OFUOWOICHO
========================================
""")

if len(sys.argv) < 3:
    print("""
Usage:

python cyberlab.py recon <domain>
python cyberlab.py sqli <url>
python cyberlab.py xss <url>
python cyberlab.py csrf <url>

Example:

python cyberlab.py recon example.com
python cyberlab.py sqli http://testphp.vulnweb.com/listproducts.php?cat=1
""")
    sys.exit()

tool = sys.argv[1]
target = sys.argv[2]

if tool == "recon":
    subprocess.call(["python3", "recon_scripts/recon.py", target])

elif tool == "sqli":
    subprocess.call(["python3", "sql_injection/sqli_test.py", target])

elif tool == "xss":
    subprocess.call(["python3", "xss_scanner/xss_test.py", target])

elif tool == "csrf":
    subprocess.call(["python3", "csrf_checker/csrf_check.py", target])

else:
    print("Unknown module.")
    print("Available modules: recon, sqli, xss, csrf")

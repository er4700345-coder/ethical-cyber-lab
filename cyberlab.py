import sys
import subprocess
import threading
import time
from colorama import Fore, Style

# ASCII Hacker Banner
banner = f"""
{Fore.CYAN}
   _____ _   _ _   _ _       _     _        _ 
  | ____| |_| | | | (_) __ _| |__ | | ___  | |
  |  _| | __| | | | | |/ _` | '_ \| |/ _ \ | |
  | |___| |_| | |_| | | (_| | | | | |  __/ |_|
  |_____|\\__|_|\\___/|_|\\__, |_| |_|_|\\___| (_)
                       |___/                   
Ethical Cyber Lab - Full Pentest Toolkit
Author: Divine Sunday OFUOWOICHO
{Style.RESET_ALL}
"""

print(banner)

if len(sys.argv) < 3:
    print(f"""
Usage:

{Fore.YELLOW}python cyberlab.py recon <domain>{Style.RESET_ALL}
{Fore.YELLOW}python cyberlab.py sqli <url>{Style.RESET_ALL}
{Fore.YELLOW}python cyberlab.py xss <url>{Style.RESET_ALL}
{Fore.YELLOW}python cyberlab.py csrf <url>{Style.RESET_ALL}

Example:

python cyberlab.py recon example.com
""")
    sys.exit()

tool = sys.argv[1]
target = sys.argv[2]

# Thread wrapper for faster port scanning (used in recon)
def thread_target(func, args):
    thread = threading.Thread(target=func, args=args)
    thread.start()
    return thread

# Recon module
if tool == "recon":
    subprocess.call(["python3", "recon_scripts/recon.py", target])

# SQLi module
elif tool == "sqli":
    subprocess.call(["python3", "sql_injection/sqli_test.py", target])

# XSS module
elif tool == "xss":
    subprocess.call(["python3", "xss_scanner/xss_test.py", target])

# CSRF module
elif tool == "csrf":
    subprocess.call(["python3", "csrf_checker/csrf_check.py", target])

else:
    print(f"{Fore.RED}[!] Unknown module{Style.RESET_ALL}")
    print("Available modules: recon, sqli, xss, csrf")

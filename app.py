from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import socket

app = Flask(__name__)

# ---------------------------
# Home Page
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        module = request.form.get("module")
        target = request.form.get("target")

        if module == "recon":
            result = recon(target)
        elif module == "sqli":
            result = sqli_test(target)
        elif module == "xss":
            result = xss_test(target)
        elif module == "csrf":
            result = csrf_test(target)
        else:
            result = "Unknown module"

    return render_template("index.html", result=result)

# ---------------------------
# Recon Module
# ---------------------------
def recon(domain):
    output = f"Recon for {domain}\n\n"
    try:
        ip = socket.gethostbyname(domain)
        output += f"IP Address: {ip}\n"
    except:
        return "Cannot resolve domain"

    ports = [21,22,23,25,53,80,110,139,143,443,445,3306,8080]
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((ip, port)) == 0:
            output += f"[OPEN] Port {port}\n"
        sock.close()
    return output

# ---------------------------
# SQLi Module
# ---------------------------
def sqli_test(url):
    payloads = ["' OR '1'='1", "' OR 1=1--", "' OR ''='"]
    result = ""
    for p in payloads:
        try:
            r = requests.get(url+p, timeout=5)
            errors = ["sql syntax","mysql","warning","unterminated","odbc"]
            for e in errors:
                if e in r.text.lower():
                    result += f"[!] Possible SQLi with payload: {p}\n"
        except:
            result += "Connection error\n"
    return result or "No issues detected"

# ---------------------------
# XSS Module
# ---------------------------
def xss_test(url):
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    result = ""
    for p in payloads:
        try:
            r = requests.get(url+p, timeout=5)
            if p in r.text:
                result += f"[!] Possible XSS with payload: {p}\n"
        except:
            result += "Connection error\n"
    return result or "No issues detected"

# ---------------------------
# CSRF Module
# ---------------------------
def csrf_test(url):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        forms = soup.find_all("form")
        output = ""
        for i, form in enumerate(forms,1):
            csrf_token = any("csrf" in (inp.get("name") or "").lower() for inp in form.find_all("input"))
            output += f"Form {i}: " + ("CSRF token detected\n" if csrf_token else "Possible missing CSRF protection\n")
        return output or "No forms found"
    except:
        return "Connection error"

# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)

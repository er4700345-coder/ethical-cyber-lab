from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        module = request.form.get("module")
        target = request.form.get("target")

        try:
            if module == "recon":
                result = subprocess.check_output(["python3", "recon_scripts/recon.py", target], stderr=subprocess.STDOUT).decode()
            elif module == "sqli":
                result = subprocess.check_output(["python3", "sql_injection/sqli_test.py", target], stderr=subprocess.STDOUT).decode()
            elif module == "xss":
                result = subprocess.check_output(["python3", "xss_scanner/xss_test.py", target], stderr=subprocess.STDOUT).decode()
            elif module == "csrf":
                result = subprocess.check_output(["python3", "csrf_checker/csrf_check.py", target], stderr=subprocess.STDOUT).decode()
            elif module == "ip":
                result = subprocess.check_output(["python3", "ip_intel/ip_lookup.py", target], stderr=subprocess.STDOUT).decode()
            else:
                result = "Unknown module"
        except Exception as e:
            result = f"Error running module: {str(e)}"

    return render_template("index.html", result=result)
  
if __name__ == "__main__":
    app.run(debug=True)

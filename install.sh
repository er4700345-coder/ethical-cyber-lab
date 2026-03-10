#!/bin/bash

# ========================================
#   ETHICAL CYBER LAB - Linux Installer
# ========================================
# Author: Divine Sunday OFUOWOICHO
# Description: Sets up the Ethical Cyber Lab toolkit on Linux
# ========================================

echo "🚀 Starting Ethical Cyber Lab Linux setup..."

# 1. Update system
echo "[*] Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

# 2. Install Python3 and pip if not installed
echo "[*] Checking Python3 installation..."
if ! command -v python3 &> /dev/null
then
    echo "[!] Python3 not found. Installing..."
    sudo apt install python3 -y
else
    echo "[+] Python3 is already installed"
fi

echo "[*] Checking pip3 installation..."
if ! command -v pip3 &> /dev/null
then
    echo "[!] pip3 not found. Installing..."
    sudo apt install python3-pip -y
else
    echo "[+] pip3 is already installed"
fi

# 3. Install required Python packages
echo "[*] Installing required Python packages..."
pip3 install --upgrade pip
pip3 install requests beautifulsoup4

# 4. Make cyberlab.py executable
echo "[*] Making cyberlab.py executable..."
chmod +x cyberlab.py

# 5. Optional: Add to PATH
echo "[*] Adding cyberlab.py to /usr/local/bin..."
sudo ln -sf $(pwd)/cyberlab.py /usr/local/bin/cyberlab

echo "✅ Installation complete!"
echo "You can now run the toolkit anywhere with:"
echo "   cyberlab recon example.com"
echo "   cyberlab sqli http://target.com?id=1"
echo "   cyberlab xss http://target.com?q="
echo "   cyberlab csrf http://target.com/login"
echo "🔥 Enjoy your Ethical Cyber Lab!"

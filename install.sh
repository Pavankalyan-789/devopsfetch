#!/bin/bash
set -e

echo "[+] Installing dependencies..."
sudo apt update -y
sudo apt install -y python3 python3-pip nginx docker.io
pip3 install prettytable

echo "[+] Copying devopsfetch to /usr/local/bin..."
sudo mkdir -p /usr/local/bin/devopsfetch/modules
sudo cp devopsfetch.py /usr/local/bin/devopsfetch/
sudo cp modules/*.py /usr/local/bin/devopsfetch/modules/
sudo chmod +x /usr/local/bin/devopsfetch/devopsfetch.py

echo "[+] Setting up log directory..."
sudo mkdir -p /var/log/devopsfetch
sudo chmod 777 /var/log/devopsfetch

echo "[+] Installing systemd service..."
sudo cp devopsfetch.service /etc/systemd/system/devopsfetch.service
sudo systemctl daemon-reload
sudo systemctl enable devopsfetch.service
sudo systemctl start devopsfetch.service

echo "[+] Installation complete! Use 'sudo systemctl status devopsfetch' to check service."

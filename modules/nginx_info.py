import os
import re

NGINX_PATH = "/etc/nginx/sites-enabled/"

def list_nginx(domain):
    files = os.listdir(NGINX_PATH)
    if domain == "all":
        print("=== Nginx Domains and Ports ===")
        for file in files:
            path = os.path.join(NGINX_PATH, file)
            with open(path) as f:
                data = f.read()
                server_names = re.findall(r"server_name\s+([^\s;]+)", data)
                ports = re.findall(r"listen\s+(\d+)", data)
                print(f"{file}: Domains={server_names}, Ports={ports}")
    else:
        path = os.path.join(NGINX_PATH, domain)
        if os.path.exists(path):
            with open(path) as f:
                print(f"=== Full config for {domain} ===\n")
                print(f.read())
        else:
            print(f"Config file not found for domain: {domain}")

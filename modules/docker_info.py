import subprocess
from prettytable import PrettyTable

def list_docker(container):
    if container == "all":
        print("=== Docker Images ===")
        print(subprocess.getoutput("docker images"))
        print("\n=== Docker Containers ===")
        print(subprocess.getoutput("docker ps -a"))
    else:
        print(f"Details for container: {container}")
        print(subprocess.getoutput(f"docker inspect {container}"))

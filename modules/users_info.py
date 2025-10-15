import subprocess

def list_users(username):
    if username == "all":
        print("=== All Users and Last Login Times ===")
        print(subprocess.getoutput("lastlog"))
    else:
        print(f"Details for user: {username}")
        print(subprocess.getoutput(f"grep '^{username}:' /etc/passwd"))
        print("\nLast login info:")
        print(subprocess.getoutput(f"lastlog -u {username}"))

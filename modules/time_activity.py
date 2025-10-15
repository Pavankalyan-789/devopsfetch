import subprocess

def show_time_logs(start, end):
    print(f"=== System Logs from {start} to {end} ===")
    cmd = f"sudo journalctl --since='{start}' --until='{end}'"
    print(subprocess.getoutput(cmd))

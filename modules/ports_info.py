import psutil
from prettytable import PrettyTable

def show_ports(port_filter=None):
    table = PrettyTable()
    table.field_names = [
        "Protocol", "State", "Local Address", "Peer Address", "Process"
    ]

    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
        pid = conn.pid or "N/A"
        process_name = "N/A"
        try:
            if pid != "N/A":
                process_name = psutil.Process(pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

        state = conn.status
        proto = "TCP" if conn.type == 1 else "UDP"

        if port_filter:
            if str(conn.laddr.port) == str(port_filter):
                table.add_row([proto, state, laddr, raddr, process_name])
        else:
            table.add_row([proto, state, laddr, raddr, process_name])

    print(table)

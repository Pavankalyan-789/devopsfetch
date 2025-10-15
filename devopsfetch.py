#!/usr/bin/env python3
import argparse
from modules.ports_info import show_ports
from modules.docker_info import list_docker
from modules.nginx_info import list_nginx
from modules.users_info import list_users
from modules.time_activity import show_time_logs
from modules.monitor import monitor_loop

def main():
    parser = argparse.ArgumentParser(description="DevOpsFetch — Server Information Retrieval Tool")

    parser.add_argument("-p", "--port", nargs="?", const="all", help="Display all active ports or details for a specific port")
    parser.add_argument("-d", "--docker", nargs="?", const="all", help="List Docker images/containers or details for a specific container")
    parser.add_argument("-n", "--nginx", nargs="?", const="all", help="Display all Nginx domains or details for a specific domain")
    parser.add_argument("-u", "--users", nargs="?", const="all", help="List users and last login times or details for a specific user")
    parser.add_argument("-t", "--time", nargs=2, metavar=('START', 'END'), help="Display activities within a specified time range (YYYY-MM-DD)")
    parser.add_argument("-m", "--monitor", action="store_true", help="Start continuous monitoring mode")
    args = parser.parse_args()

    if args.port:
        show_ports(args.port)
    elif args.docker:
        list_docker(args.docker)
    elif args.nginx:
        list_nginx(args.nginx)
    elif args.users:
        list_users(args.users)
    elif args.time:
        show_time_logs(args.time[0], args.time[1])
    elif args.monitor:
        monitor_loop()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

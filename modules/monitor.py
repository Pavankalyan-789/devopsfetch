import time
import logging
from logging.handlers import RotatingFileHandler
from modules.ports_info import show_ports
from modules.docker_info import list_docker
from modules.nginx_info import list_nginx
from modules.users_info import list_users

LOG_FILE = "/var/log/devopsfetch/devopsfetch.log"

def setup_logger():
    logger = logging.getLogger("DevOpsFetch")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)
    logger.addHandler(handler)
    return logger

def monitor_loop(interval=60):
    logger = setup_logger()
    logger.info("Starting DevOpsFetch monitoring...")
    while True:
        logger.info("=== Monitoring Cycle Start ===")
        logger.info("Ports Info:")
        logger.info("".join(["\n", "="*20, "\n"]))
        logger.info(str(list_ports("all")))
        logger.info(str(list_docker("all")))
        logger.info(str(list_nginx("all")))
        logger.info(str(list_users("all")))
        logger.info("=== Monitoring Cycle End ===\n")
        time.sleep(interval)

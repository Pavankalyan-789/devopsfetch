# DevOpsFetch

DevOpsFetch is a Python-based **system information retrieval and monitoring tool** designed for DevOps engineers. It collects and displays critical system information such as active ports, logged-in users, Nginx configuration, Docker container status, and tracks time-based activities.


## **Features**

- **Port Monitoring:** Lists all active ports and their states.
- **User Monitoring:** Displays currently logged-in users.
- **Nginx Monitoring:** Retrieves Nginx installation and configuration information.
- **Docker Monitoring:** Shows Docker images and running containers.
- **Time Activity Logging:** Monitors system activity over time.
- **Systemd Service:** Optional background monitoring service for continuous logging.

---

## **Project Structure**

DEVOPSFETCH/
│
├─ modules/
│ ├─ docker_info.py # Fetches Docker images and container info
│ ├─ monitor.py # Main monitoring module
│ ├─ nginx_info.py # Retrieves Nginx configuration and status
│ ├─ ports_info.py # Checks active ports and services
│ ├─ time_activity.py # Logs system activity over time
│ └─ users_info.py # Fetches logged-in user info
│
├─ venv/ # Python virtual environment
│ ├─ bin/
│ ├─ include/
│ └─ lib/
│
├─ devopsfetch.py # Main executable script
├─ devopsfetch.service # Systemd service file for background execution
├─ install.sh # Installation script for setting up dependencies
├─ README.md # Project documentation
└─ requirements.txt # Python dependencies


## **Installation**

cd devopsfetch
Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
Install dependencies:

pip install -r requirements.txt
(Optional) Run the installation script:

bash install.sh

python3 devopsfetch.py -p 80    # Display active ports
python3 devopsfetch.py -u       # Show logged-in users
python3 devopsfetch.py -n       # Get Nginx info
python3 devopsfetch.py -d       # List Docker images and containers
python3 devopsfetch.py -t       # Log time-based activity

To display active ports and services:

python3 devopsfetch.py --port
(venv) clear@DESKTOP-Q3LJRKI:/mnt/c/Users/HP/devopsfetch$ python3 devopsfetch.py -p 80
+----------+--------+---------------+--------------+---------+
| Protocol | State  | Local Address | Peer Address | Process |
+----------+--------+---------------+--------------+---------+
|   TCP    | LISTEN |     :::80     |              |   N/A   |
|   TCP    | LISTEN |   0.0.0.0:80  |              |   N/A   |
+----------+--------+---------------+--------------+---------+

🔁 Continuous Monitoring Mode

To log port data continuously:

python3 devopsfetch.py --monitor

📜 Requirements

Python 3.10+

psutil (for network and process info)

prettytable (for formatted CLI tables)

Linux or WSL environment (for /var/log access)



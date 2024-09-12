import psutil
import time
import logging

# Set thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_info.percent}%")
    return memory_info.percent

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f"Low disk space detected: {disk_info.percent}%")
    return disk_info.percent

def check_running_processes():
    processes = len(psutil.pids())
    return processes

def monitor_system():
    while True:
        cpu = check_cpu_usage()
        memory = check_memory_usage()
        disk = check_disk_space()
        processes = check_running_processes()

        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory}%")
        print(f"Disk Usage: {disk}%")
        print(f"Running Processes: {processes}")
        print("----------------------------")

        time.sleep(10)

if __name__ == "__main__":
    monitor_system()

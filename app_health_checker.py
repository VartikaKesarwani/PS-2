import requests
import time
import logging

# Set the URL of the application
APP_URL = 'https://your-application-url.com'
EXPECTED_STATUS = 200  # Expected HTTP status code when the app is up

# Setup logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_application_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == EXPECTED_STATUS:
            logging.info(f"Application is UP. Status Code: {response.status_code}")
            print("Application is UP.")
        else:
            logging.warning(f"Application is DOWN. Status Code: {response.status_code}")
            print("Application is DOWN.")
    except requests.ConnectionError:
        logging.error("Failed to connect to the application.")
        print("Application is DOWN. Failed to connect.")

def monitor_application():
    while True:
        check_application_health()
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    monitor_application()

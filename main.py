from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import requests
import atexit
import os

load_dotenv()  # Load .env variables

# Replace with your actual Render service URL
PING_URL = os.getenv("PING_URL", "https://find-local-service-and-booking-system.onrender.com/")

def ping_render():
    try:
        response = requests.get(PING_URL)
        print(f"Pinged Render: {response.status_code}")
    except Exception as e:
        print(f"Ping failed: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(ping_render, 'interval', minutes=5)
scheduler.start()

# atexit.register(lambda: scheduler.shutdown())

# Prevent script from exiting immediately if run standalone
if __name__ == "__main__":
    import time
    while True:
        time.sleep(60)

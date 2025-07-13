from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime

app = FastAPI()

# 🔁 Dummy API endpoint
@app.get("/api/serverup")
def hello():
    return {"message": "Hello from Smart Service!", "time": str(datetime.datetime.now())}

# 🌐 Function to ping Render server
def ping_render_server():
    try:
        # Replace with your actual Render service URL
        url = "https://find-local-service-and-booking-system.onrender.com/api/serverup"
        response = requests.get(url)
        print(f"[{datetime.datetime.now()}] Pinged Render. Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error pinging Render: {e}")

# 🕒 Scheduler that runs every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(ping_render_server, 'interval', minutes=1)
scheduler.start()

# ⚠ Make sure scheduler shuts down with app
# import atexit
# atexit.register(lambda: scheduler.shutdown())
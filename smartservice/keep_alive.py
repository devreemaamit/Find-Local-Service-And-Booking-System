import requests
import time

# URL = "https://your-app.onrender.com/ping/"  # Replace with your actual Render URL
URL = "https://loan-app-wjbq.onrender.com/api/server/start"
def ping_server():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print("✅ Pinged successfully:", response.text)
        else:
            print("⚠️ Ping failed with status:", response.status_code)
    except Exception as e:
        print("❌ Error pinging server:", e)

# Ping every 5 minutes
if __name__ == "__main__":
    print("🔄 Auto-pinger started.")
    while True:
        ping_server()
        time.sleep(300)  # 5 minutes = 300 seconds

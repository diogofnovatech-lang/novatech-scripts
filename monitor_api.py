# NovaTech Solutions - API Latency Monitor
# Author: dferreira
# Polls internal endpoints and logs response times

import time
import random

ENDPOINTS = [
    "/api/v1/status",
    "/api/v1/users",
    "/api/v1/reports",
    "/api/v1/notifications",
]

def fake_ping(endpoint):
    latency = random.uniform(20, 400)
    status = 200 if latency < 350 else 503
    return status, round(latency, 2)

def monitor(interval=10):
    print("Starting API monitor...")
    while True:
        for ep in ENDPOINTS:
            status, latency = fake_ping(ep)
            tag = "OK" if status == 200 else "ERROR"
            print(f"[{tag}] {ep} — {latency}ms (HTTP {status})")
        time.sleep(interval)

if __name__ == "__main__":
    monitor()

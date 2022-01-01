import os
import time

import psutil
import requests

DISKS = os.environ.get("DISKS", "/root")
INTERVAL = os.environ.get("INTERVAL", "3600")
THRESHOLD = os.environ.get("THRESHOLD", "90")
WEBHOOK = os.environ.get("WEBHOOK")


while True:
    for disk in DISKS.split(","):
        free = psutil.disk_usage(disk).free / psutil.disk_usage(disk).total * 100
        if free > int(THRESHOLD):
            continue
        message = f"Warning - '{disk}' has {free:.2f}% free space"
        requests.post(WEBHOOK, json={"content": message})
    time.sleep(int(INTERVAL))

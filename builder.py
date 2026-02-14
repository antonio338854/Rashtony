import os

def build_exe(name: str):
    os.system(f"pyinstaller --onefile --noconsole {name}.py")
    print(f"[+] Executável '{name}.exe' criado em './dist/'")

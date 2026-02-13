import os
import shutil
from datetime import datetime


def gerar_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def criar_pasta_temporaria(nome_base):
    nome_pasta = f"temp_{nome_base}_{gerar_timestamp()}"
    os.makedirs(nome_pasta, exist_ok=True)
    return nome_pasta

def gerar_nome_pasta(nome_base):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{nome_base}_{timestamp}"

def limpar_pasta(caminho):
    try:
        if os.path.exists(caminho):
            shutil.rmtree(caminho)
            print(f"Pasta {caminho} removida com sucesso.")
    except Exception as e:
        print(f"Erro ao remover pasta {caminho}: {e}")



def sanitizar_nome(nome):
    return "".join(c for c in nome if c.isalnum() or c in (" ", "_", "-")).strip()


def log(mensagem):
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] {mensagem}")

import requests
import os


class Downloader:

    def baixar_imagens(self, urls, pasta_destino):
        arquivos = []

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        for i, url in enumerate(urls):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                nome_arquivo = os.path.join(
                    pasta_destino, f"imagem_{i+1}.jpg"
                )

                with open(nome_arquivo, "wb") as f:
                    f.write(response.content)

                arquivos.append(nome_arquivo)

            except Exception as e:
                print(f"Erro ao baixar {url}: {e}")

        return arquivos

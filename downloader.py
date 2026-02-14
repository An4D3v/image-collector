import requests
import os
from datetime import datetime


class Downloader:

    def baixar_imagens(self, imagens, pasta_destino):

        resultados = []

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        for i, imagem in enumerate(imagens):
            try:
                response = requests.get(imagem["url"], timeout=10)
                response.raise_for_status()

                nome_arquivo = f"{imagem['id']}.jpg"
                caminho_completo = os.path.join(pasta_destino, nome_arquivo)

                with open(caminho_completo, "wb") as f:
                    f.write(response.content)

                resultados.append({
                    "unsplash_id": imagem["id"],
                    "description": imagem.get("description"),
                    "image_url": imagem["url"],
                    "file_name": nome_arquivo,
                    "file_path": caminho_completo,
                    "file_size": len(response.content),
                    "downloaded_at": datetime.now(),
                    "status": "success"
                })

            except Exception as e:
                print(f"Erro ao baixar {imagem['url']}: {e}")

                resultados.append({
                    "unsplash_id": imagem["id"],
                    "image_url": imagem["url"],
                    "status": "error",
                    "error_message": str(e),
                    "downloaded_at": datetime.now()
                })

        return resultados

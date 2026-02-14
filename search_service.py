import requests
import os
from dotenv import load_dotenv

load_dotenv()


class SearchService:

    def __init__(self):
        self.base_url = "https://api.unsplash.com/search/photos"
        self.access_key = os.getenv("UNSPLASH_ACCESS_KEY")

    def buscar_imagens(self, query, quantidade):

        response = requests.get(
            self.base_url,
            params={
                "query": query,
                "per_page": quantidade,
                "client_id": self.access_key
            }
        )
 
        if response.status_code != 200:
            print("Erro na API:", response.json())
            return []

        dados = response.json()["results"]

        imagens = []

        for item in dados:
            imagens.append({
                "id": item["id"],
                "url": item["urls"]["regular"],
                "description": item.get("alt_description")
            })

        return imagens

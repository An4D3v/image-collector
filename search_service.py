import requests
from config import UNSPLASH_ACCESS_KEY


class SearchService:

    BASE_URL = "https://api.unsplash.com/search/photos"

    def buscar_imagens(self, query, quantidade=5):
        headers = {
            "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
        }

        params = {
            "query": query,
            "per_page": quantidade
        }

        response = requests.get(self.BASE_URL, headers=headers, params=params)
        data = response.json()

        imagens = []

        for item in data.get("results", []):
            imagens.append(item["urls"]["regular"])

        return imagens

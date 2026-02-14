from search_service import SearchService
from downloader import Downloader
from drive_service import DriveService
from database import Database
from utils import criar_pasta_temporaria, limpar_pasta, sanitizar_nome, log


def main():
    log("Iniciando Image Collector")

    query = input("Digite o termo de busca: ")
    query_limpa = sanitizar_nome(query)

    while True:
        try:
            quantidade = int(input("Quantidade de imagens (máx 10): "))
            if 1 <= quantidade <= 10:
                break
            else:
                print("Digite um número entre 1 e 10.")
        except ValueError:
            print("Digite um número válido.")

    search = SearchService()
    downloader = Downloader()
    drive = DriveService()
    db = Database()

    try:
        # 🔎 1️⃣ Buscar imagens
        log("Buscando imagens na API...")
        imagens = search.buscar_imagens(query_limpa, quantidade)

        if not imagens:
            log("Nenhuma imagem encontrada.")
            return

        # 📂 2️⃣ Criar pasta local temporária
        pasta_local = criar_pasta_temporaria(query_limpa)

        # ⬇ 3️⃣ Baixar imagens
        log("Baixando imagens...")
        resultados = downloader.baixar_imagens(imagens, pasta_local)

        # ☁ 4️⃣ Criar ou reutilizar pasta no Drive
        log("Criando ou reutilizando pasta no Drive...")
        pasta_id = drive.criar_pasta(query_limpa)

        # 🔁 5️⃣ Processar cada imagem
        for item in resultados:
            if item["status"] == "success":

                # 💾 Salvar ou atualizar no banco
                db.inserir_imagem(item)

                # ⬆ Upload (cria ou substitui)
                drive.upload_arquivo(item["file_path"], pasta_id)

        # 🧹 6️⃣ Limpar pasta local
        limpar_pasta(pasta_local)

        log("Processo finalizado com sucesso 🚀")

    except Exception as e:
        log(f"Erro inesperado no fluxo principal: {e}")

    finally:
        db.fechar()


if __name__ == "__main__":
    main()

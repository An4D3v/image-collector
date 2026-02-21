from services.search_service import SearchService
from services.downloader import Downloader
from services.drive_service import DriveService
from core.database import Database
from core.integrity_check import run_integrity_check
from utils.utils import criar_pasta_temporaria, limpar_pasta, sanitizar_nome, log


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
        log("Buscando imagens na API...")
        imagens = search.buscar_imagens(query_limpa, quantidade)

        if not imagens:
            log("Nenhuma imagem encontrada.")
            return

        pasta_local = criar_pasta_temporaria(query_limpa)

        log("Baixando imagens...")
        resultados = downloader.baixar_imagens(imagens, pasta_local)

        log("Criando ou reutilizando pasta no Drive...")
        pasta_id = drive.criar_pasta(query_limpa)
        modo = input("Deseja rodar verificação de integridade antes do processamento? (s/n): ")

        if modo.lower().strip() == "s":
            run_integrity_check(pasta_id, query_limpa)

        for item in resultados:
            if item["status"] == "success":

                item["folder_name"] = query_limpa

                drive.upload_arquivo(item["file_path"], pasta_id)
                db.inserir_imagem(item)


        limpar_pasta(pasta_local)

        log("Processo finalizado com sucesso 🚀")


    except Exception as e:
        log(f"Erro inesperado no fluxo principal: {e}")

    finally:
        db.fechar()


if __name__ == "__main__":
    main()

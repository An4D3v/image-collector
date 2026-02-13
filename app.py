from search_service import SearchService
from downloader import Downloader
from drive_service import DriveService
from utils import limpar_pasta, sanitizar_nome, criar_pasta_temporaria, gerar_nome_pasta, log


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

    # 1️⃣ Buscar URLs
    log("Buscando imagens na API...")
    urls = search.buscar_imagens(query_limpa, quantidade)

    if not urls:
        log("Nenhuma imagem encontrada.")
        return

    # 2️⃣ Criar pasta temporária
    pasta_local = criar_pasta_temporaria(query_limpa)

    # 3️⃣ Baixar imagens
    log("Baixando imagens...")
    arquivos = downloader.baixar_imagens(urls, pasta_local)

    if not arquivos:
        log("Falha no download das imagens.")
        return

    # 4️⃣ Criar pasta no Drive
    nome_pasta_drive = gerar_nome_pasta(query_limpa)
    log("Criando pasta no Drive...")
    pasta_id = drive.criar_pasta(nome_pasta_drive)

    # 5️⃣ Upload
    log("Enviando imagens para o Drive...")
    for arquivo in arquivos:
        drive.upload_arquivo(arquivo, pasta_id)

    # 6️⃣ Limpar pasta temporária
    limpar_pasta(pasta_local)

    log("Processo finalizado com sucesso 🚀")


if __name__ == "__main__":
    main()

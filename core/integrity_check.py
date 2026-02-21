from core.database import Database
from services.drive_service import DriveService
from config.config import GOOGLE_DRIVE_ROOT_FOLDER_ID

def run_integrity_check(pasta_id, folder_name):

    print("\n🔍 Iniciando verificação de integridade...\n")

    db = Database()
    drive = DriveService()

    try:
        imagens_db = db.buscar_imagens_ativas(folder_name)
        arquivos_drive = drive.listar_arquivos_da_pasta(pasta_id)

        imagens_para_marcar = []

        for unsplash_id, file_name in imagens_db:
            if file_name not in arquivos_drive:
                imagens_para_marcar.append((unsplash_id, file_name))

        if not imagens_para_marcar:
            print("✅ Nenhuma inconsistência encontrada.")
            return

        print("⚠️ Imagens no banco mas ausentes no Drive:\n")

        for _, nome in imagens_para_marcar:
            print(f"- {nome}")

        confirmar = input("\nDeseja marcar como deletadas no banco? (s/n): ")

        if confirmar.lower() == "s":
            for unsplash_id, _ in imagens_para_marcar:
                db.marcar_como_deletada(unsplash_id)

            print("\n🗑️ Registros atualizados com deleted_at.")
        else:
            print("\n❌ Nenhuma alteração realizada.")

    finally:
        db.fechar()
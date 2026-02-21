import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        self.conn.autocommit = True

    def inserir_imagem(self, imagem):
        try:
            with self.conn.cursor() as cursor:
                query = """
                    INSERT INTO images
                    (unsplash_id, description, image_url, file_name, file_size, folder_name)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (unsplash_id)
                    DO UPDATE SET
                        description = EXCLUDED.description,
                        image_url = EXCLUDED.image_url,
                        file_name = EXCLUDED.file_name,
                        file_size = EXCLUDED.file_size,
                        folder_name = EXCLUDED.folder_name,
                        updated_at = NOW();
                """

                cursor.execute(query, (
                    imagem["unsplash_id"],
                    imagem.get("description"),
                    imagem["image_url"],
                    imagem.get("file_name"),
                    imagem.get("file_size"),
                    imagem.get("folder_name")
                ))

                print(f"Imagem inserida/atualizada: {imagem['unsplash_id']}")

        except Exception as e:
            print(f"Erro ao inserir imagem: {e}")

    def buscar_imagens_ativas(self, folder_name):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                SELECT unsplash_id, file_name
                FROM images
                WHERE deleted_at IS NULL
                AND folder_name = %s;
            """, (folder_name,))
            return cursor.fetchall()

    def marcar_como_deletada(self, unsplash_id):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                UPDATE images
                SET deleted_at = NOW()
                WHERE unsplash_id = %s;
            """, (unsplash_id,))

    def fechar(self):
        self.conn.close()
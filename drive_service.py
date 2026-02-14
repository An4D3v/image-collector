import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config import GOOGLE_DRIVE_ROOT_FOLDER_ID

SCOPES = ['https://www.googleapis.com/auth/drive']


class DriveService:

    def __init__(self):
        creds = None

        # se já existe token salvo
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'oauth_credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Salva token para não pedir login sempre
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('drive', 'v3', credentials=creds)

    # cria ou reutiliza pasta
    def criar_pasta(self, nome):

        query = (
            f"name='{nome}' "
            f"and mimeType='application/vnd.google-apps.folder' "
            f"and '{GOOGLE_DRIVE_ROOT_FOLDER_ID}' in parents "
            f"and trashed=false"
        )

        results = self.service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name)'
        ).execute()

        files = results.get('files', [])

        if files:
            print("Pasta já existe. Reutilizando.")
            return files[0]['id']

        # cria nova pasta
        file_metadata = {
            'name': nome,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [GOOGLE_DRIVE_ROOT_FOLDER_ID]
        }

        folder = self.service.files().create(
            body=file_metadata,
            fields='id'
        ).execute()

        print("Nova pasta criada.")
        return folder.get('id')
    
    # upload ou atualização do arquivo
    def upload_arquivo(self, caminho_arquivo, pasta_id):

        nome_arquivo = os.path.basename(caminho_arquivo)

        query = (
            f"name='{nome_arquivo}' "
            f"and '{pasta_id}' in parents "
            f"and trashed=false"
        )

        results = self.service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name)'
        ).execute()

        files = results.get('files', [])

        media = MediaFileUpload(caminho_arquivo, resumable=True)

        if files:
            # atualiza arquivo existente
            file_id = files[0]['id']
            self.service.files().update(
                fileId=file_id,
                media_body=media
            ).execute()
            print(f"Arquivo atualizado: {nome_arquivo}")

        else:
            # cria novo arquivo
            file_metadata = {
                'name': nome_arquivo,
                'parents': [pasta_id]
            }

            self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()

            print(f"Arquivo criado: {nome_arquivo}")

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

        # Se já existir token salvo
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # Se não existir ou estiver inválido
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'oauth_credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Salva o token para não pedir login sempre
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('drive', 'v3', credentials=creds)

    def criar_pasta(self, nome):
        file_metadata = {
            'name': nome,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [GOOGLE_DRIVE_ROOT_FOLDER_ID]
        }

        folder = self.service.files().create(
            body=file_metadata,
            fields='id'
        ).execute()

        return folder.get('id')

    def upload_arquivo(self, caminho_arquivo, pasta_id):
        file_metadata = {
            'name': os.path.basename(caminho_arquivo),
            'parents': [pasta_id]
        }

        media = MediaFileUpload(caminho_arquivo)

        self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

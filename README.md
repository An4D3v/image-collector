# Image Collector 🚀

## 🎬 Demonstração

![Demonstração do projeto](demo.gif)

Aplicação em Python que integra APIs externas para buscar imagens por
palavra-chave e organizá-las automaticamente no Google Drive.

Este projeto foi desenvolvido com foco em prática de integração de APIs,
autenticação segura (OAuth 2.0) e organização modular de código.

------------------------------------------------------------------------

## 🔎 Funcionalidades

-   🔍 Busca imagens por palavra-chave via API do Unsplash
-   ⬇️ Download automático das imagens
-   📂 Criação dinâmica de pastas no Google Drive
-   ☁️ Upload automatizado via Google Drive API
-   🔐 Autenticação segura utilizando OAuth 2.0
-   🧹 Limpeza automática de arquivos temporários

------------------------------------------------------------------------

## 🧠 Tecnologias Utilizadas

-   Python 3
-   Requests
-   Google Drive API
-   OAuth 2.0
-   Unsplash API
-   python-dotenv

------------------------------------------------------------------------

## ⚙️ Como Funciona

1.  O usuário informa uma palavra-chave e a quantidade de imagens.
2.  A aplicação consulta a API do Unsplash.
3.  As imagens são baixadas temporariamente.
4.  Uma nova pasta é criada automaticamente no Google Drive.
5.  As imagens são enviadas para essa pasta.
6.  A pasta local temporária é removida ao final do processo.

Fluxo resumido:

Input do usuário\
↓\
Unsplash API\
↓\
Download local\
↓\
Google Drive API (OAuth)\
↓\
Organização na nuvem\
↓\
Limpeza de arquivos temporários

------------------------------------------------------------------------

## 🔐 Autenticação

O acesso ao Google Drive é feito utilizando OAuth 2.0.

Isso significa que:

-   Nenhuma senha é armazenada no código
-   Cada usuário autoriza o acesso com sua própria conta Google
-   Tokens são gerados localmente (token.json)
-   O projeto segue boas práticas de segurança

------------------------------------------------------------------------

## 📦 Estrutura do Projeto

image-collector/ │ ├── app.py \# Orquestração principal ├──
search_service.py \# Integração com Unsplash API ├── drive_service.py \#
Integração com Google Drive API ├── downloader.py \# Download das
imagens ├── utils.py \# Funções auxiliares ├── config.py \#
Configurações e variáveis de ambiente ├── requirements.txt ├── .env └──
README.md

------------------------------------------------------------------------

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o repositório

git clone https://github.com/seu-usuario/image-collector.git\
cd image-collector

### 2️⃣ Crie e ative o ambiente virtual

Windows:

python -m venv venv\
venv`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux:

python3 -m venv venv\
source venv/bin/activate

### 3️⃣ Instale as dependências

pip install -r requirements.txt

### 4️⃣ Configure o arquivo `.env`

Crie um arquivo `.env` com:

UNSPLASH_ACCESS_KEY=sua_access_key_aqui\
GOOGLE_DRIVE_ROOT_FOLDER_ID=id_da_pasta_ImageCollector

Também adicione o arquivo oauth_credentials.json na raiz do projeto
(obtido no Google Cloud Console).

------------------------------------------------------------------------

### 5️⃣ Execute

python app.py

------------------------------------------------------------------------

## 📌 Observações Importantes

-   O projeto utiliza autenticação OAuth 2.0.
-   O arquivo token.json será criado automaticamente após o primeiro
    login.
-   Não compartilhe arquivos de credenciais no GitHub.

Recomenda-se adicionar ao `.gitignore`:

.env\
oauth_credentials.json\
token.json\
venv/\
**pycache**/

------------------------------------------------------------------------

## 💡 Possíveis Evoluções

-   Interface gráfica com Streamlit
-   Barra de progresso para uploads
-   Logs estruturados
-   Armazenamento de metadados das imagens
-   Deploy como aplicação web

------------------------------------------------------------------------

## 🎯 Objetivo do Projeto

Praticar:

-   Integração com APIs REST
-   Autenticação segura com OAuth 2.0
-   Organização modular de código
-   Automação de processos
-   Manipulação de arquivos e armazenamento em nuvem

------------------------------------------------------------------------

Desenvolvido como projeto pessoal para aprimoramento técnico e prática
de integrações entre serviços externos.

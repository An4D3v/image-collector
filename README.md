# Image Collector 🚀

## 🎬 Demonstração

```{=html}
<p align="center">
```
`<img src="demo.gif" alt="Demonstração do projeto" width="700">`{=html}
```{=html}
</p>
```
Aplicação em Python que integra APIs externas para buscar imagens por
palavra-chave, armazená-las no Google Drive e manter consistência entre
banco de dados e nuvem.

Este projeto evoluiu de uma simples integração com API para um sistema
com:

-   Persistência em banco relacional
-   UPSERT com PostgreSQL
-   Soft delete
-   Verificação de integridade entre sistemas
-   Organização modular de código

------------------------------------------------------------------------

## 🔎 Funcionalidades

-   🔍 Busca imagens por palavra-chave via API do Unsplash\
-   ⬇️ Download automático das imagens\
-   📂 Criação dinâmica de pastas no Google Drive\
-   ☁️ Upload automatizado via Google Drive API\
-   🗄 Persistência em PostgreSQL\
-   🔁 UPSERT (INSERT ou UPDATE automático)\
-   🗑 Soft delete com controle via `deleted_at`\
-   🔎 Verificação opcional de integridade entre banco e Drive\
-   🧹 Limpeza automática de arquivos temporários\
-   🔐 Autenticação segura utilizando OAuth 2.0

------------------------------------------------------------------------

## 🧠 Tecnologias Utilizadas

-   Python 3
-   PostgreSQL
-   psycopg2
-   Requests
-   Google Drive API
-   OAuth 2.0
-   Unsplash API
-   python-dotenv

------------------------------------------------------------------------

## ⚙️ Como Funciona

### Fluxo Principal

1.  O usuário informa uma palavra-chave e a quantidade de imagens.
2.  A aplicação consulta a API do Unsplash.
3.  As imagens são baixadas temporariamente.
4.  Uma pasta é criada (ou reutilizada) no Google Drive.
5.  O sistema pode executar uma verificação de integridade opcional.
6.  As imagens são enviadas ao Drive.
7.  Os registros são persistidos no banco usando UPSERT.
8.  A pasta temporária local é removida.

------------------------------------------------------------------------

## 🔁 Persistência Inteligente (UPSERT)

O sistema utiliza:

    INSERT ... ON CONFLICT (unsplash_id) DO UPDATE

Isso garante:

-   Nenhuma duplicação de imagens
-   Atualização automática quando necessário
-   Idempotência do processo

------------------------------------------------------------------------

## 🗑 Soft Delete

O banco utiliza a coluna:

    deleted_at TIMESTAMP NULL

Se uma imagem for marcada como removida, o registro não é apagado,
apenas recebe timestamp em `deleted_at`.

------------------------------------------------------------------------

## 🔎 Verificação de Integridade

Antes da sincronização, o usuário pode optar por rodar uma verificação:

-   Compara imagens do banco com arquivos no Drive
-   Detecta inconsistências
-   Exibe relatório
-   Permite confirmar atualização de `deleted_at`

------------------------------------------------------------------------

## 🗄 Banco de Dados

Tabela principal:

    CREATE TABLE images (
        unsplash_id TEXT PRIMARY KEY,
        description TEXT,
        image_url TEXT NOT NULL,
        file_name TEXT,
        file_size INTEGER,
        folder_name TEXT,
        created_at TIMESTAMP DEFAULT NOW(),
        updated_at TIMESTAMP DEFAULT NOW(),
        deleted_at TIMESTAMP NULL
    );

------------------------------------------------------------------------

## 📦 Estrutura do Projeto

    image-collector/
    │
    ├── app.py
    │
    ├── core/
    │   ├── database.py
    │   └── integrity_check.py
    │
    ├── services/
    │   ├── search_service.py
    │   ├── downloader.py
    │   └── drive_service.py
    │
    ├── config/
    │   └── config.py
    │
    ├── utils/
    │   └── utils.py
    │
    ├── requirements.txt
    ├── .env
    └── README.md

Organização por responsabilidade:

-   **core/** → lógica interna do sistema (banco e verificação)
-   **services/** → integrações externas (APIs e download)
-   **config/** → configurações e variáveis de ambiente
-   **utils/** → funções auxiliares

------------------------------------------------------------------------

## 🚀 Como Executar

### 1️⃣ Clone o repositório

    git clone https://github.com/seu-usuario/image-collector.git
    cd image-collector

### 2️⃣ Crie e ative o ambiente virtual

Windows:

    python -m venv venv
    venv\Scripts\activate

Mac/Linux:

    python3 -m venv venv
    source venv/bin/activate

### 3️⃣ Instale as dependências

    pip install -r requirements.txt

### 4️⃣ Configure o arquivo `.env`

    UNSPLASH_ACCESS_KEY=sua_access_key
    GOOGLE_DRIVE_ROOT_FOLDER_ID=id_da_pasta_root
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=image_collector
    DB_USER=postgres
    DB_PASSWORD=sua_senha

Também adicione:

    oauth_credentials.json

na raiz do projeto.

------------------------------------------------------------------------

### 5️⃣ Execute

    python app.py

------------------------------------------------------------------------

## 🔐 Segurança

-   OAuth 2.0 para Google Drive
-   Nenhuma senha hardcoded
-   Variáveis sensíveis via `.env`
-   Token salvo localmente (`token.json`)

Adicionar ao `.gitignore`:

    .env
    oauth_credentials.json
    token.json
    venv/
    __pycache__/

------------------------------------------------------------------------

## 📌 Evolução Técnica do Projeto

Este projeto evoluiu de:

-   Script simples de integração\
    para\
-   Sistema com persistência e controle de conflito\
    para\
-   Aplicação com sincronização entre sistemas

Conceitos aplicados:

-   Idempotência
-   UPSERT
-   Integridade referencial
-   Soft delete
-   Separação de responsabilidades
-   Organização modular

------------------------------------------------------------------------

## 💡 Próximas Evoluções Possíveis

-   Testes automatizados
-   Logs estruturados
-   CLI com argumentos
-   Docker
-   API com FastAPI
-   Interface web
-   Métricas de execução
-   Deploy em nuvem

------------------------------------------------------------------------

## 🎯 Objetivo do Projeto

Praticar:

-   Integração com APIs REST
-   Autenticação OAuth 2.0
-   Banco relacional com PostgreSQL
-   Controle de conflito com UPSERT
-   Sincronização entre sistemas
-   Organização e evolução arquitetural

------------------------------------------------------------------------

Projeto pessoal desenvolvido para evolução técnica contínua e prática de
engenharia de software aplicada.

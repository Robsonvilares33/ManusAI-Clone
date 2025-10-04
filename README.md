# ManusAI-Clone

## Visão Geral do Projeto

O ManusAI-Clone é um projeto ambicioso que visa desenvolver um agente de IA autônomo e auto-evolutivo em larga escala. Inspirado na capacidade de aprendizado e adaptação, o agente é projetado para operar com mínima intervenção humana, integrando-se a diversas plataformas para expandir suas capacidades e otimizar seus processos.

## Objetivos Principais

*   **Autonomia:** Operação com mínima intervenção humana.
*   **Auto-evolução:** Capacidade de analisar e aprimorar seu próprio código e lógica através de integrações com GitHub.
*   **Integrações:** Conectividade com serviços essenciais como GitHub, Gmail, Google Calendar, Supabase, Sentry, Hugging Face, e outros para gerenciamento de código, comunicação, agendamento, persistência de dados e expansão de capacidades de IA.
*   **Modularidade:** Arquitetura baseada em Model Context Protocol (MCP) para orquestração de subagentes e fácil expansão.

## Funcionalidades Atuais (v1.1.0)

*   **Core do Agente:** Implementação aprimorada do núcleo do agente com gerenciamento de memória e capacidades de tomada de decisão.
*   **Integração GitHub:** Configuração para automação de versionamento, CI/CD e autoatualizações.
*   **Integração Supabase/PostgreSQL:** Persistência de dados, memória de longo prazo, logs e histórico.
*   **Integração Sentry:** Monitoramento contínuo de erros e autorrecuperação.
*   **Integração Hugging Face & APIs Externas:** Expansão das capacidades de IA com modelos de linguagem (ChatGPT, Gemini, ElevenLabs, Perplexity).
*   **MCP Personalizado:** Estrutura conceitual para orquestração de subagentes.
*   **Integração Gmail:** Configuração para autenticação OAuth 2.0, com funções de leitura, classificação, processamento e envio de e-mails em desenvolvimento.
*   **Integração Google Calendar:** Configuração para autenticação OAuth 2.0, com funções de criação, leitura e gerenciamento de eventos em desenvolvimento.
*   **Integração Notion:** Configuração para autenticação com API, com funções de leitura/escrita de páginas e gerenciamento de bancos de dados em desenvolvimento.
*   **Integração Zapier:** Configuração para webhooks, com desenvolvimento de workflows de automação em andamento.

## Configuração e Instalação

### Pré-requisitos

*   Docker e Docker Compose instalados.
*   Conta GitHub com um Personal Access Token (PAT) com as permissões necessárias (repo, workflow, write:packages, admin:repo_hook).
*   Contas e chaves de API para os serviços integrados (Supabase, Sentry, OpenAI, Google Gemini, ElevenLabs, Perplexity AI, Google Cloud Console para Gmail/Calendar, Notion, Zapier).

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```dotenv
GITHUB_TOKEN=seu_token_github
OPENAI_API_KEY=sua_chave_openai
DATABASE_URL=postgresql://<USUARIO>:<SENHA>@db.<ID_PROJETO>.supabase.co:5432/postgres
DB_USER=<USUARIO>
DB_PASSWORD=<SENHA>
DB_HOST=db.<ID_PROJETO>.supabase.co
DB_PORT=5432
DB_NAME=postgres
HUGGING_FACE_API_KEY=sua_chave_hugging_face
GOOGLE_GEMINI_API_KEY=sua_chave_google_gemini
ELEVENLABS_API_KEY=sua_chave_elevenlabs
PERPLEXITY_API_KEY=sua_chave_perplexity
SENTRY_DSN=sua_dsn_sentry
GMAIL_CLIENT_ID=seu_gmail_client_id
GMAIL_CLIENT_SECRET=seu_gmail_client_secret
GMAIL_REDIRECT_URI=sua_gmail_redirect_uri
GOOGLE_CALENDAR_CLIENT_ID=seu_google_calendar_client_id
GOOGLE_CALENDAR_CLIENT_SECRET=seu_google_calendar_client_secret
GOOGLE_CALENDAR_REDIRECT_URI=sua_google_calendar_redirect_uri
NOTION_API_KEY=sua_notion_api_key
ZAPIER_WEBHOOK_URL=sua_zapier_webhook_url
```

### Executando o Projeto

1.  Clone o repositório:
    ```bash
    git clone https://github.com/Robsonvilares33/ManusAI-Clone.git
    cd ManusAI-Clone
    ```
2.  Crie o arquivo `.env` com suas variáveis de ambiente.
3.  Construa e inicie os serviços com Docker Compose:
    ```bash
    docker-compose up --build
    ```

O agente estará acessível em `http://localhost:8000`.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

Para detalhes sobre as integrações e como configurá-las, consulte o arquivo [INTEGRATIONS.md](INTEGRATIONS.md).

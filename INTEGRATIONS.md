# Integrações do ManusAI-Clone

Este documento detalha as integrações implementadas e planejadas para o projeto ManusAI-Clone, visando aprimorar sua autonomia, capacidades de auto-evolução e modularidade.

## 1. Integrações Ativas (v1.1.0)

As seguintes integrações foram configuradas e estão prontas para uso, aguardando apenas as credenciais apropriadas no arquivo `.env`.

### 1.1. GitHub

*   **Status:** Ativa (configuração de workflows de CI/CD e autoatualizações).
*   **Propósito:** Automação total do versionamento, CI/CD e autoatualizações do projeto, permitindo que o agente gerencie seu próprio código e processos de deploy.
*   **Credenciais Necessárias:**
    *   `GITHUB_TOKEN`: Token de acesso pessoal do GitHub com permissões `repo`, `workflow`, `write:packages`, `admin:repo_hook`.

### 1.2. Supabase (PostgreSQL)

*   **Status:** Ativa (configuração de conexão com banco de dados).
*   **Propósito:** Memória de longo prazo, persistência de dados, logs e histórico para o agente, permitindo que ele armazene e recupere informações cruciais para sua operação e aprendizado.
*   **Credenciais Necessárias:**
    *   `DATABASE_URL`: URL de conexão completa do banco de dados Supabase.
    *   `DB_USER`: Usuário do banco de dados.
    *   `DB_PASSWORD`: Senha do banco de dados.
    *   `DB_HOST`: Host do banco de dados.
    *   `DB_PORT`: Porta do banco de dados.
    *   `DB_NAME`: Nome do banco de dados.

### 1.3. Sentry

*   **Status:** Ativa (configuração de monitoramento de erros).
*   **Propósito:** Monitoramento contínuo de erros e exceções, permitindo que o agente identifique e, futuramente, inicie processos de autorrecuperação.
*   **Credenciais Necessárias:**
    *   `SENTRY_DSN`: URL DSN fornecida pelo Sentry para o seu projeto.

### 1.4. Hugging Face e APIs Externas (ChatGPT, Gemini, ElevenLabs, Perplexity)

*   **Status:** Ativa (configuração de chaves de API).
*   **Propósito:** Expandir as capacidades de IA do agente, permitindo acesso a modelos de linguagem avançados, geração de texto, fala e pesquisa.
*   **Credenciais Necessárias:**
    *   `HUGGING_FACE_API_KEY`: Chave de API do Hugging Face (opcional, dependendo do uso).
    *   `OPENAI_API_KEY`: Chave de API da OpenAI.
    *   `GOOGLE_GEMINI_API_KEY`: Chave de API do Google Gemini.
    *   `ELEVENLABS_API_KEY`: Chave de API do ElevenLabs (para geração de fala).
    *   `PERPLEXITY_API_KEY`: Chave de API do Perplexity AI (para pesquisa).

### 1.5. MCP Personalizado (Model Context Protocol)

*   **Status:** Ativa (estrutura conceitual implementada).
*   **Propósito:** Orquestração de subagentes e modularidade, permitindo que o agente delegue tarefas específicas a módulos especializados e mantenha um contexto compartilhado.
*   **Credenciais Necessárias:** N/A (a implementação é conceitual e não requer credenciais externas neste estágio).

### 1.6. Gmail

*   **Status:** Em Andamento (configuração de autenticação OAuth 2.0).
*   **Propósito:** Gerenciamento de comunicações por e-mail, incluindo leitura, classificação, processamento, geração de respostas e envio de e-mails com anexos.
*   **Credenciais Necessárias:**
    *   `GMAIL_CLIENT_ID`: ID do cliente OAuth 2.0 do Google Cloud Console.
    *   `GMAIL_CLIENT_SECRET`: Segredo do cliente OAuth 2.0 do Google Cloud Console.
    *   `GMAIL_REDIRECT_URI`: URI de redirecionamento configurada no Google Cloud Console.
    *   `token.pickle`: Arquivo gerado após o fluxo de autenticação OAuth 2.0.

### 1.7. Google Calendar

*   **Status:** Em Andamento (configuração de autenticação OAuth 2.0).
*   **Propósito:** Gerenciamento de eventos e agendamento inteligente, permitindo que o agente crie, leia e gerencie eventos, agende reuniões sem conflitos e envie notificações.
*   **Credenciais Necessárias:**
    *   `GOOGLE_CALENDAR_CLIENT_ID`: ID do cliente OAuth 2.0 do Google Cloud Console.
    *   `GOOGLE_CALENDAR_CLIENT_SECRET`: Segredo do cliente OAuth 2.0 do Google Cloud Console.
    *   `GOOGLE_CALENDAR_REDIRECT_URI`: URI de redirecionamento configurada no Google Cloud Console.
    *   `calendar_token.pickle`: Arquivo gerado após o fluxo de autenticação OAuth 2.0.

### 1.8. Notion

*   **Status:** Em Andamento (configuração de chave de API).
*   **Propósito:** Gerenciamento de projetos, documentação e organização de informações, permitindo que o agente leia e escreva em páginas e gerencie bancos de dados do Notion.
*   **Credenciais Necessárias:**
    *   `NOTION_API_KEY`: Chave de integração interna do Notion.

### 1.9. Zapier

*   **Status:** Em Andamento (configuração de webhook).
*   **Propósito:** Conectar o ManusAI-Clone a milhares de outros aplicativos e serviços, expandindo exponencialmente suas capacidades de automação. Atuará como uma ponte, permitindo que o agente acione e seja acionado por eventos em outras plataformas.
*   **Credenciais Necessárias:**
    *   `ZAPIER_WEBHOOK_URL`: URL do webhook do Zapier configurado para receber dados do agente.

## 2. Integrações Pendentes (Plano Incremental)

As seguintes integrações estão planejadas para futuras fases de desenvolvimento:

*   **Outras APIs e Serviços:** Conforme a necessidade e a evolução do projeto, outras integrações podem ser adicionadas para expandir ainda mais as capacidades do agente.

## 3. Configuração de Variáveis de Ambiente

Todas as chaves de API e credenciais devem ser configuradas no arquivo `.env` na raiz do projeto. Um exemplo de arquivo `.env` pode ser encontrado no `README.md`.

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


# CHANGELOG

## v1.1.0 - 2025-10-03

### Adicionado
- Integração aprofundada com GitHub para automação de versionamento, CI/CD e autoatualizações.
- Integração com Supabase (Postgres) para memória de longo prazo, persistência de dados, logs e histórico.
- Integração com Sentry para monitoramento contínuo de erros e autorrecuperação.
- Integração com Hugging Face e APIs externas (ChatGPT, Gemini, ElevenLabs, Perplexity) para expansão das capacidades de IA.
- Implementação de MCP Personalizado para orquestração de subagentes e modularidade (estrutura conceitual).
- Integração com Gmail (autenticação OAuth 2.0, leitura, classificação, processamento, geração de respostas e envio de e-mails com anexos).
- Integração com Google Calendar (autenticação OAuth 2.0, criação, leitura, gerenciamento de eventos, agendamento inteligente, notificações e lembretes).
- Integração com Notion (autenticação API, leitura/escrita de páginas, gerenciamento de bancos de dados, sincronização de informações).
- Integração com Zapier (configuração de webhooks, criação de Zaps, desenvolvimento de workflows de automação complexos).
- Adicionados workflows de CI/CD para GitHub Actions (CI, Release Desktop, Release Android, Publish Docker Image).
- Atualização do `README.md` com as novas integrações e instruções de configuração.
- Criação de `Dockerfile` e `requirements_agent.txt` para o serviço do agente.
- Criação do `INTEGRATIONS.md` para documentação detalhada das integrações.

### Alterado
- Estrutura do projeto atualizada para suportar novas integrações e modularidade.

### Removido
- N/A


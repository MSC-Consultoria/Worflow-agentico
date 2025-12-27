# Chornos — Sistema de Gerenciamento de Atividades com IA

Chornos é a evolução do projeto original de governança agentica. O foco agora é
oferecer um sistema completo de gestão de atividades com inteligência
artificial, combinando experiência de notebook LLM, frontend em React e
integração direta com Google Drive, implantado em VPS/Hostinger.

## Visão Geral
- **Interface**: aplicação web em React, acessível via subdomínio configurado na
  VPS Hostinger.
- **Experiência de IA**: notebooks (Jupyter/LM Studio) para orquestrar fluxos de
  trabalho em linguagem natural e executar automações Python.
- **Armazenamento**: sincronização de arquivos e anexos com Google Drive para
  colaboração e histórico.
- **Governança**: mantém a disciplina de agentes, memória em Markdown e testes
  descrita na pasta `Governança/`.

## Arquitetura Proposta
1. **Frontend React**
   - Dashboard de atividades, cards de tarefas e painel de execução de agentes.
   - Componentes para upload/download sincronizado com Google Drive.
   - Autenticação inicial com OAuth do Google (perfil e acesso ao Drive).
2. **Camada Notebook/LLM**
   - Kernel Python com bibliotecas para chamadas LLM e automação (LangChain
     opcional).
   - Cadernos versionados no repositório para fluxos de IA auditáveis.
   - Endpoint de execução exposto via API (FastAPI/Node bridge) consumido pelo
     React.
3. **Persistência e Autenticação (Supabase)**
   - Banco Postgres + Auth do Supabase hospedado na VPS/Hostinger
     (`https://srv1180544.hstgr.cloud/project/default`).
   - Tabelas de tarefas, projetos, vínculos com Google Drive e auditoria de
     execuções de notebooks.
   - As chaves `SUPABASE_URL`, `SUPABASE_ANON_KEY` e `SUPABASE_SERVICE_ROLE`
     serão carregadas via variáveis de ambiente (nunca versionadas).
4. **Orquestração e Memória**
   - Pipelines descritos em Markdown/JSON, seguindo os padrões de
     `PIPELINE_ENGINE*.md`.
   - Logs e resultados gravados em pastas versionadas + Drive.
5. **Infra/VPS Hostinger**
   - Deploy em contêiner (Docker Compose) com serviços: `web` (React build),
     `api` (FastAPI/Node), `notebook` (Jupyter/LM), `proxy` (Caddy/Nginx com
     TLS) e conexão segura com o Supabase existente. Nenhuma credencial é
     versionada.

## Estado Atual
- Documentação de governança e agentes existente em `Governança/`.
- Backups históricos em `Backup/`.
- Ainda não há código-fonte de frontend ou backend; este repositório servirá
  como base de planejamento e implementação.

## Próximos Passos
1. Criar monorepo ou estrutura `apps/web` (React) + `apps/api` (FastAPI/Node)
   + `apps/notebook` (imagem Jupyter customizada).
2. Definir modelo de dados de tarefas/projetos e contratos de integração com
   Google Drive (upload/download, permissões), salvando metadados em Supabase.
3. Configurar client Supabase no web/API com variáveis de ambiente e teste de
   conexão ao endpoint da VPS.
4. Configurar CI com testes de lint/build para web e API, além de notebooks de
   validação.
5. Preparar scripts de deploy (Docker Compose) para a VPS Hostinger, incluindo
   variáveis de Supabase e pipeline de publicação automática.
6. Conectar a disciplina de governança existente (tests/checklists de
   `Governança/`) ao novo código.

## Como Contribuir
1. Abra um branch a partir de `work`.
2. Descreva alterações e validações em Markdown seguindo os padrões de
   `PR_STANDARD.md`.
3. Garanta que novas funcionalidades incluam cobertura de testes e atualizações
   de memória (documentação em Markdown).

# Supabase no Chornos

Guia rápido para usar o Supabase já provisionado na VPS Hostinger
(`https://srv1180544.hstgr.cloud/project/default`) como camada de dados e
autenticação do Chornos.

## Variáveis de Ambiente
Defina os valores no ambiente (ou `.env/.env.local` fora do versionamento):

- `SUPABASE_URL` — URL do projeto Supabase.
- `SUPABASE_ANON_KEY` — chave pública para o frontend.
- `SUPABASE_SERVICE_ROLE` — chave de serviço para a API (usar apenas no backend).
- `SUPABASE_DB_PASSWORD` — senha do banco para migrações (não expor no frontend).

## Coleções/Tabelas Iniciais
1. `projects`
   - `id`, `name`, `owner`, `drive_folder_id`, `created_at`.
2. `tasks`
   - `id`, `project_id`, `title`, `status`, `assignee`, `drive_file_id`,
     `llm_run_id`, `created_at`, `updated_at`.
3. `llm_runs`
   - `id`, `task_id`, `notebook`, `input_params`, `output_path`, `status`,
     `executed_at`.
4. `audit_logs`
   - `id`, `entity_type`, `entity_id`, `action`, `actor`, `metadata`,
     `created_at`.

Aplique RLS (Row Level Security) em todas as tabelas e políticas por usuário
(autenticado via Supabase Auth/Google) antes de expor endpoints.

## Integração no Frontend (React)
- Use o client oficial `@supabase/supabase-js` configurado com `SUPABASE_URL` e
  `SUPABASE_ANON_KEY` via `.env.local`.
- Mantenha o login social do Google habilitado no projeto Supabase e reutilize o
  token para acessar o Drive quando possível.

## Integração na API (FastAPI/Node)
- Armazene `SUPABASE_SERVICE_ROLE` somente no backend para operações protegidas
  (ex.: criação de tarefas, rotas de auditoria, sincronização de Drive).
- Centralize a criação do client Supabase em um módulo de configuração e injete
  nos serviços (ex.: `services/supabase_client.py` ou `services/supabase.ts`).
- Inclua smoke test de conexão no startup da API e monitore falhas de RLS.

## Deploy/Compose
- Injetar variáveis do Supabase nos serviços `web` (apenas `ANON_KEY`) e `api`
  (`SERVICE_ROLE`, `URL`).
- Evitar logar chaves em stdout/stderr; use arquivos de configuração ou secrets
  do orquestrador.

## Checklist de Segurança
- Nunca commitar chaves no repositório.
- Ativar RLS por padrão e revisar políticas de inserção/seleção por usuário.
- Habilitar logs de auditoria no Supabase para operações críticas.
- Rotacionar chaves se houver suspeita de vazamento.

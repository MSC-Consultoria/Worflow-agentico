# Plano de Implementação do Chornos

Este plano traduz o objetivo de transformar o "Workflow Agentico" no sistema
Chornos — um gerenciador de atividades com IA, notebooks LLM, frontend React e
integração com Google Drive, implantado na VPS Hostinger.

## 1. Estrutura de Repositório
- `apps/web` — React + Vite/Next, componentes de dashboard, painel de execução e
  integração Drive.
- `apps/api` — FastAPI ou Node/Express para autenticação, orquestração de
  tarefas, webhooks do Drive e ponte com notebooks.
- `apps/notebook` — imagem Docker com Jupyter + extensões (nbconvert, papermill)
  e SDK de LLM.
- `infra/` — Docker Compose, proxy (Caddy/Nginx), certificados e scripts de
  deploy para a VPS Hostinger, conectando web/api ao Supabase já provisionado.
- `governanca/` — reaproveitar `Governança/` atual como base de processos,
  testes e memória.

## 2. Funcionalidades Prioritárias
1. **Cadastro e gestão de atividades**: CRUD com status, responsáveis, links para
   arquivos no Drive e registro de execuções de IA com persistência no
   Supabase.
2. **Notebook LLM executável**: API para disparar notebooks parametrizados e
   armazenar saídas em Markdown/HTML + Drive.
3. **Integração Google Drive**: OAuth, criação de pastas por projeto, upload e
   leitura de arquivos. Tokens guardados em cofre/variáveis de ambiente (nunca
   versionados).
4. **Dashboard React**: cards de tarefas, painel de logs da IA, botão de
   execução de notebook e upload/download do Drive.
5. **Autenticação**: Google OAuth inicial; fallback para contas locais.

## 3. Segurança e Governança
- Aplicar `SECURITY_CHECKLIST.md` e `SECURITY_AND_BENCHMARK_TESTS.md` às novas
  APIs e notebooks.
- Manter memória em Markdown para cada fluxo de notebook (inputs/outputs,
  observações).
- Testes: lint + unit + smoke de notebook (papermill) + contrato API/Drive.

## 4. Deploy na VPS Hostinger
- Usar Docker Compose com serviços `proxy`, `web`, `api`, `notebook`.
- `proxy`: Caddy/Nginx servindo build do React e roteando `/api` e `/notebook`.
- `web`: build React servido em static container.
- `api`: FastAPI/Node com certificados via proxy e client Supabase configurado
  via variáveis de ambiente.
- `notebook`: Jupyter Lab autenticado, acesso restrito via proxy e rede interna.
- Variáveis de ambiente para chaves OAuth e segredos; nunca armazenar senhas ou
  tokens no repositório.

## 5. Passos de Curto Prazo
1. Inicializar `apps/web` com scaffold React + roteamento básico e client
   Supabase carregado via `.env.local`.
2. Subir `apps/api` com endpoints stub (healthcheck, atividades mock) e teste
   de conexão Supabase no bootstrap.
3. Adicionar Compose inicial (proxy + web + api) sem segredos, usando
   variáveis `SUPABASE_URL` e `SUPABASE_SERVICE_ROLE` injetadas no container da
   API.
4. Conectar checklist de governança aos novos módulos (README + docs).
5. Preparar guia de DNS/subdomínio (Hostinger) sem expor credenciais e incluir
   nota de que o Supabase roda na mesma VPS.

## 6. Métricas de Sucesso
- Deploy funcional em subdomínio Hostinger com TLS.
- Execução de notebook via botão no dashboard, registrando resultado no Drive.
- Log de auditoria em Markdown para cada tarefa executada pela IA.
- Pipeline CI com lint/build/test verde para web, api e notebooks.

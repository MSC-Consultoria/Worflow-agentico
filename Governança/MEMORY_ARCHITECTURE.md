# MEMORY_ARCHITECTURE.md

Padrões para armazenamento e uso de memória em agentes e pipelines.

## 1) Formatos
- **Contexto imediato**: janela curta em memória volátil (ex.: últimos N turnos ou K tokens), representada em JSON estruturado com metadados (`timestamp`, `source`, `confidence`).
- **Memória de trabalho**: KV store indexada por `trace_id`/`session_id`, com versões e checksums.
- **Memória de longo prazo**: embeddings + documentos com referências canônicas e política de atualização (append-only + versões).
- **Eventos**: trilha de execução (event sourcing) como fonte de verdade para reconstrução de estado.

## 2) Escopo
- **Por sessão**: dados transitórios usados para coerência de curto prazo; expiram automaticamente.
- **Por pipeline**: estados intermediários, checkpoints e decisões; necessários para reexecução e auditoria.
- **Compartilhada**: conhecimento reutilizável entre agentes (glossário, políticas, decisões aprovadas).
- **Restrita**: dados sensíveis (PII, credenciais) com acesso controlado e criptografia.

## 3) Retenção e expurgo
- **Contexto imediato**: expirar por tamanho (tokens) ou tempo (padrão 24h); no expurgo, preservar resumos.
- **Memória de trabalho**: retenção mínima 30 dias; expurgo por LRU + snapshots para consistência.
- **Longo prazo**: retenção conforme classificação de dados; conteúdo sensível requer políticas de minimização.
- **Logs/eventos**: manter por 90 dias ou conforme requisito regulatório.
- **Direito ao esquecimento**: suportar remoção seletiva e reindexação de embeddings.

## 4) Proteções e controles
- Criptografia em repouso e em trânsito; rotação de chaves periódica.
- Máscara e tokenização para PII; acesso via RBAC e trilha de auditoria.
- Limites de leitura/escrita por agente para evitar abuso ou vazamento acidental.
- Backups verificáveis e testes de restauração periódicos.

## 5) Observabilidade
- Métricas: taxa de acertos de recuperação, tamanho de memória por escopo, latência de leitura/escrita, falhas de cache.
- Alertas: vazão anômala, erros de autorização, crescimento acelerado de armazenamento.
- Logs estruturados com `trace_id` e `session_id` para correlação.

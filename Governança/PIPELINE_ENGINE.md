# PIPELINE_ENGINE.md

Descrição de estados, eventos e garantias do mecanismo de pipeline orquestrador de tarefas.

## 1) Estados do pipeline
- **Created**: pipeline registrado, mas não iniciado.
- **Pending**: aguardando recursos ou pré-condições.
- **Running**: etapas em execução; eventos de progresso emitidos.
- **Paused**: execução suspensa manualmente ou por política.
- **WaitingInput**: requer decisão humana ou sinal externo.
- **Retrying**: reprocessando etapa após falha recuperável.
- **Failed**: falha não-recuperável ou número de tentativas excedido.
- **Canceled**: cancelado por usuário ou sistema.
- **Completed**: todas as etapas concluídas com sucesso.

## 2) Eventos-chave
- `pipeline.created(pipeline_id)`
- `pipeline.started(pipeline_id, config_hash)`
- `stage.started(stage_id, name)` / `stage.completed(stage_id, result)`
- `stage.failed(stage_id, error, retryable)`
- `stage.paused(stage_id, reason)` / `stage.resumed(stage_id)`
- `pipeline.waiting_input(pipeline_id, schema_ref)`
- `pipeline.canceled(reason)`
- `pipeline.failed(error_summary)`
- `pipeline.completed(metrics)`

Todos os eventos devem ser enviados para o barramento padrão com metadata: `trace_id`, `correlation_id`, `requester`, `timestamp` e `version`.

## 3) Garantias e políticas
- **Idempotência**: replays de eventos não devem duplicar efeitos; `stage_id` e `event_id` são únicos.
- **Consistência observável**: estados visíveis são derivados somente de eventos confirmados.
- **Time-outs**: cada estágio tem SLA e política de retry exponencial com jitter.
- **Isolamento de falhas**: falhas de estágio não propagam efeitos sem compensação/rollback.
- **Auditoria**: trilha completa de eventos persistida por no mínimo 90 dias.

## 4) Interfaces esperadas
- API e SDK devem suportar inspeção de estado, replay controlado e cancelamento seguro.
- Em caso de `WaitingInput`, fornecer schema de entrada, timeout e quem pode responder.
- Logs estruturados por estágio e correlação com métricas/alertas.

## 5) Compatibilidade
- Versões de payloads de eventos devem incluir `version` e `schema` para evolução segura.
- Mudanças breaking exigem migração guiada e teste de contrato (ver `PIPELINE_ENGINE_PYTHON_INTERFACE.md`).

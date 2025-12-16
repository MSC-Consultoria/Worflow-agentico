# PIPELINE_ENGINE_PYTHON_INTERFACE.md

Expectativas mínimas para a API Python que interage com o Pipeline Engine. O objetivo é garantir contratos claros para criação, acompanhamento e intervenção em pipelines.

## 1) Objetos e tipos
- `PipelineConfig`: definição de estágios, dependências, timeouts, políticas de retry e hooks.
- `StageConfig`: nome, executor, parâmetros, limites de recurso, tratadores de falha.
- `PipelineState`: enum que espelha os estados descritos em `PIPELINE_ENGINE.md`.
- `Event`: payload estruturado com `id`, `type`, `payload`, `timestamp`, `trace_id`, `version`.

## 2) Operações síncronas
- `create_pipeline(config: PipelineConfig) -> pipeline_id`
- `start_pipeline(pipeline_id) -> PipelineState`
- `get_status(pipeline_id) -> PipelineState`
- `get_history(pipeline_id, since: datetime | None = None) -> list[Event]`
- `cancel_pipeline(pipeline_id, reason: str) -> PipelineState`
- `retry_stage(pipeline_id, stage_id, reason: str) -> PipelineState`
- `submit_input(pipeline_id, payload: dict, responder: str) -> PipelineState` (para `WaitingInput`)

## 3) Operações assíncronas / streaming
- `subscribe_events(pipeline_id, callback: Callable[[Event], None])`
- `watch_metrics(pipeline_id, stage_id=None) -> AsyncIterator[MetricPoint]`

## 4) Comportamento esperado
- **Idempotência**: chamadas repetidas com mesmos argumentos não criam duplicatas.
- **Timeouts**: métodos expostos devem aceitar `timeout` e `retry_policy` opcionais.
- **Validadores**: schemas de `PipelineConfig` e `StageConfig` devem ser versionados e validados.
- **Segurança**: suporte a autenticação (token/service account) e autorização por papel.
- **Observabilidade**: logs estruturados e métricas (latência, filas, erros) para cada operação.
- **Erros**: expor exceções específicas (`PipelineNotFound`, `InvalidConfig`, `PermissionDenied`, `TimeoutError`).

## 5) Compatibilidade e testes
- Todo método deve ter contrato de tipo estável; mudanças breaking exigem versão nova do SDK.
- Testes de contrato e integração devem simular eventos e transições principais.
- Pacote deve fornecer ambiente de mock/fake para testes offline dos clientes.

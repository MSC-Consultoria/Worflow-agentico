# TESTS TESTS

## Validações automatizadas
- Conferir que payload de entrada inclui `scope`, `triggers` e `artifacts`.
- Validar coerência entre `scope` e resultados: para cada nível definido deve existir bloco correspondente em `details`.
- Garantir que cobertura mínima configurada seja atingida (ex.: linha >= 75%).
- Verificar que notificações foram disparadas quando `summary.status` for `fail` ou `unstable`.

## Gatilhos
- Execução em cada pipeline de CI.
- Antes de publicar relatórios oficiais de qualidade.

## Payload de teste (YAML)
```yaml
scope:
  unit:
    - "lib/auth"
  integration:
    - "auth → api"
triggers:
  - "pull_request"
artifacts:
  requirements:
    - "REQ-1"
  contracts:
    - "openapi/auth.yaml"
  fixtures:
    - "tests/fixtures/auth.json"
summary:
  status: "pass"
  execution_time_seconds: 120
  coverage:
    line: 82.3
    branch: 70.1
details:
  unit:
    - name: "auth::valid_token"
      status: "pass"
      duration_ms: 20
  integration:
    - name: "auth_flow"
      status: "pass"
notifications: []
```

## Resultados esperados
- Estrutura aceita sem erros.
- Indicadores de cobertura acima do limite.
- Falhas acionam notificações configuradas.

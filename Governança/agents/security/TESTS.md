# SECURITY TESTS

## Validações
- Confirmar que escopos SAST/DAST foram fornecidos e são acessíveis.
- Garantir que políticas obrigatórias estejam listadas e aplicadas aos resultados.
- Verificar que todos os achados críticos/altos possuem responsável e data de correção.
- Checar que secrets detectados foram classificados (revoked/rotating/false_positive).
- Validar que relatórios e alertas foram gerados quando `summary.status` não é `pass`.

## Gatilhos
- Pipelines diários de segurança ou a cada merge em branch principal.
- Antes de releases para produção.
- Após incidentes ou mudanças em políticas de segurança.

## Payload de teste (YAML)
```yaml
scope:
  sast:
    - "services/api"
  dast:
    - "https://staging.example.com/api"
  sca:
    - "package.json"
policies:
  - "OWASP ASVS"
summary:
  status: "warn"
  critical: 0
  high: 1
  medium: 2
  low: 0
sast_findings:
  - id: "SAST-1"
    severity: "high"
    file: "api/app.py"
    line: 10
    description: "eval inseguro"
    recommendation: "remover eval"
    status: "novo"
dast_findings: []
secrets:
  - location: "api/.env"
    type: "DB_PASSWORD"
    status: "rotating"
actions:
  - owner: "Segurança"
    item: "Remover eval"
    due_date: "2024-08-15"
reports:
  - "artifacts/sast.html"
alerts:
  - channel: "slack"
    recipients:
      - "#secops"
    message: "Achado high em api/app.py"
```

## Resultados esperados
- Payload válido com campos obrigatórios.
- Falhas/avisos geram alertas e ações atribuídas.
- Dados de secrets com status definidos e rastreáveis.

# SECURITY OUTPUTS

## Formato do payload (YAML)
```yaml
summary:
  status: "pass|fail|warn"
  critical: 0
  high: 0
  medium: 0
  low: 0
sast_findings:
  - id: "SAST-001"
    severity: "high"
    file: "path/to/file.py"
    line: 42
    description: "Uso inseguro de entrada"
    recommendation: "sanitizar entrada"
    status: "novo|em_mitigacao|resolvido"
dast_findings:
  - id: "DAST-010"
    severity: "critical"
    endpoint: "https://staging.example.com/login"
    description: "SQL injection detectada"
    evidence: "payload usado"
    recommendation: "parametrizar consultas"
    status: "novo"
secrets:
  - location: "services/api/.env"
    type: "AWS key"
    status: "revoked|rotating|false_positive"
actions:
  - owner: "time/role"
    item: "Corrigir validação de input"
    due_date: "2024-09-10"
reports:
  - "path/to/sast-report.html"
  - "path/to/dast-report.html"
alerts:
  - channel: "slack"
    recipients:
      - "@security-oncall"
    message: "1 critical DAST encontrado"
```

## Exemplos
```yaml
summary:
  status: "fail"
  critical: 1
  high: 2
  medium: 3
  low: 1
sast_findings:
  - id: "SAST-201"
    severity: "high"
    file: "services/auth/token.py"
    line: 88
    description: "Uso de token hardcoded"
    recommendation: "Mover para vault e variáveis de ambiente"
    status: "novo"
dast_findings:
  - id: "DAST-501"
    severity: "critical"
    endpoint: "https://staging.example.com/login"
    description: "SQLi em parâmetro user"
    evidence: "payload ' OR 1=1 --"
    recommendation: "Parametrizar queries e usar WAF"
    status: "novo"
secrets:
  - location: "services/api/.env"
    type: "AWS key"
    status: "revoked"
actions:
  - owner: "Segurança"
    item: "Criar regra de WAF para /login"
    due_date: "2024-08-20"
reports:
  - "artifacts/sast.html"
  - "artifacts/dast.html"
alerts:
  - channel: "slack"
    recipients:
      - "@security-oncall"
    message: "DAST crítico encontrado em /login"
```

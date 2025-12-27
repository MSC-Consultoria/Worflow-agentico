# TESTS OUTPUTS

## Formato do payload (YAML)
```yaml
summary:
  status: "pass|fail|unstable"
  execution_time_seconds: 0
  coverage:
    line: 0.0
    branch: 0.0
details:
  unit:
    - name: "teste"
      status: "pass|fail"
      duration_ms: 0
  integration:
    - name: "cenário"
      status: "pass|fail"
      logs: "link"
  non_functional:
    - name: "performance baseline"
      status: "pass|warn"
artifacts:
  reports:
    - "path/to/junit.xml"
    - "path/to/allure/index.html"
  logs:
    - "link para CI ou observabilidade"
notifications:
  - channel: "slack"
    recipients:
      - "#qa"
    message: "resumo"
```

## Exemplos
```yaml
summary:
  status: "fail"
  execution_time_seconds: 320
  coverage:
    line: 78.5
    branch: 65.0
details:
  unit:
    - name: "auth::should_validate_token"
      status: "pass"
      duration_ms: 35
    - name: "payments::calculates_fee"
      status: "fail"
      duration_ms: 58
      logs: "ci/job/123/log"
  integration:
    - name: "checkout_to_payments_flow"
      status: "fail"
      logs: "ci/job/123/integration.log"
  non_functional:
    - name: "performance baseline"
      status: "warn"
      logs: "ci/job/123/perf"
artifacts:
  reports:
    - "artifacts/junit.xml"
  logs:
    - "https://ci.example.com/job/123"
notifications:
  - channel: "slack"
    recipients:
      - "#qa"
      - "@oncall"
    message: "Falha nos testes de integração"
```

# TESTS INPUTS

## Formato do payload (YAML)
```yaml
scope:
  unit:
    - "módulo/arquivo"
  integration:
    - "serviço ou fluxo"
  non_functional:
    - "performance"
    - "segurança opcional"
triggers:
  - "push_principal"
  - "pull_request"
  - "pre_release"
artifacts:
  requirements:
    - "link ou id de requisito"
  contracts:
    - "OpenAPI spec"
    - "event schema"
  fixtures:
    - "caminhos de dados de teste"
environments:
  - "local"
  - "staging"
  - "prod-like"
reporting:
  format: "junit|allure|custom"
  notify:
    - "email"
    - "slack"
```

## Exemplos
```yaml
scope:
  unit:
    - "lib/payments"
    - "lib/auth"
  integration:
    - "checkout → payments"
  non_functional:
    - "performance"
triggers:
  - "pull_request"
artifacts:
  requirements:
    - "REQ-101"
    - "REQ-202"
  contracts:
    - "openapi/payments.yaml"
  fixtures:
    - "tests/fixtures/checkout.json"
environments:
  - "staging"
reporting:
  format: "junit"
  notify:
    - "slack"
```

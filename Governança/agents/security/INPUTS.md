# SECURITY INPUTS

## Formato do payload (YAML)
```yaml
scope:
  sast:
    - "paths/dir1"
    - "paths/dir2"
  dast:
    - "https://staging.example.com/api"
  sca:
    - "package.json"
    - "requirements.txt"
policies:
  - "OWASP ASVS"
  - "SOC2"
  - "LGPD"
secrets_management:
  providers:
    - "vault"
    - "aws_kms"
  detection_rules:
    - "regex chave"
    - "entropia"
  rotation_window_days: 90
environments:
  - "dev"
  - "staging"
risk_tolerance: "baixo|médio|alto"
ci_context:
  pipeline_id: "ci-123"
  commit: "sha"
  branch: "feature/x"
```

## Exemplos
```yaml
scope:
  sast:
    - "services/auth"
    - "services/api"
  dast:
    - "https://staging.example.com/api"
  sca:
    - "package.json"
policies:
  - "OWASP ASVS"
  - "LGPD"
secrets_management:
  providers:
    - "vault"
  detection_rules:
    - "AWS_ACCESS_KEY"
    - "JWT_SECRET"
  rotation_window_days: 60
environments:
  - "staging"
risk_tolerance: "médio"
ci_context:
  pipeline_id: "ci-456"
  commit: "abc123"
  branch: "feature/login"
```

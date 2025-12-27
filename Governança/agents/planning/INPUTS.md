# PLANNING INPUTS

## Formato do payload (YAML)
```yaml
objective: "Texto claro do resultado esperado"
timeframe: "YYYY-MM ou data alvo"
constraints:
  - "restrição 1"
  - "restrição 2"
stakeholders:
  - "nome/área"
backlog:
  - title: "Item ou iniciativa"
    status: "novo|em_andamento|bloqueado"
    dependencies:
      - "item X"
      - "fornecedor Y"
    value: "alto|médio|baixo"
    effort: "alto|médio|baixo"
    risk: "alto|médio|baixo"
policies:
  - "padrões de segurança"
  - "budget"
  - "SLAs relevantes"
notes: "observações adicionais"
```

## Exemplos
```yaml
objective: "Lançar MVP do portal de parceiros"
timeframe: "2024-11"
constraints:
  - "limite de budget trimestral"
  - "integração obrigatória com SSO"
stakeholders:
  - "Comercial"
  - "Segurança"
  - "Infra"
backlog:
  - title: "Autenticação SSO"
    status: "novo"
    dependencies:
      - "diretrizes IAM"
    value: "alto"
    effort: "médio"
    risk: "médio"
  - title: "Catálogo de parceiros"
    status: "novo"
    dependencies: []
    value: "alto"
    effort: "médio"
    risk: "baixo"
policies:
  - "SOC2"
  - "LGPD"
notes: "Primeira release focada em onboarding"
```

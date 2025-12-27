# PLANNING OUTPUTS

## Formato do payload (YAML)
```yaml
prioritized_backlog:
  - id: "REF-001"
    title: "Item ou iniciativa"
    priority: 1
    rationale: "Justificativa de impacto/risco/esforço"
    dependencies:
      - "REF-002"
    target_window: "2024-10"
    owner: "time/role"
    status: "planejado|em_andamento|bloqueado"
work_breakdown:
  - epic: "Entrega principal"
    stories:
      - story: "História de usuário"
        acceptance_criteria:
          - "critério 1"
          - "critério 2"
        tasks:
          - "tarefa 1"
          - "tarefa 2"
risks:
  - description: "risco identificado"
    severity: "alto|médio|baixo"
    mitigation: "ação"
assumptions:
  - "premissa 1"
  - "premissa 2"
open_blockers:
  - "dependência externa"
  - "falta de ambiente"
communication_plan:
  cadence: "semanal|quinzenal"
  audience:
    - "stakeholders"
    - "equipes"
  artifacts:
    - "roadmap"
    - "burndown"
    - "status report"
```

## Exemplos
```yaml
prioritized_backlog:
  - id: "MVP-01"
    title: "Autenticação SSO"
    priority: 1
    rationale: "Bloqueia todo acesso e tem alto valor"
    dependencies: []
    target_window: "2024-09"
    owner: "Plataforma"
    status: "planejado"
  - id: "MVP-02"
    title: "Catálogo de parceiros"
    priority: 2
    rationale: "Entrega valor principal após login"
    dependencies:
      - "MVP-01"
    target_window: "2024-10"
    owner: "Produtos"
    status: "planejado"
work_breakdown:
  - epic: "Autenticação SSO"
    stories:
      - story: "Como parceiro, quero autenticar via SSO para acessar o portal"
        acceptance_criteria:
          - "Login com IdP corporativo"
          - "Provisionamento mínimo de perfil"
          - "Logs de auditoria gerados"
        tasks:
          - "Configurar integração OIDC"
          - "Testar fluxos de erro"
          - "Documentar onboarding"
risks:
  - description: "Dependência do time de IAM para provisionamento"
    severity: "médio"
    mitigation: "Agendar janela compartilhada e mockar ambiente"
assumptions:
  - "IdP com suporte a OIDC"
  - "Equipe de parceiros disponível para UAT"
open_blockers: []
communication_plan:
  cadence: "semanal"
  audience:
    - "Comercial"
    - "Segurança"
    - "Engenharia"
  artifacts:
    - "roadmap"
    - "risco/mitigação"
    - "status semanal"
```

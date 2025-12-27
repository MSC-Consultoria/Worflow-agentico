# PLANNING TESTS

## Estratégia de validação
- Verificar presença de campos obrigatórios (`objective`, `timeframe`, `prioritized_backlog`, `work_breakdown`).
- Garantir que cada item priorizado tenha `priority`, `rationale`, `owner` e `target_window`.
- Confirmar que histórias possuem critérios de aceitação e tarefas associadas.
- Validar consistência de dependências (referências válidas entre itens).

## Gatilhos
- A cada nova solicitação de planejamento.
- Sempre que o backlog priorizado for atualizado.
- Antes de comunicar roadmap para stakeholders.

## Payload de teste (YAML)
```yaml
objective: "Liberar MVP do portal de parceiros"
timeframe: "2024-11"
prioritized_backlog:
  - id: "MVP-01"
    title: "SSO"
    priority: 1
    rationale: "bloqueia acesso"
    dependencies: []
    target_window: "2024-09"
    owner: "Plataforma"
  - id: "MVP-02"
    title: "Catálogo"
    priority: 2
    rationale: "valor core"
    dependencies:
      - "MVP-01"
    target_window: "2024-10"
    owner: "Produtos"
work_breakdown:
  - epic: "SSO"
    stories:
      - story: "Login via IdP"
        acceptance_criteria:
          - "login ok"
          - "erro tratado"
        tasks:
          - "OIDC config"
          - "QA"
```

## Resultados esperados
- Payload aceito sem erros estruturais.
- Dependências resolvidas ou sinalizadas como ausentes.
- Indicadores de completude exibem 100% dos campos críticos preenchidos.

# TESTS AGENT

## Estratégia de testes
- Cobrir níveis unitário (funções/módulos isolados) e integração (fluxos entre serviços e dependências externas).
- Mapear critérios de entrada/saída por camada, com dados de teste representativos e negativos.
- Automatizar regressão em pipelines de CI e validar contratos (APIs, eventos).

## Gatilhos
- Commits em branches principais ou pull requests.
- Antes de releases e deploys para ambientes produtivos.
- Mudanças em contratos externos ou dependências críticas.

## Reporting
- Consolidar resultados em relatórios de CI com métricas de cobertura, tempo de execução e falhas por módulo.
- Notificar responsáveis quando casos críticos falham, com links para logs e reproduções mínimas.

## Inputs e outputs
- Inputs: especificações de requisitos, contratos de API/eventos, dados de fixtures (padronizados em YAML para submissão).
- Outputs: relatórios de execução (JUnit/Allure), indicadores de cobertura e matriz de rastreabilidade requisito → teste, exportados em YAML.

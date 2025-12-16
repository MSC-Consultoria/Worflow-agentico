# SECURITY_AND_BENCHMARK_TESTS.md

Padrões mínimos de segurança e desempenho que bloqueiam merge e deploy. Aplicável a serviços, pipelines e agentes.

## 1) Testes obrigatórios
- **SAST**: análise estática em cada PR; falhas `High`/`Critical` bloqueiam.
- **Secrets scanning**: sem chaves, tokens ou credenciais hardcoded.
- **Linting/Type-check**: regras do projeto (ex.: `ruff`, `mypy`, `eslint`).
- **Testes unitários e de contrato**: cobrem fluxos críticos e contratos públicos.
- **Testes de integração**: cenários fim-a-fim com dependências principais.
- **Testes de segurança dinâmica (DAST)**: endpoints expostos ou mudanças em autenticação/autorização.
- **Benchmarks de regressão**: latência média/p95, throughput e custo estimado por operação.
- **Fuzzing direcionado** (quando entrada não-confiável): validações de schema e limites.

## 2) Critérios de bloqueio (qualidade)
- Cobertura mínima: acordada por serviço (padrão 80% linhas; 100% para funções de segurança).
- Falha de teste automatizado bloqueia merge.
- Mudanças de contrato sem testes de contrato atualizados: bloqueiam.
- Código sem caminhos de rollback testados: bloqueia.

## 3) Critérios de bloqueio (segurança)
- Vulnerabilidades `High/Critical` em SAST/DAST.
- Dependências com CVE `High/Critical` sem remediação ou exceção aprovada.
- Ausência de autenticação/autorização em endpoints que manipulam dados sensíveis.
- Logs contendo PII sem mascaramento/controle de acesso.
- Ausência de criptografia em trânsito ou em repouso para dados classificados.

## 4) Benchmarks e limites
- **Latência**: regressão máxima permitida de +5% no p95 ou +3% no p50 em rotas críticas.
- **Throughput**: não reduzir TPS sustentado em >3% sem justificativa.
- **Custo**: aumento projetado >5% por transação requer aprovação de negócio e plataforma.
- **Memória/CPU**: não ultrapassar limites definidos para o serviço/pipeline.
- Todos os benchmarks devem ser executados em ambiente reprodutível e anexados ao PR.

## 5) Matriz de severidade
| Impacto \ Probabilidade | Baixa | Média | Alta |
| --- | --- | --- | --- |
| Baixo | Low | Medium | High |
| Médio | Medium | High | High |
| Alto | High | Critical | Critical |

Classificação:
- **Low**: não bloqueia; registrar e priorizar.
- **Medium**: requer remediação planejada antes do próximo release.
- **High**: bloqueia merge; exceção apenas com aprovação formal (segurança + owner).
- **Critical**: bloqueio imediato; incident response se em produção.

## 6) Evidências e automação
- Resultados de testes e benchmarks devem ser publicados no PR (logs ou artefatos).
- Aplicar labels `qa-passed`, `security-passed` ou `benchmark-approved` conforme responsáveis.
- Falhas devem abrir issue vinculada ao PR com plano de correção.

# PYTHON AGENT — EXECUTION PLAYBOOK

Guia consolidado de execução para agentes Python: como construir, testar e entregar mudanças.

## 1) TDD e ciclo de entrega
- Escrever testes antes da implementação para cada requisito funcional ou bug.
- Manter suíte rápida: preferir testes puros e usar fakes/mocks para dependências externas.
- Para regressões, primeiro reproduzir com teste vermelho; só então corrigir.
- Todo bug corrigido deve ter teste que falha no estado anterior.
- Executar lint, type-check e testes antes de abrir PR.

## 2) Variabilidade de contexto
- Limitar tokens de contexto conforme `MEMORY_ARCHITECTURE.md` (contexto imediato e memória de trabalho).
- Normalizar entradas: remover ruído, validar schemas, aplicar limites de tamanho.
- Controlar deriva: revalidar premissas a cada iteração longa e registrar deltas de estado.
- Usar feature flags ou parâmetros de sessão para comportamentos variantes.

## 3) Hooks de segurança
- Implementar autenticação/autorizações obrigatórias antes de expor endpoints.
- Validar todas as entradas com schemas e limites; rejeitar inputs sem origem confiável.
- Sanitizar logs e outputs para evitar vazamento de PII ou chaves.
- Integrar scanners de segredo e SAST no pipeline (ver `SECURITY_AND_BENCHMARK_TESTS.md`).

## 4) Padrão de PR
- Incluir descrição curta do problema, solução, escopo afetado e riscos.
- Anexar evidências: resultados de testes, benchmarks, screenshots quando visual.
- Citar decisões relevantes (`DECISIONS.md`) e atualizar documentação tocada.
- Garantir revisão dupla: 1 aprovador técnico + 1 de domínio, conforme `PROCESS_GUARDRAILS.md`.
- Labels recomendados: `tdd`, `security`, `qa-passed`, `docs-updated`.

## 5) Checklist de execução
- [ ] Issue ou RFC vinculada
- [ ] Teste reproduzindo o problema
- [ ] Implementação com TDD
- [ ] Lint/Type-check/Testes rodados
- [ ] Benchmarks se afetar performance
- [ ] Documentação atualizada
- [ ] Plano de rollback
- [ ] Revisões e aprovações registradas

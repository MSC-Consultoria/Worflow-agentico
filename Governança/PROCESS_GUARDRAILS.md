# PROCESS_GUARDRAILS.md

Fluxo obrigatório de decisão e aprovação para mudanças relevantes em sistemas e processos críticos. O objetivo é garantir segurança, conformidade e rastreabilidade de forma previsível.

## 1) Escopo do fluxo obrigatório
- Mudanças em contratos de interface pública (APIs, eventos, schemas de memória).
- Alterações de segurança, privacidade, compliance ou observabilidade.
- Ajustes que impactem disponibilidade, latência ou custo de execução.
- Novos pipelines ou mudanças em gates de qualidade.

## 2) Sequência de aprovação
1. **Proposição** — RFC ou issue com objetivo, riscos, rollback e plano de testes.
2. **Revisão funcional** — validação de requisitos de negócio e usuários.
3. **Revisão técnica** — arquitetura, performance, integridade de dados e logging.
4. **Segurança & Privacidade** — checklist de ameaças, dados sensíveis, criptografia e RBAC.
5. **Conformidade** — LGPD/PII, retenção e trilhas de auditoria.
6. **SRE/Plataforma** — impacto em confiabilidade, quotas, escalabilidade e custos.
7. **Qualidade** — testes automatizados, benchmarks e critérios de aceite.
8. **Aprovação final** — um aprovador de negócio e um técnico (duplo-par), seguindo matriz de responsabilidade definida na equipe. **June** é a owner padrão de produto/negócio; o lead técnico é designado por serviço.

## 3) Gates obrigatórios antes de merge/deploy
- **Checklist de segurança** concluído e assinado (ver `SECURITY_CHECKLIST.md`).
- **Cobertura de testes mínimos** atingida conforme `SECURITY_AND_BENCHMARK_TESTS.md`.
- **Benchmark de regressão** sem piora superior aos limites definidos.
- **Validação de rollback**: plano testado ou comprovadamente reversível.
- **Documentação** atualizada (pipelines, memória e APIs) quando afetadas.
- **Observabilidade**: métricas/alerts atualizados para o novo comportamento.

## 3.1) Stack de deploy aprovada
- **Firebase (Google)**: serviços web e autenticados preferencialmente hospedados aqui.
- **Streamlit + Supabase**: para demos ou painéis; sempre armazenar dados em Supabase quando usar Streamlit.
- **Hugging Face Spaces**: permitido para protótipos/ML; tokens devem ficar em variáveis de ambiente ou secret stores.

## 4) Exceções e desvios
- Exceções só são permitidas para incidentes críticos (SEV-1) ou correções de disponibilidade.
- Devem ser aprovadas por: (a) responsável de SRE/Oncall, (b) responsável de Segurança, (c) owner de produto.
- Registrar desvio no postmortem com: razão, risco assumido, mitigação temporária e prazo de regularização.
- Qualquer gate pulado exige tarefa de follow-up atribuída com due date e responsável.

## 5) Evidências e trilha de auditoria
- Registrar decisões no `DECISIONS.md` com link para RFC/issue/PR.
- Anexar resultados de testes e benchmarks ao PR.
- Usar labels de aprovação (ex.: `security-approved`, `sre-approved`, `qa-approved`).
- Guardar logs de deploy e rollback por no mínimo 90 dias.

# Base de Conhecimento — GitHub Agent

## Objetivo
Esta base documenta padrões, responsabilidades e mecanismos de governança aplicados ao GitHub como sistema nervoso do projeto.

## Princípios
- GitHub é fonte da verdade
- Markdown é contrato durável
- Tudo é auditável
- Nada entra sem PR

## Responsabilidades do GitHub Agent
- Governar Pull Requests
- Enforçar políticas de branch
- Garantir checks obrigatórios
- Preservar histórico e trilha de decisão

## Pull Requests
- Todo código entra via PR
- PR deve referenciar Issue
- PR passa por checks automáticos
- PR exige aprovação humana quando definido

### Checklist para abertura de PR
- [ ] Link para a Issue no corpo do PR (fixes/closes #123)
- [ ] Labels iniciais aplicadas
- [ ] Template de PR preenchido (contexto, mudanças, testes, riscos)
- [ ] Descrição clara do objetivo e escopo
- [ ] Evidências ou testes mencionados

## Issues
- Porta de entrada de trabalho
- Templates obrigatórios
- Labels definem fluxo e prioridade

## Checks e Status
- CI obrigatório
- Segurança bloqueia se crítico
- Qualidade pode alertar

## Políticas de Branch
- main protegido
- Sem push direto
- Revisões mínimas exigidas

| Tipo de branch | Finalidade | Exemplo de nomenclatura | Base recomendada | Regras |
| --- | --- | --- | --- | --- |
| feature/ | Novas funcionalidades ou evoluções | `feature/checkout-arquivos` | main | Atualizar frequentemente a partir de main; manter escopo focado |
| bugfix/ | Correções sem impacto crítico em produção | `bugfix/fix-null-user-id` | main | Incluir teste cobrindo o bug; evitar mudanças de escopo |
| hotfix/ | Correções urgentes em produção | `hotfix/corrige-500-login` | main ou tag de produção | Minimizar diffs; publicar release note; revisar reversão |

## Governança
- Bloqueio: falha crítica
- Alerta: aviso não bloqueante
- Comentário: instrução automática
- Escalonamento: decisão humana

## Integração com Pipeline
- Observa: métricas e eventos
- Propõe: abre PR
- Exige: bloqueia merge

## Convenções
- Branch: feature/, bugfix/, hotfix/
- Commits: Conventional Commits
- Labels padronizados

### Commits (Conventional Commits)
- `feat`: nova funcionalidade. Ex.: `feat: adiciona suporte a múltiplos idiomas`
- `fix`: correção de bug. Ex.: `fix: impede crash ao salvar rascunho`
- `chore`: manutenção sem impacto no produto. Ex.: `chore: atualiza dependências de lint`
- `docs`: documentação. Ex.: `docs: adiciona guia de contribuição`
- `refactor`: mudanças internas sem alterar comportamento. Ex.: `refactor: simplifica serviço de autenticação`
- `test`: inclusão ou ajuste de testes. Ex.: `test: cobre fluxos de erro no login`
- `build`: mudanças de build ou CI. Ex.: `build: ajusta pipeline para rodar lint`
- `perf`: melhorias de desempenho. Ex.: `perf: reduz queries duplicadas no feed`
- `revert`: desfaz commit anterior. Ex.: `revert: "feat: adiciona suporte a múltiplos idiomas"`

### Labels sugeridas
| Label | Quando aplicar |
| --- | --- |
| `type:feature` | PR que entrega nova funcionalidade |
| `type:bug` | Correção de comportamento existente |
| `type:hotfix` | Correção crítica em produção |
| `area:frontend` / `area:backend` / `area:devops` | Delimitar área afetada |
| `impact:breaking` | Mudança incompatível ou que exige migração |
| `priority:alta` / `priority:média` / `priority:baixa` | Definir urgência e ordem de avaliação |
| `status:wip` | PR em construção, não pronto para revisão |
| `needs:tests` | Falta evidência de testes |
| `needs:review` | PR pronto, aguardando revisão |

## Histórico
- PR = unidade de decisão
- Commit = evidência técnica
- Comentário = contexto humano

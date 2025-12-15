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

## Histórico
- PR = unidade de decisão
- Commit = evidência técnica
- Comentário = contexto humano

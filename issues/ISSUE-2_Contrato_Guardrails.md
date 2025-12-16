# Issue: Contrato de Guardrails

**Status:** Open
**Created:** 2025-12-16
**Author:** Agent

## Objetivo
Estabelecer o contrato de guardrails para agentes e pipelines, definindo limites de atuação, procedimentos de fallback e critérios de escalonamento.

## Escopo
- Documentar objetivos de segurança e alinhamento para cada tipo de agente.
- Definir políticas de bloqueio, revisão humana e registros obrigatórios.
- Mapear indicadores de aderência e métricas de auditoria.

## Entregáveis
- Documento de contrato em `Governança/PROCESS_GUARDRAILS.md` com responsabilidades, fluxos de exceção e rastreabilidade.
- Checklist de revisão para PR curto.
- Itens de validação manual definidos na descrição do PR.

## Branch & PR
- Branch dedicada: `feature/governanca-guardrails`.
- PR curto com checklist de revisão obrigatório.
- Descrição do PR deve listar riscos conhecidos e passos de validação manual executados.

## Riscos iniciais
- Lacunas de bloqueio para ações destrutivas ou alto impacto.
- Falta de critérios de override humano e logging consistente.

## Validação manual esperada
- Revisar se cada guardrail tem owner, condição de disparo e ação padrão.
- Validar exemplos de prompts/cenários que exercitem os guardrails críticos.

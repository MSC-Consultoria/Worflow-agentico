# DECISIONS.md

Registro resumido de decisões, próximos passos e ideias de projeto.

## Decisões — 2025-12-16
- Abrir issues separadas para contratos de guardrails, testes de segurança, Pipeline Engine e Memória, cada uma com branch dedicada `feature/governanca-<tema>`.
- Para cada branch, produzir PR curto com checklist de revisão obrigatório e descrição contendo riscos conhecidos e passos de validação manual realizados.
- Criar issue priorizada para treinamento de embeddings no Hugging Face via Colab, com notebook Jupyter pronto e branch `feature/governanca-embedding-colab`.
- Criar issue para configurar testes de aprendizado por reforço no Hugging Face alinhado ao guia OpenEvals/tool-calling, com branch `feature/governanca-rl-hf-tests` e documentação técnica futura.

## Próximos passos (ação)
- Publicar catálogo de testes no repositório de automação e integrar no pipeline CI.
- Definir owners para aprovação dupla (técnico + domínio) e aplicar labels automáticos.
- Preparar ambiente de benchmark reproduzível e anexar ao PR template.
- Configurar stack de deploy: Firebase (app principal), Streamlit + Supabase (painéis/demos) e Space no Hugging Face para protótipo ML.

## Ideias de projeto
- **Hugging Face Space + Colab**: criar notebook de setup que autentica na HF, faz deploy de um Space minimal (API demo) e executa testes de conectividade; usar secrets/vars seguros.
- **Observabilidade do Pipeline Engine**: dashboard com estados, tempos de estágio e alertas de regressão.
- **Memória compartilhada de políticas**: serviço leve para servir glossário, guardrails e decisões aprovadas com versionamento.

## Plano detalhado — Hugging Face Space
1) Variáveis/segredos: definir `HUGGINGFACE_API_TOKEN` no ambiente (NÃO commitar). Use o token fornecido (hf_...) apenas via secret manager/variável. Opcional: `HF_SPACE_NAME=workflow-space`.
2) Setup local: usar script `scripts/hf_connection_test.py` para validar token e permissão de criação/listagem.
3) Deploy inicial: Space mínimo (API echo) a partir de template; habilitar privacy conforme necessidade.
4) Integração com Colab: notebook de provisionamento que consome o token de secret (Colab/Secrets) e publica atualização no Space.
5) Observabilidade: capturar logs de build/deploy do Space e armazenar em Supabase para auditoria rápida.

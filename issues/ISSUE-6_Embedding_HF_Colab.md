# Issue (Prioritária): Treinamento de Embeddings no Hugging Face com Colab

**Status:** Open
**Priority:** Alta
**Created:** 2025-12-16
**Author:** Agent

## Objetivo
Treinar (ou ajustar) um modelo de embeddings no Hugging Face usando todo o conteúdo do repositório atual, executando o pipeline em Google Colab com notebook pronto (Jupyter) para reproducibilidade.

## Escopo
- Preparar dataset de texto a partir do repositório (Markdown, código e docs relevantes), com limpeza e chunking.
- Selecionar modelo base de embeddings (ex.: `sentence-transformers/all-MiniLM-L12-v2`) e definir hiperparâmetros de fine-tuning.
- Rodar treinamento no Google Colab, salvando checkpoints e publicando o modelo no Hugging Face Hub.
- Validar qualidade com métricas (ex.: MTEB subset) e exemplos práticos do domínio.
- Registrar instruções de push/pull do modelo e dataset no Hub.

## Entregáveis
- Notebook Colab pronto (`scripts/colab_embedding_training.ipynb`) com passos de setup, extração do repositório, preparação do dataset, treinamento e push para o Hugging Face Hub.
- Artefatos de configuração (vars/segredos) documentados no notebook.
- Resultados mínimos: loss final, métricas de similaridade/STS em amostra, exemplos qualitativos.
- Modelo e dataset publicados no Hugging Face (privado ou público conforme política).

## Branch & PR
- Branch dedicada: `feature/governanca-embedding-colab`.
- PR curto com checklist de revisão obrigatório.
- Descrição do PR deve listar riscos e passos de validação manual executados no Colab.

## Riscos iniciais
- Custos de compute no Colab e limites de sessão.
- Overfitting em corpus interno ou vazamento de dados sensíveis.
- Falta de balanceamento entre tipos de arquivo (código vs. docs) afetando qualidade de embedding.

## Validação manual esperada
- Executar notebook até o push do modelo/dataset em ambiente de teste (token HF configurado via secret).
- Validar métricas de similaridade em amostra do domínio (ex.: pares de documentos do repositório).
- Verificar tamanho/qualidade do dataset gerado e logs de treinamento.

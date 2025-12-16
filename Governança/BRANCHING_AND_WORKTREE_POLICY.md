# Política de Ramificação e Worktree (Branching & Worktree Policy)

Esta política define como o trabalho deve ser estruturado no repositório, garantindo a integridade do código e a fluidez da colaboração.

## 1. Modelo de Fluxo (Workflow)

Adotamos o **GitHub Flow** com convenções estritas. A simplicidade é a chave.

### Estrutura da Worktree
O repositório possui uma única ramificação de longa duração:

*   **`main`**: Fonte da verdade (Source of Truth). Contém sempre código estável, testado e pronto para produção. **Nunca** deve receber commits diretos (Direct Push).

### Ramificações de Trabalho (Short-Lived Branches)
Todo trabalho novo deve ser realizado em ramificações efêmeras criadas a partir da `main`.

| Tipo | Prefixo | Uso | Exemplo |
| :--- | :--- | :--- | :--- |
| **Feature** | `feature/` | Novas funcionalidades ou melhorias. | `feature/auth-system` |
| **Bugfix** | `fix/` | Correção de erros no código. | `fix/login-error` |
| **Chore** | `chore/` | Tarefas de manutenção, deps, refatoração sem impacto funcional. | `chore/update-deps` |
| **Docs** | `docs/` | Apenas alterações em documentação. | `docs/update-readme` |
| **Hotfix** | `hotfix/` | Correções críticas urgentes para produção. | `hotfix/security-patch` |

---

## 2. Regras de Proteção (Branch Protection Rules)

Como este é um sistema governado, as seguintes regras devem ser configuradas nas **Configurações do Repositório (Settings > Branches)** para a branch `main`:

1.  **Require a pull request before merging:**
    *   Nenhum código entra na main sem revisão.
    *   *Require approvals:* Mínimo de 1 revisão (Humana ou Agente Sênior).
2.  **Require status checks to pass before merging:**
    *   Os testes (CI) definidos no Pipeline Engine devem passar.
3.  **Require conversation resolution before merging:**
    *   Todos os comentários no PR devem ser resolvidos.
4.  **Do not allow bypassing the above settings:**
    *   Administradores também estão sujeitos à governança.

---

## 3. Fluxo de Trabalho do Desenvolvedor (Developer Workflow)

Como sua worktree local deve se comportar:

1.  **Sincronizar:**
    ```bash
    git checkout main
    git pull origin main
    ```

2.  **Criar Branch:**
    ```bash
    git checkout -b feature/minha-nova-feature
    ```

3.  **Desenvolver e Commitar:**
    *   Fazer alterações granulares.
    *   Usar **Conventional Commits** (ex: `feat: add login button`, `fix: handle null token`).

4.  **Publicar:**
    ```bash
    git push origin feature/minha-nova-feature
    ```

5.  **Abrir Pull Request (PR):**
    *   Via interface do GitHub ou CLI (`gh pr create`).
    *   O "GitHub Agent" validará o PR conforme `Governança/PR_STANDARD.md`.

---

## 4. Por que minha branch não está protegida agora?

**Nota Importante:** A proteção de branch é uma configuração de **infraestrutura do GitHub**, não um arquivo de código.
*   **O Agente** define a política (este documento).
*   **O Admin do Repositório** deve ativar a opção "Branch protection rules" nas configurações do repositório no GitHub.com para efetivar a regra técnica.

Até que essa configuração seja feita manualmente na interface do GitHub, o bloqueio técnico não existirá, mas a **regra de governança** permanece válida: **Não faça push direto na main.**

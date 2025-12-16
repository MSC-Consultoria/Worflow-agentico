"""
Script rápido para validar token e conectividade com Hugging Face Spaces.

Configuração segura:
- Defina a variável de ambiente HUGGINGFACE_API_TOKEN (não commitá-la).
- Opcional: HUGGINGFACE_SPACE (ex.: workflow-space) para verificar existência.

Uso:
    python scripts/hf_connection_test.py
    HUGGINGFACE_SPACE=workflow-space python scripts/hf_connection_test.py

Saídas esperadas:
- Confirmação de identidade (whoami)
- Listagem curta de Spaces acessíveis
- Verificação opcional de existência de um Space específico
"""

from __future__ import annotations

import os
import sys
from typing import Any, Dict, List

import requests

API_TOKEN_ENV = "HUGGINGFACE_API_TOKEN"
SPACE_ENV = "HUGGINGFACE_SPACE"
BASE_URL = "https://huggingface.co/api"


def _auth_headers(token: str) -> Dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def whoami(token: str) -> Dict[str, Any]:
    resp = requests.get(f"{BASE_URL}/whoami-v2", headers=_auth_headers(token), timeout=10)
    resp.raise_for_status()
    return resp.json()


def list_spaces(token: str, limit: int = 5) -> List[Dict[str, Any]]:
    params = {"full": "false", "limit": str(limit)}
    resp = requests.get(f"{BASE_URL}/spaces", headers=_auth_headers(token), params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def check_space_exists(spaces: List[Dict[str, Any]], target: str) -> bool:
    return any(space.get("id", "").endswith(target) for space in spaces)


def main() -> int:
    token = os.getenv(API_TOKEN_ENV)
    if not token:
        print(f"Erro: defina a variável {API_TOKEN_ENV} com seu token HF (não commitá-la).", file=sys.stderr)
        return 1

    try:
        me = whoami(token)
        print(f"Autenticado como: {me.get('name')} (orgs: {me.get('orgs', [])})")

        spaces = list_spaces(token)
        print(f"Spaces acessíveis (máx 5): {[s.get('id') for s in spaces]}")

        target_space = os.getenv(SPACE_ENV)
        if target_space:
            exists = check_space_exists(spaces, target_space)
            status = "encontrado" if exists else "não encontrado"
            print(f"Space '{target_space}': {status} na conta atual")

        print("Conexão OK. Use este token via variável de ambiente ou secret manager; não o commit.")
        return 0
    except requests.HTTPError as exc:  # type: ignore[no-untyped-call]
        print(f"Falha na API HF: {exc} | resposta: {getattr(exc.response, 'text', '')}", file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001
        print(f"Erro inesperado: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())

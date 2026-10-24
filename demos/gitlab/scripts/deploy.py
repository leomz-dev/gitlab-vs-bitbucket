"""Despliegue simulado de NotasApp.

Se ejecuta desde los jobs/steps de despliegue de GitLab y Bitbucket.

Uso:
    python scripts/deploy.py <entorno>
"""

import os
import sys
from datetime import datetime


def desplegar(entorno):
    """Simula el despliegue de la aplicación en el entorno indicado."""
    commit = os.environ.get("CI_COMMIT_SHA") or os.environ.get("BITBUCKET_COMMIT") or "local"
    rama = os.environ.get("CI_COMMIT_REF_NAME") or os.environ.get("BITBUCKET_BRANCH") or "local"

    print("== Despliegue de NotasApp ==")
    print(f"Entorno .....: {entorno}")
    print(f"Commit ......: {commit[:8]}")
    print(f"Rama ........: {rama}")
    print(f"Fecha .......: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Resultado ...: despliegue en {entorno} completado.")


if __name__ == "__main__":
    desplegar(sys.argv[1] if len(sys.argv) > 1 else "staging")

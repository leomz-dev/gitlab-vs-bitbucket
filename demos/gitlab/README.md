# NotasApp - Ejemplo GitLab

Repositorio de demostración para el **Ejemplo 1 (GitLab)** del informe comparativo
"GitLab vs Bitbucket".

## Contenido

| Ruta | Descripción |
|---|---|
| `src/notas.py` | Lógica de negocio (validación de notas, promedio, aprobación). |
| `tests/test_notas.py` | Pruebas unitarias con `unittest` (16 casos). |
| `.gitlab-ci.yml` | Pipeline CI/CD: `build` -> `test` -> `deploy`. |
| `scripts/deploy.py` | Despliegue simulado invocado por el pipeline. |

## Ejecución local

```bash
python -m unittest discover -s tests -v
```

## Flujo de trabajo (GitLab Flow)

1. Se crea una rama corta: `git switch -c feature/promedio-ponderado`.
2. Se implementa la funcionalidad y se confirma.
3. Se sube la rama y GitLab abre un **Merge Request**:
   `git push -o merge_request.create -o merge_request.target=main origin feature/promedio-ponderado`
4. El pipeline se ejecuta automáticamente sobre el MR (build + test + estilo).
5. Con el pipeline en verde y las aprobaciones requeridas, se fusiona con
   `git merge --no-ff` (queda registrado como `Merge branch 'feature/...' into 'main'`).
6. Se etiqueta la entrega: `git tag -a v1.0.0 -m "Release 1.0.0"`.

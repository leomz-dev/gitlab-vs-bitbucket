# NotasApp - Ejemplo Bitbucket

Repositorio de demostración para el **Ejemplo 2 (Bitbucket)** del informe comparativo
"GitLab vs Bitbucket".

## Contenido

| Ruta | Descripción |
|---|---|
| `src/notas.py` | Lógica de negocio (validación de notas, promedio, aprobación). |
| `tests/test_notas.py` | Pruebas unitarias con `unittest` (16 casos). |
| `bitbucket-pipelines.yml` | Pipelines: `default`, `pull-requests` y `branches.main`. |
| `scripts/deploy.py` | Despliegue simulado invocado por los steps de despliegue. |

## Ejecución local

```bash
python -m unittest discover -s tests -v
```

## Flujo de trabajo (feature branch + Pull Request)

1. Se crea una rama corta: `git switch -c feature/promedio-ponderado`.
2. Se implementa la funcionalidad y se confirma.
3. Se sube la rama; en Bitbucket **el Pull Request se crea desde la interfaz web**
   (no existe una bandera equivalente a `-o merge_request.create`).
4. Los *merge checks* configurados (build correcto, mínimo de revisores) deben
   cumplirse antes de habilitar el botón de fusión.
5. Se fusiona con `git merge --no-ff`, lo que genera el mensaje
   `Merged in feature/... (pull request #1)`.
6. Se etiqueta la entrega: `git tag -a v1.0.0 -m "Release 1.0.0"`.

> Nota: Bitbucket **no** ofrece `needs` (grafo DAG) ni `include`/pipelines
> padre-hijo. El orden de ejecución es siempre secuencial (lista de `step`).

"""NotasApp - cálculo de notas académicas.

Módulo de ejemplo utilizado en la demostración de GitLab y Bitbucket.
"""


class NotaInvalidaError(ValueError):
    """Se lanza cuando una nota está fuera del rango permitido 0.0 - 5.0."""


def validar_nota(nota: float) -> float:
    """Valida que la nota esté en el rango permitido (0.0 a 5.0).

    Args:
        nota: Valor numérico de la nota.

    Returns:
        La nota convertida a float si es válida.

    Raises:
        NotaInvalidaError: Si la nota no es numérica o está fuera del rango.
    """
    if isinstance(nota, bool) or not isinstance(nota, (int, float)):
        raise NotaInvalidaError(f"La nota debe ser numérica, se recibió: {nota!r}")
    if nota < 0.0 or nota > 5.0:
        raise NotaInvalidaError(f"La nota {nota} está fuera del rango 0.0 - 5.0")
    return float(nota)


def promedio(notas):
    """Calcula el promedio aritmético de una lista de notas.

    Args:
        notas: Lista de notas numéricas.

    Returns:
        El promedio redondeado a dos decimales.
    """
    if not notas:
        raise NotaInvalidaError("La lista de notas no puede estar vacía")
    return round(sum(validar_nota(n) for n in notas) / len(notas), 2)


def aprobo(notas, umbral=3.0):
    """Indica si el estudiante aprobó según un umbral.

    Args:
        notas: Lista de notas numéricas.
        umbral: Nota mínima para aprobar (por defecto 3.0).

    Returns:
        True si el promedio alcanza el umbral, False en caso contrario.
    """
    return promedio(notas) >= umbral


def promedio_ponderado(notas, pesos):
    """Calcula el promedio ponderado de las notas según sus pesos.

    Args:
        notas: Lista de notas numéricas.
        pesos: Lista de pesos (créditos o porcentajes) del mismo tamaño.

    Returns:
        El promedio ponderado redondeado a dos decimales.
    """
    if len(notas) != len(pesos):
        raise NotaInvalidaError("La cantidad de notas y de pesos debe coincidir")
    if sum(pesos) <= 0:
        raise NotaInvalidaError("La suma de los pesos debe ser mayor que cero")
    total = sum(validar_nota(n) * p for n, p in zip(notas, pesos))
    return round(total / sum(pesos), 2)

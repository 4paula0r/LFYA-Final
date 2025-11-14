# classifier.py

from typing import Dict, List, Tuple
from utils import es_variable, partir_rhs


def _analizar_regular(reglas: Dict[str, List[str]]) -> (bool, List[str]):
    """
    Verifica si la gramática es Regular (Tipo 3).

    Formas permitidas (lineal a la derecha):
      A -> aB   (terminal seguido de variable)
      A -> a    (solo terminal)
      A -> ε    (epsilon)
    donde A y B son variables (mayúsculas) y a es terminal (no mayúscula).
    """
    razones: List[str] = []
    es_reg = True

    for A, rhss in reglas.items():
        if not es_variable(A):
            es_reg = False
            razones.append(
                f"El lado izquierdo '{A}' no es una sola variable mayúscula (rompe la forma regular)."
            )
            continue

        for rhs in rhss:
            simbolos = partir_rhs(rhs)

            # Caso epsilon
            if simbolos == ["ε"]:
                razones.append(f"La producción {A} -> ε es permitida en gramáticas regulares.")
                continue

            # Un solo símbolo
            if len(simbolos) == 1:
                X = simbolos[0]
                if es_variable(X):
                    es_reg = False
                    razones.append(
                        f"La producción {A} -> {rhs} tiene solo una variable en el lado derecho (no regular)."
                    )
                else:
                    razones.append(
                        f"La producción {A} -> {rhs} es de la forma a (solo terminal), válida en gramáticas regulares."
                    )
                continue

            # Dos símbolos
            if len(simbolos) == 2:
                a, B = simbolos
                if (not es_variable(a)) and es_variable(B):
                    razones.append(
                        f"La producción {A} -> {rhs} es de la forma aB (terminal+variable), válida en gramáticas regulares."
                    )
                else:
                    es_reg = False
                    razones.append(
                        f"La producción {A} -> {rhs} NO es de la forma aB (terminal+variable)."
                    )
                continue

            # Más de dos símbolos → rompe regularidad
            es_reg = False
            razones.append(
                f"La producción {A} -> {rhs} tiene longitud mayor a 2 (no regular)."
            )

    if es_reg:
        razones.append("Conclusión: todas las producciones cumplen la forma Regular (Tipo 3).")

    return es_reg, razones


def _analizar_glc(reglas: Dict[str, List[str]]) -> (bool, List[str]):
    """
    Verifica si es Gramática Libre de Contexto (Tipo 2):
      - Cada lado izquierdo debe ser UNA sola variable.
    """
    razones: List[str] = []
    es_glc = True

    for A in reglas.keys():
        if not es_variable(A):
            es_glc = False
            razones.append(
                f"El lado izquierdo '{A}' no es una sola variable (rompe la forma A -> β de una GLC)."
            )

    if es_glc:
        razones.append("Conclusión: todos los lados izquierdos son una sola variable (forma A -> β).")

    return es_glc, razones


def _analizar_csg(start: str, reglas: Dict[str, List[str]]) -> (bool, List[str]):
    """
    Comprobación simplificada de Gramática Sensible al Contexto (Tipo 1).

    Como nuestro formato solo permite una variable en el lado izquierdo,
    revisamos que ninguna producción 'encoga' longitud:
        |α| <= |β|
    y que solo S pueda producir ε.
    """
    razones: List[str] = []
    es_csg = True

    for A, rhss in reglas.items():
        for rhs in rhss:
            if rhs == "ε":
                if A != start:
                    es_csg = False
                    razones.append(
                        f"La producción {A} -> ε no está permitida en CSG (solo S -> ε puede existir)."
                    )
                else:
                    razones.append("La producción S -> ε es aceptada en CSG.")
                continue

            lhs_len = 1  # siempre una sola variable en el lado izquierdo
            rhs_len = len(partir_rhs(rhs))

            if rhs_len < lhs_len:
                es_csg = False
                razones.append(
                    f"La producción {A} -> {rhs} disminuye longitud (|α| > |β|), lo cual rompe la condición de CSG."
                )

    if es_csg:
        razones.append(
            "Conclusión: ninguna producción disminuye longitud (|α| ≤ |β|), salvo quizá S -> ε; cumple condiciones de Tipo 1."
        )

    return es_csg, razones


def clasificar(start: str, reglas: Dict[str, List[str]]) -> Tuple[int, str, List[str]]:
    """
    Clasifica la gramática en el tipo más restrictivo posible.

    Retorna:
        tipo_id  (3,2,1,0)
        tipo_nombre (string legible)
        razones (lista de explicaciones)
    """
    razones_globales: List[str] = []

    # 1) Intentar Tipo 3 (Regular)
    es_reg, razones_reg = _analizar_regular(reglas)
    razones_globales.extend(razones_reg)
    if es_reg:
        return 3, "Tipo 3 (Regular)", razones_globales

    razones_globales.append(
        "La gramática NO cumple completamente las restricciones de una gramática regular (Tipo 3)."
    )

    # 2) Intentar Tipo 2 (GLC)
    es_glc, razones_glc = _analizar_glc(reglas)
    razones_globales.extend(razones_glc)
    if es_glc:
        return 2, "Tipo 2 (Libre de Contexto)", razones_globales

    razones_globales.append(
        "La gramática NO cumple las restricciones de una gramática libre de contexto (Tipo 2)."
    )

    # 3) Intentar Tipo 1 (CSG)
    es_csg, razones_csg = _analizar_csg(start, reglas)
    razones_globales.extend(razones_csg)
    if es_csg:
        return 1, "Tipo 1 (Sensible al Contexto)", razones_globales

    razones_globales.append(
        "La gramática NO cumple las restricciones de una gramática sensible al contexto (Tipo 1)."
    )

    # 4) Si nada de lo anterior se cumple, es Tipo 0
    razones_globales.append("Conclusión final: la gramática es al menos de Tipo 0 (recursivamente enumerable).")
    return 0, "Tipo 0 (Recursivamente Enumerable)", razones_globales

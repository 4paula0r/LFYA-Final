# grammar_parser.py

from utils import limpiar_linea

def leer_gramatica(desde_texto: str):
    reglas = {}
    start = None

    texto = desde_texto.replace(";", "\n")

    for cruda in texto.splitlines():
        linea = limpiar_linea(cruda)
        if not linea:
            continue

        if "->" not in linea:
            raise ValueError(f"Regla inválida: {linea}")

        izquierda, derecha = linea.split("->", 1)
        A = izquierda.strip()
        if start is None:
            start = A

        alternativas = [r.strip() for r in derecha.split("|")]
        norm = []
        for alt in alternativas:
            if alt in ("e", "epsilon", "ɛ"):
                norm.append("ε")
            else:
                norm.append(alt)

        reglas.setdefault(A, []).extend(norm)

    return start, reglas

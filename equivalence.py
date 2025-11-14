# equivalence.py

from grammar_parser import leer_gramatica


def _expand(start, reglas, max_len):
    resultados = set()

    def terminaron(s):
        return all(not c.isupper() for c in s) or s == "ε"

    def expandir(cad):
        if terminaron(cad):
            cadf = "" if cad == "ε" else cad
            if len(cadf) <= max_len:
                resultados.add(cadf)
            return

        for i, c in enumerate(cad):
            if c.isupper():
                for rhs in reglas[c]:
                    nueva = cad[:i] + ("" if rhs == "ε" else rhs) + cad[i+1:]
                    if len(nueva) <= max_len + 2:
                        expandir(nueva)
                break

    expandir(start)
    return resultados


def comparar_gramaticas(g1, g2, max_len=4):
    start1, r1 = leer_gramatica(g1)
    start2, r2 = leer_gramatica(g2)

    L1 = _expand(start1, r1, max_len)
    L2 = _expand(start2, r2, max_len)

    return {
        "L1": L1,
        "L2": L2,
        "solo_L1": L1 - L2,
        "solo_L2": L2 - L1,
    }

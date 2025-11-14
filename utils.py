# utils.py

def es_variable(simbolo: str) -> bool:
    return len(simbolo) == 1 and simbolo.isupper()

def partir_rhs(texto_rhs: str):
    if texto_rhs == "ε":
        return ["ε"]
    return list(texto_rhs)

def limpiar_linea(linea: str) -> str:
    linea = linea.split("//")[0]
    return linea.strip()

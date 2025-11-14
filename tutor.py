# tutor.py

import random
from classifier import clasificar
from grammar_parser import leer_gramatica


def generar_ejemplo(tipo):
    if tipo == 3:
        return "S", {"S": ["aS", "b", "ε"]}, "Regular"
    if tipo == 2:
        return "S", {"S": ["aSb", "ab"]}, "GLC"
    if tipo == 1:
        return "S", {"S": ["aS", "aA"], "A": ["ab"]}, "CSG"
    return "S", {"S": ["SaS", "b"]}, "Tipo 0"


def jugar_una_ronda():
    tipo_real = random.choice([3, 2, 1, 0])
    start, reglas, exp = generar_ejemplo(tipo_real)

    print("\n--- NUEVA GRAMÁTICA ---")
    for A, rhss in reglas.items():
        print(f"{A} -> " + " | ".join(rhss))

    user = int(input("¿Qué tipo crees que es (3/2/1/0)? "))

    clasif, _, _ = clasificar(start, reglas)

    if clasif == user:
        print("¡Correcto!")
        return True
    print("Incorrecto.")
    return False


def ejecutar_tutor():
    n = int(input("Rondas: "))
    score = 0

    for i in range(n):
        print(f"Ronda {i+1}/{n}")
        if jugar_una_ronda():
            score += 1

    print(f"\nPuntuación final: {score}/{n}")

# main.py

from grammar_parser import leer_gramatica
from classifier import clasificar
from visualizer import generar_diagrama_gramatica
from tutor import ejecutar_tutor
from graphviz.backend.execute import ExecutableNotFound


def ejecutar_clasificacion():
    print("Introduce las reglas de la gramática.")
    print("Escribe una regla por línea. Deja una línea vacía para terminar.\n")

    lineas = []
    while True:
        linea = input()
        if not linea.strip():
            break
        lineas.append(linea)

    reglas_texto = "\n".join(lineas)
    if not reglas_texto.strip():
        print("No se ingresaron reglas.")
        return

    try:
        start, reglas = leer_gramatica(reglas_texto)
    except ValueError as e:
        print("Error al leer la gramática:", e)
        return

    tipo_id, tipo_nombre, razones = clasificar(start, reglas)

    print(f"\nResultado: {tipo_nombre} (Tipo {tipo_id})")
    for razon in razones:
        print(" -", razon)

    try:
        dot = generar_diagrama_gramatica(reglas, start_symbol=start)
        salida = dot.render("diagrama_gramatica", view=True)
        print("Diagrama generado:", salida)
    except ExecutableNotFound:
        print(" No se encontró Graphviz. Instálalo para generar diagramas.")


if __name__ == "__main__":
    print("-------------Clasificador de Chomsky-------------")
    print("1. Clasificar gramática")
    print("2. Modo Tutor")
    print("0. Salir")

    while True:
        op = input("Elige una opción: ")
        if op == "1":
            ejecutar_clasificacion()
        elif op == "2":
            ejecutar_tutor()
        elif op == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")

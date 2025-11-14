# visualizer.py

import os
import graphviz

# Ajusta la ruta a tu instalación de Graphviz si es diferente
GRAPHVIZ_BIN = r"C:\Program Files\Graphviz\bin"
if GRAPHVIZ_BIN not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + GRAPHVIZ_BIN


def generar_diagrama_gramatica(reglas, start_symbol=None):
    """
    Genera un diagrama tipo ÁRBOL de la gramática:

      - El símbolo inicial queda arriba.
      - Debajo cuelgan las producciones A → rhs.
      - Debajo de cada producción cuelgan los símbolos del rhs.

    Ejemplo visual (conceptual):

          S
          │
      ┌───┴─────┐
    S→aSb     S→ab
     / | \      / \
    a  S  b    a   b
    """
    dot = graphviz.Digraph(format="png", engine="dot")

    # Top-Bottom (de arriba hacia abajo) para que parezca árbol
    dot.attr(rankdir="TB", bgcolor="#ffffff")

    if start_symbol is not None:
        dot.attr(
            label=f"Árbol de derivación (símbolo inicial: {start_symbol})",
            labelloc="t"
        )

    # Estilo por defecto para NO terminales
    dot.attr(
        "node",
        shape="circle",
        style="filled",
        fillcolor="#bbdefb",
        color="#0d47a1"
    )

    for A, rhss in reglas.items():
        # Nodo de la variable A
        dot.node(A)

        for idx, rhs in enumerate(rhss, start=1):
            # Nodo para la PRODUCCIÓN completa (ej: "S → aSb")
            prod_node_id = f"{A}_prod_{idx}"
            prod_label = f"{A} → {rhs}"

            dot.node(
                prod_node_id,
                label=prod_label,
                shape="box",
                style="filled",
                fillcolor="#e8f5e9",
                color="#1b5e20"
            )

            # Conectar A con su producción
            dot.edge(A, prod_node_id, color="#7f8c8d")

            # Ahora desglosamos los símbolos del lado derecho (rhs)
            if rhs != "ε":  # epsilon lo dejamos como hoja solo en el nodo de producción
                for j, symbol in enumerate(rhs, start=1):
                    symbol_node_id = f"{prod_node_id}_sym_{j}"

                    if symbol.isupper():
                        # No terminal -> circulito azul como A
                        dot.node(
                            symbol_node_id,
                            label=symbol,
                            shape="circle",
                            style="filled",
                            fillcolor="#bbdefb",
                            color="#0d47a1"
                        )
                    else:
                        # Terminal -> texto simple
                        dot.node(
                            symbol_node_id,
                            label=symbol,
                            shape="plaintext"
                        )

                    # Conectar producción con cada símbolo (rama del árbol)
                    dot.edge(prod_node_id, symbol_node_id, color="#95a5a6")

    return dot

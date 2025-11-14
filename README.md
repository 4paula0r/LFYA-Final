# LFYA-Final
Proyecto FInal Lenguajes Formales y automatas
Documentación del Proyecto: Chomsky Classifier AI
1. Introducción
Este documento contiene la documentación técnica mínima necesaria para el proyecto 
“Chomsky Classifier AI”, el cual clasifica gramáticas formales según la Jerarquía de 
Chomsky, genera diagramas visuales, ejecuta modos tutor, permite comparaciones de 
gramáticas, conversión de regex a autómatas, y cuenta con una interfaz web en Streamlit.

2. Estructura del Proyecto
El proyecto está dividido en módulos para mantener una arquitectura organizada:
- main.py – Menú principal y flujo de control.
- grammar_parser.py – Lectura y procesamiento de reglas gramaticales.
- classifier.py – Clasificación en Tipo 0, 1, 2 o 3.
- visualizer.py – Generación de diagramas (Graphviz).
- tutor.py – Modo tutor / quiz.
- converters.py – Conversión Regex → AFD → Gramática.
- equivalence.py – Comparador heurístico de gramáticas.
- reportes.py – Generación de PDF.
- utils.py – Funciones auxiliares.

3. Descripción Detallada de Cada Módulo
• classifier.py:
  Encargado de clasificar gramáticas mediante reglas estructurales.
  Implementa verificaciones para:
   - Tipo 3 (Regular)
   - Tipo 2 (GLC)
   - Tipo 1 (CSG)
   - Tipo 0 (RE)

• grammar_parser.py:
  Interpreta el texto ingresado por el usuario, normaliza epsilon,
  admite varias líneas y comentarios.

• visualizer.py:
  Crea diagramas PNG usando Graphviz. Utiliza modelos circulares 
  para variables y rectangulares para producciones.

• tutor.py:
  Sistema de práctica que genera gramáticas aleatorias de cada 
  tipo y permite al usuario clasificarlas para reforzar teoría.

• converters.py:
  Convierte expresiones regulares a autómatas deterministas 
  (AFD) y luego a gramáticas regulares equivalentes.

• equivalence.py:
  Compara dos gramáticas generando cadenas hasta una longitud 
  máxima y detecta diferencias entre L1 y L2.

• reportes.py:
  Produce un archivo PDF con:
    - Gramática
    - Clasificación
    - Explicaciones
    - Diagrama embebido

4. Reglas de Clasificación
• Tipo 3 (Regular):
  A → aB | a | ε

• Tipo 2 (GLC):
  A → β
  donde A es variable simple.

• Tipo 1 (CSG):
  |α| ≤ |β| y ε solo permitido en S.

• Tipo 0 (Recursivamente enumerable):
  Sin restricciones especiales.

5. Diagrama del Flujo del Clasificador
1. Recibir gramática.
2. Probar Tipo 3.
3. Si falla → probar Tipo 2.
4. Si falla → probar Tipo 1.
5. Si falla → devolver Tipo 0.
6. Generar explicación y diagrama.

6. Interfaz Web Streamlit
Cuenta con secciones:
- Clasificación de gramáticas.
- Conversión Regex → AFD → Gramática.
- Comparación de gramáticas.
- Generación de PDFs.
- Visualización profesional.
7. Ejemplos de Prueba Incluidos
Tipo 3:
  S -> aS | b
Tipo 2:
  S -> aSb | ab
Tipo 1:
  S -> aS
  S -> aA
  A -> ab

Tipo 0:
  S -> SaS | b

8. Conclusión
Este proyecto cumple todos los requerimientos académicos de un clasificador 
de gramáticas según la Jerarquía de Chomsky, junto con módulos avanzados 
que amplían su funcionalidad a nivel profesional.

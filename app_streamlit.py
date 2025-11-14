# app_streamlit.py

import streamlit as st
from io import BytesIO
from grammar_parser import leer_gramatica
from classifier import clasificar
from visualizer import generar_diagrama_gramatica
from converters import regex_a_dfa_y_gramatica
from equivalence import comparar_gramaticas
from reportes import generar_reporte_pdf


st.set_page_config(page_title="Chomsky Classifier AI", page_icon="🤖")

st.title("🤖 Chomsky Classifier AI")
tabs = st.tabs(["Clasificar", "Regex → Gramática", "Comparar", "PDF"])


# TAB 1
with tabs[0]:
    st.subheader("Clasificar Gramática")
    texto = st.text_area("Gramática:", "S -> aSb | ab")

    if st.button("Clasificar"):
        start, reglas = leer_gramatica(texto)
        tipo_id, tipo_nombre, razones = clasificar(start, reglas)
        st.success(f"{tipo_nombre}")

        for r in razones:
            st.write("-", r)

        dot = generar_diagrama_gramatica(reglas, start_symbol=start)
        st.image(dot.pipe("png"))


# TAB 2
with tabs[1]:
    regex = st.text_input("Regex:", "(a|b)*abb")

    if st.button("Convertir Regex"):
        dfa, start, reglas = regex_a_dfa_y_gramatica(regex)
        st.write("Gramática generada:")
        for A, rhss in reglas.items():
            st.write(A, "->", " | ".join(rhss))
        dot = generar_diagrama_gramatica(reglas, start_symbol=start)
        st.image(dot.pipe("png"))


# TAB 3
with tabs[2]:
    g1 = st.text_area("Gramática 1:", "S -> aSb | ab")
    g2 = st.text_area("Gramática 2:", "S -> aA\nA -> b | aAb")
    max_len = st.slider("Longitud", 1, 6, 4)

    if st.button("Comparar"):
        res = comparar_gramaticas(g1, g2, max_len)
        st.write("Solo en L1:", res["solo_L1"])
        st.write("Solo en L2:", res["solo_L2"])


# TAB 4
with tabs[3]:
    gr = st.text_area("Gramática:", "S -> aSb | ab")
    name = st.text_input("Nombre PDF:", "reporte.pdf")

    if st.button("Generar PDF"):
        start, reglas = leer_gramatica(gr)
        tipo_id, tipo_nombre, razones = clasificar(start, reglas)
        dot = generar_diagrama_gramatica(reglas, start_symbol=start)

        buffer = BytesIO()
        generar_reporte_pdf(
            buffer, start, reglas, f"{tipo_nombre} (Tipo {tipo_id})",
            razones, dot.pipe("png")
        )
        buffer.seek(0)

        st.download_button("Descargar", buffer, file_name=name)

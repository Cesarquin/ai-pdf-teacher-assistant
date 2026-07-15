import streamlit as st


st.title("AI PDF Teacher Assistant")

st.write(
    "Asistente inteligente para ayudar a docentes "
    "a analizar documentos."
)

nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.success(f"Bienvenido {nombre}")
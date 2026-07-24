import streamlit as st
import fitz

st.title("AI PDF Teacher Assistant")

st.write(
    "Asistente inteligente para ayudar a docentes "
    "a analizar documentos."
)

nombre = st.text_input("Escribe tu nombre")
asignatura = st.text_input("Asignatura:")
grado = st.text_input("Grado:")

if nombre and asignatura and grado:
    st.success(
        f"""
        Bienvenido {nombre}

        Asignatura: {asignatura}

        Grado: {grado}
        """
    )

    archivo = st.file_uploader(
        "Selecciona un archivo PDF",
        type=["pdf"]
    )

    if archivo:
        st.write(archivo.name)
        st.write(archivo.type)

        contenido_binario = archivo.getvalue()

        try:
            documento = fitz.open(
                stream=contenido_binario,
                filetype="pdf"
            )

            st.write(f"El documento tiene {documento.page_count} páginas.")

            primera_pagina = documento.load_page(0)
            texto = primera_pagina.get_text()

            st.subheader("Vista previa")
            st.write(texto[:500])
            documento.close()

        except Exception as e:
            st.error(f"Error al abrir el documento: {e}")
import streamlit as st
from pdf_reader import leer_pdf


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

        resultado = leer_pdf(archivo)

        if resultado["error"]:
            st.error(resultado["error"])
        else:
            st.write(
                f"El documento tiene {resultado['paginas']} páginas."
            )

            st.subheader("Vista previa")
            st.write(resultado["texto"])
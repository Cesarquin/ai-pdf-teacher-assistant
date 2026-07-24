import fitz


def leer_pdf(archivo):
    try:
        contenido_binario = archivo.getvalue()

        documento = fitz.open(
            stream=contenido_binario,
            filetype="pdf"
        )

        primera_pagina = documento.load_page(0)

        texto = primera_pagina.get_text()

        return {
            "paginas": documento.page_count,
            "texto": texto[:500],
            "error": None
        }

    except Exception as e:
        return {
            "paginas": 0,
            "texto": "",
            "error": f"Error al abrir el documento: {e}"
        }
import os

import docx2txt
import pandas as pd
import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader


@st.cache_data
def cargar_imagen(image_file):
    img = Image.open(image_file)
    return img


def leer_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.page)
    todo_el_texto = ""
    for i in range(count):
        pagina = pdfReader.page[i]
        todo_el_texto += pagina.extract_text()
        return todo_el_texto

def guardar_archivo(uploadefile):
    #crear el archivo si no existe
    if not os.path.exists("temp"):
        os.makedirs("temp")

    #guardar el archivo en el directorio
    with open(os.path.join("temp", uploadefile.name), "wb") as f:
        f.write(uploadefile.getbuffer())
        return  st.success("archivo guardado :{} en temp".format(uploadefile.name))




def main():
    st.title("tutorial de carga de archivos")
    menu = ["Imagenes", "Conjunto De Datos", "Archivos De Documentos"]
    eleccion = st.sidebar.selectbox("Menu", menu)

    if eleccion == "Imagenes":
        st.subheader("imagen")
        archivo_imagen = st.file_uploader("Subir Imagen", type=["png", "jpg", "jpeg"])
        if archivo_imagen is not None:
            detalles_archivo = {"nombre_archivo": archivo_imagen.name,
                                "tipo_archivo": archivo_imagen.type,
                                "tamaño_archivo": archivo_imagen.size}

            st.write(detalles_archivo)
            st.image(cargar_imagen(archivo_imagen), width=250)
            guardar_archivo(archivo_imagen)










    elif eleccion == "Conjunto De Datos":
        st.subheader("conjunto de datos")
        archivo_datos = st.file_uploader("Subir CVS", type=["cvs", "xlsx"])
        if archivo_datos is not None:
            detalles_archivo = {"nombre_archivo": archivo_datos.name,
                                "tipo_archivo": archivo_datos.type,
                                "tamaño_archivo": archivo_datos.size}

            st.write(detalles_archivo)
            if detalles_archivo["tipo_archivo"] == "text/csv":
                df = pd.read_csv("archivo_datos")
            elif detalles_archivo[
                "tipo_archivo"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(archivo_datos)
            else:
                df = pd.DataFrame()
            st.dataframe(df)
            guardar_archivo(archivo_datos)





    elif eleccion == "Archivos De Documentos":
        st.subheader("Archivo De Documentos")
        archivo_doc = st.file_uploader("subir documento", type=["pdf", "docx", "txt"])
        if st.button("procesar"):
            if archivo_doc is not None:
                detalles_archivo = {"nombre_archivo": archivo_doc.name,
                                    "tipo_archivo": archivo_doc.type,
                                    "tamaño_archivo": archivo_doc.size}
                st.write(detalles_archivo)

                if archivo_doc.type == "tex/plain":
                    texto = str(archivo_doc.read(), "utf-8")
                    st.text(texto)
                elif archivo_doc.type == "application/pdf":
                    texto = leer_pdf(archivo_doc)
                    st.write(texto)
                elif archivo_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    texto = docx2txt.process(archivo_doc)
                    st.write(texto)

                guardar_archivo(archivo_doc)





if __name__ == "__main__":
    main()

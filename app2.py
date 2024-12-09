import streamlit as st
import os
from PyPDF2 import PdfReader
import docx2txt
from PIL import Image
import plotly.express as px
import pandas as pd
from info import cargar_partidos
from Comentarios import come
from posiciones import pos
from foto import bio
from video import vid
from archivos import carga
from preguntas2 import pre



img = Image.open("data/logo.jpg")

st.set_page_config(page_title="BEISBOL INVERNAL", page_icon= img, layout="wide")

def main():
    st.title("BEISBOL INVERNAL")
    menu = ["Pagina principal", "Calendario", "Pocisiones" , "Fotos", "Videos", "Cargar Archivos", "Encuentas", "Comentarios"]
    barra = st.sidebar.selectbox("Menu", menu)
    img = Image.open("data/logo.jpg")
    st.image(img, use_container_width=True)

    if barra == "Pagina principal":
        st.subheader("noticias y mas")
        st.write("Esta pagina esta creada por CESAR Y LEURIS, para las informaciones sobre beisbol"
                 " ayudanos a mejor y traerte mas noticias y mas sobre el beisbol no solo se tratara"
                 "de beisbol tambien te traeremos NBA,MLB Y MUCHOS DEPORTES MAS.....")

    elif barra == "Calendario":
        cargar_partidos()
    elif barra == "Pocisiones":
        pos()
    elif barra == "Fotos":
        bio()
    elif barra == "Videos":
        vid()
    elif barra == "Cargar Archivos":
        carga()
    elif barra == "Encuentas":
        pre()
    elif barra == "Comentarios":
        st.subheader("Dejanos tus Comentarios")
        come()























if __name__ == "__main__":
        main()


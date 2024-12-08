import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

def come():
    st.subheader("ayudanos a mejorar")
    nombre = st.text_input("ingresa tu usernames...")
    st.write(nombre)
    mensaje = st.text_area("comentanos....", height=800)
    st.write(mensaje)
    return st.success("Gracias por tu comentario:{}".format(mensaje) + (nombre))

if __name__ == "__main__":
    come()
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

def come():
    nombre = st.text_input("ingresa tu usernames...")
    st.write(nombre)
    st.write("Por favor, responde a las siguientes preguntas:")
    opciones_servicio = ['Excelente', 'Bueno', 'Regular', 'Malo']
    respuesta_servicio = st.radio('¿Cómo calificarías nuestro servicio?', opciones_servicio)
    frecuencia_servicio = st.selectbox('¿Con qué frecuencia usas nuestro servicio?',
                                       ['Diariamente', 'Semanalmente', 'Mensualmente', 'Rara vez'])

    mejora = st.text_area('¿Te gustaría sugerir alguna mejora?')

    if st.button('Enviar'):
        # Mostrar las respuestas del usuario al enviar
        st.write('Gracias por tu participación. Aquí están tus respuestas:')
        st.write(f'1. Calificación del servicio: {respuesta_servicio}')
        st.write(f'2. Frecuencia de uso: {frecuencia_servicio}')
        if mejora:
            st.write(f'3. Sugerencias de mejora: {mejora}')
        else:
            st.write('3. No se proporcionaron sugerencias de mejora.')
    mensaje = st.text_area("comentanos....", height=800)
    st.write(mensaje)
    return st.success("Gracias por tu comentario:{}".format(mensaje) + (nombre))

if __name__ == "__main__":
    come()
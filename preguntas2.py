

import streamlit as st

def pre():
    st.title("Encuesta sobre Béisbol Invernal")

    preguntas = [
        "¿Cuál es tu equipo favorito en la liga invernal?",
        "¿Qué jugador crees que ha tenido el mejor rendimiento esta temporada?",
        "¿Qué aspectos del béisbol invernal te parecen más emocionantes: la estrategia del juego o la habilidad individual de los jugadores?",
        "¿Cuál ha sido el partido más memorable que has visto en la liga invernal?",
        "¿Qué opinas sobre las nuevas reglas implementadas en la liga esta temporada?",
        "¿Cómo crees que afecta la agencia libre a la competitividad de los equipos?",
        "¿Qué jugador dominicano crees que ha dejado una huella más profunda en la historia del béisbol invernal?",
        "¿Cuál es tu recuerdo favorito relacionado con el béisbol invernal?",
        "¿Qué importancia tiene el béisbol invernal en la cultura dominicana?",
        "¿Cómo te sientes acerca de la cobertura mediática del béisbol invernal?",
        "¿Qué cambios te gustaría ver en la liga para mejorar la experiencia de los fanáticos?",
        "¿Cuál es tu pronóstico para la próxima temporada en términos de equipos y jugadores destacados?",
        "¿Qué impacto crees que tiene el béisbol invernal en el desarrollo de jóvenes talentos en la República Dominicana?"
    ]

    with st.form(key='encuesta'):
        respuestas = []
        for pregunta in preguntas:
            respuesta = st.text_input(pregunta)
            respuestas.append(respuesta)

        submit_button = st.form_submit_button(label='Enviar Respuestas')

    if submit_button:
        st.success("¡Gracias por participar en la encuesta!")
        # Aquí podrías guardar las respuestas en un archivo o base de datos
        for i, respuesta in enumerate(respuestas):
            st.write(f"Pregunta {i + 1}: {respuesta}")



if __name__ == "__main__":
    pre()
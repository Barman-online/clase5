import streamlit as st
import pandas as pd

def cargar_partidos():
    st.subheader("Calendario temp regular")
    df = pd.read_csv("data/mache.csv")
    st.dataframe(df)

if __name__ == "__main__":
    cargar_partidos()

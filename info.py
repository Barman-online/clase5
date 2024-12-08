import streamlit as st
import pandas as pd

df = pd.read_csv("data/mache.csv")

def cargar_partidos():
    st.subheader("Calendario temp regular")
    st.dataframe(df)
    st.table(df)








if __name__ == "__main__":
    cargar_partidos()

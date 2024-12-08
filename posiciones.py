import streamlit as st
import pandas as pd

def pos():
    st.subheader("TABLA DE POSICIONES")
    df = pd.read_csv("data/posici.csv")
    st.dataframe(df)


if __name__ == "__main__":
    pos()
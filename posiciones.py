import streamlit as st
import pandas as pd
from numpy.f2py.f90mod_rules import fgetdims2


def pos():
    st.subheader("TABLA DE POSICIONES")
    df = pd.read_csv("data/posici.csv")
    st.dataframe(df)
    st.table(df)

if __name__ == "__main__":
    pos()
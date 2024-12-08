import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd


img = Image.open("data/logo.jpg")

st.set_page_config(page_title="Besiboll Invernal", page_icon= img, layout="wide")

def main():
    st.title("BEISBOLL INVERNAL")
    img = Image.open("data/logo.jpg")
    st.image(img, use_container_width=True)
    st.header("calendario oficial")
    df = pd.read_csv("calendario.csv")
    st.dataframe(df)












if __name__ == "__main__":
    main()

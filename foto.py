import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd


def bio():
    st.header("fotos..")
    imag = Image.open("data/proxy-image.jpg")
    st.image(imag, use_container_width=800)
    imag1 = Image.open("data/proxy-image1.jpg")
    st.image(imag1, use_container_width=800)
    imag2 = Image.open("data/proxy-image (2).jpg")
    st.image(imag2, use_container_width=800)
    imag3 = Image.open("data/proxy-image (3).jpg")
    st.image(imag3, use_container_width=800)
    imag4 = Image.open("data/proxy-image (4).jpg")
    st.image(imag4, use_container_width=800)
    imag5 = Image.open("data/proxy-image (5).jpg")
    st.image(imag5, use_container_width=800)
    imag6 = Image.open("data/proxy-image (6).jpg")
    st.image(imag6, use_container_width=800)
    imag7 = Image.open("data/proxy-image (7).jpg")
    st.image(imag7, use_container_width=800)
    imag8 = Image.open("data/proxy-image (8).jpg")
    st.image(imag8, use_container_width=800)
    imag9 = Image.open("data/proxy-image (9).jpg")
    st.image(imag9, use_container_width=800)


if __name__ == "__main__":
    bio()


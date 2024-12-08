import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd


def vid():

    with open("data/video1.mp4", "rb") as video_file:
        st.video(video_file.read(), start_time=0)

    with open("data/2024.mp4", "rb") as video_file:
        st.video(video_file.read(), start_time=0)

    with open("data/video2.mp4", "rb") as video_file:
        st.video(video_file.read(), start_time=0)

    with open("data/video3.mp4", "rb") as video_file:
        st.video(video_file.read(), start_time=0)

    with open("data/video5.mp4", "rb") as video_file:
        st.video(video_file.read(), start_time=0)












if __name__ == "__main__":
    vid()
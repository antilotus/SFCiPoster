import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="Videos", layout="wide")

st.title("Videos")
st.header('TMT escaping the binding site')
video_file2 = open("Media/TMTescapes.mp4", "rb")
video_bytes2 = video_file2.read()
st.video(video_bytes2)
st.sidebar.page_link("app.py", label="Home")

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
st.sidebar.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges")
#st.sidebar.page_link("pages/2_Videos.py", label="Videos")
st.sidebar.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation")
st.sidebar.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods")
st.sidebar.page_link("pages/5_The_Poster_itself.py")

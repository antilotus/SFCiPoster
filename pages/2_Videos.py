import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="Videos", layout="wide")

st.title("Videos")
st.header('TMT escaping the binding site')
video_file2 = open("Media/TMTescapes.mp4", "rb")
video_bytes2 = video_file2.read()
st.video(video_bytes2)
st.markdown('**Video S1.** MD run showing TMT leaving the binding pocket, within 30 ns')
st.header('Acetophenone in the binding site')
video_file3 = open("Media/acetostays.mp4", "rb")
video_bytes3 = video_file3.read()
st.video(video_bytes3)
st.markdown('**Video S2.** MD run showing acetophenone staying in the binding pocket, 100 ns long')
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges")
#st.sidebar.page_link("pages/2_Videos.py", label="Videos")
st.sidebar.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation")
st.sidebar.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods")
st.sidebar.page_link("pages/5_The_Poster_itself.py")
st.sidebar.page_link("pages/6_Single_Point_Energies.py")

import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="ChargesallQM", layout="wide")

st.title("All QM region heatmaps")

st.header('Natural Population Analysis Charges all QM atoms')
video_file = open("Media/NPAfullqm.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
st.image('Media/NBOcharges_colorbar.png', width=1200)
st.header('Mulliken Charges all QM atoms')
video_file1 = open("Media/Mullikenfullqm.mp4", "rb")
video_bytes1 = video_file1.read()
st.video(video_bytes1)
st.image('Media/mulliken_colorbar.png', width=1200)
st.sidebar.page_link("app.py", label="Home")
#st.sidebar.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges")
st.sidebar.page_link("pages/2_Videos.py", label="Videos")
st.sidebar.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation")
st.sidebar.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods")
st.sidebar.page_link("pages/5_The_Poster_itself.py")

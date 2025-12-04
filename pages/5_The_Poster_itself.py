import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="Poster", layout="wide")

st.title("My SFCi poster")

st.pdf("Media/POSTER_Thorhallsson_ICN.pdf", height="stretch")
st.sidebar.page_link("app.py", label="Home")

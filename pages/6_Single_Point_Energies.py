import streamlit as st
import pandas as pd

st.set_page_config(page_title="SPE", layout="wide")

st.title("Single point energies of snapshots")
SPEframe = pd.read_table('../Media/SPE.dat', sep=r"\s+", header=None, names=["Snapshot nr.", "Energy (QM/MM)"])
st.dataframe(SPEframe)

st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges")
st.sidebar.page_link("pages/2_Videos.py", label="Videos")
st.sidebar.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation")
st.sidebar.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods")
st.sidebar.page_link("pages/5_The_Poster_itself.py")
#st.sidebar.page_link("pages/6_Single_Point_Energies.py")

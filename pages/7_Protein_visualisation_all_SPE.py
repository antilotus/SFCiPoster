import streamlit as st
import py3Dmol
import os
import glob

st.set_page_config(page_title="All SPE vis", layout="wide")

st.title("Visulisation of AgOR28 with TMT bound all SPE")

# Path to your local PDB file
pdbs = glob.glob("Media/*.pdb")
pdbs_sorted = sorted(pdbs)

def display_protein(pdb_path):
    if os.path.exists(pdb_path):
        with open(pdb_path, "r") as f:
            pdb_data = f.read()

        # Load and visualize the PDB
        view = py3Dmol.view(width=800, height=500)
        view.addModel(pdb_data, "pdb")
    
        # Show full protein in cartoon
        view.setStyle({'cartoon': {'color': 'white'}})
    
        # Optional: zoom to whole protein first (you can adjust this)
        view.zoomTo()
    
        # Zoom to specific resnames (only if they exist)
        view.setStyle({'resn': 'LIG'}, {'stick': {'colorscheme': 'GreyCarbon'}})
        #view.setStyle({'resn': 'NPH'}, {'stick': {'colorscheme': 'GreenCarbon'}})
    
        view.addLabel("TMT", {
            'position': {'resn': "LIG"},
            'backgroundColor': 'blue',
            'fontColor': 'black',
            'fontSize': 12
        })
    
        # Licorice for specific residue numbers
        highlight_residues = [1466,1490,1493,1494,1497,1562,1589,1614,1617,1618,1621,1725]
        for resid in highlight_residues:
            view.setStyle({'resi': str(resid)}, {'stick': {'colorscheme': 'RedCarbon'}})
            view.addLabel(f"Resid {resid}", {
                'position': {'resi': str(resid)},
                'backgroundColor': 'white',
                'fontColor': 'red',
                'fontSize': 10
            })
    
        # Set orientation manually (rotation in degrees)
        view.rotate(0, 'x')
        view.rotate(0, 'y')
        view.rotate(0, 'z') 
        view.zoomTo({'or': [
            {'resn': 'LIG'},
            {'resi': [str(r) for r in highlight_residues]}
        ]})
    
        view.setBackgroundColor('white')
        st.components.v1.html(view._make_html(), height=500)
    
    else:
        st.error(f"PDB file not found at: {pdb_path}")

st.header("SPE1")
display_protein(pdbs_sorted[0])
st.header("SPE2 lowest energy")
display_protein(pdbs_sorted[9])
st.header("SPE3")
display_protein(pdbs_sorted[10])
st.header("SPE4")
display_protein(pdbs_sorted[11])
st.header("SPE5")
display_protein(pdbs_sorted[12])
st.header("SPE6")
display_protein(pdbs_sorted[13])
st.header("SPE7")
display_protein(pdbs_sorted[14])
st.header("SPE8")
display_protein(pdbs_sorted[15])
st.header("SPE9")
display_protein(pdbs_sorted[16])
st.header("SPE10")
display_protein(pdbs_sorted[1])
st.header("SPE11")
display_protein(pdbs_sorted[2])
st.header("SPE12")
display_protein(pdbs_sorted[3])
st.header("SPE13")
display_protein(pdbs_sorted[4])
st.header("SPE14")
display_protein(pdbs_sorted[5])
st.header("SPE15")
display_protein(pdbs_sorted[6])
st.header("SPE16")
display_protein(pdbs_sorted[7])
st.header("SPE17")
display_protein(pdbs_sorted[8])

st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges")
st.sidebar.page_link("pages/2_Videos.py", label="Videos")
st.sidebar.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation")
st.sidebar.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods")
st.sidebar.page_link("pages/5_The_Poster_itself.py")
st.sidebar.page_link("pages/6_Single_Point_Energies.py")
#st.sidebar.page_link("pages/7_Protein_visualisation_all_SPE.py")

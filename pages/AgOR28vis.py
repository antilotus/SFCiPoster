import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="AgVis", layout="wide")

st.title("AgOR28 with TMT bound")

# Path to your local PDB file
pdb_path = "../Media/SPE2.pdb"

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

    #view.addLabel("NPH", {
    #    'position': {'resn': 'NPH'},
    #    'backgroundColor': 'blue',
    #    'fontColor': 'blue',
    #    'fontSize': 12
    #})
    # view.zoomTo({'resn': ['DHK', 'NPH']})

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

st.page_link("app.py", label="Home")

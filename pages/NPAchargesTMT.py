from rdkit import Chem
from rdkit.Chem import Draw
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable, get_cmap
from rdkit_heatmaps import mapvalues2mol
from rdkit_heatmaps.utils import transform2png
import streamlit as st
st.set_page_config(page_title="NPA charges", layout="wide")
st.title("NPA charges")

# the molecule I want to draw the heatmap on
test_mol = Chem.MolFromSmiles("Cc1nc(C)c(C)s1")
test_mol = Draw.PrepareMolForDrawing(test_mol)
# only the 2nd column is of interest
charges = np.loadtxt("NBO.txt",usecols=(2))
revcharges = charges[::-1]
sepcharges = np.split(revcharges,18)
# --- Define colormap normalization ---
vmin = np.min(charges)
vmax = np.max(charges)
cmap = get_cmap("bwr")
norm = Normalize(vmin=vmin, vmax=vmax)

imgs = []  # empty list to store images

for i, snaps in enumerate(sepcharges):
    # Draw RDKit heatmap
    canvas = mapvalues2mol(test_mol, snaps)
    img = transform2png(canvas.GetDrawingText())
    imgs.append(img)

# Combine molecule image with colorbar
fig, ax = plt.subplots(figsize=(3, 3))
ax.imshow(imgs)
ax.axis("off")

# Add colorbar beside the molecule
sm = ScalarMappable(norm=norm, cmap=cmap)
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04, orientation='horizontal')
cbar.set_label("NPA charge")
plt.tight_layout()
plt

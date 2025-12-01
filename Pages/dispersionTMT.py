from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import SimilarityMaps
from rdkit.Chem import rdMolDescriptors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable, get_cmap
import streamlit as st
from rdkit_heatmaps import mapvalues2mol
from rdkit_heatmaps.utils import transform2png
import glob

files = glob.glob("*.atomwise.txt")
# the molecule I want to draw the heatmap on
test_mol = Chem.MolFromSmiles("Cc1nc(C)c(C)s1")
test_mol = Draw.PrepareMolForDrawing(test_mol)
A = []
for fname in files:
    inf_from_every_file = np.loadtxt(fname, usecols=(4))
    A.append(inf_from_every_file)

vmin = np.min(A)
vmax = np.max(A)
cmap = get_cmap("PiYG")
norm = Normalize(vmin=vmin, vmax=vmax)

imgs = []  # empty list to store images

for i, snaps in enumerate(A):
    weights = np.array(snaps, dtype=float).flatten().tolist()
    d = Draw.MolDraw2DCairo(800, 800)
    SimilarityMaps.GetSimilarityMapFromWeights(test_mol,weights,draw2d=d,colorMap=cmap)
    d.FinishDrawing()

    img = transform2png(d.GetDrawingText())

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


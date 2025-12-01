from rdkit import Chem
from rdkit.Chem import Draw
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable, get_cmap
import streamlit as st
import py3Dmol

st.set_page_config(page_title="NPA charges", layout="wide")
st.title("NPA charges")
"""
As there is an issue with trying to pip install this package I simply did a git clone and then cp the rdkit_heatmap folder into the directory I am working in. It is not a very good fix but it is fine for just trying the package
"""
from rdkit_heatmaps import mapvalues2mol
from rdkit_heatmaps.utils import transform2png

"""
In my case I had many files with charges that I wanted to use and so
to get the mull charges, I simply reverse cat the outputfiles and grep the charges I am interested in
for i in *.log
do tac $i | grep 'Summary of Natural Population Analysis' -m 1 -B13 >> NBO.txt
done
"""
# the molecule I want to draw the heatmap on
test_mol = Chem.MolFromSmiles("Cc1nc(C)c(C)s1")
test_mol = Draw.PrepareMolForDrawing(test_mol)
# only the 2nd column is of interest
charges = np.loadtxt("NBO.txt",usecols=(2))
"""
An to make sure that my charges are in the same order as the atoms drawn by rdkit I used this to print out the order
I basically revealed that the atoms are in the same order as in the output file, which makes sense as I used obabel to turn the smile into the coords
"""
# for atom in test_mol.GetAtoms():
#
#   print(atom.GetSymbol())
"""
Here I reverse the reverse and then split the array into as many parts as the files I had in the beginning
"""
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

    #plt.savefig(f"NBOcharges_frame_{i}.png", dpi=600)
    #plt.close(fig)

    #imgs.append(transform2png(open(f"NBOcharges_frame_{i}.png", "rb").read()))


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

import streamlit as st

st.set_page_config(page_title="Thesis Portal", layout="wide")

st.title("🎓 Welcome to the SFCi poster ESI")
#st.markdown("### 🔍 Explore a Topic:")

# Uniform image display size (e.g., 250px height)
IMAGE_HEIGHT = 250

# Helper to make consistent tile layout
def display_tile(image_path, link_path, label, height=IMAGE_HEIGHT):
    st.image(image_path,  output_format="auto", caption="", clamp=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)  # vertical spacing
    st.page_link(link_path, label=label)

# ---- Tile Layout ----
col1, col2, col3 = st.columns(3)

with col1:
    display_tile("NBOcharges_frame_10.png", "pages/NPAchargesTMT.py", " NPA Charges")

with col2:
    display_tile("disp_frame_10.png", "pages/NPAchargesTMT.py", " ADLD")

with col3:
    display_tile("charges_frame_10.png", "pages/NPAchargesTMT.py", " Mulliken Charges")

<<<<<<< HEAD
# Path to your local PDB file
pdb_path = "./Media/SPE2.pdb"
=======
# ---- Contact Section ----
st.header("📬 Contact")
>>>>>>> 0a5ca80 (Fixing first commit)

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send Email")

<<<<<<< HEAD
    # Show full protein in cartoon
    view.setStyle({'cartoon': {'color': 'white'}})

    # Optional: zoom to whole protein first (you can adjust this)
    view.zoomTo()

    # Zoom to specific resnames (only if they exist)
    view.setStyle({'resn': 'LIG'}, {'stick': {'colorscheme': 'greenCarbon'}})
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
        view.setStyle({'resi': str(resid)}, {'stick': {'colorscheme': 'BlueCarbon'}})
        view.addLabel(f"Resid {resid}", {
            'position': {'resi': str(resid)},
            'backgroundColor': 'white',
            'fontColor': 'red',
            'fontSize': 10
        })





    # Set orientation manually (rotation in degrees)
    view.rotate(-220, 'x')
    view.rotate(-40, 'y')
    view.rotate(-160, 'z') 
    view.zoomTo({'or': [
        {'resn': 'LIG'},
        {'resi': [str(r) for r in highlight_residues]}
    ]})

    view.setBackgroundColor('white')
    st.components.v1.html(view._make_html(), height=500)


else:
    st.error(f"PDB file not found at: {pdb_path}")





# --- Section 5: Video ---
#st.header("Video")
#st.video("../media.mp4",autoplay=True)  # Supports local or URL path

# --- Section 6: Markdown and Uploads ---
# st.header("Upload & Notes")
# uploaded_file = st.file_uploader("Upload a CSV file")
# if uploaded_file:
#     df_uploaded = pd.read_csv(uploaded_file)
#     st.write("Uploaded Data Preview:")
#     st.dataframe(df_uploaded)

# st.markdown("""
# ### Notes
# - You can use this portal to showcase results dynamically.
# - Combine static images with interactive elements.
# - Perfect for defending or sharing complex bioinformatics visualizations.
# """)
=======
    if submitted:
        mailto_link = f"mailto:Albert.THORHALLSSON@univ-cotedazur.fr?subject={subject}&body=From: {name} ({email})%0A%0A{message}"
        st.markdown(f"[📨 Click here to send via your email client]({mailto_link})", unsafe_allow_html=True)
>>>>>>> 0a5ca80 (Fixing first commit)

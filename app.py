import streamlit as st

st.set_page_config(page_title="SFCi poster ESI", layout="wide")

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
    display_tile("charges_frame_10.png", "pages/AgOR28vis.py", " Mulliken Charges")
    
# ---- Contact Section ----
st.header("📬 Contact")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send Email")

    if submitted:
        mailto_link = f"mailto:Albert.THORHALLSSON@univ-cotedazur.fr?subject={subject}&body=From: {name} ({email})%0A%0A{message}"
        st.markdown(f"[📨 Click here to send via your email client]({mailto_link})", unsafe_allow_html=True)

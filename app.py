import streamlit as st

st.set_page_config(page_title="SFCi poster ESI", layout="wide")

st.title("🎓 Welcome to the SFCi poster ESI")

# Uniform image display size (e.g., 250px height)
IMAGE_HEIGHT = 250

st.header('Natural Population Analysis Charges')
st.image('Media/NBO.gif')
st.header('Atomic Decomposition of London Dispersion')
st.image('Media/dispersion.gif')
st.header('Mulliken Analysis Charges')
st.image('Media/mullikencharges.gif')
st.header('Mulliken Analysis Charges (all QM atoms)')
st.image('Media/mullikenallqmwcolorbar.gif')

st.write('(1) Zhao, J.; Chen, A. Q.; Ryu, J.; del Mármol, J. Structural Basis of Odor Sensing by Insect Heteromeric Odorant Receptors. Science 2024, 384 (6703), 1460–1467. https://doi.org/10.1126/science.adn6384.')

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

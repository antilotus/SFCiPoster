import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="Home", layout="wide")

st.title("🎓 Welcome to the my SFCi poster ESI")
st.header('By Albert Thor Thorhallson')

st.subheader('Natural Population Analysis Charges')
st.image('Media/NBO.gif')
st.image('Media/NBOcharges_colorbar.png', width=800)
st.subheader('Atomic Decomposition of London Dispersion')
st.image('Media/dispersion.gif', width=500)
st.image('Media/disp_colorbar.png', width=500)
st.subheader('Mulliken Analysis Charges')
st.image('Media/mullikencharges.gif')
st.image('Media/mulliken_colorbar.png', width=800)

st.sidebar.page_link("pages/AgOR28vis.py")
st.sidebar.page_link("pages/NPAallQM.py")
st.sidebar.page_link("pages/references.py")
st.sidebar.page_link("pages/videos.py")

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
        

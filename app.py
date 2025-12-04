import streamlit as st
import py3Dmol
import os

st.set_page_config(page_title="Home", layout="wide")

st.title(":material/source_notes: Welcome to my SFCi poster ESI")
st.header('By Albert Thor Thorhallson')

st.subheader('Natural Population Analysis Charges')
st.image('Media/NBO.gif')
st.image('Media/NBOcharges_colorbar.png', width=800)
st.markdown('**Figure S1.** First frame is the RESP derived charges followed by NPA of 17 SPE snapshots')

st.subheader('Atomic Decomposition of London Dispersion')
st.image('Media/dispersion.gif', width=500)
st.image('Media/disp_colorbar.png', width=500)
st.markdown('**Figure S2.** Dispersion stabilization of each atom of TMT in the protein environment')

st.subheader('Mulliken Analysis Charges')
st.image('Media/mullikencharges.gif')
st.image('Media/mulliken_colorbar.png', width=800)
st.markdown('**Figure S3.** Mulliken charges of the 17 SPE snapshots')

#st.sidebar.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges")
#st.sidebar.page_link("pages/2_Videos.py", label="Videos")
#st.sidebar.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation")
#st.sidebar.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods")
#st.sidebar.page_link("pages/5_The_Poster_itself.py")
st.subheader('Further information:')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("pages/1_All_QM_atom_charges.py", label="All QM atom charges", icon=":material/ev_shadow_minus:")

with col2:
    st.page_link("pages/2_Videos.py", label="Videos", icon=":material/video_library:")

with col3:
    st.page_link("pages/3_Protein_visualisation.py", label="Protein visualisation", icon=":material/genetics:", help="Warning, slow and doesn't work on mobile")

with col4:
    st.page_link("pages/4_Detailed_methods_and_references.py", label="Detailed methods and references", icon=":material/book_ribbon:")

st.page_link("pages/5_The_Poster_itself.py", icon=":material/picture_as_pdf:")

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
        

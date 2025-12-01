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

st.header('References')
st.write('(1) WHO. 2024. Global strategic preparedness, readiness and response plan for dengue and other Aedes-borne arbovirus')
st.write('(2) Zhao, J.; Chen, A. Q.; Ryu, J.; del Mármol, J. Structural Basis of Odor Sensing by Insect Heteromeric Odorant Receptors. Science 2024, 384 (6703), 1460–1467. https://doi.org/10.1126/science.adn6384.')
st.write('(3) Wang, Y.; Qiu, L.; Wang, B.; Guan, Z.; Dong, Z.; Zhang, J.; Cao, S.; Yang, L.; Wang, B.; Gong, Z.; Zhang, L.; Ma, W.; Liu, Z.; Zhang, D.; Wang, G.; Yin, P. Structural Basis for Odorant Recognition of the Insect Odorant Receptor OR-Orco Heterocomplex. Science 2024, 384 (6703), 1453–1460. https://doi.org/10.1126/science.adn6881.')
st.write('(4) Wang, G.; Carey, A. F.; Carlson, J. R.; Zwiebel, L. J. Molecular Basis of Odor Coding in the Malaria Vector Mosquito Anopheles Gambiae. Proceedings of the National Academy of Sciences 2010, 107 (9), 4418–4423. https://doi.org/10.1073/pnas.0913392107.')
st.write('(5) Xia, Y.; Wang, G.; Buscariollo, D.; Pitts, R. J.; Wenger, H.; Zwiebel, L. J. The Molecular and Cellular Basis of Olfactory-Driven Behavior in Anopheles Gambiae Larvae. Proceedings of the National Academy of Sciences 2008, 105 (17), 6433–6438. https://doi.org/10.1073/pnas.0801007105.')
st.write('(6) Olsson, M. H. M.; Søndergaard, C. R.; Rostkowski, M.; Jensen, J. H. PROPKA3: Consistent Treatment of Internal and Surface Residues in Empirical pKa Predictions. ACS Publications. https://doi.org/10.1021/ct100578z.')
st.write('(7) Schott-Verdugo, S.; Gohlke, H. PACKMOL-Memgen: A Simple-To-Use, Generalized Workflow for Membrane-Protein–Lipid-Bilayer System Building. Journal of Chemical Information and Modeling 2019. https://doi.org/10.1021/acs.jcim.9b00269.')
st.write('(8) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D.; Impey, R. W.; Klein, M. L. Comparison of Simple Potential Functions for Simulating Liquid Water. J. Chem. Phys. 1983, 79 (2), 926–935. https://doi.org/10.1063/1.445869.')
st.write('(9) Tian, C.; Kasavajhala, K.; Belfon, K. A. A.; Raguette, L.; Huang, H.; Migues, A. N.; Bickel, J.; Wang, Y.; Pincay, J.; Wu, Q.; Simmerling, C. ff19SB: Amino-Acid-Specific Protein Backbone Parameters Trained against Quantum Mechanics Energy Surfaces in Solution. Journal of Chemical Theory and Computation 2019. https://doi.org/10.1021/acs.jctc.9b00591.')
st.write("""
(10) Gaussian 16, Revision A.03,
 M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria,
 M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone,
 G. A. Petersson, H. Nakatsuji, X. Li, M. Caricato, A. V. Marenich,
 J. Bloino, B. G. Janesko, R. Gomperts, B. Mennucci, H. P. Hratchian,
 J. V. Ortiz, A. F. Izmaylov, J. L. Sonnenberg, D. Williams-Young,
 F. Ding, F. Lipparini, F. Egidi, J. Goings, B. Peng, A. Petrone,
 T. Henderson, D. Ranasinghe, V. G. Zakrzewski, J. Gao, N. Rega,
 G. Zheng, W. Liang, M. Hada, M. Ehara, K. Toyota, R. Fukuda,
 J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai,
 T. Vreven, K. Throssell, J. A. Montgomery, Jr., J. E. Peralta,
 F. Ogliaro, M. J. Bearpark, J. J. Heyd, E. N. Brothers, K. N. Kudin,
 V. N. Staroverov, T. A. Keith, R. Kobayashi, J. Normand,
 K. Raghavachari, A. P. Rendell, J. C. Burant, S. S. Iyengar,
 J. Tomasi, M. Cossi, J. M. Millam, M. Klene, C. Adamo, R. Cammi,
 J. W. Ochterski, R. L. Martin, K. Morokuma, O. Farkas,
 J. B. Foresman, and D. J. Fox, Gaussian, Inc., Wallingford CT, 2016.
 """)
st.write('(11) Becke, A. D. Density-Functional Exchange-Energy Approximation with Correct Asymptotic Behavior. Phys. Rev. A 1988, 38 (6), 3098. https://doi.org/10.1103/PhysRevA.38.3098.')
st.write('(12) Lee, C.; Yang, W.; Parr, R. G. Development of the Colle-Salvetti Correlation-Energy Formula into a Functional of the Electron Density. Phys. Rev. B 1988, 37 (2), 785. https://doi.org/10.1103/PhysRevB.37.785.')
st.write('(13) Becke, A. D. Density‐functional Thermochemistry. III. The Role of Exact Exchange. J. Chem. Phys. 1993, 98 (7), 5648–5652. https://doi.org/10.1063/1.464913.')
st.write('(14) Francl, M. M.; Pietro, W. J.; Hehre, W. J.; Binkley, J. S.; Gordon, M. S.; DeFrees, D. J.; Pople, J. A. Self‐consistent Molecular Orbital Methods. XXIII. A Polarization‐type Basis Set for Second‐row Elements. J. Chem. Phys. 1982, 77 (7), 3654–3665. https://doi.org/10.1063/1.444267.')
st.write('(15) Wang, J.; Cieplak, P.; Kollman, P. A. How well does a restrained electrostatic potential (RESP) model perform in calculating conformational energies of organic and biological molecules? Journal of Computational Chemistry 2000, 21 (12), 1049–1074. https://doi.org/10.1002/1096-987X(200009)21:12%253C1049::AID-JCC3%253E3.0.CO;2-F.')
st.write('(16) Case, D. A.; Aktulga, H. M.; Belfon, K.; Cerutti, D. S.; Cisneros, G. A.; Cruzeiro, V. W. D.; Forouzesh, N.; Giese, T. J.; Götz, A. W.; Gohlke, H.; Izadi, S.; Kasavajhala, K.; Kaymak, M. C.; King, E.; Kurtzman, T.; Lee, T.-S.; Li, P.; Liu, J.; Luchko, T.; Luo, R.; Manathunga, M.; Machado, M. R.; Nguyen, H. M.; O’Hearn, K. A.; Onufriev, A. V.; Pan, F.; Pantano, S.; Qi, R.; Rahnamoun, A.; Risheh, A.; Schott-Verdugo, S.; Shajan, A.; Swails, J.; Wang, J.; Wei, H.; Wu, X.; Wu, Y.; Zhang, S.; Zhao, S.; Zhu, Q.; Thomas E.  Cheatham, I. I. I.; Roe, D. R.; Roitberg, A.; Simmerling, C.; York, D. M.; Nagan, M. C.; Kenneth M.  Merz, J. AmberTools. Journal of Chemical Information and Modeling 2023. https://doi.org/10.1021/acs.jcim.3c01153.')
st.write("""(17) D.A. Case, H.M. Aktulga, K. Belfon, I.Y. Ben-Shalom, J.T. Berryman, S.R. Brozell, F.S. Carvahol, D.S. Cerutti, T.E. Cheatham, III, G.A. Cisneros, V.W.D. Cruzeiro, T.A. Darden, N. Forouzesh, M. Ghazimirsaeed, G. Giambaşu, T. Giese, M.K. Gilson, H. Gohlke, A.W. Goetz, J. Harris, Z. Huang, S. Izadi, S.A. Izmailov, K. Kasavajhala, M.C. Kaymak, I. Kolossv\'a ry, A. Kovalenko, T. Kurtzman, T.S. Lee, P. Li, Z. Li, C. Lin, J. Liu, T. Luchko, R. Luo, M. Machado, M. Manathunga, K.M. Merz, Y. Miao, O. Mikhailovskii, G. Monard, H. Nguyen, K.A. O'Hearn, A. Onufriev, F. Pan, S. Pantano, A. Rahnamoun, D.R. Roe, A. Roitberg, C. Sagui, S. Schott-Verdugo, A. Shajan, J. Shen, C.L. Simmerling, N.R. Skrynnikov, J. Smith, J. Swails, R.C. Walker, J. Wang, J. Wang, X. Wu, Y. Wu, Y. Xiong, Y. Xue, D.M. York, C. Zhao, Q. Zhu, and P.A. Kollman (2025), Amber 2025, University of California, San Francisco.
""")
st.write('(18) Abraham, M.; Alekseenko, A.; Andrews, B.; Basov, V.; Bauer, P.; Bird, H.; Briand, E.; Brown, A.; Doijade, M.; Fiorin, G.; Fleischmann, S.; Gorelov, S.; Gouaillardet, G.; Gray, A.; Irrgang, M. E.; Jalalypour, F.; Johansson, P.; Kutzner, C.; Łazarski, G.; Lemkul, J. A.; Lundborg, M.; Merz, P.; Miletić, V.; Morozov, D.; Müllender, L.; Nabet, J.; Páll, S.; Pasquadibisceglie, A.; Pellegrino, M.; Piasentin, N.; Rapetti, D.; Sadiq, M. U.; Santuz, H.; Schulz, R.; Shirts, M.; Shugaeva, T.; Shvetsov, A.; Turner, P.; Villa, A.; Wingbermühle, S.; Hess, B.; Lindahl, E. GROMACS 2025.2 Source Code, 2025. https://doi.org/10.5281/zenodo.15387018. (18b) GROMACS: High Performance Molecular Simulations through Multi-Level Parallelism from Laptops to Supercomputers. SoftwareX 2015, 1–2, 19–25. https://doi.org/10.1016/j.softx.2015.06.001.')
st.write('(19) Hess, B.; Bekker, H.; Berendsen, H. J. C.; Fraaije, J. G. E. M. LINCS: A Linear Constraint Solver for Molecular Simulations. Journal of Computational Chemistry 1997, 18 (12), 1463–1472. https://doi.org/10.1002/(SICI)1096-987X(199709)18:12%253C1463::AID-JCC4%253E3.0.CO;2-H.')
st.write('(20) Bussi, G.; Donadio, D.; Parrinello, M. Canonical Sampling through Velocity Rescaling. J. Chem. Phys. 2007, 126 (1). https://doi.org/10.1063/1.2408420.')
st.write('(21) Bernetti, M.; Bussi, G. Pressure Control Using Stochastic Cell Rescaling. J. Chem. Phys. 2020, 153 (11). https://doi.org/10.1063/5.0020514.')
st.write('(22) Michaud-Agrawal, N.; Denning, E. J.; Woolf, T. B.; Beckstein, O. MDAnalysis: A Toolkit for the Analysis of Molecular Dynamics Simulations. Journal of Computational Chemistry 2011, 32 (10), 2319–2327. https://doi.org/10.1002/jcc.21787.')
st.write('(23) Neese, F. Software Update: The ORCA Program System—Version 6.0. Wiley Interdisciplinary Reviews: Computational Molecular Science 2025, 15 (2), e70019. https://doi.org/10.1002/wcms.70019.')
st.write('(24) Furness, J. W.; Kaplan, A. D.; Ning, J.; Perdew, J. P.; Sun, J. Accurate and Numerically Efficient r2SCAN Meta-Generalized Gradient Approximation. The Journal of Physical Chemistry Letters 2020. https://doi.org/10.1021/acs.jpclett.0c02405.')
st.write('(25) Weigend, F.; Ahlrichs, R. Balanced Basis Sets of Split Valence, Triple Zeta Valence and Quadruple Zeta Valence Quality for H to Rn: Design and Assessment of Accuracy. Physical Chemistry Chemical Physics 2005, 7 (18), 3297–3305. https://doi.org/10.1039/B508541A.')
st.write('(26) Weigend, F. Accurate Coulomb-Fitting Basis Sets for H to Rn. Physical Chemistry Chemical Physics 2006, 8 (9), 1057–1065. https://doi.org/10.1039/B515623H.')
st.write('(27) Caldeweyher, E.; Bannwarth, C.; Grimme, S. Extension of the D3 Dispersion Coefficient Model. J. Chem. Phys. 2017, 147 (3). https://doi.org/10.1063/1.4993215.')
st.write('(28) Caldeweyher, E.; Ehlert, S.; Hansen, A.; Neugebauer, H.; Spicher, S.; Bannwarth, C.; Grimme, S. A Generally Applicable Atomic-Charge Dependent London Dispersion Correction. J. Chem. Phys. 2019, 150 (15). https://doi.org/10.1063/1.5090222.')
st.write('(29) Reed, A. E.; Weinstock, R. B.; Weinhold, F. Natural Population Analysis. J. Chem. Phys. 1985, 83 (2), 735–746. https://doi.org/10.1063/1.449486.')

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

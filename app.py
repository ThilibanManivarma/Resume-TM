from pathlib import Path

import streamlit as st 
from PIL import Image 

#  PATH SETTINGS

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assests"/"CV_THILIBAN.pdf"
profile_file = current_dir/"assests"/"profile-pic.png"

# GENERAL SETTINGS 

PAGE_TITLE = "Digital CV | Thiliban Manivarma"
PAGE_ICON = ":wave:"
NAME = "Thiliban Manivarma"
DESCRIPTION = """
Ph.D. Scholar | Molecular Modelling | Computer-aided-drug-design | AI/ML | Data science """
EMAIL = "thilibanaussie@gmail.com"
LINKS = {
    "Google scholar" : "https://scholar.google.com/citations?user=i2GzGagAAAAJ&hl=en",
    "Linkedin" : "https://www.linkedin.com/in/thiliban-manivarma-0ab537115/ ",
    "Github" : "https://github.com/ThilibanManivarma1997"

}

PROJECTS = {
    "XXX" : "YYY",
    "ZZZ" : "AAA"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("Hello there")

#Load CSS, PDF, PROFILE PIC 

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_file = Image.open(profile_file)

#HERO SECTION 

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_file, width=230)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL)

#social links 

st.write("#")

cols = st.columns(len(LINKS))

for index, (platform,link) in enumerate(LINKS.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- **Ph.D. – Computational biophysics** ( SONATA15, National Science Centre (2019/35/D/ST4/02203; 2020-2023) grant obtained by Dr. Karolina Mikulska-Ruminska, 08/2020-present.

    Project name: “Computational studies of regulatory mechanism and inhibition of ferroptotic cell death signal”,
    Key words : Molecular docking, Molecular dynamic simulation, protein-protein system, protein-membrane system, Virtual screening, Pharmacophore modelling, Hotspots prediction, NAMD, CHARMM-GUI.

- **Mtech Thesis - Computational Biology** – supported and funded (12500 RS per month) by Govt. of India, 10/2018-05/2020,

    Project name: “In-silico studies on Nipah virus proteins and their host pathogen interaction studies”,
    Key words : Molecular docking, protein-protein interaction, Systems biology, Machine learning.  

- **BTech Thesis - Pharmaceutical Technology**, 07/2017-10/2018, 

    Project name: “In-silico docking studies on dengue protein (DEN 4)”,
    Key words : Molecular docking, protein-ligand interaction.  

- **Uresearcher, a research education company**, 09/2021-05/2022: I was an instructor and handled “Python essentials for Drug Discovery”.

- **University, Ph.D. course works**, 03/2023-07/2023: I had been teaching “Introduction to python programming” to the students of informatics (8) and several doctoral candidates (9) from different disciplines as a part of my Ph.D. studies.
"""
)

# SKILLS
st.write('#')
st.subheader('Tools and Programming Skills')
st.write("""

- Molecular dynamics simulation software: NAMD, GROMACS, Desmond.
- Molecular docking analysis: Autodock, SMINA, Glide.
- OS handle: Windows, Linux/Unix.
- Programming skills : Python, Tcl.
- Version control system : Git.
- Machine learning analysis: Using Python packages sci-kit learn, Keras, TensorFlow. RDkit package for Computational Chemistry.
- Web development : HTML.
- Database management : SQL.
         
""")

#Personal projects 
st.write('#')
st.subheader('Personal Projects')
st.write("""
- Predicting HOTSPOT residues in the protein-protein complex, 15LOX1/PEBP1 (Artificial intelligence):
          
     **Protein-protein interface dataset | Supervised learning | Python | Tensorflow | Neural network | Jupyter notebook**.
         
- Finding potential inhibitors for 15LOX1 in the chEMBL (Machine Learning/Artificial intelligence): 
         
     **Inhibitors | Supervised learning | chEMBL | Python | Machine learning | Tensorflow | Jupyter notebook**.
         
- Classifying sialic acid independent and dependent viruses (Machine learning):
         
    **Protein sequence dataset | supervised learning | python | scikit learn | Jupyter notebook**.
         

- Classifying two south indian dishes using Convolutional Neural Network:
          
     **Convolutional Neural Network  | supervised learning | AI | python | cv2 | VS CODE | streamlit**.
    
- Drug Discovery Hackathon 2020, Govt of India – Participated and guided a group of students in national wide competition to find potential inhibitors for Covid 19:
         
     **Molecular docking | Structural bioinformatics | Virtual screening**.
         
- Phytochemical analysis on Rhizopora mangle:
         
    **soxhlet extraction | antioxidants | cancer therapy**.

         """)
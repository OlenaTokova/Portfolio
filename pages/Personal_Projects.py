import streamlit as st
from pathlib import Path
from PIL import Image


import streamlit as st

# Page configuration
st.set_page_config(page_title="Personal Projects | Olena Tokova", page_icon=":school:")

# Content of the page
st.title("Personal Projects")
st.write("""
My portfolio is a collection of diverse personal projects that showcase my creativity and technical skills. I would be grateful if you take the time to look through my portfolio.
""")


# Define PROJECTS with detailed information
PROJECTS = {
    "Alloy-Analyzer": {
        "period": "Feb 2024 - Apr 2024",
        "association": "Network Technology Academy Institute · Apprenticeship",
        "description": """
        The GMDH approach is especially suited for complex and nonlinear data, making it ideal for the intricate relationships in materials science. 
        The project is an advanced predictive tool designed to forecast the mechanical properties of steel castings based on their chemical compositions.
        """,
        "skills": "Skills: Analyze Information · GMDH",
        "link": "https://github.com/OlenaTokova/Alloy-Analyzer"
    },
    "Automated Research Assistant": {
        "period": "Feb 2024 - Apr 2024",
        "association": "Network Technology Academy Institute · Apprenticeship",
        "description": """
        A web-based application designed to simplify and expedite the process of finding academic papers and articles. Utilizes APIs like arXiv and GPT-3 for semantic analysis.
        """,
        "skills": "Skills: Time Management · Python (Programming Language) · Flask · Streamlit",
        "link": "https://github.com/OlenaTokova/Automated_Research_Assistant"
    },
    "BreastCancer Project": {
        "period": "Jen 2024 - Feb 2024",
        "association": "Network Technology Academy Institute · Apprenticeship",
        "description": """
        Focuses on the development and application of a deep learning model for semantic segmentation of breast cancer imagery. The goal is to improve the accuracy and efficiency of breast cancer diagnosis through automated image segmentation.
        """,
        "link": "https://github.com/OlenaTokova/BreastCancer_project"
    }
}

# Display projects with detailed information
st.subheader("Projects 🌟")
for name, details in PROJECTS.items():
    st.markdown(f"### {name}")
    if "period" in details:
        st.markdown(f"*{details['period']}*")
    if "association" in details:
        st.markdown(f"*{details['association']}*")
    st.markdown(details["description"])
    if "skills" in details:
        st.markdown(details["skills"])
    st.markdown(f"[GitHub]({details['link']})", unsafe_allow_html=True)
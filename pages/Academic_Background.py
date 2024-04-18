import streamlit as st
from pathlib import Path



# Create sidebar navigation links
#for page, page_script in pages.items():
#   st.sidebar.write(f"[{page}](http://localhost:8501/{page_script})")

# Page configuration
# It's commented out because it should only be set once and at the very beginning of the app.
# st.set_page_config(page_title="Academic Background | Olena Tokova", page_icon=":school:")

# Content of the page
st.title("Academic Background")
st.write("""
My portfolio showcases my academic background in applied mathematics and my passion for combining mathematical principles with information technology. With a Bachelor's degree in Applied Mathematics from Kyiv, Ukraine, I have honed my logical thinking and analytical skills.
""")

# Define sidebar for navigation or additional information
#st.sidebar.title("Navigation")
#st.sidebar.write("Here you can place navigation links or any other side-panel content for your portfolio.")

# Constants
PAGE_TITLE = "Academia | Olena Tokova"
PAGE_ICON = "🏛"
NAME = "Olena Tokova"
DESCRIPTION = """
Here you can describe your academic background, qualifications, and any relevant experiences or coursework that highlight your expertise in your field.
"""

# Academic Background Section
st.subheader("My Journey 🚩")
st.write('---')

# Custom function to create background sections
def create_background_section(title, description):
    st.write(title)
    st.write(description, unsafe_allow_html=True)


# Display your academic journey
create_background_section("Hello! My name is Olena Tokova.", """
I'm originally from Kyiv, Ukraine. I hold a Bachelor's degree in Applied Mathematics. My biography in the world of science began with academic training in mathematics, which helped me develop logical thinking and analytical skills. I believe that the combination of the mathematical basis with information technology has great potential in various fields. 
Nowadays, the development of new technologies happens every day, and it is necessary to be aware of all the latest innovations and have the relevant knowledge to understand the processes of the relevant systems.
Achieving a real breakthrough in science and technology requires high-speed computing, large volumes of data and intelligent algorithms, constant study of new tools and technologies, such as artificial intelligence and machine learning. All this opens up new opportunities for scientific research and innovation.
Therefore, in order to obtain the desired position, I need to improve my qualifications and knowledge in the field of technical sciences and information technologies. Competent and fluent English is very necessary for successful communication with colleagues and clients.
In conclusion, I believe that mathematics and information technology are indispensable for achieving new scientific discoveries and moving forward in many fields.
""")

st.write('----')

import streamlit as st
from pathlib import Path
from PIL import Image

# Set page configuration as the very first command
st.set_page_config(page_title="Digital Portfolio | Olena Tokova", page_icon=":star:")

# Sidebar Navigation
st.sidebar.title("Portfolio Navigation")
page = st.sidebar.radio(
    "Go to",  # This is the missing label that needs to be added
    ["Home", "Academic Background", "Certifications", "Personal Projects", "Professional Experiences", "Publications"]
)

# Define base directory and paths for resources
base_dir = Path(__file__).resolve().parent
profile_pic_path = base_dir / "add_info" / "Olena_tokova.jpg"
resume_path = base_dir / "add_info" / "Resume.pdf"

# Try to load the profile picture
try:
    profile_pic = Image.open(profile_pic_path)
except Exception as e:
    st.error(f"Failed to load image: {str(e)}")
    profile_pic = None

if page == "Home":
    # Display the hero section with the profile picture if available
    if profile_pic:
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(profile_pic, caption='Olena Tokova', width=230)
        with cols[1]:
            st.title("Olena Tokova")
            st.markdown("""
            Hello! My name is Olena Tokova.<br><br>
            I have a bachelor's degree in applied mathematics. I like to analyze data and create mathematical models necessary for solving various problems and making decisions. This supports the forecasting of future events, optimizing processes, identifying cause-and-effect relationships, and increasing the efficiency of any processes and systems.
            """, unsafe_allow_html=True)
    else:
        st.error("Profile picture is not available.")

    # Include the download button for the resume
    try:
        with open(resume_path, "rb") as file:
            btn = st.download_button(
                label="Download My Resume",
                data=file.read(),
                file_name="Olena_Tokova_Resume.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"Failed to load resume: {str(e)}")

    # Goal and importance section as a separate paragraph
    st.markdown("""
    **My Goal:** I aim to secure a long-term position in a company, with competitive compensation and a favorable work-life balance. My goal is to find a stable and fulfilling job that aligns with my skills and interests, allowing me to contribute to the company's success while also maintaining a healthy work-life balance.<br><br>
    **This goal is important because:** It aligns with my personal values and aspirations. First, securing a long-term position with competitive compensation is important to me as it provides stability and financial security. This allows me to plan for the future and achieve my financial goals. I believe that achieving balance between my professional and personal life is essential to maintaining a healthy and fulfilling lifestyle.
    """, unsafe_allow_html=True)

    # Contact information and social media links
    st.markdown("""
    <div style="background-color: #87CEEB; padding: 10px; border-radius: 10px; text-align: center;">
        <b>Contact Information:</b><br>
        📫 <a href="mailto:elenatokareva363@gmail.com" style="color: white; text-decoration: none;">elenatokareva363@gmail.com</a><br>
        <a href="https://www.linkedin.com/in/olena-tokova-737a002b0/" style="color: white; text-decoration: none;">LinkedIn</a> |
        <a href="https://github.com/OlenaTokova" style="color: white; text-decoration: none;">GitHub</a><br>
    </div>
    """, unsafe_allow_html=True)
else:
    st.write(f"This is the {page} Page")  # Placeholder for other pages

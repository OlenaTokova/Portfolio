import streamlit as st

# Page configuration
st.set_page_config(page_title="Professional Experience | Olena Tokova", page_icon=":briefcase:")

# Content of the page
st.title("Professional Experience")
st.write("""
I believe that the combination of mathematics and technology has immense potential in various fields, and I am committed to continuously improving my skills and knowledge to contribute to scientific research and innovation. 
""")

# Define PROFESSIONAL EXPERIENCES with detailed information
EXPERIENCES = {
    "Interregional Academy of Personnel Management": {
        "degree": "Bachelor Degree, Applied Mathematics",
        "period": "Sep 2006 - Jul 2011",
        "location": "Kyiv, Ukraine",
        "description": """
        During my time at the InterRegional Academy of Personnel Management, I pursued a Bachelor's Degree in Applied Mathematics. I acquired a strong foundation in mathematical theory, problem-solving skills, and analytical thinking. I also gained proficiency in using various mathematical tools and techniques to solve real-world problems. This program helped me develop the ability to communicate complex mathematical concepts effectively and work collaboratively.
        """
    },
    "Holyoke Community College": {
        "course": "English classes, Accelerated Career English",
        "period": "Jan 2024 - Mar 2024",
        "location": "Holyoke, MA, USA",
        "description": """
        I gained valuable skills and knowledge in the Accelerated Career English program, learning to effectively work in Canvas, write resumes, CVs, and cover letters, and understand grammar rules. My time here enhanced my English proficiency and equipped me with the tools to succeed in future endeavors.
        """
    },
    "Network Technology Academy Institute": {
        "program": "Training Program, AI-Powered Business and Data Analytics Specialist",
        "period": "Dec 2023 - May 2024",
        "location": "Somerville, MA, USA",
        "description": """
        At Network Technology Academy, I am completing a training program focused on AI-Powered Business and Data Analytics. Learning Python programming, data science, AI, and machine learning prepares me to excel in the data analytics field with hands-on projects and certifications, ready for complex challenges in AI development.
        """
    }
}

# Display experiences with detailed information
st.subheader("Experience Highlights 📚")
for institution, details in EXPERIENCES.items():
    st.markdown(f"### {institution}")
    if "degree" in details or "program" in details:
        st.markdown(f"*{details.get('degree', details.get('program', ''))}*")
    st.markdown(f"*{details['period']}*")
    st.markdown(f"*{details['location']}*")
    st.markdown(details["description"])
    st.write('----')

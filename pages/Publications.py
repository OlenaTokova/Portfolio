import streamlit as st

# Page configuration
st.set_page_config(page_title="Publications | Olena Tokova", page_icon=":books:")

# Title of the page
st.title("Publications")

# List of publications
publications = {
    "Computer Systems of Thermal Analysis for Monitoring of Foundry and Metallurgical Processes": {
        "journal": "Інформаційні технології та комп’ютерна інженерія",
        "date": "Jun 29, 2022",
        "description": """A computer system for monitoring thermal processes occurring in foundries and metallurgical plants is described. Methods of thermal analysis of metal, and methods of optimization of cast structures based on thermal analysis are presented.""",
        "link": "https://www.researchgate.net/publication/362095640_COMPUTER_SYSTEMS_OF_THERMAL_ANALYSIS_FOR_MONITORING_OF_FOUNDRY_AND_METALLURGICAL_PROCESSES"
    },
    "Filtering-based Estimating the Cast Iron Quality Using Recognition of Cooling Curves": {
        "conference": "2020 IEEE 15th International Conference on Computer Sciences and Information Technologies (CSIT)",
        "date": "Sep 26, 2020",
        "description": """The method of high-frequency filtering of cooling curves of melts by the extrema of the derivative was applied and a procedure for identifying crystallization points of gray cast iron was proposed.""",
        "link": "https://www.researchgate.net/publication/358318671_Filtering-based_Estimating_the_Cast_Iron_Quality_Using_Recognition_of_Cooling_Curves"
    },
    "Modelling of Dependence of Mechanical Properties of Cast Iron on Chemical Composition of Raw Materials": {
        "journal": "Boundary Field Problems and Computer Simulation",
        "date": "Sep 22, 2019",
        "description": """Based on the combinatorial GMDH algorithm, models of dependence of mechanical properties of cast iron on its chemical composition are constructed.""",
        "link": "https://www.researchgate.net/publication/345354537_Modelling_of_Dependence_of_Mechanical_Properties_of_Cast_Iron_on_Chemical_Composition_of_Raw_Materials"
    },
    "Inductive Modelling as a Basis of Informational Support of Decisions in Foundry Production": {
        "conference": "2017 12th International Scientific and Technical Conference on Computer Sciences and Information Technologies (CSIT)",
        "date": "Sep 23, 2017",
        "description": """The article describes the application of the inductive approach to constructing an informational support system for decision-making in the foundry industry.""",
        "link": "https://www.researchgate.net/publication/320966992_Inductive_modelling_as_a_basis_of_informational_support_of_decisions_in_foundry_production"
    }
}

# Display each publication with a button to read more
for title, info in publications.items():
    st.subheader(title)
    st.write(f"**Date:** {info['date']}")
    if 'journal' in info:
        st.write(f"**Journal:** {info['journal']}")
    if 'conference' in info:
        st.write(f"**Conference:** {info['conference']}")
    st.write(info['description'])
    st.markdown(f"[Read More]({info['link']})", unsafe_allow_html=True)
    st.write("---")

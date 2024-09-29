import streamlit as st
import requests
import base64
from streamlit_lottie import st_lottie
from streamlit_extras.stylable_container import stylable_container
from model import match_descs
from apply import apply


st.markdown("""
<style>
    .reportview-container {
        background: #8BAC9E;
    }
    .sidebar .sidebar-content {
        background: #7A9A8F;
    }
    .Widget>label {
        color: #2E4052;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        color: #2E4052;
    }
            
    .stButton>button {
        font-size: 90px;
        padding: 10px 30px;
        color: #2E4052;
        background-color: #D0E3CC;
        border-radius: 10px;
        font-weight: bold;
        border: 1px solid #2E4052;
    }
            
    .stButton>button:hover {
        background-color: #2E4052;
        color: #D0E3CC;
    }
    .big-font {
        font-size: 75px !important;
        color: #283618;
        font-weight: bold;
        text-align: center;
    }
    .tagline-font {
        font-size: 40px !important;
        color: #606C38;
        font-weight: bold;
        text-align: center;
    }
            
    .footer-font {
        font-size: 40px !important;
        color: #653500;
        font-weight: bold;
        text-align: center;
    }
            
    .center-col {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
            
    .custom-button {
        font-size: 30px;
        padding: 15px 50px;
        color: #2E4052;
        background-color: #D0E3CC;
        border-radius: 10px;
        font-weight: bold;
        border: 2px solid #2E4052;
        cursor: pointer;
        display: inline-block;
        transition: background-color 0.3s, color 0.3s;
    }
            
    .box {
        padding: 20px;
        margin: 40px 20px 20px 20px;
        border-radius: 15px;
        background-color: #606C38;
        color: white;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        height: 80px;
        width: 320px;
        align-items: center; 
        justify-content: center;
    }
    /* Styling the input text */
    .stTextInput>div>div>input {
        font-size: 20px;
        color: #2E4052;
        background-color: #F0F4F8;
        padding: 10px;
        border: 2px solid #2E4052;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# custom background
def set_background(image):
    with open(image, 'rb') as image:
        encoded_string = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: left;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Function to load Lottie file
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_test = load_lottieurl("https://lottie.host/421df829-e2f1-46b0-876e-865cd7c28e02/iwKk8et0jn.json")


# Application Page (placeholder)
def application():
    st.markdown('<p class="tagline-font" style="color: #2E4052;">Tell us more about yourself!</p>', unsafe_allow_html=True)
    with st.form("Application", clear_on_submit=True, border=False):
        name = st.text_input("Please enter your full name (first name, last name)", "")
        address = st.text_input("Please enter your full address", "")
        contact = st.text_input("Please enter your email address", "")
        skills = st.text_input("What technical skills, software proficiencies, or languages (spoken or programming) do you possess? Provide examples of how you have applied these skills in past projects or roles, including any leadership or team experiences.", "")
        experience = st.text_input("Summarize your recent or most relevant work experience, including the employer's name, your job title, dates of employment, key responsibilities, achievements, and reasons for leaving (if applicable).", "")
        education = st.text_input("Please describe your educational background, including the highest degree obtained, institution name, major/field of study, graduation year, and any relevant courses or certifications.", "")
        submitted = st.form_submit_button("Submit form")
        
    if submitted:
        with st.status("Finding best matches..."):
            results = match_descs(skills, experience, education)
        #num_results = st.radio("Select number of matches to display", [5, 10, 25], index=0) #not working rn
        top_matches = results.head(5)
        for idx, row in top_matches.iterrows():
                # Display job title, company, and similarity score
                st.write(f"**Job Title**: {row['title']} at {row['company']}")
                st.write(f"**Similarity Score**: {row['similarity_score']}")
                st.write(f"**Description**: {row['desc']}")  
                # Create an 'Apply' button for each job (not functional for now)
                if st.button(f"Apply", key=f"apply_{idx}"):
                    st.session_state.page = "apply"
                    #apply(name, address, contact, skills, education, experience)
                    st.rerun()
                    # Add a divider between job entries
                st.write("---")

    # col1, col2 = st.columns([2, 1])
    # with col1:

    #     with stylable_container(
    #         key="container_with_border",
    #         css_styles="""
    #             {
    #                 border: 1px solid rgba(49, 51, 63, 0.2);
    #                 border-radius: 0.5rem;
    #                 padding: 20px;
    #             }
    #             """,
    #     ):
            
    #         st.markdown('<p class="tagline-font" style="color: #2E4052;">Tell us more about yourself!</p>', unsafe_allow_html=True)

    #         with st.form("Application", clear_on_submit=True, border=False):
    #             name = st.text_input("Please enter your full name (first name, last name)", "")
    #             address = st.text_input("Please enter your full address", "")
    #             contact = st.text_input("Please enter your email address", "")
    #             skills = st.text_input("What technical skills, software proficiencies, or languages (spoken or programming) do you possess? Provide examples of how you have applied these skills in past projects or roles, including any leadership or team experiences.", "")
    #             experience = st.text_input("Summarize your recent or most relevant work experience, including the employer's name, your job title, dates of employment, key responsibilities, achievements, and reasons for leaving (if applicable).", "")
    #             education = st.text_input("Please describe your educational background, including the highest degree obtained, institution name, major/field of study, graduation year, and any relevant courses or certifications.", "")
    #             submitted = st.form_submit_button("Submit form")

    #         if submitted:
    #             with st.status("Finding best matches..."):
    #                 results = match_descs(skills, experience, education)
    #             num_results = st.selectbox("Select number of matches to display", [5, 10, 25], index=0)
    #             top_matches = results.sort_values(by='similarity_score', ascending=False).head(num_results)
    #             for idx, row in top_matches.iterrows():
    #                 # Display job title, company, and similarity score
    #                 st.write(f"**Job Title**: {row['title']} at {row['company']}")
    #                 st.write(f"**Similarity Score**: {row['similarity_score']:.2f}")
    #                 st.write(f"**Description**: {row['desc']}")  
    #                 # Create an 'Apply' button for each job (not functional for now)
    #                 if st.button(f"Apply", key=f"apply_{idx}"):
    #                     st.write(f"You clicked apply for {row['title']}")
    #                     # Add a divider between job entries
    #                 st.write("---")
    # with col2:
    #     with stylable_container(
    #         key="container_with_border",
    #         css_styles="""
    #             {
    #                 padding: 30px;
    #                 align-items: center;
    #                 border: None;
    #                 justify-content:center;
    #             }
    #             """,
    #     ):
    #         st_lottie(
    #             lottie_test,
    #             speed=1,
    #             reverse=False,
    #             loop=True,
    #             quality="high",
    #             height=480,
    #             key="application_form"
    #         )




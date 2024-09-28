import streamlit as st
import requests
import base64

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
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Application Page (placeholder)
def application():
    set_background("test2.png")
    st.title("Job Application")
    st.write("This is where the job application form will go.")


    # navigate back to home
    if st.button("Back to Home", key="back_home"):
        st.session_state.page = "home"
        st.rerun()
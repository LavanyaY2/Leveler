import streamlit as st
from streamlit_lottie import st_lottie
import requests
import streamlit as st

# Set page config
st.set_page_config(page_title="Jobify", layout="wide")

# Function to load Lottie file
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_woman_working = load_lottieurl("https://lottie.host/f4bafe32-bd0a-4774-b6f6-87bc33d541ef/lQKUbk3xW3.json")

# Custom CSS with sage color palette and centered text
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
        font-size: 80px !important;
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
    .center-col {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)


# Function to load Lottie file
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Home Page
def home():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="center-col">', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Welcome to Jobify!</p>', unsafe_allow_html=True)
        st.markdown('<p class="tagline-font" style="text-align: left; color: #2E4052;">Your gateway to exciting career opportunities.</p>', unsafe_allow_html=True)
        if st.button("Get Started", key="get_started"):
            st.session_state.page = "application"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st_lottie(
            lottie_woman_working,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=400,
            key="woman_working"
        )

# Application Page (placeholder)
def application():
    st.title("Job Application")
    st.write("This is where the job application form will go.")
    if st.button("Back to Home", key="back_home"):
        st.session_state.page = "home"
        st.experimental_rerun()

# Main app logic
def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "application":
        application()

if __name__ == "__main__":
    main()
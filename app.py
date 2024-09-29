import streamlit as st
from streamlit_lottie import st_lottie
import requests
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_navigation_bar import st_navbar
import time

# Set page config
st.set_page_config(page_title="Leveler", layout="wide", initial_sidebar_state="collapsed")

# import pages
from application import application

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
        margin: 40px 20px 40px 20px;
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
            
    /* Custom styles for the full-width sticky navigation bar */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 60px;
        background-color: #283618;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .navbar-brand {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: bold;
    }
    .navbar-menu {
        display: flex;
        gap: 20px;
    }
    .navbar-menu .stSelectbox {
        min-width: 120px;
    }
    .navbar-menu .stSelectbox > div > div {
        background-color: #D0E3CC;
        color: #2E4052;
        border: none;
        border-radius: 20px;
    }
    /* Hide the default Streamlit header */
    header {
        display: none !important;
    }
            
    .button-container {
        display: flex;
        gap: 10px; /* Adjust the gap for spacing */
    }
    .button-container button {
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        border: 1px solid transparent;
        cursor: pointer;
    }
    
    
</style>
""", unsafe_allow_html=True)



# FOR NAVBAR
# Function to handle page display
def display_page():
    page = st.session_state.get('current_page', 'home')  # Default to 'home' if not set

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

# Update session state based on query parameter
def on_page_change():
    query_params = st.session_state.get('query_params', {})
    page = query_params.get('page', ['home'])[0]  # Get 'page' query parameter (default 'home')
    if page != st.session_state['current_page']:
        st.session_state['current_page'] = page
        st.rerun()

def navigation_bar():
    st.markdown("""
    <div class="navbar">
        <div class="navbar-brand">Leveler</div>
        <div class="navbar-menu">
            <a id="nav-select" style='color: white; text-decoration: none; display: block; text-align: center;' href="?page=application">Home</a>
            <a id="nav-select" style='color: white; text-decoration: none; display: block; text-align: center;' href="?page=application">Apply</a>
            <a id="nav-select" style='color: white; text-decoration: none; display: block; text-align: center;' href="?page=application">Sign In</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Detect if the page query parameter changes
    on_page_change()

    # Display content based on current page
    display_page()

# Function to load Lottie file
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_woman_working = load_lottieurl("https://lottie.host/f4bafe32-bd0a-4774-b6f6-87bc33d541ef/lQKUbk3xW3.json")    

# Home Page
def home():

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="center-col">', unsafe_allow_html=True)
        st.markdown('<p class="big-font">Welcome to Leveler!</p>', unsafe_allow_html=True)
        st.markdown('<p class="tagline-font" style="text-align: left; color: #2E4052;">Your gateway to exciting career opportunities.</p>', unsafe_allow_html=True)
        
        if st.button("Get Started", key="get_started"):
            st.session_state.page = "application"
            st.rerun()
        
        st.link_button("Log in", "http://localhost:8000")
    
        # col1_button, col2_button = st.columns(2)

        # with col1_button:
        #     st.markdown('<div class="custom-column">', unsafe_allow_html=True)
            

        # with col2_button:
        #     st.markdown('<div class="custom-column">', unsafe_allow_html=True)
            
        
    
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
    
    st.markdown('<p class="footer-font">Wondering how this works? Just follow these 4 steps!</p>', unsafe_allow_html=True)
    # footer boxes
    col1_1, col1_2, col1_3, col1_4 = st.columns(4)
    with col1_1:
        st.markdown('<div class="box">01. \nCreate your profile</div>', unsafe_allow_html=True)
    with col1_2:
        st.markdown('<div class="box">02. \nExplore job postings</div>', unsafe_allow_html=True)
    with col1_3:
        st.markdown('<div class="box">03. \nMatch your skills</div>', unsafe_allow_html=True)
    with col1_4:
        st.markdown('<div class="box">04. \nApply!</div>', unsafe_allow_html=True)
        

# Navigation
def main():

    page = st.session_state.get('current_page', 'Home')
    navigation_bar()

    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "application":
        application()
    elif st.session_state.page == "auth":
        auth()

if __name__ == "__main__":
    main()
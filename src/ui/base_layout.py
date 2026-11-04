 
import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp{
                background: #35245F !important;
            }

            .stApp div[data-testid = "stColumn"] {
                align-item: center !important;
            }

        </style>
            """, unsafe_allow_html = True)

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp{
                background: #8B70CE !important;
            }

            

        </style>
            """, unsafe_allow_html = True)

def style_base_layout():
    
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

            /* Hide Top Toolbar of streamlit */
            #MainMenu, footer, header{
                visibility: hidden;
            }

            .block-container{
                padding-top: 1.5rem !important;
                padding-bottom: 0rem;
                min-height: 100vh;
            }

            h1 {
                font-family: 'Poppins', sans-serif !important;
                font-size: 6rem !important;
                font-weight: 700 !important;
                color: #E6D9FF !important;
                padding-top: 1.25rem !important;
                padding-bottom: 0 !important;
            }

            h3, h4, p {
                font-family: 'Poppins', sans-serif !important;
                color: #E6D9FF !important;
            }

            button[kind = "primary"] {
                background: #E6D9FF !important;
                border-radius: 0.5rem !important;
                padding: 9px 18px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
            }

            /* Button text */
            button[kind="primary"] p {
                font-family: 'Poppins', sans-serif !important;
                font-size: 19px !important;
                font-weight: 600 !important;
                color: #35245F !important;
            }

            button[kind="primary"]:hover {
                transform: scale(1.02);
                background: white !important;
            }

            .st-emotion-cache-1bnbo98 {
                align-items: center;
                justify-content: center;
            }

            div.stHorizontalBlock {
                justify-content: center;
                gap: 5rem;
            }

            div.stColumn {
                flex: 0 0 auto;
                width: auto !important;
            }

            button[kind="primary"] [data-testid="stIconMaterial"] {
                color: #35245F !important;
                font-weight: 700 !important;
                font-size: 20px !important;
            }
            

        </style>
            """, unsafe_allow_html = True)
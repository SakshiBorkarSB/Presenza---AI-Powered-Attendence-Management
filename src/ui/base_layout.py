 
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
                background: #E6D9FF !important;
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
                max-width: 600px !important;
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

            h3 {
                font-family: 'Poppins', sans-serif !important;
                font-size: 3rem !important;
                font-weight: 700 !important;
                color: #35245F !important;
                margin: 0 !important;
                padding: 0 !important;
                line-height: 1 !important;
            }

            h2{
                font-family: 'Poppins', sans-serif !important;
                color: #35245F !important;   
                font-size: 30px !important;   
                margin-top: 10px !important;          
            }

            h4, p {
                font-family: 'Poppins', sans-serif !important;
                color: #35245F !important;
                font-size: 16px !important;
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
                width: "stretch";
            }

            button[kind="primary"]:hover {
                transform: scale(1.02);
                background: white !important;
            }

            button[kind="primary"] [data-testid="stIconMaterial"] {
                color: #35245F !important;
                font-weight: 700 !important;
                font-size: 20px !important;
            }

            button[kind = "secondary"] {
                background: #35245F !important;
                border-radius: 0.5rem !important;
                padding: 7px 15px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
            }

            /* Button text */
            button[kind="secondary"] p {
                font-family: 'Poppins', sans-serif !important;
                font-size: 18px !important;
                font-weight: 500 !important;
                color: #E6D9FF !important;
            }

            button[kind="secondary"]:hover {
                transform: scale(1.02);
                background: #523B91 !important;
            }

            button[kind="secondary"] [data-testid="stIconMaterial"] {
                color: #E6D9FF !important;
                font-weight: 500 !important;
                font-size: 20px !important;
            }

            /* Toast notification */
            div[data-testid="stToast"] {
                background-color: #F5F0FF !important;
                border: 1px solid #C9B5F5 !important;
                border-radius: 12px !important;
            }

            div[data-testid="stToast"] [data-testid="stMarkdownContainer"] p {
                color: #35245F !important;
                font-family: 'Poppins', sans-serif !important;
                font-weight: 500 !important;
            }

            .st-key-student-container h3 {
                font-size: 18px !important;
                margin-bottom: 10px !important;
            }

            .st-key-student-container{
                max-width: 700px !important;
            }


        </style>
            """, unsafe_allow_html = True)
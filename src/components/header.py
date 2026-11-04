
import streamlit as st
import base64

def header_home():
    logo_path = "src/images/logo.png"

    with open(logo_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown("""
        <style>
            .classora-title a {
                display: none !important;
            }

            .classora-title {
                margin: 0;
                padding: 0;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 25px; margin-top: 50px">
            <img src="data:image/png;base64,{encoded}"
                 style="height: 120px; width: auto;" />
            <h1 class="classora-title">Classora</h1>
            <p style = "font-size: 20px; font-style: italic;"> Smart Classrooms. Smarter Attendance. </p>
        </div>
    """, unsafe_allow_html=True)

import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
import numpy as np
from PIL import Image

def student_screen():

    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns([2, 1], vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        st.markdown("<div style='height: 20px;'></div>",unsafe_allow_html=True)

        if st.button("Home", type="secondary", key="loginbackbtn", icon=":material/home:",icon_position="left", width = "stretch"):
            st.session_state["login_type"] = None
            st.rerun()

    # st.space()
    st.header("Login using FaceID: ", text_alignment = "center")

    photo_source = st.camera_input("Position your face in the center.")

    if photo_source:
        np.array(Image.open(photo_source))


    footer_dashboard()
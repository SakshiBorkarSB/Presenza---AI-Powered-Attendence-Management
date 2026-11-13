import streamlit as st
import segno
import io
import time
from PIL import Image


@st.dialog("Capture or upload photos")
def add_photos_dialog():
    st.write("Add photos: ")

    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "tertiary" if st.session_state.photo_tab == "camera" else "secondary"
        if st.button("Camera", type = type_camera, width = "stretch"):
            st.session_state.photo_tab = "camera"

    with t2:
        type_upload = "tertiary" if st.session_state.photo_tab == "upload" else "secondary"
        if st.button("Upload photos", type = type_upload, width = "stretch"):
            st.session_state.photo_tab = "upload"

    if st.session_state.photo_tab == "camera":
        cam_photo = st.camera_input("Take Snapshot", key = "dialog_cam")
        if cam_photo:
            st.session_state.attendence_images.append(Image.open(cam_photo))
            st.toast("Photo Captured.")
            st.rerun()

    if st.session_state.photo_tab == "upload":
        uploaded_files = st.file_uploader("choose image files", type = ["jpg", "png", "jpeg"], accept_multiple_files = True, key = "dialog_upload")
        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendence_images.append(Image.open(f))
            st.toast("Photos Uploaded Sucessfully.")
            st.rerun()

    st.divider()
    if st.button("Done", width = "stretch"):
        st.rerun()

    

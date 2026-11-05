
import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
import numpy as np
from PIL import Image
from src.pipelines.face_pipeline import predict_attendence, get_face_embeddings, train_classifer
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student


def student_dashboard():
    st.header("Student Dashboard")


def student_screen():

    style_background_dashboard()
    style_base_layout()

    if"student_data" in st.session_state:
        student_dashboard()
        return
    
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

    show_registration = False
    photo_source = st.camera_input("Position your face in the center.")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("Scanning..."):
            detected, all_ids, num_of_faces = predict_attendence(img)

            if num_of_faces == 0:
                st.warning("Face not found!")
            elif num_of_faces > 1:
                st.warning("Multiple faces found!")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"] == student_id), None)
                        
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back! {student['name']}")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face not recognised! You might be a new student!")
                    show_registration = True

    if show_registration:
        with st.container(key="student-container"):
            st.header("Register new Profile", text_alignment = "center")
            new_name = st.text_input("Enter your name: ", placeholder = "Sakshi Borkar")

            st.subheader("Optional: Voice Enrollment")
            st.info("Enroll for voice only attendence")

            audio_data = None

            try:
                audio_data = st.audio_input("Record a short phrase (e.g., I am present, my name is Sakshi.)")

            except Exception:
                st.error("Audio data failed!")

            if st.button("Create Account", type = "secondary"):
                if new_name:
                    with st.spinner("Creating profile..."):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding = face_emb, voice_embedding = voice_emb)

                            if response_data:
                                train_classifer()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile created succesfully. Hi {new_name}!")
                                import time
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldn't capture face properly for registration.")

                else:
                    st.warning("Please enter your name.")

    footer_dashboard()
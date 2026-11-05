
import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():

    style_background_dashboard()
    style_base_layout()
    

    if "teacher_data" in st.session_state:
         teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type == "login":
         teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
         teacher_screen_register()


def teacher_dashboard():
     teacher_data = st.session_state.teacher_data

     st.header(f"""Welcome, {teacher_data["name"]}""")



# LOGIN
def login_teacher(username, password):
     if not username or not password:
          return False

     teacher = teacher_login(username, password)

     if teacher:
          st.session_state.user_role = "teacher"
          st.session_state.teacher_data = teacher
          st.session_state.isloggedin = True
          return True
     return False

def teacher_screen_login():
        c1, c2 = st.columns([2, 1], vertical_alignment="center", gap="xxlarge")

        with c1:
            header_dashboard()

        with c2:
            st.markdown("<div style='height: 20px;'></div>",unsafe_allow_html=True)

            if st.button("Home", type="secondary", key="loginbackbtn", icon=":material/home:",icon_position="left", width = "stretch"):
                st.session_state["login_type"] = None
                st.rerun()

        # st.space()
        st.header("Login with Password: ", text_alignment = "center")

        teacher_username = st.text_input("Enter username: ", placeholder = "Enter username")
        teacher_password = st.text_input("Enter password: ", placeholder = "Enter password", type = "password")

        st.space()

        btnc1, btnc2 = st.columns(2, gap = "small")

        with btnc1:
            if st.button("Login now", type="secondary", icon=":material/login:",icon_position="right", width = "stretch"):
                 if login_teacher(teacher_username, teacher_password):
                      st.toast("Welcome back!")
                      import time
                      time.sleep(1)
                      st.rerun()
                 else:
                      st.error("Invalid username and password")

        with btnc2:
            if st.button("Register instead", type="secondary", icon=":material/app_registration:",icon_position="right", width = "stretch"):
                 st.session_state.teacher_login_type = "register"

        footer_dashboard()



# REGISTER
def register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm):
    if not teacher_username or not teacher_name or not teacher_password or not teacher_password_confirm:
          return False, "All fields are required."

    if check_teacher_exists(teacher_username):
          return False, "Username already exists."

    if teacher_password != teacher_password_confirm:
          return False, "Password doesn't match."

    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Successfully registered! Login now."
    except Exception as e:
         return False, "Unexpected error!"


def teacher_screen_register():
        c1, c2 = st.columns([2, 1], vertical_alignment="center", gap="xxlarge")

        with c1:
            header_dashboard()

        with c2:
            st.markdown("<div style='height: 20px;'></div>",unsafe_allow_html=True)

            if st.button("Home", type="secondary", key="loginbackbtn", icon=":material/home:",icon_position="left", width = "stretch"):
                 st.session_state["login_type"] = None
                 st.rerun()

        st.header("Register your teacher profile: ", text_alignment = "center")

        teacher_username = st.text_input("Enter username: ", placeholder = "sakshiborkar")
        teacher_name = st.text_input("Enter name: ", placeholder = "Sakshi Borkar")
        teacher_password = st.text_input("Enter password: ", placeholder = "Sakshi@1234", type = "password")
        teacher_password_confirm = st.text_input("Confirm password: ", placeholder = "Sakshi@1234", type = "password")


        st.space()

        btnc1, btnc2 = st.columns(2, gap = "small")

        with btnc1:
            if st.button("Register now", type="secondary", icon=":material/app_registration:",icon_position="right", width = "stretch"):
                 success, message = register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm)
                 if success:
                      st.success(message)
                      import time
                      time.sleep(2)  # a delay in execution of program
                      st.session_state.teacher_login_type = "login"
                      st.rerun()
                 else:
                      st.error(message)
            

        with btnc2:
            if st.button("Login instead", type="secondary", icon=":material/login:",icon_position="right", width = "stretch"):
                 st.session_state.teacher_login_type = "login"

        footer_dashboard()

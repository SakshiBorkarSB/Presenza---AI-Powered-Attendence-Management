from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def check_teacher_exists(username):
    # Checks for unique username, returns false when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    data = {"username" : username, "password" : hash_pass(password), "name" : name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data 

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None

# def create_teacher(username, password, name):

#     print("Registration password length:", len(password))
#     hashed_password = hash_pass(password)

#     data = {
#         "username": username,
#         "password": hashed_password,
#         "name": name
#     }

#     response = supabase.table("teachers").insert(data).execute()

#     saved_teacher = response.data[0]

#     print("Original and retrieved hash match:",
#           hashed_password == saved_teacher["password"])

#     return response.data

# def teacher_login(username, password):

#     response = supabase.table("teachers").select("*").eq("username", username).execute()

#     if response.data:
#         teacher = response.data[0]

#         print("Password length:", len(password))
#         print("Stored hash verification:",
#               bcrypt.checkpw(password.encode("utf-8"),
#                              teacher["password"].encode("utf-8")))

#         return teacher if check_pass(password, teacher["password"]) else None

#     return None
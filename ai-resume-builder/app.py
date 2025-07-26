import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("firebase-admin.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

st.set_page_config(page_title="AI Resume Builder")

st.title("🧠 AI Resume Builder")
st.write("Login to generate your AI resume.")

email = st.text_input("Enter Email")
name = st.text_input("Enter Name")

if st.button("Login"):
    if email and name:
        user_ref = db.collection("users").document(email)
        user_ref.set({"name": name, "email": email})
        st.success(f"Welcome {name}! You're logged in.")
    else:
        st.warning("Please enter both email and name.")

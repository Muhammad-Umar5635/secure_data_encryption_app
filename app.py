import streamlit as st
from auth import register_user, authenticate_user, get_user_data
from encryption import encrypt_message, decrypt_message
from data_store import load_data, save_data
from utils import get_session, initialize_session

# Load persistent data
users = load_data()

# Initialize Streamlit session state
initialize_session()

st.title("🔐 Secure Data Encryption App")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Register":
    st.subheader("Create Account")
    username = st.text_input("Username")
    passkey = st.text_input("Passkey", type="password")
    if st.button("Register"):
        success = register_user(username, passkey, users)
        if success:
            st.success("User registered successfully!")
            save_data(users)
        else:
            st.error("User already exists.")

elif choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    passkey = st.text_input("Passkey", type="password")
    if st.button("Login"):
        auth_success, message = authenticate_user(username, passkey, users)
        if auth_success:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login successful!")
            save_data(users)
        else:
            st.error(message)
            save_data(users)

# Encryption Interface
if st.session_state.get("logged_in"):
    st.subheader("Encrypt / Decrypt Data")
    action = st.radio("Choose Action", ["Encrypt", "Decrypt"])
    user_data = get_user_data(users, st.session_state['username'])

    if action == "Encrypt":
        plaintext = st.text_area("Enter your message")
        if st.button("Encrypt"):
            encrypted = encrypt_message(plaintext)
            user_data["data"] = encrypted
            save_data(users)
            st.success("Data encrypted and saved.")
            st.code(encrypted)

    elif action == "Decrypt":
        encrypted_data = user_data.get("data", "")
        if encrypted_data:
            decrypted = decrypt_message(encrypted_data)
            st.success("Decrypted Message:")
            st.code(decrypted)
        else:
            st.warning("No encrypted data found.")
import os
import streamlit as st
from dotenv import load_dotenv
from auth import Authenticator

load_dotenv()

# emails of users that are allowed to login
allowed_users = st.secrets["my_email"]

st.title("Streamlit Google Auth")

authenticator = Authenticator(
    allowed_users=allowed_users,
    token_key=st.secrets["google_api_key"],
    secret_client_str=st.secrets["secret_client"],
    redirect_uri="https://ao-health-app.streamlit.app/",
)
authenticator.check_auth()
authenticator.login()

# show content that requires login
if st.session_state["connected"]:
    st.write(f"welcome! {st.session_state['user_info'].get('email')}")
    if st.button("Log out"):
        authenticator.logout()

if not st.session_state["connected"]:
    st.write("you have to log in first ...")

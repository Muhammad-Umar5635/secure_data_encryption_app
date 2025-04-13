import time
import streamlit as st

def is_locked_out(user_data):
    if 'lockout_time' in user_data:
        elapsed = time.time() - user_data['lockout_time']
        if elapsed < 300:
            return True, int(300 - elapsed)
        else:
            user_data['failed_attempts'] = 0
            del user_data['lockout_time']
    return False, 0

def initialize_session():
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'login_attempts' not in st.session_state:
        st.session_state.login_attempts = 0


def get_session():
    return st.session_state
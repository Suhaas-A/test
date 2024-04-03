import streamlit as st
from database import *
import subprocess

st.set_page_config(initial_sidebar_state="collapsed")

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

with st.sidebar:
    st.divider()
    st.header('some name')
    st.divider()
    st.page_link(page='pages/login.py', label='login')
    st.page_link(page='pages/register.py', label='register')

session = Session()

st.title('Login')

st.divider()

with st.form(key='login_form'):
    username = st.text_input('Username: ')
    st.divider()

    password = st.text_input('Password: ', type='password')
    st.divider()

    st.page_link('pages/forget_password.py')

    submit = st.form_submit_button('Login')

st.divider()

if submit:
    if not username:
        st.error('Username field is required')
    elif not password:
        st.error('Password field is required')
    else:
        users = session.query(Users).all()
        usernames, passwords, ids = [], [], []
        for user in users:
            usernames.append(user.username)
            passwords.append(user.password)
            ids.append(user.id)
        if username not in usernames:
            st.error('Invalid username')
        elif password not in passwords:
            st.error('Invalid password')
        else:
            print('yes')
            # Run Streamlit app
            process = subprocess.Popen(['streamlit', 'run', 'main_files/main.py'], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)

            # Wait for Streamlit app to start
            process.stdout.readline()

            # Wait for the Streamlit app to finish
            process.wait()

signup = st.button('Create an account')
if signup:
    st.switch_page('pages/register.py')

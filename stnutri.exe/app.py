import streamlit as st

st.set_page_config(page_title="NutriAI", layout="wide")

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)
    st.switch_page("pages/5_Login.py")

else:
    st.switch_page("pages/2_Pacientes.py")
import streamlit as st

st.title("NutriAI")

st.subheader("Login")

email = st.text_input("Email")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):

    if email and senha:
        st.session_state.logado = True
        st.switch_page("pages/2_Pacientes.py")

st.divider()

st.write("Não possui conta?")

if st.button("Criar conta"):
    st.switch_page("pages/1_Cadastro.py")
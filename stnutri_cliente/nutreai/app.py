import streamlit as st

st.title("NutriAI")

st.subheader("Login do Paciente")

login = st.text_input("CPF ou Email")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if login and senha:
        st.session_state.logado = True
        st.session_state.tipo_usuario = "paciente"
        st.switch_page("pages/2_Inicio_Paciente.py")
    else:
        st.warning("Preencha CPF/Email e senha.")

st.divider()

st.write("Não possui conta?")

if st.button("Criar conta"):
    st.switch_page("pages/1_Cadastro_Paciente.py")
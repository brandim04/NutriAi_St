import streamlit as st

st.title("Cadastro Paciente")

nome = st.text_input("Nome completo")
cpf = st.text_input("CPF")
email = st.text_input("Email")

senha = st.text_input("Senha", type="password")
confirmar = st.text_input("Confirmar senha", type="password")

if st.button("Cadastrar"):
    if not nome or not cpf or not email or not senha or not confirmar:
        st.warning("Preencha todos os campos.")
    elif senha != confirmar:
        st.error("As senhas não conferem.")
    else:
        st.session_state.logado = True
        st.session_state.tipo_usuario = "paciente"
        st.success("Cadastro realizado com sucesso!")
        st.switch_page("pages/2_Inicio_Paciente.py")
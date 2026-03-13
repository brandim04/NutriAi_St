import streamlit as st

st.title("Cadastro Nutricionista")

nome = st.text_input("Nome completo")
email = st.text_input("Email")

senha = st.text_input("Senha", type="password")
confirmar = st.text_input("Confirmar senha", type="password")

st.subheader("Informações profissionais")

crn = st.text_input("CRN")
estado = st.selectbox("Estado CRN",["PI","MA","CE","SP","RJ"])

especialidade = st.text_input("Especialidade")

st.subheader("Local de atuação")

clinica = st.text_input("Clínica ou Hospital")
cidade = st.text_input("Cidade")
estado2 = st.text_input("Estado")

termos = st.checkbox("Declaro que sou profissional habilitado")

if st.button("Cadastrar"):

    if termos:
        st.session_state.logado = True
        st.success("Cadastro realizado!")
        st.switch_page("pages/2_Pacientes.py")
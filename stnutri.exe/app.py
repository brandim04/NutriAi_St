import streamlit as st

st.set_page_config(page_title="NutriAI - Login", layout="centered")

# Estado de login
if "logado" not in st.session_state:
    st.session_state.logado = False

st.title("NutriAI")
st.subheader("Login")

cpf = st.text_input("CPF")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    # aqui futuramente entra validação com banco
    st.session_state.logado = True
    st.success("Login realizado com sucesso!")
    st.switch_page("pages/2_Pacientes.py")

st.markdown("Ainda não tem conta?")
st.page_link("pages/1_Cadastro.py", label="Cadastre-se")
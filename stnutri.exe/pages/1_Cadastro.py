import streamlit as st

st.set_page_config(page_title="Cadastro - NutriAI", layout="centered")

st.title("Cadastro Nutricionista")

st.text_input("Nome completo")
st.text_input("CPF")
st.text_input("Email")
st.text_input("CRN")
st.text_input("Senha", type="password")

if st.button("Cadastrar"):
    st.success("Cadastro realizado com sucesso!")

st.page_link("app.py", label="← Voltar para login")